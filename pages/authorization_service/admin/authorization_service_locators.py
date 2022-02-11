from selenium.webdriver.common.by import By


class AuthorizationServiceLocators:
    LOGIN_INPUT = (By.XPATH,"//input[@name='login']")
    PASSWORD_INPUT = (By.XPATH,"//input[@name='password']")
    SUBMIT_BUTTON = (By.XPATH,"//button[@type='submit']")

    #region Панель элементов
    ADD_USER_BUTTON = (By.XPATH,"//a[contains(.,'Добавить')]")
    EDIT_USER_BUTTON = (By.XPATH,"//button[@title='Редактировать']")
    DELETE_USER_BUTTON = (By.XPATH,"//button[@title='Удалить']")
    COPY_USER_BUTTON = (By.XPATH,"//button[@title='Копировать']")
    BLOCK_USER_BUTTON = (By.XPATH,"//button[@title='Заблокировать']")
    UNBLOCK_USER_BUTTON = (By.XPATH,"//button[@title='Разблокировать']")
    CONFIRM_USER_BUTTON = (By.XPATH,"//button[@title='Подтвердить']")
    EVENT_JOURNAL_BUTTON = (By.XPATH,"//button[@title='Журнал событий']")
    UPDATE_SESSION_BUTTON = (By.XPATH,"//button[@title='Обновить список']")
    SEARCH_USER_BUTTON = (By.XPATH,"//input[@type='search']")
    #endregion
    #region Свойства пользователей

    BACK_BUTTON = (By.XPATH,"//*[@class='form-header']//button[@class='btn btn-primary']")
    SAVE_BUTTON = (By.XPATH,"//*[@class='form-header']//button[@class='btn btn-success']")

    # Разделы
    USER_PROFILE_TAB = (By.XPATH,"//*[@class='nav-item' and @role]//a[contains(.,'Профиль')]")
    USER_PROFILE_TAB = (By.XPATH,"//*[@class='nav-item' and @role]//a[contains(.,'Приложения')]")

    # Профиль
    USER_PASSWORD_INPUT = (By.XPATH,"(//*[@class='row']//fieldset[@class='form-group'])[1]//input")
    USER_PASSWORD_SHOW_BUTTON = (By.XPATH,"(//*[@class='row']//fieldset[@class='form-group'])[1]//button")

    USER_PASSWORD_POLITIC_CHECKBOX = (By.XPATH,"(//*[@class='row']//fieldset[@class='form-group'])[3]//input")
    USER_PASSWORD_GENERATE_BUTTON = (By.XPATH,"(//*[@class='row']//fieldset[@class='form-group'])[2]//button")
    USER_PASSWORD_CHANGE_CHECKBOX = (By.XPATH,"(//*[@class='row']//fieldset[@class='form-group'])[2]//input")

    CERTIFICATE_INPUT = (By.XPATH,"(//*[@class='row']//fieldset[@class='form-group'])[4]//input")
    CERTIFICATE_PUBLISHER_INPUT = (By.XPATH,"(//*[@class='row']//fieldset[@class='form-group'])[5]//input")
    USER_LOGIN_INPUT = (By.XPATH,"(//*[@class='row']//fieldset[@class='form-group'])[6]//input")
    USER_SURNAME_INPUT = (By.XPATH,"(//*[@class='row']//fieldset[@class='form-group'])[7]//input")
    USER_NAME_INPUT = (By.XPATH,"(//*[@class='row']//fieldset[@class='form-group'])[8]//input")
    USER_LASTNAME_INPUT = (By.XPATH,"(//*[@class='row']//fieldset[@class='form-group'])[9]//input")
    USER_SNILS = (By.XPATH,"(//*[@class='row']//fieldset[@class='form-group'])[10]//input")
    USER_DOMAIN_MANE_INPUT = (By.XPATH,"(//*[@class='row']//fieldset[@class='form-group'])[11]//input")
    USER_EMAL_INPUT = (By.XPATH,"(//*[@class='row']//fieldset[@class='form-group'])[12]//input")

    #Приложения
    ADD_APP_BUTTON = (By.XPATH,"//button[contains(.,'Добавить')]")
    DELETE_APP_BUTTON = (By.XPATH,"//button[contains(.,'Удалить')]")
    ATTRIBUTE_APP_BUTTON = (By.XPATH,"//button[contains(.,'Атрибуты')]")
    APPS_TABLE = (By.XPATH,"//*[@role='table']")

    #endregion

    #region Настройки сервиса
    SERVICE_TAB = (By.XPATH,"//span[contains(.,'Сервис')]")
    SERVICE_SETTING = (By.XPATH,"//a[contains(.,'Настройки')]")
    SETTINGS_SAVE_BUTTON = (By.XPATH, "//button[contains(.,'Сохранить')]")
    # Политика блокировок
    MAX_FAIL_LOGIN_COUNT_INPUT =(By.XPATH,"(//*[@class='card-header bg-white' and contains(.,'Политики блокировок')]/parent::*//*[@class='row']//input)[1]")
    LOGIN_BLOCK_NOT_USE_TIME_INPUT =(By.XPATH,"(//*[@class='card-header bg-white' and contains(.,'Политики блокировок')]/parent::*//*[@class='row']//input)[2]")
    LOGIN_BLOCK_TIME_INPUT =(By.XPATH,"(//*[@class='card-header bg-white' and contains(.,'Политики блокировок')]/parent::*//*[@class='row']//input)[3]")

    # Парольные политики
    CHECK_PASSWORDS = (By.XPATH,"//*[@class='card-header bg-white' and contains(.,'Парольные политики')]/parent::*//*[@class='row']//select")
    MIN_SYMBOL_IN_PASSWORD = (By.XPATH,"(//*[@class='card-header bg-white' and contains(.,'Парольные политики')]/parent::*//*[@class='row']//input)[1]")
    MIN_LIFE_PASSWORD_IN_DAYS = (By.XPATH,"(//*[@class='card-header bg-white' and contains(.,'Парольные политики')]/parent::*//*[@class='row']//input)[2]")
    MAX_LIFE_PASSWORD_IN_DAYS = (By.XPATH,"(//*[@class='card-header bg-white' and contains(.,'Парольные политики')]/parent::*//*[@class='row']//input)[3]")
    MIN_CHANGE_SYMBOL_IN_PASSWORD = (By.XPATH,"(//*[@class='card-header bg-white' and contains(.,'Парольные политики')]/parent::*//*[@class='row']//input)[4]")
    LAST_PASSWORD_COUNT = (By.XPATH,"(//*[@class='card-header bg-white' and contains(.,'Парольные политики')]/parent::*//*[@class='row']//input)[5]")


    #endregion