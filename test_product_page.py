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
