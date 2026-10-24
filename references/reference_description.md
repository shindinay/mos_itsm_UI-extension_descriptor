## История изменений

<table><tr><th data-colwidth="173">
Дата
</th><th>
Запрос (РП/ЗНИ)
</th><th>
Изменения
</th></tr><tr><td>
24.10.2026
</td><td>
00000
</td><td>
Первичное создание описания расширения (расширение 58).
</td></tr></table>

# О расширении

Расширение предназначено для сбора входных данных при оформлении заявки на увольнение сотрудника (категория request_template, вкладка «Входные данные»). 


## Использование 

Пользователь указывает ФИО сотрудника (выбор из представления «лица_все»), его организацию (выбор из представления «подведы_дит»), должность, фактического руководителя (подсказки по сотрудникам), точное место локации (подсказки по локациям), кабинет и дату увольнения.


## Особенности

Вкладка состоит из пяти секций. Заполнению доступна только секция с данными сотрудника; остальные четыре секции скрыты классом hide и размещают в разметке вкладки служебные поля записи (время регистрации, сведения об инициаторе и о том, для кого запрошена услуга, услуга и короткое описание) — без показа пользователю. JavaScript- и CSS-вкладки отсутствуют: динамическая логика не выполняется, видимость секций и полей задана статически классами в разметке, стили платформы не переопределяются. Обязательность полей обеспечивается классом required.


# Спецификация

### Секция "section0" (служебная)

<table><tr><th data-colwidth="173">
Параметр
</th><th>
Значение
</th></tr><tr><td>
ID
</td><td>
section0
</td></tr><tr><td>
Class
</td><td>
section-top hide
</td></tr><tr><td>
Видимость секции
</td><td>
Служебная скрытая секция: заголовок не задан. Скрыта (класс hide); JavaScript-вкладка отсутствует — секция никогда не показывается.
</td></tr></table>

Поля секции

<table><tr><th style="text-align:left;background-color:rgb(244, 245, 247)">
**Экранное название**
</th><th style="text-align:left;background-color:rgb(244, 245, 247)">
**label**
</th><th style="text-align:left;background-color:rgb(244, 245, 247)">
**Тип**
</th><th style="text-align:left;background-color:rgb(244, 245, 247)">
**Значение по умолчанию**
</th><th style="text-align:left;background-color:rgb(244, 245, 247)">
**Обязат.**
</th><th style="text-align:left;background-color:rgb(244, 245, 247)">
**Способ взаимодействия**
</th><th style="text-align:left;background-color:rgb(244, 245, 247)">
**Источник данных (при необход.)**
</th><th style="text-align:left;background-color:rgb(244, 245, 247)">
**Видимость**
</th><th style="text-align:left;background-color:rgb(244, 245, 247)" data-colwidth="88">
**Доступность**
</th><th>
Фильтрация и Поиск
</th><th style="text-align:left;background-color:rgb(244, 245, 247)">
**Примечание**
</th></tr><tr><td>
Время регистрации
</td><td style="text-align:left">
created_at
</td><td style="text-align:left">
Дата и время
</td><td style="text-align:left">
пусто
</td><td style="text-align:left">
нет
</td><td style="text-align:left">
Ввод вручную
</td><td>
autocomplete="off"; класс date-time
</td><td>
Всегда скрыто: секция скрыта (класс hide), строка поля имеет класс hide
</td><td>
<c #172b4d>не заблокир.</c>
</td><td>
не требуется
</td><td>
Служебное поле записи (время регистрации запроса)
</td></tr></table>

### Секция "Инициировано кем"

<table><tr><th data-colwidth="173">
Параметр
</th><th>
Значение
</th></tr><tr><td>
ID
</td><td>
section
</td></tr><tr><td>
Class
</td><td>
section hide
</td></tr><tr><td>
Видимость секции
</td><td>
Скрыта при открытии вкладки (класс hide); JavaScript-вкладка отсутствует — динамический показ не предусмотрен.
</td></tr></table>

Поля секции

<table><tr><th style="text-align:left;background-color:rgb(244, 245, 247)">
**Экранное название**
</th><th style="text-align:left;background-color:rgb(244, 245, 247)">
**label**
</th><th style="text-align:left;background-color:rgb(244, 245, 247)">
**Тип**
</th><th style="text-align:left;background-color:rgb(244, 245, 247)">
**Значение по умолчанию**
</th><th style="text-align:left;background-color:rgb(244, 245, 247)">
**Обязат.**
</th><th style="text-align:left;background-color:rgb(244, 245, 247)">
**Способ взаимодействия**
</th><th style="text-align:left;background-color:rgb(244, 245, 247)">
**Источник данных (при необход.)**
</th><th style="text-align:left;background-color:rgb(244, 245, 247)">
**Видимость**
</th><th style="text-align:left;background-color:rgb(244, 245, 247)" data-colwidth="88">
**Доступность**
</th><th>
Фильтрация и Поиск
</th><th style="text-align:left;background-color:rgb(244, 245, 247)">
**Примечание**
</th></tr><tr><td>
Создано кем
</td><td style="text-align:left">
reqs_by_fio
</td><td style="text-align:left">
Текст
</td><td style="text-align:left">
пусто
</td><td style="text-align:left">
нет
</td><td style="text-align:left">
Ввод вручную
</td><td>
autocomplete="off"
</td><td>
Всегда скрыто: секция скрыта (класс hide), строка поля имеет класс hide
</td><td>
<c #172b4d>не заблокир.</c>
</td><td>
не требуется
</td><td>
Служебное поле записи (инициатор запроса)
</td></tr><tr><td>
Учреждение
</td><td style="text-align:left">
reqs_by_oiv
</td><td style="text-align:left">
Текст
</td><td style="text-align:left">
пусто
</td><td style="text-align:left">
нет
</td><td style="text-align:left">
Ввод вручную
</td><td>
autocomplete="off"
</td><td>
Всегда скрыто: секция скрыта (класс hide), строка поля имеет класс hide
</td><td>
<c #172b4d>не заблокир.</c>
</td><td>
не требуется
</td><td>
Служебное поле записи
</td></tr><tr><td>
Локация
</td><td style="text-align:left">
reqs_by_site
</td><td style="text-align:left">
Текст
</td><td style="text-align:left">
пусто
</td><td style="text-align:left">
нет
</td><td style="text-align:left">
Ввод вручную
</td><td>
autocomplete="off"
</td><td>
Всегда скрыто: секция скрыта (класс hide), строка поля имеет класс hide
</td><td>
<c #172b4d>не заблокир.</c>
</td><td>
не требуется
</td><td>
Служебное поле записи
</td></tr><tr><td>
Рабочий
</td><td style="text-align:left">
reqs_by_tel_work
</td><td style="text-align:left">
Текст
</td><td style="text-align:left">
пусто
</td><td style="text-align:left">
нет
</td><td style="text-align:left">
Ввод вручную
</td><td>
autocomplete="off"
</td><td>
Всегда скрыто: секция скрыта (класс hide), строка поля имеет класс hide
</td><td>
<c #172b4d>не заблокир.</c>
</td><td>
не требуется
</td><td>
Поле телефона (подпись label — «Рабочий», подсказка — «Телефон»)
</td></tr><tr><td>
Мобильный
</td><td style="text-align:left">
reqs_by_tel_mobile
</td><td style="text-align:left">
Текст
</td><td style="text-align:left">
пусто
</td><td style="text-align:left">
нет
</td><td style="text-align:left">
Ввод вручную
</td><td>
autocomplete="off"
</td><td>
Всегда скрыто: секция скрыта (класс hide), строка поля имеет класс hide
</td><td>
<c #172b4d>не заблокир.</c>
</td><td>
не требуется
</td><td>
Поле телефона (подпись label — «Мобильный», подсказка — «Телефон»)
</td></tr><tr><td>
E-mail
</td><td style="text-align:left">
reqs_by_email
</td><td style="text-align:left">
Текст
</td><td style="text-align:left">
пусто
</td><td style="text-align:left">
нет
</td><td style="text-align:left">
Ввод вручную
</td><td>
autocomplete="off"
</td><td>
Всегда скрыто: секция скрыта (класс hide), строка поля имеет класс hide
</td><td>
<c #172b4d>не заблокир.</c>
</td><td>
не требуется
</td><td>
Служебное поле записи
</td></tr></table>

### Секция "Инициировано для кого"

<table><tr><th data-colwidth="173">
Параметр
</th><th>
Значение
</th></tr><tr><td>
ID
</td><td>
section1
</td></tr><tr><td>
Class
</td><td>
section hide
</td></tr><tr><td>
Видимость секции
</td><td>
Скрыта при открытии вкладки (класс hide); JavaScript-вкладка отсутствует — динамический показ не предусмотрен.
</td></tr></table>

Поля секции

<table><tr><th style="text-align:left;background-color:rgb(244, 245, 247)">
**Экранное название**
</th><th style="text-align:left;background-color:rgb(244, 245, 247)">
**label**
</th><th style="text-align:left;background-color:rgb(244, 245, 247)">
**Тип**
</th><th style="text-align:left;background-color:rgb(244, 245, 247)">
**Значение по умолчанию**
</th><th style="text-align:left;background-color:rgb(244, 245, 247)">
**Обязат.**
</th><th style="text-align:left;background-color:rgb(244, 245, 247)">
**Способ взаимодействия**
</th><th style="text-align:left;background-color:rgb(244, 245, 247)">
**Источник данных (при необход.)**
</th><th style="text-align:left;background-color:rgb(244, 245, 247)">
**Видимость**
</th><th style="text-align:left;background-color:rgb(244, 245, 247)" data-colwidth="88">
**Доступность**
</th><th>
Фильтрация и Поиск
</th><th style="text-align:left;background-color:rgb(244, 245, 247)">
**Примечание**
</th></tr><tr><td>
Услуга запрошено для
</td><td style="text-align:left">
reqs_for_fio
</td><td style="text-align:left">
Текст
</td><td style="text-align:left">
пусто
</td><td style="text-align:left">
нет
</td><td style="text-align:left">
Ввод вручную
</td><td>
autocomplete="off"
</td><td>
Всегда скрыто: секция скрыта (класс hide), строка поля имеет класс hide
</td><td>
<c #172b4d>не заблокир.</c>
</td><td>
не требуется
</td><td>
Служебное поле записи (получатель услуги)
</td></tr><tr><td>
Учреждение
</td><td style="text-align:left">
reqs_for_oiv
</td><td style="text-align:left">
Текст
</td><td style="text-align:left">
пусто
</td><td style="text-align:left">
нет
</td><td style="text-align:left">
Ввод вручную
</td><td>
autocomplete="off"
</td><td>
Всегда скрыто: секция скрыта (класс hide), строка поля имеет класс hide
</td><td>
<c #172b4d>не заблокир.</c>
</td><td>
не требуется
</td><td>
Служебное поле записи
</td></tr><tr><td>
Локация
</td><td style="text-align:left">
reqs_for_site
</td><td style="text-align:left">
Текст
</td><td style="text-align:left">
пусто
</td><td style="text-align:left">
нет
</td><td style="text-align:left">
Ввод вручную
</td><td>
autocomplete="off"
</td><td>
Всегда скрыто: секция скрыта (класс hide), строка поля имеет класс hide
</td><td>
<c #172b4d>не заблокир.</c>
</td><td>
не требуется
</td><td>
Служебное поле записи
</td></tr><tr><td>
Рабочий
</td><td style="text-align:left">
reqs_for_tel_work
</td><td style="text-align:left">
Текст
</td><td style="text-align:left">
пусто
</td><td style="text-align:left">
нет
</td><td style="text-align:left">
Ввод вручную
</td><td>
autocomplete="off"
</td><td>
Всегда скрыто: секция скрыта (класс hide), строка поля имеет класс hide
</td><td>
<c #172b4d>не заблокир.</c>
</td><td>
не требуется
</td><td>
Поле телефона (подпись label — «Рабочий», подсказка — «Телефон»)
</td></tr><tr><td>
Мобильный
</td><td style="text-align:left">
reqs_for_tel_mobile
</td><td style="text-align:left">
Текст
</td><td style="text-align:left">
пусто
</td><td style="text-align:left">
нет
</td><td style="text-align:left">
Ввод вручную
</td><td>
autocomplete="off"
</td><td>
Всегда скрыто: секция скрыта (класс hide), строка поля имеет класс hide
</td><td>
<c #172b4d>не заблокир.</c>
</td><td>
не требуется
</td><td>
Поле телефона (подпись label — «Мобильный», подсказка — «Телефон»)
</td></tr><tr><td>
E-mail
</td><td style="text-align:left">
reqs_for_email
</td><td style="text-align:left">
Текст
</td><td style="text-align:left">
пусто
</td><td style="text-align:left">
нет
</td><td style="text-align:left">
Ввод вручную
</td><td>
autocomplete="off"
</td><td>
Всегда скрыто: секция скрыта (класс hide), строка поля имеет класс hide
</td><td>
<c #172b4d>не заблокир.</c>
</td><td>
не требуется
</td><td>
Служебное поле записи
</td></tr></table>

#### Секция "Описание запроса, требующего согласование"

<table><tr><th data-colwidth="173">
Параметр
</th><th>
Значение
</th></tr><tr><td>
ID
</td><td>
section2
</td></tr><tr><td>
Class
</td><td>
section hide
</td></tr><tr><td>
Видимость секции
</td><td>
Скрыта при открытии вкладки (класс hide); JavaScript-вкладка отсутствует — динамический показ не предусмотрен.
</td></tr></table>

Поля секции

<table><tr><th style="text-align:left;background-color:rgb(244, 245, 247)">
**Экранное название**
</th><th style="text-align:left;background-color:rgb(244, 245, 247)">
**label**
</th><th style="text-align:left;background-color:rgb(244, 245, 247)">
**Тип**
</th><th style="text-align:left;background-color:rgb(244, 245, 247)">
**Значение по умолчанию**
</th><th style="text-align:left;background-color:rgb(244, 245, 247)">
**Обязат.**
</th><th style="text-align:left;background-color:rgb(244, 245, 247)">
**Способ взаимодействия**
</th><th style="text-align:left;background-color:rgb(244, 245, 247)">
**Источник данных (при необход.)**
</th><th style="text-align:left;background-color:rgb(244, 245, 247)">
**Видимость**
</th><th style="text-align:left;background-color:rgb(244, 245, 247)" data-colwidth="88">
**Доступность**
</th><th>
Фильтрация и Поиск
</th><th style="text-align:left;background-color:rgb(244, 245, 247)">
**Примечание**
</th></tr><tr><td>
Услуга
</td><td style="text-align:left">
service_name
</td><td style="text-align:left">
Текст
</td><td style="text-align:left">
пусто
</td><td style="text-align:left">
нет
</td><td style="text-align:left">
Ввод вручную
</td><td>
autocomplete="off"
</td><td>
Всегда скрыто: секция скрыта (класс hide), строка поля имеет класс hide
</td><td>
<c #172b4d>не заблокир.</c>
</td><td>
не требуется
</td><td>
Служебное поле записи
</td></tr><tr><td>
Короткое описание
</td><td style="text-align:left">
subject
</td><td style="text-align:left">
Текст
</td><td style="text-align:left">
пусто
</td><td style="text-align:left">
нет
</td><td style="text-align:left">
Ввод вручную
</td><td>
autocomplete="off"
</td><td>
Всегда скрыто: секция скрыта (класс hide), строка поля имеет класс hide
</td><td>
<c #172b4d>не заблокир.</c>
</td><td>
не требуется
</td><td>
Служебное поле записи
</td></tr></table>

### Секция "section3" (без заголовка)

<table><tr><th data-colwidth="173">
Параметр
</th><th>
Значение
</th></tr><tr><td>
ID
</td><td>
section3
</td></tr><tr><td>
Class
</td><td>
section
</td></tr><tr><td>
Видимость секции
</td><td>
Видна всегда при открытой вкладке; заголовок секции пустой и скрыт (span с классом section-header hide). Основная заполняемая секция вкладки.
</td></tr></table>

Поля секции

<table><tr><th style="text-align:left;background-color:rgb(244, 245, 247)">
**Экранное название**
</th><th style="text-align:left;background-color:rgb(244, 245, 247)">
**label**
</th><th style="text-align:left;background-color:rgb(244, 245, 247)">
**Тип**
</th><th style="text-align:left;background-color:rgb(244, 245, 247)">
**Значение по умолчанию**
</th><th style="text-align:left;background-color:rgb(244, 245, 247)">
**Обязат.**
</th><th style="text-align:left;background-color:rgb(244, 245, 247)">
**Способ взаимодействия**
</th><th style="text-align:left;background-color:rgb(244, 245, 247)">
**Источник данных (при необход.)**
</th><th style="text-align:left;background-color:rgb(244, 245, 247)">
**Видимость**
</th><th style="text-align:left;background-color:rgb(244, 245, 247)" data-colwidth="88">
**Доступность**
</th><th>
Фильтрация и Поиск
</th><th style="text-align:left;background-color:rgb(244, 245, 247)">
**Примечание**
</th></tr><tr><td>
ФИО сотрудника
</td><td style="text-align:left">
fio
</td><td style="text-align:left">
Справочник
</td><td style="text-align:left">
пусто
</td><td style="text-align:left">
да
</td><td style="text-align:left">
Выбор из справочника
</td><td>
Представление «лица_все» (data-custom-view="лица_все")
</td><td>
Видно всегда при открытой вкладке
</td><td>
<c #172b4d>не заблокир.</c>
</td><td>
не требуется
</td><td>
Обязательное поле (класс required)
</td></tr><tr><td>
Организация сотрудника
</td><td style="text-align:left">
oiv
</td><td style="text-align:left">
Справочник
</td><td style="text-align:left">
пусто
</td><td style="text-align:left">
да
</td><td style="text-align:left">
Выбор из справочника
</td><td>
Представление «подведы_дит» (data-custom-view="подведы_дит")
</td><td>
Видно всегда при открытой вкладке
</td><td>
<c #172b4d>не заблокир.</c>
</td><td>
не требуется
</td><td>
Обязательное поле (класс required)
</td></tr><tr><td>
Должность сотрудника
</td><td style="text-align:left">
position
</td><td style="text-align:left">
Текст
</td><td style="text-align:left">
пусто
</td><td style="text-align:left">
да
</td><td style="text-align:left">
Ввод вручную
</td><td>
autocomplete="off"
</td><td>
Видно всегда при открытой вкладке
</td><td>
<c #172b4d>не заблокир.</c>
</td><td>
не требуется
</td><td>
Обязательное поле (класс required)
</td></tr><tr><td>
Руководитель сотрудника
</td><td style="text-align:left">
executive
</td><td style="text-align:left">
Справочник
</td><td style="text-align:left">
пусто
</td><td style="text-align:left">
да
</td><td style="text-align:left">
Выбор из справочника
</td><td>
Подсказки по сотрудникам (person-suggest)
</td><td>
Видно всегда при открытой вкладке
</td><td>
<c #172b4d>не заблокир.</c>
</td><td>
не требуется
</td><td>
Подсказка label — «Фактический руководитель сотрудника»; обязательное поле (класс required)
</td></tr><tr><td>
Точное место локации сотрудника
</td><td style="text-align:left">
site
</td><td style="text-align:left">
Справочник
</td><td style="text-align:left">
пусто
</td><td style="text-align:left">
да
</td><td style="text-align:left">
Выбор из справочника
</td><td>
Подсказки по локациям (site-suggest)
</td><td>
Видно всегда при открытой вкладке
</td><td>
<c #172b4d>не заблокир.</c>
</td><td>
не требуется
</td><td>
Обязательное поле (класс required)
</td></tr><tr><td>
Кабинет
</td><td style="text-align:left">
cabinet
</td><td style="text-align:left">
Текст
</td><td style="text-align:left">
пусто
</td><td style="text-align:left">
нет
</td><td style="text-align:left">
Ввод вручную
</td><td>
autocomplete="off"
</td><td>
Видно всегда при открытой вкладке
</td><td>
<c #172b4d>не заблокир.</c>
</td><td>
не требуется
</td><td>
Единственное необязательное поле вкладки
</td></tr><tr><td>
Дата увольнения
</td><td style="text-align:left">
dismissal_date
</td><td style="text-align:left">
Дата
</td><td style="text-align:left">
пусто
</td><td style="text-align:left">
да
</td><td style="text-align:left">
Ввод вручную (виджет даты, класс date)
</td><td>
autocomplete="off"
</td><td>
Видно всегда при открытой вкладке
</td><td>
<c #172b4d>не заблокир.</c>
</td><td>
не требуется
</td><td>
Обязательное поле (класс required)
</td></tr></table>

В разметке секции «section3» закомментированы два поля, отмеченные как используемые для API (cfc): oiv_cfc «Организация сотрудника» и location «Точное место локации сотрудника». На форму они не влияют и не отображаются.

# Элементы управения (кнопки и динамическое поведение)

Кнопки в разметке отсутствуют. JavaScript- и CSS-вкладки пустые: обработчики событий, хуки платформы (в том числе after-prefill) и обращение к данным записи не используются; после открытия вкладки состояние формы не меняется. Видимость секций и полей задана статическими классами hide в HTML-вкладке: видимы только поля секции «section3» (данные сотрудника), остальные секции скрыты постоянно.