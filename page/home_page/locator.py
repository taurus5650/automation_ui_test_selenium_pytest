from selenium.webdriver.common.by import By


class Locator(object):

    ENTER_HOMPAGE_URL = "https://automationexercise.com/"
    SIGN_IN_OR_SIGN_UP_HYPERLINK = (
        By.XPATH, '//*[@id="header"]/div/div/div/div[2]/div/ul/li[4]/a'
    )
