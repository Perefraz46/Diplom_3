import allure
from selenium.common import TimeoutException, ElementClickInterceptedException
from locators.constructor_locators import ConstructorPageLocators
from pages.base_page import BasePage


class ConstructorPage(BasePage):
    @allure.step('Переход в личный кабинет')
    def go_to_profile(self):
        self.click_element(ConstructorPageLocators.PROFILE_LINK)

    @allure.step('Переход в конструктор')
    def go_to_constructor(self):
        self.click_element(ConstructorPageLocators.CONSTRUCTOR_LINK)

    @allure.step('Переход в ленту заказов')
    def go_to_order_feed(self):
        self.click_element(ConstructorPageLocators.ORDER_FEED_LINK)

    @allure.step('Выбор ингредиента')
    def select_ingredient(self, ingredient_id):
        self.click_element(ConstructorPageLocators.get_ingredient_locator(ingredient_id))

    @allure.step('Проверка отсутствия модального окна')
    def is_modal_closed(self):
        try:
            self.wait_until_invisible(ConstructorPageLocators.MODAL_WINDOW)
            return True
        except TimeoutException:
            return False

    @allure.step('Проверка состояния модального окна')
    def check_modal_state(self):
        return self.get_element_attribute(ConstructorPageLocators.MODAL_WINDOW, 'class')

    @allure.step('Закрытие модального окна')
    def close_modal(self):
        self.click_element(ConstructorPageLocators.MODAL_CLOSE_BUTTON)

    @allure.step('Закрытие окна заказа')
    def close_order_modal(self):
        self.click_with_overlay_wait(ConstructorPageLocators.MODAL_CLOSE_BUTTON,
                                   'visibility', 'hidden', 'visible')

    @allure.step('Добавление ингредиента в заказ')
    def add_ingredient_to_order(self, ingredient_id):
        self.drag_and_drop(
            ConstructorPageLocators.get_ingredient_locator(ingredient_id),
            ConstructorPageLocators.CONSTRUCTOR_DROP_AREA
        )

    @allure.step('Получение счетчика ингредиента')
    def get_ingredient_counter(self, ingredient_id):
        return self.get_element_text(ConstructorPageLocators.get_ingredient_counter_locator(ingredient_id))

    @allure.step('Создание заказа')
    def create_order(self):
        self.click_element(ConstructorPageLocators.CREATE_ORDER_BUTTON)

    @allure.step('Получение номера заказа')
    def get_order_number(self):
        return self.get_element_text(ConstructorPageLocators.ORDER_NUMBER_TEXT)
