import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from Utilities.BaseClass import BaseClass
from pageobject.checkoutpage import CheckOutPage
from pageobject.confirmpage import ConfirmationPage
from pageobject.homepage import HomePage


# @pytest.mark.use fixtures("setup")
class TestFramework(BaseClass):
    def test_e2e(self):
        log = self.get_logger()
        self.driver.implicitly_wait(5)

        # object of HomePage class(page object)
        home_page = HomePage(self.driver)
        # confirmation = ConfirmationPage(self.driver)
        # Click on the 'Shop' link
        check_out_page_variable = home_page.shop_items()

        time.sleep(2)
        log.info("getting all the product name")
        # finding blackberry phone from different brands of phone available on page and clicking on it.
        products = check_out_page_variable.get_card_titles()

        for product in products:
            # productName = product.find_element(By.XPATH, "div/h4/a").text
            product_name = check_out_page_variable.mobile_name_fun(product).text
            log.info(product_name)
            if product_name == "Blackberry":
                check_out_page_variable.product_button_click(product).click()
                break

        check_out_page_variable.checkout_button_click().click()

        # Click on the 'Checkout' button
        confirmation_variable = check_out_page_variable.checkout_amount_button_click()

        # Enter 'Ind' in the country field and select India from dropdown
        confirmation_variable.country_click().send_keys("ind")

        # Wait until 'India' link appears and click on it(Explicit wait)
        self.verify_link_presence("India")
        confirmation_variable.country_dropdown_click().click()

        # Agree to terms and conditions (checkbox) and submit the form
        confirmation_variable.checkbox_click().click()
        confirmation_variable.purchase_button_click().click()

        # Verify success message
        success_text = confirmation_variable.confirmation_message().text
        log.info("Text received from application is " + success_text)
        # asserting partial text only by using in instead of ==(whole text).
        assert "Success! Thank you!" in success_text




