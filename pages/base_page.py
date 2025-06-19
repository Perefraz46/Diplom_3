import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from seletools.actions import drag_and_drop
from config import TIMEOUT_VALUE
from locators.constructor_locators import ConstructorPageLocators


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Загрузка страницы')
    def load_page(self, page):
        self.driver.get(page)

    @allure.step('Возврат текущего URL')
    def get_current_url(self):
        return self.driver.current_url

    @allure.step('Ожидание невидимости элемента')
    def wait_until_invisible(self, locator, timeout=TIMEOUT_VALUE):
        return WebDriverWait(self.driver, timeout).until(EC.invisibility_of_element_located(locator))

    @allure.step('Ожидание видимости элемента')
    def wait_until_visible(self, locator, timeout=TIMEOUT_VALUE):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    @allure.step('Подождать кликабельность элемента')
    def wait_until_clickable(self, locator, timeout=TIMEOUT_VALUE):
        return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    @allure.step('Ожидание текста внутри элемента')
    def wait_for_text(self, locator, text, timeout=TIMEOUT_VALUE):
        return WebDriverWait(self.driver, timeout).until(EC.text_to_be_present_in_element(locator, text))

    @allure.step('Кликнуть на элемент')
    def click_element(self, locator, timeout=TIMEOUT_VALUE):
        self.wait_until_invisible(ConstructorPageLocators.MODAL_OVERLAY)
        element = self.wait_until_clickable(locator, timeout)
        element.click()

    @allure.step('Ожидание скрытия оверлея по СSS свойству элемента')
    def wait_for_overlay_hidden(self, property_name, expected_value,
                              not_expected_value, timeout=TIMEOUT_VALUE):
        def condition(driver):
            element = driver.find_element(*ConstructorPageLocators.MODAL_OVERLAY)
            return (element.value_of_css_property(property_name) == expected_value
                    and element.value_of_css_property(property_name) != not_expected_value)
        return WebDriverWait(self.driver, timeout).until(condition)

    @allure.step('Кликнуть на элемент c ожиданием скрытия оверлея')
    def click_with_overlay_wait(self, locator, property_name, expected_value,
                              not_expected_value, timeout=TIMEOUT_VALUE):
        self.wait_for_overlay_hidden(property_name, expected_value, not_expected_value)
        element = self.wait_until_clickable(locator, timeout)
        element.click()

    @allure.step('Ввести текст в поле ввода')
    def fill_input(self, locator, text, timeout=TIMEOUT_VALUE):
        element = self.wait_until_visible(locator, timeout)
        element.clear()
        element.send_keys(text)

    @allure.step('Получить значение элемента')
    def get_element_attribute(self, locator, attribute, timeout=TIMEOUT_VALUE):
        element = self.wait_until_visible(locator, timeout)
        return element.get_attribute(attribute)

    @allure.step('Получить текст элемента')
    def get_element_text(self, locator, timeout=TIMEOUT_VALUE):
        self.wait_until_invisible(ConstructorPageLocators.MODAL_OVERLAY)
        element = self.wait_until_visible(locator, timeout)
        return element.text

    @allure.step('Перетащить элемент')
    def drag_and_drop(self, source_locator, target_locator):
        self.wait_until_invisible(ConstructorPageLocators.MODAL_OVERLAY)
        source = self.wait_until_visible(source_locator)
        target = self.wait_until_visible(target_locator)
        drag_and_drop(self.driver, source, target)
