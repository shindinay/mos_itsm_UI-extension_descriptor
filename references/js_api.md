# JS API платформы (объект ITRP)

Все вызовы начинаются с `ITRP`. Полная справка (локальная копия): `C:\Users\shindinay\.zcode\internal_base\03_developer_markdown\developer.r-service.tech\developer\v1\ui_extensions\js_api.md`.

## Обязательное начало скрипта

```javascript
var $ = ITRP.$;            // jQuery платформы
var $extension = $(this);  // корневой элемент расширения
```

Дальше все элементы ищи через `$extension.find('#myext_id')`.

## Чтение данных записи

```javascript
// Начальные значения полей записи (при редактировании)
ITRP.record.initialValues.get('status');
ITRP.record.initialValues.get('id');            // уникальный ID записи (запрос: только id, поля nr нет)
ITRP.record.initialValues.get('team', 'name');  // атрибут ссылки (reference)
ITRP.record.initialValues.custom_data.myfield;  // кастомные поля расширения (в образце вендора)

// Новая запись или существующая?
ITRP.record.new;  // true / false

// Контекст: 'self_service' (Портал МосИТСМ) или 'full_ui' (Консоль МосИТСМ)
ITRP.context;
```

Имена полей зависят от типа записи и совпадают с полями из «Collection Fields» справки API этого типа (Requests, Tasks, People...). Не выдумывай поля: проверь по локальной копии справки (`C:\Users\shindinay\.zcode\internal_base\03_developer_markdown\...\v1\requests.md` и т.п.) или оборачивай в try/catch.

## Работа с полями формы

```javascript
ITRP.field('subject').val();              // получить значение
ITRP.field('subject').val('Новое');       // установить
ITRP.field('note').placeholder('...');    // подсказка поля Note
ITRP.field('note').required(true);        // обязательное / необязательное
ITRP.field('severity').readonly(true);    // только чтение
ITRP.field('note').hide();  .show();  .toggle(true|false);
ITRP.field('status').on('change', function() { ... }).trigger('change');
ITRP.field('status').off('change', handler);
ITRP.field('service_instance').data('item');  // атрибуты выбранного элемента suggest-поля
```

Доступные поля для каждого типа записи и контекста (Портал/Консоль) перечислены в справке js_api.md — у request_template на Портале это subject, note, attachment, asset, service_instance; в Консоли дополнительно internal_note, impact, status и др.

## Кастомные поля (suggest) и метаданные

```javascript
var item = $extension.find('#myext_suggest').data('item');   // одиночный выбор
// item.id, item.display_name, item.reference
var items = $extension.find('#myext_multi').data('items');   // множественный выбор (массив)
// Метаданные из Custom View: item.assetID, item.custom_fields['Статья затрат']
```

## Утилиты

```javascript
ITRP.hooks.register('after-prefill', function() { ... });  // после предзаполнения полей
ITRP.hasFormData($extension);    // заполнено ли что-то в scope расширения
ITRP.clearFormData($extension);  // очистить все поля расширения
ITRP.field('attachment').size(); // число вложений
```

## jQuery

jQuery доступен только через `ITRP.$` (это старая версия jQuery, без современных методов). AJAX доступен как `$.ajax` / `$.getScript` — CORS должен быть разрешён на внешнем сервисе, иначе запрос упадёт; проверяй это до встраивания.
