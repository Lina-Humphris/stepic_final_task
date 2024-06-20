from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    ADD_TO_BASKET = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    NAME_OF_BOOK = (By.CSS_SELECTOR, "div.alert-success")
    NAME_OF_BOOK_RIGHT = (By.CSS_SELECTOR, "div h1")
    COST_OF_BASKET = (By.CSS_SELECTOR, "div.alert-info")
    COST_OF_BASKET_RIGHT = (By.CSS_SELECTOR, "div.col-sm-6 p.price_color")
    