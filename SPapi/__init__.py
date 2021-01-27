"""
SPapi v1.1.2 by Spagetik
"""
from requests import post


# Errors
class Error(Exception):
    pass


class SpApiError(Error):
    pass


class Card:

    def __init__(self, data: dict):
        self.id = int(data['id'])
        self.name = data['name']
        self.balance = int(data['balance'])
        self.bg_color = data['bg_color']
        self.font_color = data['font_color']
        self.image = data['image']

    def __repr__(self):
        return f'<id={self.id}>\n<name={self.name}>\n<balance={self.balance}>\n<bg_color={self.bg_color}>\n<font_color={self.font_color}>\n<image={self.image}>'


class Notify:

    def __init__(self, data: dict):
        self.id = int(data['id'])
        self.type = int(data['type'])
        self.type_title = data['type_title']
        self.message = data['message']
        self.time = int(data['time'])

    def __repr__(self):
        return f'<id={self.id}>\n<type={self.type}>\n<type_title={self.type_title}>\n<message={self.message}>\n<time={self.time}>'


class Response:
    """
    Методы:

    * success - успешен ли запрос (True or False)
    * response_key - ключ ответа от сервера (str)
    * data - массив полученных данных (list)
    * errors - массив с ошибками, если они есть (list)
    """

    def __init__(self, response: dict):
        self.success = response['success']
        self.response_key = response['response_key']
        try:
            if len(response['data'][0].keys()) == 6:
                self.data = []
                for data in response['data']:
                    self.data.append(Card(data))
            elif len(response['data'][0].keys()) == 5:
                self.data = []
                for data in response['data']:
                    self.data.append(Notify(data))
            else:
                self.data = response['data']
        except:
            self.data = response['data']
        self.errors = response['errors']

    def __repr__(self):
        return f'<success={self.success}>\n<response_key={self.response_key}>\n<data={self.data}>'


class SpApi:

    # Приватные функции
    def __init__(self, server: str, token: str, response_key: str):
        self.server = server
        self.token = token
        self.response_key = response_key

    def __repr__(self):
        return f"<SpApi server={self.server}>\n<SpApi token={self.token}>"

    # Функция отправки запроса
    def post_request(self, action: str, data=None):
        if data is None:
            data = {}
        data.update({'token': self.token, 'action': action})
        response_data = post(f'https://{self.server}.jakksoft.com/api/request', data=data).json()
        response = Response(response_data)
        if self.response_key == response.response_key:
            return response
        else:
            return SpApiError(f'Response Key error! Response Key is "{response.response_key}" but have to be "{self.response_key}"')

    # Вызываемые функции
    def test(self):
        return self.post_request('test')

    def permission_test(self, your_license_key: str):
        """
        Тест ВАШИХ прав приложения.

        :param your_license_key: ВАШ ключ-лицензия из личного кабинета.

        :return: Возвращает ответ в виде json (словаря).
        """
        return self.post_request('permission_test', data={'license_key': your_license_key})

    def pay(self, sp_pay_code: int, summa: int, trans_mes='Оплата SP-pay'):
        """
        Оплата ваших услуг игроками.

        :param sp_pay_code: Код SP-pay, полученный игроком на сайте.

        :param summa: Сумма оплаты.

        :param trans_mes: Сообщение, привязанное к транзакции (ОПЦИОНАЛЬНО).

        :return: Возвращает ответ в виде json (словаря)
        """
        return self.post_request('pay', data={'spPayCode': sp_pay_code, 'sum': summa, 'transactionMessage': trans_mes})

    def get_permission(self, license_key: str, permission_id: int):
        """
        Запрос прав доступа к некоторым возможностям.

        **1** - Тестовое разрешение.

        **2** - Чтение информации о банковских счетах.

        **3** - Чтение уведомлений.

        **4** - Пометка уведомлений прочитанными.

        :param license_key: ключ-лицензия из личного кабинета игрока.

        :param permission_id: номер разрешения, все разрешения указаны выше.

        :return: Возвращает ответ в виде json (словаря)
        """
        return self.post_request('get_permission', data={'license_key': license_key, 'permission_id': permission_id})

    def get_cards_info(self, license_key: str):
        """
        Получить информацию о карте.

        :param license_key: ключ-лицензия из личного кабинета игрока.

        :return: возвращает ответ в виде json (словаря)
        """
        return self.post_request('get_cards_info', data={'license_key': license_key})

    def get_unread_notifications(self, license_key: str):
        """
        Получить непрочитанные уведомления с сайта.

        :param license_key: ключ-лицензия из личного кабинета игрока.

        :return: возвращает ответ в виде json (словаря)
        """
        return self.post_request('get_unread_notifications', data={'license_key': license_key})

    def mark_notifications_as_read(self, license_key: str):
        """
        Отметить непрочитанные уведомления как прочитанные.

        :param license_key: ключ-лицензия из личного кабинета игрока.

        :return: возвращает ответ в виде json (словаря)
        """
        return self.post_request('mark_notifications_as_read', data={'license_key': license_key})
