from selenium.webdriver.support import expected_conditions as EC

from action.driver import Driver
from page.home_page.locator import Locator


class HomePage:
    locator = Locator()
    driver = Driver()

    def click_signup_login_href(self, launch_driver: str):
        self.driver._wait_for_element(
            driver=launch_driver,
            condition=EC.element_to_be_clickable,
            locator=Locator.SIGN_IN_OR_SIGN_UP_HYPERLINK
        ).click()
