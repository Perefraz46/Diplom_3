from selenium.webdriver.common.by import By


class ProfilePageLocators:
    ORDER_HISTORY_LINK = (
        By.XPATH,
        "//a[@class='Account_link__2ETsJ text text_type_main-medium text_color_inactive' and text()='История заказов']"
    )
    LOGOUT_BUTTON = (
        By.CSS_SELECTOR,
        '.Account_button__14Yp3'
    )
    FIRST_ORDER_NUMBER = (
        By.XPATH,
        "//div[@class='OrderHistory_textBox__3lgbs mb-6'][1]/p"
    )
    FIRST_ORDER_NAME = (
        By.XPATH,
        "//a[@class='OrderHistory_link__1iNby'][1]/h2"
    )
