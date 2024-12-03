from selenium.webdriver.common.by import By


def test_guest_can_go_to_login_page(driver):
    link = "http://selenium1py.pythonanywhere.com/"

    driver.get(link)

    login_link = driver.find_element(By.XPATH, "//a[@id='login_link']")
    login_link.click()
