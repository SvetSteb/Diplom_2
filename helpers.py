import random
import string
import faker as f
import allure

def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

@allure.step('Генерация новых рег.данных')
def generate_user_data():
        fake = f.Faker()
        #генерация email выполнена более примитивным способом, чем с помощью faker
        #из-за частого повторнения email и возникающей ошибки already exist
        data = {"email": f'{generate_random_string(8)}@{generate_random_string(4)}.{generate_random_string(3)}',
                "password": generate_random_string(8),
                "name": fake.first_name()}

        return data
