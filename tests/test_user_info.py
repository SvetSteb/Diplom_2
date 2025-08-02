import pytest
import allure

from methods.auth_methods import Register
from data import Messages, User
from helpers import *


@allure.feature('Тестирование ручки получения и изменения данных УЗ пользователя')
class TestModifyUser:

    @allure.title('Получение данных зарегистрированного пользователя')
    @allure.description("""Предусловие: сгенерировать набор корректных рег. данных
                           1. Отправить запрос на создание УЗ пользователя
                           2. Отправить запрос на получение данных УЗ пользователя
                           ОР: Код ответа 200, сообщение об успешной обработке запроса
                           Постусловие: удалить зарегистрированную УЗ""")
    def test_get_new_user_info(self,new_user):
        data, registr_result = new_user
        del data['password']
        accessToken = registr_result.json().get('accessToken')
        response = Register.get_user_info(accessToken)
        status = response.status_code
        message = response.json().get('success')
        user_info = response.json().get('user')
        assert status == 200 and user_info == data and message == True, f'Статус ответа {status}, текст ответа {message}'


    @allure.title('Изменение данных зарегистрированного пользователя С АВТОРИЗАЦИЕЙ')
    @allure.description("""Предусловие: в файле data.py:User/USER_INFO определен статичный набор корректных рег.данных
                           1. Отправить запрос на создание УЗ пользователя
                           2. Отправить запрос на изменение данных УЗ пользователя
                           ОР: Код ответа 200, сообщение об успешной обработке запроса
                           Постусловие: удалить зарегистрированную УЗ""")
    @pytest.mark.parametrize('new_data', [{"email": f'{generate_random_string(8)}@ttest.tss',"password": User.USER_INFO.get("password"),"name": User.USER_INFO.get("name")},
                                            {"email": User.USER_INFO.get('email'),"password": generate_random_string(8),"name": User.USER_INFO.get("name")},
                                            {"email": User.USER_INFO.get('email'),"password":User.USER_INFO.get("password"),"name": generate_random_string(6)}])
    def test_change_users_info_parametrize(self, new_data):
        registr_result= Register.register_user(User.USER_INFO)
        accessToken = registr_result[1].json().get('accessToken')
        response = Register.change_user_info(new_data, accessToken)
        status = response.status_code
        message = response.json().get('success')
        user_info = response.json().get('user')
        del new_data['password']
        assert status == 200 and user_info == new_data and message == True, f'Статус ответа {status}, текст ответа {message}'
        Register.delete_user(accessToken)


    @allure.title('Изменение EMAIL пользователя на уже использующийся, С АВТОРИЗАЦИЕЙ')
    @allure.description("""Предусловие: сгенерировать набор корректных рег. данных
                           1. Отправить запрос на создание УЗ пользователя
                           2. Отправить запрос на изменение данных УЗ пользователя
                           ОР: Код ответа 403, сообщение об ошибке
                           Постусловие: удалить зарегистрированную УЗ""")
    def test_change_users_email_set_exist_email(self, new_user):
        data, registr_result = new_user
        accessToken = registr_result.json().get('accessToken')
        data['email'] = User.USER_EMAIL
        response = Register.change_user_info(data, accessToken)
        status = response.status_code
        message = response.json().get('message')
        assert status == 403 and message == Messages.EMAIL_EXIST, f'Статус ответа {status}, текст ответа {message}'


    @allure.title('Изменение данных пользователя БЕЗ АВТОРИЗАЦИИ')
    @allure.description("""Предусловие: в файле data.py:User/USER_INFO определен статичный набор корректных рег.данных
                           1. Отправить запрос на создание УЗ пользователя
                           2. Отправить запрос на изменение данных УЗ пользователя БЕЗ АВТОРИЗАЦИИ
                           ОР: Код ответа 200, сообщение об успешной обработке запроса
                           Постусловие: удалить зарегистрированную УЗ""")
    @pytest.mark.parametrize('new_data', [{"email": f'{generate_random_string(8)}@ttest.tss',"password": User.USER_INFO.get("password"),"name": User.USER_INFO.get("name")},
                                            {"email": User.USER_INFO.get('email'),"password": generate_random_string(8),"name": User.USER_INFO.get("name")},
                                            {"email": User.USER_INFO.get('email'),"password":User.USER_INFO.get("password"),"name": generate_random_string(6)}])
    def test_change_users_info_without_auth(self, new_data):
        registr_result= Register.register_user(User.USER_INFO)
        accessToken = registr_result[1].json().get('accessToken')
        response = Register.change_user_info(new_data)
        status = response.status_code
        message = response.json().get('message')
        assert status == 401 and message == Messages.UNAUTH_USER, f'Статус ответа {status}, текст ответа {message}'
        Register.delete_user(accessToken)

    