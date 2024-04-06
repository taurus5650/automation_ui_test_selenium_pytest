from selenium.webdriver.common.by import By


class Locators(object):

    ENTER_HOMPAGE_URL = "https://automationexercise.com/"
    TEST_CASES_HYPERLINK = (By.XPATH, "//a[@href='/test_cases']")
    TEST_CASES_PAGE_H2 = (By.XPATH, '//h2')