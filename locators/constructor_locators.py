from selenium.webdriver.common.by import By


class ConstructorPageLocators:
    MODAL_OVERLAY = (
        By.XPATH,
        "//div[contains(@class, 'Modal_modal_overlay__x2ZCr')]/parent::div"
    )
    PROFILE_LINK = (
        By.XPATH,
        "//p[@class='AppHeader_header__linkText__3q_va ml-2' and text()='Личный Кабинет']"
    )
    CONSTRUCTOR_LINK = (
        By.XPATH,
        "//p[contains(@class, 'AppHeader_header__linkText__3q_va ml-2') and text()='Конструктор']"
    )
    ORDER_FEED_LINK = (
        By.XPATH,
        "//p[contains(@class, 'AppHeader_header__linkText__3q_va ml-2') and text()='Лента Заказов']"
    )

    @staticmethod
    def get_ingredient_locator(ingredient_id):
        return (
            By.XPATH,
            f'//a[contains(@class, "BurgerIngredient_ingredient__1TVf6") and @href="/ingredient/{ingredient_id}"]'
        )

    @staticmethod
    def get_ingredient_counter_locator(ingredient_id):
        return (
            By.XPATH,
            f'//a[contains(@class, "BurgerIngredient_ingredient__1TVf6") '
            f'and @href="/ingredient/{ingredient_id}"]//p[contains(@class, "counter_counter__num__3nue1")]'
        )

    MODAL_WINDOW = (
        By.XPATH,
        "//div[contains(@class ,'Modal_modal__contentBox__sCy8X')]/ancestor::section"
    )
    OPENED_MODAL_CLASS = 'Modal_modal_opened__3ISw4 Modal_modal__P3_V5'
    CLOSED_MODAL_CLASS = 'Modal_modal__P3_V5'
    MODAL_CLOSE_BUTTON = (
        By.XPATH,
        "//div[contains(@class, 'Modal_modal__container__Wo2l_')]"
        "/div[contains(@class, 'Modal_modal__contentBox__sCy8X')]"
        "/following-sibling::button"
    )
    CONSTRUCTOR_DROP_AREA = (
        By.CSS_SELECTOR,
        'ul.BurgerConstructor_basket__list__l9dp_'
    )
    CREATE_ORDER_BUTTON = (
        By.CSS_SELECTOR,
        'button.button_button__33qZ0.button_button_type_primary__1O7Bx.button_button_size_large__G21Vg'
    )
    ORDER_NUMBER_TEXT = (
        By.XPATH,
        "//div[contains(@class, 'Modal_modal__contentBox__sCy8X')]"
        "/h2[contains(@class, 'Modal_modal__title_shadow__3ikwq')]"
    )
