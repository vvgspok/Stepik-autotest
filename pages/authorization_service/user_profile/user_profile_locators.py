from selenium.webdriver.common.by import By


class UserProfileLocators:
    SAVE_BUTTON = (By.XPATH, "//*[@data-original-title='Сохранить']")
    CHANGE_PASSWORD_BUTTON = (By.XPATH, "//*[@data-original-title='Сменить пароль']")
    LOGOUT_BUTTON = (By.XPATH, "//*[@data-original-title='Сохранить']")

    LASTNAME_INPUT = (By.XPATH,"//input[@name='LastName']")
    NAME_INPUT = (By.XPATH,"//input[@name='FirstName']")
    MIDDLENAME_INPUT = (By.XPATH,"//input[@name='MiddleName']")
    SNILS_INPUT = (By.XPATH,"//input[@name='Snils']")
    DOMAINNAME_INPUT = (By.XPATH,"//input[@name='DomainName']")
    EMAIL_INPUT = (By.XPATH,"//input[@name='Email']")