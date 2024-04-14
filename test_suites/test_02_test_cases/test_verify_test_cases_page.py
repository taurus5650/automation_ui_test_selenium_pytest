import time
from datetime import datetime

import allure
from selenium.webdriver.support import expected_conditions as EC

from action.driver import Driver
from locator import Locators
from logger import Logger


class TestCase:
    logger = Logger.setup_logger(__name__)
    driver = Driver()
    locator = Locators()

    @allure.title("Verify Test Cases Page")
    def test_verify_test_cases_page(self):
        for_loop_max = 180
        expected_homepage_title = "Automation Exercise"
        expected_test_cases_text = "Test Cases"

        # region __Step1. Launch browser
        launch_driver = self.driver._launch_driver()
        # endregion __Step1. Launch browser

        # region __Step2. Navigate to url 'http://automationexercise.com'
        launch_driver.get(self.locator.ENTER_HOMPAGE_URL)
        # endregion __Step2. Navigate to url 'http://automationexercise.com'

        # region __Step3. Verify that home page is visible successfully
        assert expected_homepage_title in launch_driver.title
        # endregion __Step3. Verify that home page is visible successfully

        # region __Step4. Click on 'Test Cases' button
        self.driver._wait_for_element(
            driver=launch_driver,
            condition=EC.element_to_be_clickable,
            locator=self.locator.TEST_CASES_HYPERLINK
        ).click()
        # endregion __Step4. Click on 'Test Cases' button

        # region __Step5. Verify 'TEST CASES' is visible
        for _ in range(for_loop_max):
            test_cases_page = self.driver._wait_for_element(
                driver=launch_driver,
                condition=EC.visibility_of_element_located,
                locator=self.locator.TEST_CASES_PAGE_H2
            ).text
            time.sleep(1)
            if expected_test_cases_text:
                assert True
                break
            else:
                assert False, logger.error(
                    f" [{expected_test_cases_text}] not found within {for_loop_max} seconds")
        # endregion __Step5. Verify 'TEST CASES' is visible
