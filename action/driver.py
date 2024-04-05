import os
from datetime import datetime

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait

from logger import Logger


class Driver:
    logger = Logger.setup_logger()

    def __init__(self):
        self.driver = self._launch_driver()

    def _launch_driver(self):
        try:
            options = Options()
            options.add_argument("--no-sandbox")
            options.add_argument("--incognito")
            options.add_argument("--headless=new")
            options.add_argument("--start-maximized")
            driver = webdriver.Chrome(options=options)
            self.logger.info(driver)
            return driver
        except Exception as e:
            self.logger.error(f"Error initializing driver: {e}")
            return None

    def _wait_for_element(self, driver, condition, locator, timeout=10):
        """
        Wait for the specified condition on the element.

        :param condition: Expected condition from EC module (e.g., EC.element_to_be_clickable)
        :param locator: Tuple containing the locator strategy (e.g., By.XPATH) and the locator string
        :param timeout: Timeout in seconds
        :return: WebElement once the condition is met
        """
        try:
            element = WebDriverWait(driver, timeout).until(condition(locator))
            self.logger.info(element)
            return element
        except Exception as e:
            self._capture_screenshot()
            self.logger.error(f"Error while waiting for element: {e}")

    def _execute_script(self, script, *args):
        """
        Execute JavaScript in the context of the current driver instance.

        :param script: The JavaScript to execute
        :param args: Arguments to pass to the JavaScript
        :return: The result of executing the JavaScript
        """
        return self.driver.execute_script(script, *args)

    def _capture_screenshot(self):
        """
        Capture a screenshot of the current browser window.
        """
        try:
            current_time = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"screenshot_{current_time}.jpg"
            directory = os.path.join(os.getcwd(), "screenshots")

            filepath = os.path.join(directory, filename)
            screenshot = self.driver.save_screenshot(filepath)
            self.logger.info(f"Screenshot captured: {filepath}")
            return screenshot
        except Exception as e:
            self.logger.error(f"Error capturing screenshot: {e}")


