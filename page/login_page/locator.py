from selenium.webdriver.common.by import By


class Locator(object):

    SIGN_IN_OR_SIGN_UP_PAGE_H2 = (By.XPATH, '//h2')
    SIGN_UP_NAME = (By.CSS_SELECTOR, '[data-qa="signup-name"]')
    SIGN_UP_EMAIL = (By.CSS_SELECTOR, '[data-qa="signup-email"]')
    SIGN_UP_BTN = (By.CSS_SELECTOR, '[data-qa="signup-button"]')
    EMAIL_ADDRESS_ALR_EXIST = (
        By.XPATH, '//*[@id="form"]/div/div/div[3]/div/form/p')
