import allure
import data
import url
from locators.feed_locators import FeedPageLocators
from pages.auth_page import AuthPage
from pages.constructor_page import ConstructorPage
from pages.feed_page import FeedPage
from pages.profile_page import ProfilePage


class TestOrderFeed:
    @allure.title('Открытие модального окна заказа')
    def test_order_modal(self, driver):
        constructor_page = ConstructorPage(driver)
        constructor_page.load_page(url.MAIN_PAGE_URL)
        constructor_page.go_to_order_feed()

        feed_page = FeedPage(driver)
        feed_page.select_order()
        modal_state = feed_page.check_modal_state()

        with allure.step('Проверка открытия модального окна'):
            assert modal_state == FeedPageLocators.MODAL_OPENED_CLASS

    @allure.title('Совпадение заказов в истории и ленте')
    def test_order_history_match(self, driver, create_user):
        constructor_page = ConstructorPage(driver)
        constructor_page.load_page(url.MAIN_PAGE_URL)
        constructor_page.go_to_profile()

        auth_page = AuthPage(driver)
        auth_page.login(create_user['email'], create_user['password'])

        with allure.step('Создание тестового заказа'):
            constructor_page.add_ingredient_to_order(data.INGREDIENTS[0])
            constructor_page.add_ingredient_to_order(data.INGREDIENTS[1])
            constructor_page.add_ingredient_to_order(data.INGREDIENTS[2])
            constructor_page.create_order()
            constructor_page.close_order_modal()

        constructor_page.go_to_profile()
        profile_page = ProfilePage(driver)
        profile_page.go_to_order_history()
        history_order_number = profile_page.get_last_order_number()
        history_order_name = profile_page.get_last_order_name()

        constructor_page.go_to_order_feed()
        feed_page = FeedPage(driver)
        feed_order_number = feed_page.get_order_number_text(history_order_number)
        feed_order_name = feed_page.get_order_name_text(history_order_name)

        with allure.step('Проверка совпадения номеров заказов'):
            assert history_order_number == feed_order_number
        with allure.step('Проверка совпадения названий заказов'):
            assert history_order_name == feed_order_name

    @allure.title('Изменение общего счетчика заказов')
    def test_total_orders_counter(self, driver, create_user):
        constructor_page = ConstructorPage(driver)
        constructor_page.load_page(url.MAIN_PAGE_URL)
        constructor_page.go_to_profile()

        auth_page = AuthPage(driver)
        auth_page.login(create_user['email'], create_user['password'])
        constructor_page.go_to_order_feed()

        feed_page = FeedPage(driver)
        initial_count = feed_page.get_total_orders_count()
        constructor_page.go_to_constructor()

        with allure.step('Создание тестового заказа'):
            constructor_page.add_ingredient_to_order(data.INGREDIENTS[0])
            constructor_page.add_ingredient_to_order(data.INGREDIENTS[1])
            constructor_page.add_ingredient_to_order(data.INGREDIENTS[2])
            constructor_page.create_order()
            constructor_page.close_order_modal()

        constructor_page.go_to_order_feed()
        updated_count = feed_page.get_total_orders_count()

        with allure.step('Проверка изменения счетчика'):
            assert int(updated_count) > int(initial_count)

    @allure.title('Изменение дневного счетчика заказов')
    def test_daily_orders_counter(self, driver, create_user):
        constructor_page = ConstructorPage(driver)
        constructor_page.load_page(url.MAIN_PAGE_URL)
        constructor_page.go_to_profile()

        auth_page = AuthPage(driver)
        auth_page.login(create_user['email'], create_user['password'])
        constructor_page.go_to_order_feed()

        feed_page = FeedPage(driver)
        initial_count = feed_page.get_today_orders_count()
        constructor_page.go_to_constructor()

        with allure.step('Создание тестового заказа'):
            constructor_page.add_ingredient_to_order(data.INGREDIENTS[0])
            constructor_page.add_ingredient_to_order(data.INGREDIENTS[1])
            constructor_page.add_ingredient_to_order(data.INGREDIENTS[2])
            constructor_page.create_order()
            constructor_page.close_order_modal()

        constructor_page.go_to_order_feed()
        updated_count = feed_page.get_today_orders_count()

        with allure.step('Проверка изменения счетчика'):
            assert int(updated_count) > int(initial_count)

    @allure.title('Появление заказа в списке "В работе"')
    def test_order_in_progress(self, driver, create_user):
        constructor_page = ConstructorPage(driver)
        constructor_page.load_page(url.MAIN_PAGE_URL)
        constructor_page.go_to_profile()

        auth_page = AuthPage(driver)
        auth_page.login(create_user['email'], create_user['password'])

        with allure.step('Создание тестового заказа'):
            constructor_page.add_ingredient_to_order(data.INGREDIENTS[0])
            constructor_page.add_ingredient_to_order(data.INGREDIENTS[1])
            constructor_page.add_ingredient_to_order(data.INGREDIENTS[2])
            constructor_page.create_order()
            order_number = constructor_page.get_order_number()
            constructor_page.close_order_modal()

        constructor_page.go_to_order_feed()
        feed_page = FeedPage(driver)
        feed_page.wait_for_order_in_progress(order_number)
        in_progress_number = feed_page.get_in_progress_order_number()

        with allure.step('Проверка появления заказа'):
            assert f'0{order_number}' == in_progress_number
