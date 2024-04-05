from selenium.webdriver.common.by import By


class VerifyTestCasesPageLocators(object):

    ENTER_HOMPAGE_URL = "https://automationexercise.com/"
    TEST_CASES_HYPERLINK = (By.XPATH, '//*[@id="header"]/div/div/div/div[2]/div/ul/li[5]/a')
    TEST_CASES_PAGE_H2 = (By.XPATH, '//h2')