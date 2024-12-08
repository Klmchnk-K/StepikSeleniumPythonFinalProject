from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.XPATH, "//a[@id='login_link']")
    BASKET_LINK = (By.XPATH, "//div[contains(@class, 'basket-mini')]//a")


class LoginPageLocators():
    LOGIN_FORM = (By.XPATH, "//form[@id='login_form']")
    REGISTER_FORM = (By.XPATH, "//form[@id='register_form']")


class BasketPageLocators():
    NONEMPTY_BASKET = (By.XPATH, "//form[@id='basket_formset']")
    EMPTY_BASKET_MESSAGE = (By.XPATH, "//div[@id='content_inner']/p")


class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.XPATH, "//button[contains(@class, 'btn-add-to-basket')]")
    ADDED_PRODUCT_MESSAGE = (By.XPATH, "(//div[@id='messages']//strong)[1]")
    BASKET_TOTAL_MESSAGE = (By.XPATH, "(//div[@id='messages']//strong)[3]")
    PRODUCT_NAME = (By.XPATH, "//div[contains(@class, 'product_main')]/h1")
    PRODUCT_PRICE = (By.XPATH, "//div[contains(@class, 'product_main')]/p")
