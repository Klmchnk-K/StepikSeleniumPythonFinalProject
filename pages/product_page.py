from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_basket(self):
        add_to_basket_button = self.driver.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_to_basket_button.click()

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.ADDED_PRODUCT_MESSAGE), \
            "Success message is presented, but should not be"

    def should_disappear_of_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.ADDED_PRODUCT_MESSAGE), \
            "Success message is presented, but should not be, due its disappearing"

    def should_be_added_product_message(self):
        assert (self.get_text(*ProductPageLocators.ADDED_PRODUCT_MESSAGE) ==
                self.get_text(*ProductPageLocators.PRODUCT_NAME)), "Wrong name of the added product"

    def should_be_basket_total_message(self):
        assert (self.get_text(*ProductPageLocators.BASKET_TOTAL_MESSAGE) ==
                self.get_text(*ProductPageLocators.PRODUCT_PRICE)), "Wrong basket total"
