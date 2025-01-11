from selenium.webdriver.support import expected_conditions as EC

from action.driver import Driver
from .locator import Locator


class LoginPage:
    locator = Locator()
    driver = Driver()

    def check_signin_or_signup_h2(self, launch_driver: str):
        sign_in_or_sign_up_page = self.driver._wait_for_element(
            driver=launch_driver,
            condition=EC.visibility_of_element_located,
            locator=self.locator.SIGN_IN_OR_SIGN_UP_PAGE_H2
        ).text

    def input_sign_up_name(self, launch_driver: str, text: str):
        self.driver._wait_for_element(
            driver=launch_driver,
            condition=EC.visibility_of_element_located,
            locator=self.locator.SIGN_UP_NAME
        ).send_keys(text)

    def input_sign_up_email(self, launch_driver: str, text: str):
        self.driver._wait_for_element(
            driver=launch_driver,
            condition=EC.visibility_of_element_located,
            locator=self.locator.SIGN_UP_EMAIL
        ).send_keys(text)

    def click_sign_up_btn(self, launch_driver: str):
        self.driver._wait_for_element(
            driver=launch_driver,
            condition=EC.element_to_be_clickable,
            locator=self.locator.SIGN_UP_BTN
        ).click()

    def check_email_addr_alr_exist(self, launch_driver: str):
        element = self.driver._wait_for_element(
            driver=launch_driver,
            condition=EC.visibility_of_element_located,
            locator=self.locator.EMAIL_ADDRESS_ALR_EXIST
        ).text
        return element
