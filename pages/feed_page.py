import allure
from locators.feed_locators import FeedPageLocators
from pages.base_page import BasePage


class FeedPage(BasePage):
    @allure.step('Выбор заказа')
    def select_order(self):
        self.click_element(FeedPageLocators.FIRST_ORDER_IN_LIST)

    @allure.step('Проверка состояния модального окна')
    def check_modal_state(self):
        return self.get_element_attribute(FeedPageLocators.ORDER_DETAILS_MODAL, 'class')

    @allure.step('Получение номера заказа')
    def get_order_number_text(self, number):
        return self.get_element_text(FeedPageLocators.get_order_number_locator(number))

    @allure.step('Получение названия заказа')
    def get_order_name_text(self, name):
        return self.get_element_text(FeedPageLocators.get_order_name_locator(name))

    @allure.step('Получение общего количества заказов')
    def get_total_orders_count(self):
        return self.get_element_text(FeedPageLocators.TOTAL_ORDERS_COUNT)

    @allure.step('Получение количества заказов за сегодня')
    def get_today_orders_count(self):
        return self.get_element_text(FeedPageLocators.TODAY_ORDERS_COUNT)

    @allure.step('Получение номера заказа в работе')
    def get_in_progress_order_number(self):
        return self.get_element_text(FeedPageLocators.ORDERS_IN_PROGRESS_LIST)

    @allure.step('Ожидание номера заказа в списке "В работе"')
    def wait_for_order_in_progress(self, order_number):
        self.wait_for_text(FeedPageLocators.ORDERS_IN_PROGRESS_LIST, order_number)
