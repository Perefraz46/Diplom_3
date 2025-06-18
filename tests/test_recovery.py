import allure
import url
from generators import fake_data
from locators.auth_locators import AuthPageLocators
from pages.auth_page import AuthPage
from pages.constructor_page import ConstructorPage


class TestPasswordRecovery:
    @allure.title('Переход на страницу восстановления пароля')
    def test_navigate_to_recovery(self, driver):
        constructor_page = ConstructorPage(driver)
        constructor_page.load_page(url.MAIN_PAGE_URL)
        constructor_page.go_to_profile()

        auth_page = AuthPage(driver)
        auth_page.go_to_password_recovery()

        with allure.step('Проверка URL страницы восстановления'):
            assert auth_page.get_current_url() == url.FORGOT_PASSWORD_URL

    @allure.title('Восстановление пароля')
    def test_password_recovery_flow(self, driver):
        _, email, _ = fake_data()
        constructor_page = ConstructorPage(driver)
        constructor_page.load_page(url.MAIN_PAGE_URL)
        constructor_page.go_to_profile()

        auth_page = AuthPage(driver)
        auth_page.go_to_password_recovery()
        auth_page.enter_recovery_email(email)
        auth_page.submit_password_recovery()
        auth_page.wait_for_recovery_page()

        with allure.step('Проверка перехода на страницу сброса пароля'):
            assert auth_page.get_current_url() == url.RESET_PASSWORD_URL

    @allure.title('Переключение видимости пароля')
    def test_password_visibility_toggle(self, driver):
        _, email, password = fake_data()
        constructor_page = ConstructorPage(driver)
        constructor_page.load_page(url.MAIN_PAGE_URL)
        constructor_page.go_to_profile()

        auth_page = AuthPage(driver)
        auth_page.go_to_password_recovery()
        auth_page.enter_recovery_email(email)
        auth_page.submit_password_recovery()
        auth_page.enter_new_password(password)
        auth_page.toggle_password_visibility()
        field_state = auth_page.get_password_field_state()

        with allure.step('Проверка состояния поля пароля'):
            assert AuthPageLocators.ACTIVE_PASSWORD_FIELD_CLASS in field_state
