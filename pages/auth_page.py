import allure
from locators.auth_locators import AuthPageLocators
from pages.base_page import BasePage


class AuthPage(BasePage):
    @allure.step('Авторизация пользователя')
    def login(self, email, password):
        self.fill_input(AuthPageLocators.EMAIL_INPUT, email)
        self.fill_input(AuthPageLocators.PASSWORD_INPUT, password)
        self.click_element(AuthPageLocators.LOGIN_BUTTON)

    @allure.step('Переход на страницу восстановления пароля')
    def go_to_password_recovery(self):
        self.click_element(AuthPageLocators.PASSWORD_RECOVERY_LINK)

    @allure.step('Ввод email для восстановления пароля')
    def enter_recovery_email(self, email):
        self.fill_input(AuthPageLocators.RECOVERY_EMAIL_INPUT, email)

    @allure.step('Подтверждение восстановления пароля')
    def submit_password_recovery(self):
        self.click_element(AuthPageLocators.RECOVERY_SUBMIT_BUTTON)

    @allure.step('Ожидание страницы восстановления пароля')
    def wait_for_recovery_page(self):
        self.wait_until_visible(AuthPageLocators.NEW_PASSWORD_INPUT)

    @allure.step('Ввод нового пароля')
    def enter_new_password(self, password):
        self.fill_input(AuthPageLocators.NEW_PASSWORD_INPUT, password)

    @allure.step('Переключение видимости пароля')
    def toggle_password_visibility(self):
        self.click_element(AuthPageLocators.TOGGLE_PASSWORD_VISIBILITY_BUTTON)

    @allure.step('Проверка состояния поля пароля')
    def get_password_field_state(self):
        return self.get_element_attribute(AuthPageLocators.PASSWORD_FIELD_CONTAINER, 'class')

    @allure.step('Ожидание загрузки страницы авторизации')
    def wait_for_login_page(self):
        self.wait_until_visible(AuthPageLocators.EMAIL_INPUT)
