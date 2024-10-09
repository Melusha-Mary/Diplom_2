import pytest
import helpers
from data_generators import data_generate
from api_methods import ApiMethods


@pytest.fixture
def create_user():
    user_data = data_generate()
    user_creation = ApiMethods.create_user(user_data)
    token = user_creation.json()['accessToken']
    yield [user_data, user_data["email"], user_data["password"], token]
    ApiMethods.delete_user(token)


@pytest.fixture
def collect_ingredients_hash():
    response = ApiMethods.get_ingredients_hash()
    ingredients_list = {"ingredients": [response['data'][helpers.random_int]['_id'],
                                        response['data'][helpers.random_int]['_id'],
                                        response['data'][helpers.random_int]['_id']]}
    yield ingredients_list
