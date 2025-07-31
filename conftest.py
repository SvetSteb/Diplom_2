import pytest
from methods.auth_methods import Register
from methods.order_methods import Order
from data import Order_info
from helpers import *

@pytest.fixture
def new_user():
    payload = generate_user_data()
    result = Register.register_user(payload)
    auth_token = result[1].json().get('accessToken')
    yield result
    Register.delete_user(auth_token)

@pytest.fixture
def new_order(new_user):
    accessToken = new_user[1].json().get('accessToken')
    response = Order.create_order(Order_info.INGREDIENTS, accessToken)
    order_id = str(response.json()['order'].get("number"))
    return accessToken, order_id

