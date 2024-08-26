from selenium.webdriver.common.by import By

from pageobject.confirmpage import ConfirmationPage


class CheckOutPage:

    def __init__(self, driver):
        self.driver = driver

    # driver.find_elements(By.XPATH, "//div[@class='card h-100']")
    card_title = (By.XPATH, "//div[@class='card h-100']")

    # product.find_element(By.XPATH, "div/h4/a")

    # mobile_name = (By.XPATH, "//div[@class='card h-100']/div/h4/a")
    #
    # product_button = (By.XPATH, "//div[@class='card h-100']/div/button")

    checkout_click = (By.XPATH, "//a[@class='nav-link btn btn-primary']")
    # productName = product.find_element(By.XPATH, "div/h4/a").text
    mobile_name = (By.XPATH, "div/h4/a")  # Updated to be a relative XPath
    product_button = (By.XPATH, "div/button")  # Updated to be a relative XPath

    checkout_amount = (By.CSS_SELECTOR, ".btn.btn-success")

    def get_card_titles(self):
        return self.driver.find_elements(*CheckOutPage.card_title)

    # return self.driver.find_elements(*CheckOutPage.card_title)

    def mobile_name_fun(self, product):
        # productName = product.find_element(By.XPATH, "div/h4/a").text
        return product.find_element(*self.mobile_name)  # Find within product

    def product_button_click(self, product):
        # Finds and returns the mobile name within the product element
        return product.find_element(*self.product_button)

    def checkout_button_click(self):
        return self.driver.find_element(*CheckOutPage.checkout_click)

    def checkout_amount_button_click(self):
        self.driver.find_element(*CheckOutPage.checkout_amount).click()
        confirmation = ConfirmationPage(self.driver)
        return confirmation
