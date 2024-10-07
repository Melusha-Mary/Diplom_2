import allure
from api_methods import ApiMethods
from endpoints import ErrorMessageText
from order_data import OrderData

@allure.feature("Создание заказа")
class TestOrderCreation:

    @allure.title('Успешное создание заказа с авторизацией')
    def test_create_order_with_auth_success(self, create_user, collect_ingredients_hash):
        response = ApiMethods.create_order_auth(collect_ingredients_hash, create_user[3])
        assert response.status_code == 200 and response.json()["success"] == True

    @allure.title('Успешное создание заказа без авторизациии')
    def test_create_order_with_no_auth_success(self, collect_ingredients_hash):
        response = ApiMethods.create_order_non_auth(collect_ingredients_hash)
        assert response.status_code == 200 and response.json()["success"] == True

    @allure.title('Создание заказа без ингредиентов и без авторизациии')
    def test_create_order_no_ingredients_no_auth(self):
        response = ApiMethods.create_order_non_auth(OrderData.null_ingredients)
        assert response.status_code == 400 and response.json()['message'] == ErrorMessageText.NOT_ENOUGH_INGREDIENTS

    @allure.title('Создание заказа без ингредиентов, но с авторизацией')
    def test_create_order_no_ingredients_with_auth(self, create_user):
        response = ApiMethods.create_order_auth(OrderData.null_ingredients, create_user[3])
        assert response.status_code == 400 and response.json()['message'] == ErrorMessageText.NOT_ENOUGH_INGREDIENTS

    @allure.title('Создание заказа с неправильными ингредиентами')
    def test_create_order_with_invalid_ingredients(self):
        response = ApiMethods.create_order_non_auth(OrderData.invalid_ingredients)
        assert response.status_code == 500
