# Diplom_2
# Автотесты для проверки веб-приложения Stellar Burgers

Этот проект предназначен для автоматизированного тестирования [API](https://code.s3.yandex.net/qa-automation-engineer/python-full/diploma/api-documentation.pdf?etag=3403196b527ca03259bfd0cb41163a89)
веб-сервиса "[Stellar Burgers](https://stellarburgers.nomoreparties.site/)".

## Структура проекта

Основная структура проекта автотестов - Директория tests:

    test_user_update.py - Проверка создания пользователя
    test_order_creation.py - Проверка логина пользователя
    test_user_creation.py - Проверка изменения данных пользователя
    test_get_user_orders.py - Проверка создание заказа
    test_user_login.py - Проверка получения заказов конкретного пользователя


## Инструкции по запуску

1. **Установить зависимости:**

pip install -r requirements.txt


2 **Запуск тестов с использованием pytest:**

pytest --alluredir=allure_results


3 **Генерация и просмотр отчетов Allure:**

allure serve allure_results


## Используемые технологии и инструменты

- **Pytest**: Фреймворк для написания и запуска тестов.
- **Requests**: Библиотека для отправки HTTP-запросов.
- **Allure**: Инструмент для создания наглядных отчетов о тестировании.
- **Faker**: Библиотека для генерации тестовых данных.

