# Платформа МосИТСМ: правила UI extension

Система МосИТСМ построена на платформе 4me (Xurrent). Экранная форма расширяется UI extension из трёх вкладок: HTML, JavaScript, CSS. Справка вендора размещена в developer-разделе портала МосИТСМ; локальные копии лежат в `C:\Users\shindinay\.zcode\internal_base` (папки `03_developer_markdown`, `01_developer_html`).

## Ограничения вкладок

| Вкладка | Лимит | Что это |
|---------|-------|---------|
| HTML | 64 КБ | Фрагмент разметки, вставляемый в форму. Без `<html>`, `<head>`, `<body>`. |
| JavaScript | 64 КБ | Исполняется при открытии формы на редактирование, после JS платформы. |
| CSS | 64 КБ | Обычный stylesheet, применяется к форме. |

## Категории (Category)

Категория задаётся при создании и не меняется: `request_template` (шаблон заявки), `task_template`, `workflow_template`, `problem`, `release`, `project`, `project_task_template`, `knowledge_article_template`, `service`, `service_instance`, `product`, `product_category`, `contract`, `organization`, `team`, `person`, `site`, `risk`, `custom_collection`, `app_offering`, `shop_article`.

## Готовые классы платформы (HTML)

Используй их, чтобы расширение выглядело нативно:

```html
<!-- Секция с заголовком -->
<div class="section" id="myext_section">
  <span class="section-header">Заголовок секции</span>
</div>

<!-- Строка поле + подпись (vertical = подпись сверху) -->
<div class="row vertical" data-searchable data-filterable>
  <label for="myext_field" title="Подсказка">Подпись поля</label>
  <input id="myext_field" type="text" autocomplete="off" data-filterable-name="Подпись поля">
</div>

<!-- Кнопка в стиле платформы -->
<span class="btn check" id="myext_btn"><span class="button">Текст кнопки</span></span>

<!-- Служебные классы: hide (скрыть), show-when-empty (показывать в режиме просмотра,
     даже если пусто), invalid (невалидное значение), required-on-completion (обязательно
     при завершении) -->
```

`data-searchable` включает попадание значения в поиск, `data-filterable` + `data-filterable-name="..."` — создание фильтра при активации версии.

## Хуки и порядок загрузки

При редактировании записи платформа выполняет: (1) загрузку HTML, (2) JS платформы, (3) JS расширения, (4) заполнение кастомных полей значениями, (5) хук `after-prefill`. Поэтому значения кастомных полей читай в хуке:

```javascript
ITRP.hooks.register('after-prefill', function() {
  var value = $extension.find('#myext_field').val();
});
```

## Версионирование расширения

Изменения попадают в Prepared Version и не действуют, пока не нажать «Activate» (переводит Prepared в Active, прежняя активная архивируется). Установка: Консоль МосИТСМ → Настройки → UI Extensions → создать/открыть → вставить вкладки → Activate → привязать к шаблону записи.

## Убираемое за кадром

- REST/GraphQL API платформы для создания расширений скриптом — раздел developer-справки МосИТСМ по ui_extensions (поля `html`, `javascript`, `css`, `category`, `name`, `title`, `activate`; локальная копия — `03_developer_markdown\developer.r-service.tech\developer\v1\ui_extensions.md`). Вручную через интерфейс проще и надёжнее.
- Дизайнер форм (`form_definition_json`) — альтернатива без кода; не подходит, когда нужна логика на JS.
