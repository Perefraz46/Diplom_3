from selenium.webdriver.common.by import By


class AuthPageLocators:
    EMAIL_INPUT = (
        By.XPATH,
        "//input[@class='text input__textfield text_type_main-default' and @name='name']"
    )
    PASSWORD_INPUT = (
        By.XPATH,
        "//input[@class='text input__textfield text_type_main-default' and @name='Пароль']"
    )
    LOGIN_BUTTON = (
        By.CSS_SELECTOR,
        '.button_button__33qZ0.button_button_type_primary__1O7Bx.button_button_size_medium__3zxIa'
    )
    PASSWORD_RECOVERY_LINK = (
        By.XPATH,
        "//a[@class='Auth_link__1fOlj' and text()='Восстановить пароль']"
    )
    RECOVERY_EMAIL_INPUT = (
        By.XPATH,
        "//label[contains(text(), 'Email')]/following-sibling::input"
    )
    RECOVERY_SUBMIT_BUTTON = (
        By.CSS_SELECTOR,
        '.button_button__33qZ0.button_button_type_primary__1O7Bx.button_button_size_medium__3zxIa'
    )
    NEW_PASSWORD_INPUT = (
        By.XPATH,
        "//label[contains(text(), 'Пароль')]/following-sibling::input"
    )
    TOGGLE_PASSWORD_VISIBILITY_BUTTON = (
        By.CSS_SELECTOR,
        '.input__icon.input__icon-action'
    )
    PASSWORD_FIELD_CONTAINER = (
        By.XPATH,
        "//label[contains(text(), 'Пароль')]/parent::div"
    )
    ACTIVE_PASSWORD_FIELD_CLASS = 'input_status_active'
