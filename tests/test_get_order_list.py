import allure

from methods.order_methods import Order
from data import Messages
from helpers import *

@allure.feature('Тестирование ручки получения списка заказов')
class TestOrdersList:

    @allure.title('Тестирование получения списка заказов пользователем БЕЗ АВТОРИЗАЦИИ')
    @allure.description("""Предусловие: существует набор корректных ингридиентов Data.py:Burger/INGREDIENTS
                           1. Отправить запрос на получение списка заказов без авторизации
                           ОР: Код ответа 401, сообщение об ошибке""")
    def test_unauthorize_user_get_orders_list(self):
        response = Order.get_users_orders_list()
        status = response.status_code
        message = response.json().get('message')
        assert status == 401 and message == Messages.UNAUTH_USER


    @allure.title('Тестирование получения списка заказов АВТОРИЗОВАННОГО пользователя')
    @allure.description("""Предусловие: существует набор корректных ингридиентов Data.py:Burger/INGREDIENTS
                            Предусловие: создается новый пользователь, новый заказ пользователя
                           1. Отправить запрос на получение списка заказов созданого пользователя (с авторизацией)
                           ОР: Код ответа 200, в ответе содержится созданный заказ""")
    def test_authorize_user_get_orders_list(self, new_order):
        accessToken, order_id = new_order
        response = Order.get_users_orders_list(accessToken)
        status = response.status_code
        message = response.text
        assert status == 200 and order_id in message

