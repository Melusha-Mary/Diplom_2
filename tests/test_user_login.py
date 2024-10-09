import pytest
import allure
from api_methods import ApiMethods
from endpoints import ErrorMessageText

@allure.feature("Создание пользователя")
class TestUserLogin:

    @allure.title("Успешная авторизация существующего пользователя")
    def test_user_login_success(self, create_user):
        login_data = {'email': create_user[1], 'password': create_user[2]}
        response = ApiMethods.login_user(login_data)
        assert response.status_code == 200 and (response.json()['success'] == True)

    @allure.title('Проверка на ошибку при вводе неправильного пароля пользователя')
    def test_user_login_with_invalid_password(self, create_user):
        login_data = {'email': create_user[1], 'password': 'test_password'}
        response = ApiMethods.login_user(login_data)
        assert response.status_code == 401 and (response.json()['message'] == ErrorMessageText.INCORRECT_DATA)

