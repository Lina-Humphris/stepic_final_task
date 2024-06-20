from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.common.by import By

class ProductPage(BasePage):
    def add_to_basket(self):
        link = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        link.click()
 
    def should_right_book_in_basket(self):
        self.basket_cost()
        self.should_be_right_name_of_book()
        

    def should_be_right_name_of_book(self):
        name_of_book = self.browser.find_element(*ProductPageLocators.NAME_OF_BOOK)
        assert "The shellcoder's handbook" in name_of_book.text, name_of_book.text
    
    def basket_cost(self):
        cost_of_basket = self.browser.find_element(*ProductPageLocators.COST_OF_BASKET)
        assert "9.99" in cost_of_basket.text, cost_of_busket.text