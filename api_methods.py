import allure
import requests

from endpoints import Url


class ApiMethods:

    @staticmethod
    @allure.step("Регистрация пользователя")
    def create_user(body):
        return requests.post(f'{Url.MAIN_URL}{Url.CREATE_USER}', json=body)

    @staticmethod
    @allure.step("Удаление пользователя")
    def delete_user(token):
        return requests.delete(f'{Url.MAIN_URL}{Url.DELETE_USER}', headers={'Authorization': token})

    @staticmethod
    @allure.step("Авторизация пользователя")
    def login_user(body):
        return requests.post(f'{Url.MAIN_URL}{Url.LOGIN}', json=body)

    @staticmethod
    @allure.step("Изменение данных пользователя (с токеном)")
    def update_user_data_with_token(token, body):
        return requests.patch(f'{Url.MAIN_URL}{Url.UPDATE_USER_DATA}', json=body, headers={
            'Authorization': token})

    @staticmethod
    @allure.step("Изменение данных пользователя")
    def update_user_data_no_token(body):
        return requests.patch(f'{Url.MAIN_URL}{Url.UPDATE_USER_DATA}', json=body)

    @staticmethod
    @allure.step("Получение списка ингредиентов")
    def get_ingredients_hash():
        return requests.get(f'{Url.MAIN_URL}{Url.GET_INGREDIENTS}').json()

    @staticmethod
    @allure.step("Создание заказа (с авториз)")
    def create_order_auth(body, token):
        return requests.post(f'{Url.MAIN_URL}{Url.CREATE_ORDER}', json=body, headers={
            'Authorization': token})

    @staticmethod
    @allure.step("Создание заказа (без авториз)")
    def create_order_non_auth(body):
        return requests.post(f'{Url.MAIN_URL}{Url.CREATE_ORDER}', json=body)

    @staticmethod
    @allure.step("Получение заказов пользователя (с авториз) ")
    def get_orders_auth(token):
        return requests.get(f'{Url.MAIN_URL}{Url.GET_ORDERS}', headers={
            'Authorization': token})

    @staticmethod
    @allure.step("Получение заказов пользователя (без авториз) ")
    def get_orders_no_auth():
        return requests.get(f'{Url.MAIN_URL}{Url.GET_ORDERS}')
