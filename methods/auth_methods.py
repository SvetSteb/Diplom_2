import requests
import allure

from helpers import *
from data import Urls

class Register:

    @staticmethod
    @allure.step('Регистрация пользователя')
    def register_user(payload):
        response = requests.post(Urls.REGISTER_URL, data=payload)
        auth_data = []
        if response.status_code == 200:
            auth_data = payload
        return auth_data, response

    @staticmethod
    @allure.step('Удаление УЗ пользователя')
    def delete_user(auth_token):
        delete = requests.delete(Urls.USER_URL, headers={'Authorization': auth_token})
        return delete
    
    @staticmethod
    @allure.step('Логин пользователя')
    def login_user(payload):
        response = requests.post(Urls.LOGIN_URL, data=payload)
        return response
    
    @staticmethod
    @allure.step('Получение данных УЗ пользователя')
    def get_user_info(accessToken):
        response = requests.get(Urls.USER_URL, headers={'Authorization': accessToken})
        return response
    
    @staticmethod
    @allure.step('Изменение данных УЗ пользователя')
    def change_user_info(data, accessToken=None):
        response = requests.patch(Urls.USER_URL, data=data, headers={'Authorization': accessToken})
        return response
    