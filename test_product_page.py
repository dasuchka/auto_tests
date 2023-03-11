from .pages.product_page import ProductPage


def test_guest_can_add_product_to_basket(browser):
    link='http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'
    page=ProductPage(browser, link)
    page.open()
    page.should_be_button_add_to_basket()
    page.add_to_basket()
    #page.should_be_message_added_to_basket()
    #page.should_be_messages_about_book_name_price()
    #page.should_be_book_name_the_same()
    #page.should_be_book_price_the_same()

