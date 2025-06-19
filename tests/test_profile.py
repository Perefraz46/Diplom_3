import allure
import url
from pages.auth_page import AuthPage
from pages.constructor_page import ConstructorPage
from pages.profile_page import ProfilePage


class TestProfile:
    @allure.title('Переход в личный кабинет')
    def test_navigate_to_profile(self, driver, create_user):
        constructor_page = ConstructorPage(driver)
        constructor_page.load_page(url.MAIN_PAGE_URL)
        constructor_page.go_to_profile()

        auth_page = AuthPage(driver)
        auth_page.login(create_user['email'], create_user['password'])
        constructor_page.go_to_profile()

        profile_page = ProfilePage(driver)
        profile_page.wait_for_profile_load()

        with allure.step('Проверка URL профиля'):
            assert profile_page.get_current_url() == url.PERSONAL_ACCOUNT_URL

    @allure.title('Переход в историю заказов')
    def test_navigate_to_order_history(self, driver, create_user):
        constructor_page = ConstructorPage(driver)
        constructor_page.load_page(url.MAIN_PAGE_URL)
        constructor_page.go_to_profile()

        auth_page = AuthPage(driver)
        auth_page.login(create_user['email'], create_user['password'])
        constructor_page.go_to_profile()

        profile_page = ProfilePage(driver)
        profile_page.go_to_order_history()

        with allure.step('Проверка URL истории заказов'):
            assert profile_page.get_current_url() == url.ORDER_HISTORY_URL

    @allure.title('Выход из аккаунта')
    def test_logout(self, driver, create_user):
        constructor_page = ConstructorPage(driver)
        constructor_page.load_page(url.MAIN_PAGE_URL)
        constructor_page.go_to_profile()

        auth_page = AuthPage(driver)
        auth_page.login(create_user['email'], create_user['password'])
        constructor_page.go_to_profile()

        profile_page = ProfilePage(driver)
        profile_page.logout()
        auth_page.wait_for_login_page()

        with allure.step('Проверка URL страницы авторизации'):
            assert auth_page.get_current_url() == url.LOGIN_URL
