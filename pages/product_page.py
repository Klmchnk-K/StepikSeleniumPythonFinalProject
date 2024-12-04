from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_basket(self):
        add_to_basket_button = self.driver.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_to_basket_button.click()

        self.solve_quiz_and_get_code()

    def should_be_added_product_message(self):
        assert (self.get_text(*ProductPageLocators.ADDED_PRODUCT_MESSAGE) ==
                self.get_text(*ProductPageLocators.PRODUCT_NAME)), "Wrong name of the added product"

    def should_be_basket_total_message(self):
        assert (self.get_text(*ProductPageLocators.BASKET_TOTAL_MESSAGE) ==
                self.get_text(*ProductPageLocators.PRODUCT_PRICE)), "Wrong basket total"
