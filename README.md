# SPapi v1.1.2

Модуль создан Spagetik для серверов СП, СПм, СПк.

## 1. Начало работы
### 1.1 Установка и импортирование модуля

Для начала работы с модулем нужно установить сам модуль командой:

Для Windows
```commandline
> pip install SPapi
```
Для Linux
```commandline
$ sudo apt pip3 install SPapi
```

После установки модуля следует импортировать все классы из модуля:
```python
from SPapi import *
```
Сразу после импортирования следует создать переменные **server**, **token**, **response_key**:
```python
from SPapi import *

token = 'Your_Token'
server = 'Your_Server'
response_key = 'Your_Response_Key'

api = SpApi(server, token, response_key)
```
| Param | Type | Description |
| --- | --- | --- |
| server | <code>Str</code> | Сервер с которым будет работать API. ('sp', 'spm', 'spk') |
| token | <code>Str</code> | Секретный TOKEN вашего приложения. Получить [здесь](https://spk.jakksoft.com/dev/apps).|
| response_key | <code>Str</code> | Ключ ответа. Используется для проверки подлинности источника серверного ответа.  Получить [здесь](https://spk.jakksoft.com/dev/apps). |

### 1.2 Пример отправки тестового запроса

Код:
```python
from SPapi import *

token = 'Your_Token'
server = 'Your_Server'
response_key = 'Your_Response_Key'

api = SpApi(server, token, response_key)

response = api.test()

print(response)
```
Пример вывода:
```commandline
<success=True>
<response_key=kaSfzshJQXWOU8OOTcZy2IPq>
<data=['Hello world!']>
```

## 2. Классы модуля

### <a href="#SpApi">SpApi</a>

Основной класс модуля для оправки запросов на сайт.

### <a href="#Response">Response</a>

Класс получаемых ответов с сервера. Нужен для удобства получения данных с сервера.

### <a href="#Card">Card</a>

Класс для удобного доступа к данным карт, запрошенным методом <a href="#get_cards_info">get_cards_info()</a>.

### <a href="#Notify">Notify</a>

Класс для удобного доступа к данным карт, запрошенным методом <a href="#get_unread_notifications">get_unread_notifications()</a>.

## 3. Методы классов

### 3.1 Класс <a href="#SpApi" name="SpApi">SpApi</a>

#### 3.1.1 <a href="#test" name="test">test()</a> ⇒  <a href="#Response">Response</a>
Тестовый метод для проверки работоспособности кода и соединения с сайтом. Не требует дополнительных аргументов.

#### 3.1.2 <a href="#permission_test" name="permission_test">permission_test()</a> ⇒ <a href="#Response">Response</a>
Тестовый метод для проверки выданных вами разрешений приложению. Требует дополнительные аргументы: `your_license_key`

| Param | Type | Description |
| --- | --- | --- |
|your_license_key|<code>str</code>| ВАШ ключ-лицензия. Найти можно [тут](https://spk.jakksoft.com/settings#collapseApps).

#### 3.1.3 <a href="#pay" name="pay">pay()</a> ⇒ <a href="#Response">Response</a>
Метод для оплаты через SP-pay. Требует дополнительные аргументы: `sp_pay_code`, `summa`, `trans_mes`

| Param | Type | Description |
| --- | --- | --- |
|sp_pay_code|<code>int</code>|Код, полученный игроком на сайте.
|summa|<code>int</code>|Сумма оплаты. ВАЖНО! Должна соответствовать сумме указанной, при получении кода
|trans_mes|<code>str</code>|Сообщение, сопровождающее транзакцию оплаты. (Опционально)|

#### 3.1.4 <a href="#get_permission" name="get_permission">get_permission()</a> ⇒ <a href="#Response">Response</a>
Метод для запроса разрешений у пользователя. Требует дополнительные аргументы: `license_key`, `permission_id`

| Param | Type | Description |
| --- | --- | --- |
|license_key|<code>str</code>|Ключ-лицензия игрока, у которого запрашиваются разрешения.|
|permission_id|<code>int</code>|id требуемого разрешения. Посмотреть все разрешения можно [тут](https://spk.jakksoft.com/dev/permissions).|

#### 3.1.5 <a href="#get_cards_info" name="get_cards_info">get_cards_info()</a> ⇒ <a href="#Response">Response</a>
Метод для запроса информации о картах игрока. Требует дополнительные аргументы: `license_key`

| Param | Type | Description |
| --- | --- | --- |
|license_key|<code>str</code>|Ключ-лицензия игрока, у которого запрашиваются данные.|

#### 3.1.6 <a href="#get_cards_info" name="get_cards_info">get_cards_info()</a> ⇒ <a href="#Response">Response</a>
Метод для запроса непрочитанных уведомлений игрока. Требует дополнительные аргументы: `license_key`

| Param | Type | Description |
| --- | --- | --- |
|license_key|<code>str</code>|Ключ-лицензия игрока, у которого запрашиваются данные.|

#### 3.1.7 <a href="#get_cards_info" name="get_cards_info">get_cards_info()</a> ⇒ <a href="#Response">Response</a>
Метод для пометки непрочитанных уведомлений игрока как прочитанные. Требует дополнительные аргументы: `license_key`

| Param | Type | Description |
| --- | --- | --- |
|license_key|<code>str</code>|Ключ-лицензия игрока, у которого запрашиваются данные.|

## 4. Атрибуты классов

### 4.1 Класс <a href="#SpApi">SpApi</a>

| Param | Type | Description |
| --- | --- | --- |
|.server|<code>str</code>|Сервер с которым работает класс.|
|.token|<code>str</code>|Токен приложения.|
|.response_key|<code>str</code>|Ключ ответ приложения.|

### 4.2 Класс <a href="#Response">Response</a>

| Param | Type | Description |
| --- | --- | --- |
|.success|<code>boolean</code>|Удачен ли запрос. True or False.|
|.response_key|<code>str</code>|Ключ ответ приложения.|
|.data|<code>list</code><p><code>list of class \<Card><p></code><code>list of class \<Notify></code>|Список данных.<p>Либо список карт пользователя (class \<Card>) при использовании <a href="#get_card_info">get_card_info()</a><p>Либо список уведомлений пользователя (class \<Notify>) при использовании <a href="#get_unread_notifications">get_unread_notifications()</a>|
|.errors|<code>list</code>|Список ошибок, если есть.|

### 4.3 Класс <a href="#Card">Card</a>

| Param | Type | Description |
| --- | --- | --- |
|.id|<code>int</code>|ID Счета игрока.|
|.name|<code>str</code>|Название счета игрока. |
|.balance|<code>int</code>|Баланс счета игрока.|
|.bg_color|<code>str</code>|Цвет фона карты в формате `#xxxxxx`.|
|.font_color|<code>str</code>|Цвет текста карты в формате `#xxxxxx`.|
|.image|<code>str</code>|Ссылка на изображение фона карты.|

### 4.4 Класс <a href="#Notify">Notify</a>

| Param | Type | Description |
| --- | --- | --- |
|.id|<code>int</code>|ID уведомления.|
|.type|<code>int</code>|Тип уведомления.|
|.type_title|<code>str</code>|Название типа уведомления.|
|.message|<code>str</code>|	Текст уведомления.|
|.time|<code>int</code>|Unix-время когда пришло уведомление в секундах.|

# Made with love by Spagetik from SPk ♥


