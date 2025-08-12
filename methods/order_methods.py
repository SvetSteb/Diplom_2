import requests
import allure

from helpers import *
from data import Urls

class Order:

    @staticmethod
    @allure.step('Создание заказа')
    def create_order(ingredients=None, accessToken=None):
        response = requests.post(Urls.ORDER_URL, data=ingredients, headers={'Authorization': accessToken})
        return response
    

    @staticmethod
    @allure.step('Получение списка заказа пользователя')
    def get_users_orders_list(accessToken=None):
        response = requests.get(Urls.ORDER_URL, headers={'Authorization': accessToken})
        return response
    