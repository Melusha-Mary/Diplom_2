import allure
from api_methods import ApiMethods
from endpoints import ErrorMessageText

@allure.feature("Получение заказов пользователя")
class TestGetUserOrders:

    @allure.title("Успешное получение заказов авторизованным пользователем")
    def test_get_orders_auth_user(self, create_user, collect_ingredients_hash):
        ApiMethods.create_order_auth(collect_ingredients_hash, create_user[3])
        response = ApiMethods.get_orders_auth(create_user[3])
        assert response.status_code == 200 and "orders" in response.text

    @allure.title("Попытка получения заказов неавторизованным пользователем")
    def test_get_orders_non_auth_user(self):
        response = ApiMethods.get_orders_no_auth()
        assert response.status_code == 401 and response.json()['message'] == ErrorMessageText.GET_ORDERS_ERROR
