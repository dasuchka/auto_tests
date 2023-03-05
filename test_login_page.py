from .pages.login_page import LoginPage


def test_existence_login_in_url(browser):
    link = "http://selenium1py.pythonanywhere.com"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_url()


def test_existence_login_form(browser):
    link = "http://selenium1py.pythonanywhere.com"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_form()


def test_existence_register_form(browser):
    link = "http://selenium1py.pythonanywhere.com"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_register_form()
