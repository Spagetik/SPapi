"""
SPapi v1.1.0 by SPagetik
"""


from requests import post


# Errors
class Error(Exception):
    pass


class SpApiError(Error):
    print(Error)


class SpApi:
    # Приватные функции
    def __init__(self, server: str, token: str, response_key: str):
        self.server = server
        self.token = token
        self.response_key = response_key

    def __repr__(self):
        return f"<SpApi server={self.server}>\n<SpApi token={self.token}>"

    def post_request(self, action: str, data=None):
        if data is None:
            data = {}
        data.update({'token': self.token, 'action': action})
        response = post(f'https://{self.server}.jakksoft.com/api/request', data=data)
        if self.response_key == response.json().get('response_key'):
            return response.json()
        else:
            return SpApiError('response_key error!')

    # Вызываемые функции
    def test(self):
        return self.post_request('test')

    def permission_test(self, your_license_key: str):
        """
        Тест ВАШИХ прав приложения.

        :param your_license_key: ВАШ ключ-лицензия из личного кабинета.

        :return: Возращает ответ в виде json (словаря).
        """
        return self.post_request('permission_test', data={'license_key': your_license_key})

    def pay(self, sp_pay_code: int, summa: int, trans_mes='Оплата SP-pay'):
        """
        Оплата ваших услуг игроками.

        :param sp_pay_code: Код SP-pay, полученный игроком на сайте.

        :param summa: Сумма оплаты.

        :param trans_mes: Сообщение, привязанное к транзакции (ОПЦИОНАЛЬНО).

        :return: Возращает ответ в виде json (словаря)
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

        :return: Возращает ответ в виде json (словаря)
        """
        return self.post_request('get_permission', data={'license_key': license_key, 'permission_id': permission_id})

    def get_cards_info(self, license_key: str):
        """
        Получить информацию о карте.

        :param license_key: ключ-лицензия из личного кабинета игрока.

        :return: возращает ответ в виде json (словаря)
        """
        return self.post_request('get_cards_info', data={'license_key': license_key})

    def get_unread_notifications(self, license_key: str):
        """
        Получить непрочитаные уведомления с сайта.

        :param license_key: ключ-лицензия из личного кабинета игрока.

        :return: возращает ответ в виде json (словаря)
        """
        return self.post_request('get_unread_notifications', data={'license_key': license_key})

    def mark_notifications_as_read(self, license_key: str):
        """
        Отметить непрочитанные уведомления как прочитанные.

        :param license_key: ключ-лицензия из личного кабинета игрока.

        :return: возращает ответ в виде json (словаря)
        """
        return self.post_request('mark_notifications_as_read', data={'license_key': license_key})
