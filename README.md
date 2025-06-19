# Stellar Burgers - UI Automation Tests

Этот проект содержит автоматизированные UI-тесты для веб-приложения "Stellar Burgers" (космические бургеры).

## 📌 О проекте

Набор автотестов покрывает ключевые сценарии работы с приложением:
- Авторизация и работа с профилем пользователя
- Восстановление пароля
- Конструктор бургеров
- Лента заказов
- История заказов

## 📂 Структура проекта
stellarburgers-ui-tests/
├── locators/ # Локаторы элементов
│ ├── auth_locators.py # Локаторы страницы авторизации
│ ├── constructor_locators.py # Локаторы конструктора
│ ├── feed_locators.py # Локаторы ленты заказов
│ └── profile_locators.py # Локаторы профиля
├── methods/ # API методы
│ ├── auth_service.py # Методы авторизации
│ └── user_service.py # Методы работы с пользователем
├── pages/ # Page Object модели
│ ├── auth_page.py # Страница авторизации
│ ├── base_page.py # Базовые методы
│ ├── constructor_page.py # Страница конструктора
│ ├── feed_page.py # Страница ленты заказов
│ └── profile_page.py # Страница профиля
├── tests/ # Тесты
│ ├── test_constructor.py # Тесты конструктора
│ ├── test_feed.py # Тесты ленты заказов
│ ├── test_profile.py # Тесты профиля
│ └── test_recovery.py # Тесты восстановления пароля
├── config.py # Настройки времени ожидания
├── conftest.py # Фикстуры Pytest
├── data.py # Генерация тестовых данных
├── generators.py # Фейковые данные
└── url.py # URL приложения
