import allure

from methods.order_methods import Order
from data import Messages, Order_info
from helpers import *

@allure.feature('Тестирование ручки создания заказа')
class TestRegistration:

    @allure.title('Тестирование создания заказа с корректными данными БЕЗ АВТОРИЗАЦИИ')
    @allure.description("""Предусловие: существует набор корректных ингридиентов Data.py:Burger/INGREDIENTS
                           1. Отправить запрос на создание заказа
                           ОР: Код ответа 200, сообщение об успешном создании заказа""")
    def test_unauthorize_user_create_order_positive(self):
        response = Order.create_order(Order_info.INGREDIENTS)
        status = response.status_code
        message = response.json().get('success')
        assert status == 200 and message == True


    @allure.title('Тестирование создания заказа с корректными данными АВТОРИЗОВАННЫМ пользователем')
    @allure.description("""Предусловие: существует набор корректных ингридиентов Data.py:Burger/INGREDIENTS
                           1. Отправить запрос на создание заказа
                           ОР: Код ответа 200, сообщение об успешном создании заказа""")
    def test_authorize_user_create_order_positive(self, new_user):
        accessToken = new_user[1].json().get('accessToken')
        response = Order.create_order(Order_info.INGREDIENTS, accessToken)
        status = response.status_code
        message = response.json().get('success')
        assert status == 200 and message == True


    @allure.title('Тестирование создания заказа с БЕЗ ингридиентов, АВТОРИЗОВАННЫМ пользователем')
    @allure.description("""1. Отправить запрос на создание заказа без указания ингридиентов, авторизованным пользователем
                           ОР: Код ответа 400, сообщение об ошибке""")
    def test_authorize_user_create_order_without_ingredients(self, new_user):
        accessToken = new_user[1].json().get('accessToken')
        response = Order.create_order(accessToken=accessToken)
        status = response.status_code
        message = response.json().get('message')
        assert status == 400 and message == Messages.ORDER_WITHOUT_INGREDIENTS

    @allure.title('Тестирование создания заказа БЕЗ ингридиентов, НЕАВТОРИЗОВАННЫМ пользователем')
    @allure.description("""1. Отправить запрос на создание заказа без игридиентов, без авторизации
                           ОР: Код ответа 400, сообщение об ошибке""")
    def test_unauthorize_user_create_order_without_ingredients(self):
        response = Order.create_order()
        status = response.status_code
        message = response.json().get('message')
        assert status == 400 and message == Messages.ORDER_WITHOUT_INGREDIENTS

    @allure.title('Тестирование создания заказа c неверным хэшем ингридиентов, НЕАВТОРИЗОВАННЫМ пользователем')
    @allure.description("""Предусловие: существует набор корректных ингридиентов Data.py:Burger/WRONG_INGREDIENTS
                           1. Отправить запрос на создание заказа с некоррекным хэшем в ингридиентах, без авторизации
                           ОР: Код ответа 400, сообщение об ошибке""")
    def test_unauthorize_user_create_order_incorrect_ingredients(self):
        response = Order.create_order(Order_info.WRONG_INGREDIENTS)
        status = response.status_code
        message = response.json().get('message')
        assert status == 400 and message == Messages.INCORRECT_INGREDIENTS
