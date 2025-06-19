from selenium.webdriver.common.by import By


class FeedPageLocators:
    FIRST_ORDER_IN_LIST = (
        By.XPATH,
        "//ul[@class='OrderFeed_list__OLh59']/li[1]"
    )
    ORDER_DETAILS_MODAL = (
        By.XPATH,
        "//div[@class='Modal_orderBox__1xWdi Modal_modal__contentBox__sCy8X p-10']/ancestor::section"
    )
    MODAL_OPENED_CLASS = 'Modal_modal_opened__3ISw4 Modal_modal__P3_V5'

    @staticmethod
    def get_order_number_locator(number):
        return (
            By.XPATH,
            f'//div[contains(@class, "OrderHistory_textBox__3lgbs mb-6")]'
            f'//p[contains(@class, "text text_type_digits-default") and text()="{number}"]'
        )

    @staticmethod
    def get_order_name_locator(name):
        return (
            By.XPATH,
            f'//a[contains(@class, "OrderHistory_link__1iNby")]'
            f'//h2[contains(@class, "text text_type_main-medium mb-2") and text()="{name}"]'
        )

    TOTAL_ORDERS_COUNT = (
        By.XPATH,
        "//div[contains(@class, 'OrderFeed_ordersData__1L6Iv')]//div/p[contains(text(), 'Выполнено за все время:')]"
        "/following-sibling::p[contains(@class, 'OrderFeed_number__2MbrQ')]"
    )
    TODAY_ORDERS_COUNT = (
        By.XPATH,
        "//div[contains(@class, 'OrderFeed_ordersData__1L6Iv')]//div/p[contains(text(), 'Выполнено за сегодня:')]"
        "/following-sibling::p[contains(@class, 'OrderFeed_number__2MbrQ')]"
    )
    ORDERS_IN_PROGRESS_LIST = (
        By.XPATH,
        "//div[contains(@class, 'OrderFeed_ordersData__1L6Iv')]//ul[contains(@class, 'orderListReady__1YFem')]/li"
    )
