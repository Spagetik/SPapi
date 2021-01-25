# SPapi v1.1.0
## 1. Начало работы
### 1.1 Установка и импортирование

Для начала работы с модулем нужно установить сам модуль командой:

Для Windows
```commandline
> pip install SPapi
```
Для Linux
```commandline
$ sudo apt pip3 install SPapi
```


После установки модуля следует его импортировать класс SpApi из модуля:
```python
from SPapi import SpApi
```

Сразу после импортирования следует создать переменные **server**, **token**, **response_key**:
```python
token = 'Your_Token'
server = 'Your_Server'
response_key = 'Your_Response_Key'
```

Токен  ключ ответа можно узнать на этой [странице](https://spk.jakksoft.com/dev/apps).

В случае, если у вас ещё нет приложения, создайте его [здесь](https://spk.jakksoft.com/dev/apps). Для создания приложения требуется **роль разработчика**, тикет для получения роли можно создать [здесь](https://spk.jakksoft.com/support/new_ticket).

В параметре **server** укажите сервер для которого используется API:
 - СП - 'sp'
 - СПм - 'spm'
 - СПк - 'spk'

### 1.2 Создание переменной для обработки запросов

Для создания переменной для обработки запросов потребуется написать следущее:
```python
api = SpApi(server, token, response_key)
```

### 1.3 Отправка тестового запроса

Для оправки тестового запроса потребуется написать следующий код:
```python
response = api.test()

print(response)
```

После выполнения этого кода в консоле должно вывестись:
```commandline
{'success': True, 'response_key': 'CrzmtXg2Stw909omziWnVdig', 'data': ['Hello world!'], 'errors': []}
```
Если тестовый запрос отправился и пришел ответ, **поздравляю, вы сделали все правильно!**

## 2. Описание функций класса SpApi

### 2.1 Функция 'test()'

Данная функция является тестовой, для проверки соединения с сайтом. У неё нет параметров которые нужно указывать.

Пример кода:
```python
response = api.test()

print(response)
```
Пример вывода:
```commandline
{'success': True, 'response_key': 'CrzmtXg2Stw909omziWnVdig', 'data': ['Hello world!'], 'errors': []}
```

### 2.2 Функция 'permission_test(your_license_key: str)'

Данная функция является второй тестовой функцией, для проверки соединения с сайтом. Функция требует параметр **your_license_key**, который является **ВАШИМ ключом лицензии** к **ВАШЕМУ приложению**.

- **your_license_key** - строка!

Пример кода:
```python
your_license_key = 'hsjhfdjsdfsjjdf'

response = api.permission_test(your_license_key)

print(response)
```
Пример ответа при выданном праве "Тестовое разрешение":
```commandline
{'success': True, 'response_key': 'CrzmtXg2Stw909omziWnVdig', 'data': ['Ваше приложение имеет тестовое разрешение!'], 'errors': []}
```
Пример ответа при невыданном праве "Тестовое разрешение":
```commandline
{'success': False, 'response_key': 'CrzmtXg2Stw909omziWnVdig', 'data': [], 'errors': ['Приложению не предоставлен доступ на "тестовое разрешение".']}
```

### 2.3 Функция 'pay(sp_pay_code: int, summa: int, trans_mes='Оплата SP-pay')'

####Обязательно:

- **sp_pay_code** - код, полученный на сайте (int)
- **summa** - сумма оплаты (int). ВАЖНО! Сумма при получении кода и при отправке запроса должный быть одинаковыми!

####Опционально:

- **trans_mes** - Сообщение, сопровождающее платёж (str)

Пример кода:
```python
sp_pay_code = 123456
summa = 64
trans_mes = 'ЛИХ'

response = api.pay(sp_pay_code, summa, trans_mes)

print(response)
```
Пример ответа при успешной транзакции:
```commandline
{'success': True, 'response_key': 'CrzmtXg2Stw909omziWnVdig', 'data': ['Транзакция успешно совершена.'], 'errors': []}
```

### 2.4 Функция 'get_permission(license_key: str, permission_id: int)'

Функция запроса разрешений.

####Обязательно:
- **license_key** - Ключ-лицензия игрока, у которого запрашивают доступ к разрешениям (str)
- **permission_id** - id запрашиваемого разрешения (int)
    - 1 - Тестовое разрешение
    - 2 - Чтение информации о банковских счетах
    - 3 - Чтение новых уведомлений
    - 4 - Пометка новых уведомлений прочитанными

Пример кода:
```python
license_key = 'kdehjfjksdhjsfj'
permission_id = 1

response = api.get_permission(license_key, permission_id)
```

### 2.5 Функция 'get_cards_info(license_key: str)'

Функция для получения информации о счетах игрока.

####Обязательно:
- **license_key** - Ключ-лицензия игрока, у которого запрашивают доступ к информации о картах (str)

Пример кода:
```python
license_key = 'kdehjfjksdhjsfj'

response = api.get_cards_info(license_key)
```

### 2.6 Функция 'get_unread_notifications(license_key: str)'

Функция для получения новых уведомлений игрока.

####Обязательно:
- **license_key** - Ключ-лицензия игрока, у которого будут получать новые уведомления (str)

Пример кода:
```python
license_key = 'kdehjfjksdhjsfj'

response = api.get_unread_notifications(license_key)
```

### 2.7 Функция 'mark_notifications_as_read(license_key: str)'

Функция для пометки новых уведомлений игрока прочитанными.

####Обязательно:
- **license_key** - Ключ-лицензия игрока, у которого новые уведомления будут отмечаться прочитанными (str)

Пример кода:
```python
license_key = 'kdehjfjksdhjsfj'

response = api.mark_notifications_as_read(license_key)
```

## 3. Немного про возвращаемое значение функциями

При удачном выполнении функции будет возвращаться json ответ в виде словаря (dict). Получить доступ к информации можно будет по ключам словаря:
- **success** - Успешен ли запрос (true / false)
- **response_key** - Секретный RESPONSE ключ вашего приложения
- **data** - Массив возвращаемых данных
- **errors** - 	Массив ошибок (при success == false)

В случае, если **response_key** ответе будет неверным, выведется `response_key error!`

Подробнее про данные, возвращаемые каждой функцией, можно глянуть [здесь](https://spk.jakksoft.com/dev/docs)