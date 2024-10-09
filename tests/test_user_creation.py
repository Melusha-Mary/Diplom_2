import pytest
import allure
from data_generators import data_generate, InvalidUserData
from api_methods import ApiMethods
from endpoints import ErrorMessageText


class TestCreateUser:

    @allure.title("Успешное создание нового пользователя")
    def test_create_user_success(self):
        body = data_generate()
        creation_user = ApiMethods.create_user(body)
        token = creation_user.json()['accessToken']
        assert creation_user.status_code == 200 and ('accessToken' in creation_user.json())
        ApiMethods.delete_user(token)

    @allure.title("Попытка создания уже существующего пользователя")
    def test_create_user_clone_error(self, create_user):
        response = ApiMethods.create_user(create_user[0])
        assert response.status_code == 403 and (response.json()['message'] == ErrorMessageText.USER_ALREADY_EXIST)

    @allure.title('Ошибка регистрации пользователя с недостающими данными')
    @pytest.mark.parametrize('data', InvalidUserData.invalid_data)
    def test_create_user_deficit_data_error(self, data):
        response = ApiMethods.create_user(data)
        assert response.status_code == 403 and (response.json()['message'] == ErrorMessageText.DEFICIT_DATA)


