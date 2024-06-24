from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    ADD_TO_BASKET = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    NAME_OF_BOOK = (By.CSS_SELECTOR, "div.alert-success div strong")
    NAME_OF_BOOK_RIGHT = (By.CSS_SELECTOR, "div h1")
    COST_OF_BASKET = (By.CSS_SELECTOR, "div.alert-info p strong")
    COST_OF_BASKET_RIGHT = (By.CSS_SELECTOR, "div.col-sm-6 p.price_color")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div.alert-success div")
    