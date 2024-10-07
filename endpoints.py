class Url:
    MAIN_URL = "https://stellarburgers.nomoreparties.site"
    CREATE_USER = "/api/auth/register"
    LOGIN = "/api/auth/login"
    CREATE_ORDER = "/api/orders"
    DELETE_USER = "/api/auth/user"
    UPDATE_USER_DATA = '/api/auth/user'
    GET_INGREDIENTS = "/api/ingredients"
    GET_ORDERS = "/api/orders"


class ErrorMessageText:
    INCORRECT_DATA = 'email or password are incorrect'
    USER_NOT_FOUND = "Учетная запись не найдена"
    USER_ALREADY_EXIST = "User already exists"
    DEFICIT_DATA = "Email, password and name are required fields"
    USER_DATA_UPDATE_ERROR = "You should be authorised"
    NOT_ENOUGH_INGREDIENTS = "Ingredient ids must be provided"
    GET_ORDERS_ERROR = "You should be authorised"
