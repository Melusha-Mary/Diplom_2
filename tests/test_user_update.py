import allure
import pytest
from data_generators import data_generate, SingleDataFiled
from api_methods import ApiMethods
from endpoints import ErrorMessageText


@allure.feature("Изменение данных пользователя")
class TestUserUpdate:

    @allure.title("Успешное изменение данных авторизованного пользователя")
    @pytest.mark.parametrize('data_field, new_data', (['email', SingleDataFiled.email], [
        'name', SingleDataFiled.name], ["password", SingleDataFiled.password]))
    def test_user_update_success(self, create_user, data_field, new_data):
        create_user[0][data_field] = new_data
        response = ApiMethods.update_user_data_with_token(create_user[3], create_user[0])
        assert response.status_code == 200 and response.json()['success'] == True

    @allure.title("Попытка изменения данных неавторизованного пользователя")
    def test_user_update_non_auth_error(self, create_user):
        updated_user_data = data_generate()
        response = ApiMethods.update_user_data_no_token(updated_user_data)
        assert response.status_code == 401 and response.json()['message'] == ErrorMessageText.USER_DATA_UPDATE_ERROR