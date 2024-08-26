from selenium.webdriver.common.by import By

from pageobject.checkoutpage import CheckOutPage


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    shop = (By.XPATH, "//a[@href='/angularpractice/shop']")

    def shop_items(self):

        # self.driver.find_element(By.XPATH, "//a[@href='/angularpractice/shop']")
        self.driver.find_element(*HomePage.shop).click()
        check_out_page = CheckOutPage(self.driver)
        return check_out_page




