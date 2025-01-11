from selenium.webdriver.support import expected_conditions as EC

from action.driver import Driver
from .locator import Locator


class AccCreateConfirmationPage:
    locator = Locator()
    driver = Driver()

    def check_account_created_text(self, launch_driver: str):
        element = self.driver._wait_for_element(
            driver=launch_driver,
            condition=EC.visibility_of_element_located,
            locator=self.locator.ACCOUNT_CREATED_TEXT
        ).text
        return element
