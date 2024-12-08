import pytest
from .pages.product_page import ProductPage


@pytest.mark.parametrize('number', [pytest.param(i, marks=pytest.mark.xfail(i == 7, reason='Bug')) for i in range(10)])
def test_guest_can_add_product_to_basket(driver, number):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{number}"

    page = ProductPage(driver, link)

    page.open()
    page.add_product_to_basket()

    page.should_be_added_product_message()
    page.should_be_basket_total_message()


#def test_guest_cant_see_success_message_after_adding_product_to_basket(driver):

#def test_guest_cant_see_success_message(driver):

#def test_message_disappeared_after_adding_product_to_basket(driver):


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
