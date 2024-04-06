import os
import platform
import random
from datetime import datetime

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

from logger import Logger


class Driver:
    logger = Logger.setup_logger()

    def __init__(self):
        self.user_agents = [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",
        ]
        self.driver = self._launch_driver()

    def _launch_driver(self):
        try:

            if platform.system() == "Linux":
                current_directory = os.path.dirname(os.path.abspath(__file__))
                chromedriver_path = os.path.join(current_directory, "..", "chromedriver", "chromedriver")
                os.chmod(chromedriver_path, 0o755)
            else:
                chromedriver_path = ChromeDriverManager().install()

            service = Service(executable_path=chromedriver_path)
            options = webdriver.ChromeOptions()
            options.add_argument("--verbose")
            options.add_argument("--no-sandbox")
            options.add_argument("--headless=new")
            options.add_argument("--ignore-certificate-errors")
            options.add_argument("--disable-dev-shm-usage")
            options.add_argument("--disable-extensions")
            options.add_argument("--disable-gpu")
            options.add_argument("--user-agent={}".format(random.choice(list(self.user_agents))))

            driver = webdriver.Chrome(
                service=service,
                options=options
            )
            self.logger.info(driver)
            return driver
        except Exception as e:
            self.logger.error(f"Initial Error：{e}")
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
