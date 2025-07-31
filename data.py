class Urls:
    URL = 'https://stellarburgers.nomoreparties.site/api/'
    AUTH_URL = f'{URL}auth/'
    REGISTER_URL = f'{AUTH_URL}register/'
    REFRESH_URL = f'{AUTH_URL}token/'
    USER_URL = f'{AUTH_URL}user/'
    LOGIN_URL = f'{AUTH_URL}login/'
    ORDER_URL = f'{URL}orders/'

class Messages:
    USER_EXISTS = "User already exists"
    REQUIRED_FIELADS = "Email, password and name are required fields"
    PASSWORD_INCORRECT = "email or password are incorrect"
    EMAIL_EXIST = "User with such email already exists"
    UNAUTH_USER = "You should be authorised"
    ORDER_WITHOUT_INGREDIENTS = "Ingredient ids must be provided"
    INCORRECT_INGREDIENTS = "One or more ids provided are incorrect"
    

class User:
    #зарегистрированный пользователь
    USER_EMAIL = 'sveta1@ggmail.ru'
    USER_PASSWORD = '2345678975'

    #корректные рег.данные для параметризованного теста изменения УЗ
    #удалять УЗ после теста с указанными данными
    USER_INFO = {"email": 'sveta3_test@ttest.ts',
                "password": '123456',
                "name": 'Svetlana'}

class Order_info:

    INGREDIENTS = {"ingredients": ["61c0c5a71d1f82001bdaaa6d","61c0c5a71d1f82001bdaaa71"]}
    WRONG_INGREDIENTS = {"ingredients": ["61c0c5a71d1f82001bdaba6d","61c0c5a71d1f82001ddaaa71"]}
    