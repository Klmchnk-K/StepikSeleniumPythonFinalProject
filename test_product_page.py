import time
import pytest
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage


def test_guest_should_see_login_link_on_product_page(driver):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"

    page = ProductPage(driver, link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(driver):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"

    page = ProductPage(driver, link)
    page.open()
    page.go_to_login_page()


@pytest.mark.skip
def test_guest_cant_see_success_message_after_adding_product_to_basket(driver):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/reversing_202/"

    page = ProductPage(driver, link)
    page.open()
    page.add_product_to_basket()
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(driver):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/reversing_202/"

    page = ProductPage(driver, link)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.skip
def test_message_disappeared_after_adding_product_to_basket(driver):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/reversing_202/"

    page = ProductPage(driver, link)
    page.open()
    page.add_product_to_basket()
    page.should_disappear_of_success_message()


def test_guest_cant_see_product_in_basket_opened_from_product_page(driver):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"

    page = ProductPage(driver, link)
    page.open()
    page.go_to_basket_page()

    basket_page = BasketPage(driver, driver.current_url)
    basket_page.should_be_empty_basket()
    basket_page.should_be_empty_basket_message()


@pytest.mark.skip
@pytest.mark.parametrize('number', [pytest.param(i, marks=pytest.mark.xfail(i == 7, reason='Bug')) for i in range(10)])
def test_guest_can_add_product_to_basket(driver, number):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{number}"

    page = ProductPage(driver, link)
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_added_product_message()
    page.should_be_basket_total_message()


class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, driver):
        link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"

        email = str(time.time()) + "@fakemail.org"
        password = str(time.time())

        page = LoginPage(driver, link)
        page.open()
        page.register_new_user(email, password)
        page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, driver):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/metasploit_193/"

        page = ProductPage(driver, link)
        page.open()
        page.should_not_be_success_message()

    def test_user_can_add_product_to_basket(self, driver):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/metasploit_193/"

        page = ProductPage(driver, link)
        page.open()
        page.add_product_to_basket()
        page.should_be_added_product_message()
        page.should_be_basket_total_message()
