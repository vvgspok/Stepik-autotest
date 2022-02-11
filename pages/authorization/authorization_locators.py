from selenium.webdriver.common.by import By


class AuthorizationLocators():
    #Кнопка "Войти"
    ENTER_BTN = (By.CSS_SELECTOR, ".enter-button")
    SERVICE_AUTH = (By.LINK_TEXT, "Войти через сервис авторизации")

    LOGIN_INPUT = (By.ID, "loginInput")
    PASSWORD_INPUT = (By.ID, "passwordInput")
    LOGIN_SUBMIT = (By.CSS_SELECTOR, ".login__submit-password-btn")
    REMEMBER_CHECKBOX = (By.CSS_SELECTOR, "#rememberLogin")
    RECOVERY_PASSWORD = (By.CSS_SELECTOR, ".login__recovery-password-btn")

    ALERT_MESSAGE = (By.XPATH, f'//div[@class="alert alert-danger mt-5 alert-dismissible fade show"]/span')