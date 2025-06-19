import allure
from locators.profile_locators import ProfilePageLocators
from pages.base_page import BasePage


class ProfilePage(BasePage):
    @allure.step('Переход в историю заказов')
    def go_to_order_history(self):
        self.click_element(ProfilePageLocators.ORDER_HISTORY_LINK)

    @allure.step('Ожидание загрузки профиля')
    def wait_for_profile_load(self):
        self.wait_until_visible(ProfilePageLocators.ORDER_HISTORY_LINK)

    @allure.step('Выход из аккаунта')
    def logout(self):
        self.click_element(ProfilePageLocators.LOGOUT_BUTTON)

    @allure.step('Получение номера последнего заказа')
    def get_last_order_number(self):
        return self.get_element_text(ProfilePageLocators.FIRST_ORDER_NUMBER)

    @allure.step('Получение названия последнего заказа')
    def get_last_order_name(self):
        return self.get_element_text(ProfilePageLocators.FIRST_ORDER_NAME)
