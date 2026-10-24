#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""CLI-помощник скилла mos_itsm_ui_extension_descriptor.

Работает с REST API МосИТСМ (Xurrent-совместимым):
  GET   {api_base}/ui_extensions/{id}            — карточка расширения (вместе с кодом вкладок)
  GET   {api_base}/ui_extensions/{id}/versions   — история версий
  PATCH {api_base}/ui_extensions/{id}            — обновляет ТОЛЬКО поле description

Команды:
  get             - скачать расширение целиком в JSON (бэкап/анализ)
  set-description - записать описание из файла в поле description (с автоматическим бэкапом)
  check           - сверить description с файлом (если задан) и проверить вёрстку description_html
  list            - найти расширения по имени (без вложенного кода)

Примеры:
  python ui_extension.py get --ext https://community.itsm-qa.mos.ru/ui_extensions/19507
  python ui_extension.py get --ext 19507 --env QA --out ext.json
  python ui_extension.py set-description --ext 19507 --env QA --file desc.md --dry-run
  python ui_extension.py set-description --ext 19507 --env QA --file desc.md --yes
  python ui_extension.py check --ext 19507 --env QA --file desc.md
  python ui_extension.py list --name "Добавление КЕ"
"""
import argparse
import json
import re
import ssl
import urllib.error
import urllib.request
from datetime import datetime
from pathlib import Path

SKILL_DIR = Path(__file__).resolve().parent.parent
ENV_FILES = (SKILL_DIR / "skill_env.json", SKILL_DIR / ".env")
BACKUP_DIR = SKILL_DIR / "backups"

# Корпоративные сертификаты не установлены в системное хранилище — работаем без проверки TLS
SSL_CTX = ssl._create_unverified_context()


def load_env():
    for path in ENV_FILES:
        if path.exists():
            with open(path, encoding="utf-8") as f:
                cfg = json.load(f)
            if "MOSITSM_ACCOUNT" not in cfg and "MOSITSM_DEFAULT_ACCOUNT" in cfg:
                cfg["MOSITSM_ACCOUNT"] = cfg["MOSITSM_DEFAULT_ACCOUNT"]
            return cfg
    raise SystemExit(f"Не найден skill_env.json или .env в {SKILL_DIR}")


def resolve_api_base(env_name: str, env_cfg: dict) -> str:
    key = f"MOSITSM_API_URL_{env_name.upper()}"
    base = env_cfg.get(key)
    if not base:
        raise SystemExit(f"В {ENV_FILES[0].name} нет ключа {key}")
    return base.rstrip("/")


def resolve_token(env_name: str, token_arg, env_cfg: dict) -> str:
    if token_arg:
        return token_arg
    key = f"MOSITSM_PERS_TOKEN_{env_name.upper()}"
    token = env_cfg.get(key, "")
    if not token:
        raise SystemExit(f"Токен не задан: ни через --token, ни ключ {key} в .env")
    return token


def parse_ext_id(ext_arg: str) -> str:
    """Принимает и ID, и полную ссылку вида .../ui_extensions/19507."""
    ext_arg = ext_arg.strip().rstrip("/")
    m = re.search(r"(\d+)$", ext_arg)
    if not m:
        raise SystemExit(f"Не удалось извлечь ID расширения из: {ext_arg!r}")
    return m.group(1)


def api_request(method: str, url: str, token: str, account: str, payload=None):
    headers = {
        "Authorization": f"Bearer {token}",
        "X-4me-Account": account,
        "Accept": "application/json",
    }
    data = None
    if payload is not None:
        data = json.dumps(payload, ensure_ascii=False).encode("utf-8")
        headers["Content-Type"] = "application/json"
    req = urllib.request.Request(url, data=data, headers=headers, method=method)
    try:
        with urllib.request.urlopen(req, context=SSL_CTX, timeout=60) as resp:
            body = resp.read().decode("utf-8")
            return resp.status, (json.loads(body) if body.strip() else {})
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", errors="replace")
        raise SystemExit(f"HTTP {e.code} {method} {url}\n{body[:2000]}")


def fetch_ext(base, ext_id, token, account):
    """GET расширения целиком: карточка + код активной версии + текущее описание."""
    status, ext = api_request("GET", f"{base}/ui_extensions/{ext_id}", token, account)
    return status, ext


def do_get(args, env_cfg):
    env_name = args.env or env_cfg.get("MOSITSM_STAGE", "QA")
    base = resolve_api_base(env_name, env_cfg)
    token = resolve_token(env_name, args.token, env_cfg)
    account = env_cfg["MOSITSM_ACCOUNT"]
    ext_id = parse_ext_id(args.ext)
    status, ext = fetch_ext(base, ext_id, token, account)
    out = Path(args.out) if args.out else BACKUP_DIR / f"uiext_{ext_id}_{datetime.now():%Y%m%d_%H%M%S}.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(ext, ensure_ascii=False, indent=2), encoding="utf-8")
    av = ext.get("active_version") or {}
    pv = ext.get("prepared_version") or {}
    print(f"HTTP {status}; расширение {ext_id} сохранено: {out}")
    print(f"name={ext.get('name')!r}; category={ext.get('category')!r}; title={ext.get('title')!r}")
    print(f"disabled={ext.get('disabled')}; active_version={av.get('version')} (id {av.get('id')}); "
          f"prepared_version={pv.get('version')} (id {pv.get('id')})")
    print(f"html_len={len(ext.get('html') or '')}; js_len={len(ext.get('javascript') or '')}; "
          f"css_len={len(ext.get('css') or '')}; form_definition={bool(ext.get('form_definition_json'))}")
    desc = ext.get("description") or ""
    print(f"description_len={len(desc)}")


def do_versions(args, env_cfg):
    env_name = args.env or env_cfg.get("MOSITSM_STAGE", "QA")
    base = resolve_api_base(env_name, env_cfg)
    token = resolve_token(env_name, args.token, env_cfg)
    account = env_cfg["MOSITSM_ACCOUNT"]
    ext_id = parse_ext_id(args.ext)
    status, versions = api_request(
        "GET",
        f"{base}/ui_extensions/{ext_id}/versions?fields=id,version_nr,status,activated_at,archived_at,updated_at&per_page=100&sort=-version_nr",
        token, account,
    )
    out = Path(args.out) if args.out else BACKUP_DIR / f"uiext_{ext_id}_versions_{datetime.now():%Y%m%d_%H%M%S}.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(versions, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"HTTP {status}; версий: {len(versions)}; сохранено: {out}")
    for v in versions:
        print(f"  v{v.get('version_nr')} [{v.get('status')}] id={v.get('id')} "
              f"activated={v.get('activated_at') or '-'} updated={v.get('updated_at')}")


def do_list(args, env_cfg):
    env_name = args.env or env_cfg.get("MOSITSM_STAGE", "QA")
    base = resolve_api_base(env_name, env_cfg)
    token = resolve_token(env_name, args.token, env_cfg)
    account = env_cfg["MOSITSM_ACCOUNT"]
    url = f"{base}/ui_extensions?fields=id,name,category,disabled&per_page=100"
    items = []
    while url:
        status, page = api_request("GET", url, token, account)
        items.extend(page)
        # пагинация по Link-заголовку (Xurrent использует search_after, не page=N)
        req = urllib.request.Request(url, headers={
            "Authorization": f"Bearer {token}", "X-4me-Account": account, "Accept": "application/json",
        })
        with urllib.request.urlopen(req, context=SSL_CTX, timeout=60) as resp:
            link = resp.headers.get("Link") or resp.headers.get("link") or ""
        m = re.search(r'<([^>]+)>; *rel="next"', link)
        url = m.group(1) if m else None
    if args.name:
        needle = args.name.lower()
        items = [x for x in items if needle in x.get("name", "").lower()]
    print(f"Найдено: {len(items)}")
    for x in sorted(items, key=lambda z: z["id"]):
        flag = " [отключено]" if x.get("disabled") else ""
        print(f"  {x['id']}  {x.get('name')!r}  ({x.get('category')}){flag}")


def check_rendered_html(html: str) -> int:
    """Считает экранированные табличные теги в description_html.

    Серверный рендерер экранирует HTML-таблицы, свёрстанные «в одну строку»,
    — они превращаются в нечитаемый текст вида &lt;/th&gt;&lt;th&gt;.
    """
    return sum(html.count(f"&lt;{tag}") for tag in ("table", "tr", "td", "th"))


def do_set_description(args, env_cfg):
    env_name = args.env or env_cfg.get("MOSITSM_STAGE", "QA")
    base = resolve_api_base(env_name, env_cfg)
    token = resolve_token(env_name, args.token, env_cfg)
    account = env_cfg["MOSITSM_ACCOUNT"]
    ext_id = parse_ext_id(args.ext)
    new_desc = Path(args.file).read_text(encoding="utf-8")
    if len(new_desc.encode("utf-8")) > 64_000:
        raise SystemExit("Описание больше 64KB — API его не примет, сократите текст.")

    if not args.no_backup:
        _, ext = fetch_ext(base, ext_id, token, account)
        bdir = Path(args.backup_dir) if args.backup_dir else BACKUP_DIR
        bdir.mkdir(parents=True, exist_ok=True)
        bpath = bdir / f"uiext_{ext_id}_{datetime.now():%Y%m%d_%H%M%S}.json"
        bpath.write_text(json.dumps(ext, ensure_ascii=False, indent=2), encoding="utf-8")
        print(f"Бэкап текущего расширения: {bpath}")

    if args.dry_run:
        print(f"DRY-RUN: PATCH {base}/ui_extensions/{ext_id} (только description, {len(new_desc)} символов)")
        print("--- первые 500 символов нового описания ---")
        print(new_desc[:500])
        return

    if not args.yes:
        print("Не задан --yes — запись не выполняется. Первые 500 символов нового описания:")
        print(new_desc[:500])
        return

    status, resp = api_request(
        "PATCH", f"{base}/ui_extensions/{ext_id}", token, account,
        payload={"description": new_desc},
    )
    ok = resp.get("description") == new_desc
    print(f"HTTP {status}; updated_at={resp.get('updated_at')}; description совпадает: {ok}")
    if not ok:
        raise SystemExit("Сервер вернул иное описание — проверьте результат командой check")

    do_check_core(base, token, account, ext_id, args.file)


def do_check_core(base, token, account, ext_id, file_arg):
    """Сверка description с файлом (если задан) и состояния description_html."""
    status, ext = api_request("GET", f"{base}/ui_extensions/{ext_id}", token, account)
    desc = ext.get("description") or ""
    if file_arg:
        local = Path(file_arg).read_text(encoding="utf-8")
        print(f"description на сервере совпадает с файлом: {desc == local}")
    desc_html = ext.get("description_html")
    if desc_html is None:
        # У UI-расширений серверный рендерер не формирует description_html —
        # таблицы в описании верстаются обычным способом, проверять нечего.
        print("description_html пуст (у UI-расширений сервер его не рендерит) — сверка вёрстки не требуется")
        return
    escaped = check_rendered_html(desc_html)
    tables = desc_html.count("<table>")
    print(f"Вёрстка description_html: таблиц <table>={tables}, экранированных тегов={escaped}")
    if escaped:
        raise SystemExit(
            "В description_html найдены экранированные теги — таблицы свёрстаны "
            "«в одну строку». Перепишите таблицы построчно (каждый тег и текст ячейки "
            "на своей строке, как в references/reference_description.md) и запишите снова."
        )


def do_check(args, env_cfg):
    env_name = args.env or env_cfg.get("MOSITSM_STAGE", "QA")
    base = resolve_api_base(env_name, env_cfg)
    token = resolve_token(env_name, args.token, env_cfg)
    account = env_cfg["MOSITSM_ACCOUNT"]
    ext_id = parse_ext_id(args.ext)
    do_check_core(base, token, account, ext_id, args.file)


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--env", default=None, help="QA (по умолчанию из .env) или PROD")
    sub = p.add_subparsers(dest="cmd", required=True)

    sp = sub.add_parser("get", help="скачать расширение целиком в JSON")
    sp.add_argument("--ext", required=True, help="ID или ссылка на расширение")
    sp.add_argument("--out", default=None, help="куда сохранить JSON")
    sp.add_argument("--token", default=None)

    sp = sub.add_parser("versions", help="история версий расширения")
    sp.add_argument("--ext", required=True)
    sp.add_argument("--out", default=None)
    sp.add_argument("--token", default=None)

    sp = sub.add_parser("list", help="найти расширения по имени")
    sp.add_argument("--name", default=None, help="подстрока имени (без учёта регистра)")
    sp.add_argument("--token", default=None)

    sp = sub.add_parser("set-description", help="записать описание из файла (с бэкапом)")
    sp.add_argument("--ext", required=True)
    sp.add_argument("--file", required=True, help="файл с новым описанием (markdown)")
    sp.add_argument("--dry-run", action="store_true")
    sp.add_argument("--yes", action="store_true")
    sp.add_argument("--no-backup", action="store_true")
    sp.add_argument("--backup-dir", default=None)
    sp.add_argument("--token", default=None)

    sp = sub.add_parser("check", help="сверить description с файлом и вёрстку description_html")
    sp.add_argument("--ext", required=True)
    sp.add_argument("--file", default=None)
    sp.add_argument("--token", default=None)

    args = p.parse_args()
    env_cfg = load_env()
    if args.env:
        env_cfg = dict(env_cfg)
        env_cfg["MOSITSM_STAGE"] = args.env

    if args.cmd == "get":
        do_get(args, env_cfg)
    elif args.cmd == "versions":
        do_versions(args, env_cfg)
    elif args.cmd == "list":
        do_list(args, env_cfg)
    elif args.cmd == "set-description":
        do_set_description(args, env_cfg)
    elif args.cmd == "check":
        do_check(args, env_cfg)


if __name__ == "__main__":
    main()
