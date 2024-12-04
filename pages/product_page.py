from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_basket(self):
        add_to_basket_button = self.driver.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_to_basket_button.click()

        self.solve_quiz_and_get_code()

    def should_be_added_product_message(self):
        added_product_message = self.driver.find_element(*ProductPageLocators.ADDED_PRODUCT_MESSAGE).text
        product_name = self.driver.find_element(*ProductPageLocators.PRODUCT_NAME).text

        assert added_product_message == product_name, "Wrong name of the added product"

    def should_be_basket_total_message(self):
        basket_total_message = self.driver.find_element(*ProductPageLocators.BASKET_TOTAL_MESSAGE).text
        product_price = self.driver.find_element(*ProductPageLocators.PRODUCT_PRICE).text

        assert basket_total_message == product_price, "Wrong basket total"
