import pytest
import allure
import requests

from methods.auth_methods import Register
from data import Urls, Messages
from helpers import *


@allure.feature('Тестирование ручки регистрации пользователя')
class TestRegistration:

    @allure.title('Позитивный сценарий: Регистрация пользователя с корректными данными')
    @allure.description("""Предусловие: сгенерировать набор корректных рег. данных
                           1. Отправить запрос на создание УЗ пользователя
                           ОР: Код ответа 200, сообщение об успешном создании УЗ
                           Постусловие: удалить зарегистрированную УЗ""")
    def test_register_new_user(self,new_user):
        status = new_user[1].status_code
        message = new_user[1].json().get('success')
        assert status == 200 and message == True, f'Статус ответа {status}, текст ответа {message}'


    @allure.title('Тестирование регистрации c ранее зарегистрированным email')
    @allure.description("""Предусловие: сгенерировать набор корректных рег. данных
                           1. Отправить запрос на создание УЗ пользователя
                           2. Отправить запрос на создание УЗ с теми же данными
                           ОР: Код ответа 403, сообщение об ошибке 
                           """)
    def test_create_new_user_same_email(self, new_user):
        payload = new_user[0]
        response = Register.register_user(payload)
        status = response[1].status_code
        message = response[1].json().get('message')
        assert status == 403 and message == Messages.USER_EXISTS


    @allure.title('Тестирование регистрации без заполнения обязательных полей')
    @allure.description("""1. Отправить запрос на создание УЗ пользователя с неполными данными
                           ОР: Код ответа 403, сообщение об ошибке""")
    @pytest.mark.parametrize('payload', [{"email": "","password": "","name": ""},
                                         {"email": f'{generate_random_string(8)}@test.ts',"password": generate_random_string(8),"name": ""},
                                         {"email": f'{generate_random_string(8)}@test.ts',"password": "","name": generate_random_string(8)},
                                         {"email": "","password": generate_random_string(8),"name": generate_random_string(8)}])
    def test_create_new_user_data_not_full(self, payload):
        response = requests.post(Urls.REGISTER_URL, data=payload)
        status = response.status_code
        message = response.json().get('message')
        assert status == 403 and message == Messages.REQUIRED_FIELADS


    @allure.title('Тестирование регистрации email неверного формата')
    @allure.description('')
    def test_create_new_user_email_has_wrong_format(self):

        payload = {"email": generate_random_string(16),
                "password": generate_random_string(8),
                "name": generate_random_string(8)}
        response = requests.post(Urls.REGISTER_URL, data=payload)
        status = response.status_code
        assert status == 500

