from selenium.webdriver.common.by import By


class Locators(object):

    ENTER_HOMPAGE_URL = "https://automationexercise.com/"
    SIGN_IN_OR_SIGN_UP_HYPERLINK = (By.XPATH, '//*[@id="header"]/div/div/div/div[2]/div/ul/li[4]/a')
    SIGN_IN_OR_SIGN_UP_PAGE_H2 = (By.XPATH, '//h2')
    SIGN_UP_NAME = (By.CSS_SELECTOR, '[data-qa="signup-name"]')
    SIGN_UP_EMAIL = (By.CSS_SELECTOR, '[data-qa="signup-email"]')
    SIGN_UP_BTN = (By.CSS_SELECTOR, '[data-qa="signup-button"]')
    ENTER_ACCOUNT_INFO_TEXT = (By.XPATH, '//*[@id="form"]/div/div/div/div/h2')
    ID_GENDER_1 = (By.ID, 'id_gender1')
    PASSWORD = (By.ID, 'password')
    DATE_OF_BIRTH_DAYS_DROPDOWN = (By.ID, 'days')
    DATE_OF_BIRTH_DAYS = (By.XPATH, f"//option[@value='26']")
    DATE_OF_BIRTH_MONTHS_DROPDOWN = (By.ID, 'months')
    DATE_OF_BIRTH_MONTHS = (By.XPATH, f"//option[@value='5']")
    DATE_OF_BIRTH_YEARS_DROPDOWN = (By.ID, 'years')
    DATE_OF_BIRTH_YEARS = (By.XPATH, f"//option[@value='1990']")
    RECEIVE_SPECIAL_OFFER_CHECKBOX = (By.ID, 'optin')
    FIRST_NAME = (By.ID, 'first_name')
    LAST_NAME = (By.ID, 'last_name')
    COMPANY = (By.ID, 'company')
    ADDRESS_1 = (By.ID, 'address1')
    COUNTRY_DROPDOWN = (By.CSS_SELECTOR, '[data-qa="country"]')
    COUNTRY = (By.XPATH, f"//option[@value='United States']")
    STATE = (By.ID, 'state')
    CITY = (By.ID, 'city')
    ZIPCODE = (By.ID, 'zipcode')
    MOBILE_NUMBER = (By.ID, 'mobile_number')
    CREATE_ACCOUNT_BTN = (By.CSS_SELECTOR, '[data-qa="create-account"]')
    ACCOUNT_CREATED_TEXT = (By.CSS_SELECTOR, '[data-qa="account-created"]')
