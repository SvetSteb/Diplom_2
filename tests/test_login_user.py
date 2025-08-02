import pytest
import allure

from methods.auth_methods import Register
from data import Messages, User
from helpers import *

@allure.feature('Тестирование ручки логина пользователя')
class TestRegistration:

    @allure.title('Тестирование авторизации существующего пользователя с корректными данными')
    @allure.description("""Предусловие: сгенерировать набор корректных рег. данных
                           1. Отправить запрос на создание УЗ пользователя
                           2. Отправить запрос на логин пользователя
                           ОР: Код ответа 200, сообщение об успешном создании УЗ
                           Постусловие: удалить зарегистрированную УЗ""")
    def test_login_user_positive(self, new_user):
        data = new_user[0]
        del data['name']
        response = Register.login_user(data)
        status = response.status_code
        message = response.json().get('success')
        assert status == 200 and message == True, f'Статус ответа {status}, текст ответа {message}'


    @allure.title('Тестирование авторизации с некоррекными авторизационными данными')
    @allure.description("""1. Отправить запрос логин с некоррекными данными
                           ОР: Код ответа 201, сообщение об успешном создании УЗ""")
    @pytest.mark.parametrize('data',  [{"email": User.USER_EMAIL,"password": generate_random_string(8)},
                                         {"email": f'{generate_random_string(8)}@test.ts',"password": User.USER_PASSWORD},
                                         {"email": User.USER_EMAIL,"password": ""},
                                         {"email": "","password": ""}])
    def test_login_user_incorrect_data(self, data):
        response = Register.login_user(data)
        status = response.status_code
        message = response.json().get('message')
        assert status == 401 and message == Messages.PASSWORD_INCORRECT, f'Статус ответа {status}, текст ответа {message}'
