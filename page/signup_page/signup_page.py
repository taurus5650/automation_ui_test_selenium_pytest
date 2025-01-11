from selenium.webdriver.support import expected_conditions as EC

from action.driver import Driver
from .locator import Locator


class SignUpPage:
    locator = Locator()
    driver = Driver()

    def check_enter_account_info(self, launch_driver: str):
        element = self.driver._wait_for_element(
            driver=launch_driver,
            condition=EC.visibility_of_element_located,
            locator=self.locator.ENTER_ACCOUNT_INFO_TEXT
        ).text
        return element

    def click_title_gender_radio(self, launch_driver: str):
        self.driver._wait_for_element(
            driver=launch_driver,
            condition=EC.element_to_be_clickable,
            locator=self.locator.ID_GENDER_1
        ).click()

    def input_password(self, launch_driver: str, text: str):
        self.driver._wait_for_element(
            driver=launch_driver,
            condition=EC.visibility_of_element_located,
            locator=self.locator.PASSWORD
        ).send_keys(text)

    def click_date_of_birth_dropdown_list(self, launch_driver: str):
        self.driver._wait_for_element(
            driver=launch_driver,
            condition=EC.element_to_be_clickable,
            locator=self.locator.DATE_OF_BIRTH_DAYS_DROPDOWN
        ).click()

        self.driver._wait_for_element(
            driver=launch_driver,
            condition=EC.element_to_be_clickable,
            locator=self.locator.DATE_OF_BIRTH_DAYS
        ).click()

        self.driver._wait_for_element(
            driver=launch_driver,
            condition=EC.element_to_be_clickable,
            locator=self.locator.DATE_OF_BIRTH_DAYS_DROPDOWN
        ).click()

        self.driver._wait_for_element(
            driver=launch_driver,
            condition=EC.element_to_be_clickable,
            locator=self.locator.DATE_OF_BIRTH_MONTHS
        ).click()

        self.driver._wait_for_element(
            driver=launch_driver,
            condition=EC.element_to_be_clickable,
            locator=self.locator.DATE_OF_BIRTH_MONTHS
        ).click()

        self.driver._wait_for_element(
            driver=launch_driver,
            condition=EC.element_to_be_clickable,
            locator=self.locator.DATE_OF_BIRTH_YEARS_DROPDOWN
        ).click()

        self.driver._wait_for_element(
            driver=launch_driver,
            condition=EC.element_to_be_clickable,
            locator=self.locator.DATE_OF_BIRTH_YEARS
        ).click()

    def input_first_name(self, launch_driver: str, text: str):
        self.driver._wait_for_element(
            driver=launch_driver,
            condition=EC.visibility_of_element_located,
            locator=self.locator.FIRST_NAME
        ).send_keys(text)

    def input_last_name(self, launch_driver: str, text: str):
        self.driver._wait_for_element(
            driver=launch_driver,
            condition=EC.visibility_of_element_located,
            locator=self.locator.LAST_NAME
        ).send_keys(text)

    def input_company(self, launch_driver: str, text: str):
        self.driver._wait_for_element(
            driver=launch_driver,
            condition=EC.visibility_of_element_located,
            locator=self.locator.COMPANY
        ).send_keys(text)

    def input_address(self, launch_driver: str, text: str):
        self.driver._wait_for_element(
            driver=launch_driver,
            condition=EC.visibility_of_element_located,
            locator=self.locator.ADDRESS_1
        ).send_keys(text)

    def input_state(self, launch_driver: str, text: str):
        self.driver._wait_for_element(
            driver=launch_driver,
            condition=EC.visibility_of_element_located,
            locator=self.locator.STATE
        ).send_keys(text)

    def input_city(self, launch_driver: str, text: str):
        self.driver._wait_for_element(
            driver=launch_driver,
            condition=EC.visibility_of_element_located,
            locator=self.locator.CITY
        ).send_keys(text)

    def input_zip_code(self, launch_driver: str, text: str):
        self.driver._wait_for_element(
            driver=launch_driver,
            condition=EC.visibility_of_element_located,
            locator=self.locator.ZIPCODE
        ).send_keys(text)

    def input_mobile_num(self, launch_driver: str, text: str):
        self.driver._wait_for_element(
            driver=launch_driver,
            condition=EC.visibility_of_element_located,
            locator=self.locator.MOBILE_NUMBER
        ).send_keys(text)

    def click_create_acc_btn(self, launch_driver: str):
        self.driver._wait_for_element(
            driver=launch_driver,
            condition=EC.element_to_be_clickable,
            locator=self.locator.CREATE_ACCOUNT_BTN
        ).click()
