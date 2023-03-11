import time

from .base_page import BasePage
from .locators import ProductPageLocators
from selenium import webdriver
from selenium.webdriver.common.by import By

class ProductPage(BasePage):

    def should_be_button_add_to_basket(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BUTTON), "no button add_to_basket on page"

    def add_to_basket(self):
        button_add_to_basket=self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        button_add_to_basket.click()
        self.solve_quiz_and_get_code()

    def should_be_message_added_to_basket(self):
        assert self.is_element_present(*ProductPageLocators.MESSAGE_ADD_BOOK), "no text message about adding a book"

    def should_be_message_about_price(self):
        assert self.is_element_present(*ProductPageLocators.MESSAGE_ABOUT_BASKET_PRICE), "no text message about basket price"

    def should_be_book_name_the_same(self):
        book_name=self.browser.find_element(*ProductPageLocators.BOOK_NAME).text
        book_name_in_basket = self.browser.find_element(*ProductPageLocators.MESSAGE_ADD_BOOK).text
        assert book_name==book_name_in_basket, "book name in message is different from added book name"

    def should_be_book_price_the_same(self):
        book_price=self.browser.find_element(*ProductPageLocators.BOOK_PRICE).text
        book_price_in_basket = self.browser.find_element(*ProductPageLocators.MESSAGE_ABOUT_BASKET_PRICE).text
        assert book_price==book_price_in_basket, "book price in message is different from the price of added book "

    def should_be_messages_about_book_name_price(self):
        self.should_be_message_added_to_basket()
        self.should_be_messages_about_book_name_price()
        self.should_be_book_name_the_same()
        self.should_be_book_price_the_same()