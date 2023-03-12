from .base_page import BasePage
from.locators import BasketPageLocators

class BasketPage(BasePage):
    def basket_should_be_empty(self):
        assert self.is_element_present(*BasketPageLocators.MESSAGE_EMPTY_BASKET), \
            "Basket is not empty or message is wrong"

    def basket_should_not_be_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.MESSAGE_EMPTY_BASKET), \
            "Basket is empty, but should not"