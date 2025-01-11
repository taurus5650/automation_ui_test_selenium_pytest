import time
from datetime import datetime

import allure


from page.home_page.home_page import HomePage
from page.login_page.login_page import LoginPage
from page.signup_page.signup_page import SignUpPage
from action.driver import Driver
from logger import Logger


class TestCase:
    logger = Logger.setup_logger(__name__)
    driver = Driver()
    home_page = HomePage()
    login_page = LoginPage()
    signup_page = SignUpPage()

    @allure.title("Register User")
    def test_register_user(self):
        home_page_url = "http://automationexercise.com"
        current_time = datetime.now()
        for_loop_max = 180
        expected_homepage_title = "Automation Exercise"
        expected_sign_up_form_text = "New User Signup!"
        name = f"automation_{current_time.strftime('%Y%m%d%H%M%S%f')}"
        print(name)
        sign_up_email = f"{current_time.strftime('%Y%m%d%H%M%S%f')}@automation.com"
        print(sign_up_email)
        expected_enter_account_info_text = "ENTER ACCOUNT INFORMATION"
        password = "1234567890"
        address = "24th Floor, Dr. S.P.M. Civic Centre, Minto Road, New Delhi, India."
        state = "Minto Road"
        city = "New Delhi"
        zipcode = "100002"
        mobile_number = "155305"
        expected_account_created_text = "ACCOUNT CREATED!"

        # region __Step1. Launch browser
        launch_driver = self.driver._launch_driver()
        # endregion __Step1. Launch browser

        # region __Step2. Navigate to url 'http://automationexercise.com'
        launch_driver.get(
            url=home_page_url
        )
        # endregion __Step2. Navigate to url 'http://automationexercise.com'

        # region __Step3. Verify that home page is visible successfully
        assert expected_homepage_title in launch_driver.title
        # endregion __Step3. Verify that home page is visible successfully

        # region __Step4. Click on 'Signup / Login' button
        self.home_page.click_signup_login_href(
            launch_driver=launch_driver
        )
        # endregion __Step4. Click on 'Signup / Login' button

        # region __Step5. Verify 'New User Signup!' is visible
        for _ in range(for_loop_max):
            sign_in_or_sign_up_page = self.login_page.check_signin_or_signup_h2(
                launch_driver=launch_driver
            )
            time.sleep(1)
            if expected_sign_up_form_text:
                assert True
                break
            else:
                assert False, logger.error(
                    f" [{sign_up_form_text}] not found within {for_loop_max} seconds")
        # endregion __Step5. Verify 'New User Signup!' is visible

        # region __Step6. Enter name and email address
        self.login_page.input_sign_up_name(
            launch_driver=launch_driver,
            text=name
        )

        self.login_page.input_sign_up_email(
            launch_driver=launch_driver,
            text=sign_up_email
        )
        # endregion __Step6. Enter name and email address

        # region __Step7. Click 'Signup' button
        self.login_page.click_sign_up_btn(
            launch_driver=launch_driver
        )
        # endregion __Step7. Click 'Signup' button

        # region __Step8. Verify that 'ENTER ACCOUNT INFORMATION' is visible
        enter_account_info = self.signup_page.check_enter_account_info(
            launch_driver=launch_driver
        )
        assert enter_account_info == expected_enter_account_info_text
        # endregion __Step8. Verify that 'ENTER ACCOUNT INFORMATION' is visible

        # region __Step9. Fill details: Title, Name, Email, Password, Date of birth
        self.signup_page.click_title_gender_radio(
            launch_driver=launch_driver
        )

        self.signup_page.input_password(
            launch_driver=launch_driver,
            text=password
        )

        self.signup_page.click_date_of_birth_dropdown_list(
            launch_driver=launch_driver
        )

        self.signup_page.input_first_name(
            launch_driver=launch_driver,
            text=name
        )

        self.signup_page.input_last_name(
            launch_driver=launch_driver,
            text=name
        )

        self.signup_page.input_company(
            launch_driver=launch_driver,
            text=name
        )

        self.signup_page.input_address(
            launch_driver=launch_driver,
            text=address
        )

        self.signup_page.input_state(
            launch_driver=launch_driver,
            text=state
        )

        self.signup_page.input_city(
            launch_driver=launch_driver,
            text=city
        )

        self.signup_page.input_zip_code(
            launch_driver=launch_driver,
            text=zipcode
        )

        self.signup_page.input_mobile_num(
            launch_driver=launch_driver,
            text=mobile_number
        )

        create_account_button = self.signup_page.click_create_acc_btn(
            launch_driver=launch_driver,
        )
        # endregion __Step9. Fill details: Title, Name, Email, Password, Date of birth

        time.sleep(1000)

        # # region __Step14. Verify that 'ACCOUNT CREATED!' is visible
        # account_created_text = self.driver._wait_for_element(
        #     driver=launch_driver,
        #     condition=EC.visibility_of_element_located,
        #     locator=self.locator.ACCOUNT_CREATED_TEXT
        # )
        # assert expected_account_created_text == account_created_text.text
        # # endregion __Step14. Verify that 'ACCOUNT CREATED!' is visible
