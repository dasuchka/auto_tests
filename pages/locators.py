from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET=(By.CSS_SELECTOR, '.basket-mini .btn')

class MainPageLocators():
    LOGIN_LINK=(By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM=(By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM=(By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    ADD_TO_BASKET_BUTTON=(By.CSS_SELECTOR,'.btn-add-to-basket')
    BOOK_NAME=(By.CSS_SELECTOR, ".product_main h1")
    BOOK_PRICE=(By.CSS_SELECTOR, ".price_color")
    MESSAGE_ADD_BOOK=(By.CSS_SELECTOR, "#messages .alert:nth-child(1) .alertinner strong")
    MESSAGE_ABOUT_BASKET_PRICE=(By.CSS_SELECTOR, "#messages .alert:nth-child(3) .alertinner p strong")

class BasketPageLocators():
    MESSAGE_EMPTY_BASKET = (By.CSS_SELECTOR, "#content_inner > p")
