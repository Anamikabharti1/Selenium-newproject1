from selenium.webdriver.common.by import By


class ConfirmationPage:

    def __init__(self, driver):
        self.driver = driver

    # checkbox-terms and condition
    checkbox = (By.XPATH, "//div[@class='checkbox checkbox-primary']")

    # purchase button on confirmation page
    purchase_button = (By.XPATH, "//input[@type='submit']")

    # country selection from dropdown
    country = (By.ID, "country")

    # confirmation message
    message = (By.CLASS_NAME, "alert-success")

    # Clicking India from dropdown
    country_dropdown = (By.LINK_TEXT, "India")

    def checkbox_click(self):
        return self.driver.find_element(*ConfirmationPage.checkbox)

    def purchase_button_click(self):
        return self.driver.find_element(*ConfirmationPage.purchase_button)

    def country_click(self):
        return self.driver.find_element(*ConfirmationPage.country)

    def confirmation_message(self):
        return self.driver.find_element(*ConfirmationPage.message)

    def country_dropdown_click(self):
        return self.driver.find_element(*ConfirmationPage.country_dropdown)
