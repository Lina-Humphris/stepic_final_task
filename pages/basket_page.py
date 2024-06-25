import math
from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def should_basket_is_empty(self):
        text = self.browser.find_element(*BasketPageLocators.BASKET_IS_EMPTY)
        assert text.text == "Your basket is empty. Continue shopping", "Basket are NOT empty"

    def should_basked_without_goods(self):
        assert super().is_not_element_present(*BasketPageLocators.GOODS), "There are goods in the basket"