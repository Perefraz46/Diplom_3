import allure
import data
import url
from locators.constructor_locators import ConstructorPageLocators
from pages.auth_page import AuthPage
from pages.constructor_page import ConstructorPage


class TestConstructorFunctionality:
    @allure.title('Переход в конструктор')
    def test_navigate_to_constructor(self, driver):
        constructor_page = ConstructorPage(driver)
        constructor_page.load_page(url.LOGIN_URL)
        constructor_page.go_to_constructor()

        with allure.step('Проверка URL главной страницы'):
            assert constructor_page.get_current_url() == url.MAIN_PAGE_URL

    @allure.title('Переход в ленту заказов')
    def test_navigate_to_feed(self, driver):
        constructor_page = ConstructorPage(driver)
        constructor_page.load_page(url.MAIN_PAGE_URL)
        constructor_page.go_to_order_feed()

        with allure.step('Проверка URL страницы "Лента Заказов"'):
            assert constructor_page.get_current_url() == url.FEED_URL

    @allure.title('Открытие модального окна ингредиента')
    def test_ingredient_modal(self, driver):
        constructor_page = ConstructorPage(driver)
        constructor_page.load_page(url.MAIN_PAGE_URL)
        constructor_page.select_ingredient(data.INGREDIENTS[0])
        modal_state = constructor_page.check_modal_state()

        with allure.step('Проверка открытия модального окна'):
            assert modal_state == ConstructorPageLocators.OPENED_MODAL_CLASS

    @allure.title('Закрытие модального окна ингредиента')
    def test_close_ingredient_modal(self, driver):
        constructor_page = ConstructorPage(driver)
        constructor_page.load_page(url.MAIN_PAGE_URL)
        constructor_page.select_ingredient(data.INGREDIENTS[0])
        constructor_page.close_modal()

        with allure.step('Проверка закрытия модального окна'):
            assert constructor_page.is_modal_closed() is True

    @allure.title('Изменение счетчика ингредиента')
    def test_ingredient_counter(self, driver):
        constructor_page = ConstructorPage(driver)
        constructor_page.load_page(url.MAIN_PAGE_URL)
        constructor_page.add_ingredient_to_order(data.INGREDIENTS[0])
        counter_value = constructor_page.get_ingredient_counter(data.INGREDIENTS[0])

        with allure.step('Проверка счетчика ингредиента'):
            assert counter_value == '2'

    @allure.title('Создание заказа авторизованным пользователем')
    def test_authenticated_order(self, driver, create_user):
        constructor_page = ConstructorPage(driver)
        constructor_page.load_page(url.MAIN_PAGE_URL)
        constructor_page.go_to_profile()

        auth_page = AuthPage(driver)
        auth_page.login(create_user['email'], create_user['password'])

        constructor_page.add_ingredient_to_order(data.INGREDIENTS[0])
        constructor_page.add_ingredient_to_order(data.INGREDIENTS[1])
        constructor_page.add_ingredient_to_order(data.INGREDIENTS[2])
        constructor_page.create_order()
        modal_state = constructor_page.check_modal_state()

        with allure.step('Проверка создания заказа'):
            assert modal_state == ConstructorPageLocators.OPENED_MODAL_CLASS
