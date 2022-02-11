import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from pages.base_page import BasePage
from pages.authorization_service.admin.authorization_service_locators import AuthorizationServiceLocators


class AuthorizationService:
    __element = None
    __add_user_button = None
    __edit_user_button = None
    __delete_user_button = None
    __copy_user_button = None
    __block_user_button = None
    __unblock_user_button = None
    __confirm_user_button = None
    __event_journal_button = None
    __update_button = None
    __search_user_input = None
    def __init__(self,page):
        """
        Конструктор объекта класса "AuthorizationService"

        :param page: елемент типа "WebElement", относительно которого будет выполнен поиск (например browser)

        """
        self.element = page.find_element_by_xpath("//div[contains(@class,'app-body')]")
        self.add_user_button = self.element.find_element(*AuthorizationServiceLocators.ADD_USER_BUTTON)
        self.edit_user_button = self.element.find_element(*AuthorizationServiceLocators.EDIT_USER_BUTTON)
        self.delete_user_button = self.element.find_element(*AuthorizationServiceLocators.DELETE_USER_BUTTON)
        self.copy_user_button = self.element.find_element(*AuthorizationServiceLocators.COPY_USER_BUTTON)
        self.block_user_button = self.element.find_element(*AuthorizationServiceLocators.BLOCK_USER_BUTTON)
        self.unblock_user_button = self.element.find_element(*AuthorizationServiceLocators.UNBLOCK_USER_BUTTON)
        self.confirm_user_button = self.element.find_element(*AuthorizationServiceLocators.CONFIRM_USER_BUTTON)
        self.event_journal_button = self.element.find_element(*AuthorizationServiceLocators.EVENT_JOURNAL_BUTTON)
        self.update_button = self.element.find_element(*AuthorizationServiceLocators.UPDATE_SESSION_BUTTON)
        self.search_user_input = self.element.find_element(*AuthorizationServiceLocators.SEARCH_USER_BUTTON)
        self.service = self.element.find_element(*AuthorizationServiceLocators.SERVICE_TAB)

    def logout(self):
        '''
        Деавторизация пользователя из сервиса авторизации средствами интерфейса. В качестве аргумента вызова передать self браузера
        :return: Ничего не возвращает. Результат выполнения - переход на страницу авторизации
        '''
        BasePage.ждать_пока_элемент_отсутсвует(self,By.CSS_SELECTOR,".nav-item.b-nav-dropdown.dropdown.ml-auto a[role='button']")
        self.browser.find_element_by_css_selector(".nav-item.b-nav-dropdown.dropdown.ml-auto a[role='button']").click()
        self.browser.find_element_by_xpath("//*[@role='menuitem' and contains(.,'Выйти')]").click()
        BasePage.ожидание_прогрузки_страницы(self)
    def login(self, login=None, password=None):
        '''
        Авторизация пользователя в админке сервисе авторизации. В случае наличия авторизованного пользователя в рамках сессии - выполняется деавторизация пользователя.

        :param string login: Имя пользователя администратора. По умолчанию - admin
        :param string password: Пароль пользователя с правами администратора. По умолчанию - в соответствии с conftest теста

        :return: Ничего не возвращает. Функция считается успешно выполненной, если по выполнению авторизации удалось найти элемент интерфейса редактирования таблимцы польщователей
        '''

        if login==None and password == None:
            login = "admin"
            password = self.autorization_service_admin_password
        try:
            current_url = self.browser.current_url
            if current_url != self.autorization_service_address + "/admin/login":
                AuthorizationService.logout(self)
                self.browser.get(self.autorization_service_address+"/admin/login")
        except:
            pass

        login_element = self.browser.find_element(*AuthorizationServiceLocators.LOGIN_INPUT)
        login_element.click()
        try:
            login_element.clear()
        except:
            pass
        login_element.send_keys(login)
        password_element = self.browser.find_element(*AuthorizationServiceLocators.PASSWORD_INPUT)
        password_element.click()
        try:
            password_element.clear()
        except:
            pass
        password_element.send_keys(password)
        enter_button = self.browser.find_element(*AuthorizationServiceLocators.SUBMIT_BUTTON)
        enter_button.click()
        BasePage.ждать_пока_элемент_отсутсвует(self, *AuthorizationServiceLocators.UPDATE_SESSION_BUTTON)
    def wait_loading(self):
        """
        Ожидание загрузки страницы сервиса авторизации - каждые пол секунды выполняется попытка поиска шапки пользователей

        :return: Функция завершается по нахождения таблицы пользователей
        """
        loading = True
        while loading:
            try:
                self.browser.find_element_by_css_selector(".app-header")
                loading = False
            except:
                time.sleep(0.5)
    # Общая таблица
    def search_user(self,username):
        """
        Фильтрация таблицы пользователей по заданному имени пользователя (логину)

        :param string username: Вхождение строки, по которому будет выполнен поиск
        :return: Ничего не возвращает. Ожидаемый результат - таблица пользоателей отфильтрована по заданному вхождению
        """
        self.search_user_input.click()
        try:
            self.search_user_input.clear()
        except:
            pass
        self.search_user_input.send_keys(username)
    def wait_while_search(self):
        """
        Ожидание прогрузки таблицы пользователей по выполнению поиска записей

        :return: Ничего не возвращает. Функция считается выполненной, когда обновление страницы будет завершено
        """
        searching = True
        while searching:
            try:
                self.browser.find_element_by_xpath("//table[@aria-busy='true']")
                time.sleep(0.5)
            except:
                searching = False
    def search_user_in_table(self,username):
        """
        Поиск записи в таблице по заданному вхождению имени пользователя (логину)

        :param string username: Логин пользователя, которого следует найти

        :return: возвращает элемент типа WebElement - строку таблицы, соответствующую заданному логину пользователя
        """
        rows = self.element.find_elements_by_xpath("//table//tbody//tr")
        for row in rows:
            try:
                found = row.find_element_by_xpath("//td[@aria-colindex='2' and contains(.,'"+username+"')]")
            except:
                pass
        return found
    def select_row(self,row):
        """
        Выделение строки таблицы

        :param object row: элемент типа WebElement, соответствующий строке таблицы

        :return: Ничего не возвращает. Результат - строка пользователя в таблице выделена
        """
        row.click()
    def delete_user(self,row):
        """
        Удаление пользователя.

        :param object row: элемент типа WebElement, соответствующий строке пользователя

        :return: Ничего не возвращает. Результат - удаление строки пользователя из таблицы
        """
        AuthorizationService.select_row(self, row)
        self.delete_user_button.click()
        delete_button = row.find_element_by_xpath("//ancestor::body//button[contains(.,'Подтвердить')]")
        delete_button.click()
        try:
            delete_button= row.find_element_by_xpath("//ancestor::body//button[contains(.,'Подтвердить')]")
            delete_button.click()
        except:
            pass
    def confirm_user(self,row):
        """
        Подтверждение почты выбранного пользователя

        :param object row: элемент типа WebElement, соответствующий строке таблицы

        :return: Ничего не возвращает. Результат - пользователь подтверждён
        """
        AuthorizationService.select_row(self, row)
        self.confirm_user_button.click()
    def block_user(self,row):
        """
        Блокировка пользователя

        :param object row: элемент типа WebElement, соответствующий строке таблицы

        :return: Ничего не возвращает. Результат - пользователь заблокирован
        """
        AuthorizationService.select_row(self, row)
        self.block_user_button.click()
    def unblock_user(self,row):
        """
        Разблокировка пользователя

        :param object row: элемент типа WebElement, соответствующий строке таблицы

        :return: Ничего не возвращает. Результат - пользователь разблокирован
        """
        AuthorizationService.select_row(self, row)
        self.unblock_user_button.click()
    def edit_user(self, row):
        """
        Переход в режим редактирования пользователя

        :param object row: элемент типа WebElement, соответствующий строке таблицы

        :return: Ничего не возвращает. Результат - открытие редактора свойств пользователя
        """

        AuthorizationService.select_row(self, row)
        self.edit_user_button.click()
        # Заменить на ожидание отображения свойств пользователя
    def update(self):
        """
        Обновление таблицы пользователей

        :return: Ничего не возвращает. Результат - обновление таблицы пользователей
        """

        self.update_button.click()
        AuthorizationService.wait_while_search(self)

    def creat_new_user(self,username):
        """
        (Не реализовано)Переход в режим создания нового пользователя.
        :param usernmae:
        :return:
        """
        pass
    # Свойства пользователя
    def get_politic_state(self):
        """
        Получение значения флага учета политик безопасности пароля
        Вызывается на странице свойств пользователя

        :return:  Значение флага "True" или "False"
        """

        password_politic_checkbox = self.browser.find_element(*AuthorizationServiceLocators.USER_PASSWORD_POLITIC_CHECKBOX)
        value = password_politic_checkbox.get_property("checked")
        return value
    def set_politic(self):
        """
        Установка флага учета политик безопасности пароля

        :return: Ничего не возвращает. Результат выполнения - установка флага
        """
        password_politic_checkbox = self.browser.find_element(*AuthorizationServiceLocators.USER_PASSWORD_POLITIC_CHECKBOX)
        password_politic_label = password_politic_checkbox.find_element_by_xpath("//parent::*/label[contains(.,'Включить политику паролей')]")
        password_politic_label.click()
    def user_change_password(self,password):
        """
        Установка нового пароля парользователю

        :param str password: Новое значение пароля

        :return: Ничего не возвращает. Результат: установка нового пароля
        """
        change_password_checkbox = self.browser.find_element(*AuthorizationServiceLocators.USER_PASSWORD_CHANGE_CHECKBOX)
        change_password_label = change_password_checkbox.find_element_by_xpath("//parent::*/label[contains(.,'Сменить пароль')]")
        change_password_label.click()

        # Проверка на заблокированность поля ввода пароля
        wait = True
        while wait:
            try:
                self.browser.find_element_by_xpath("//legend[contains(.,'Пароль')]/parent::*/parent::fieldset[@disabled='disabled']")
                change_password_checkbox.click()
                time.sleep(0.5)
            except:
                wait = False

        password_input = self.browser.find_element(*AuthorizationServiceLocators.USER_PASSWORD_INPUT)
        try:
            password_input.clear()
        except:
            pass
        password_input.send_keys(password)
    def user_save_change(self):
        """
        Сохранение внесённых изменений свойств пользователя

        :return: Ничего не возвращает. Результат выполнения - выполнение команды "Сохранить"
        """
        self.browser.find_element(*AuthorizationServiceLocators.SAVE_BUTTON).click()
        try:
            error_message = self.browser.find_element_by_xpath("//strong[contains(.,'Ошибка сохранения')]")
            return False
        except:
            return True


    # Настройки
    def open_settings(self):
        """
        Открытие настроек сервиса авторизации пользователей

        :return: Ничего не возвращает. Результат выполнения -  открытие настроек сервиса авторизации
        """
        self.browser.find_element(*AuthorizationServiceLocators.SERVICE_TAB).click()
        self.browser.find_element(*AuthorizationServiceLocators.SERVICE_SETTING).click()
        BasePage.ждать_пока_элемент_отсутсвует(self, *AuthorizationServiceLocators.SETTINGS_SAVE_BUTTON)

    def save_settings(self):
        """
        Сохранение настроек сервиса авторизации пользователей

        :return: Ничего не возвращает. Результат выполнения -  сохранение настроек сервиса авторизации        """
        self.browser.find_element(*AuthorizationServiceLocators.SETTINGS_SAVE_BUTTON).click()
        BasePage.ждать_пока_элемент_отсутсвует(self, By.XPATH, '//*[@aria-label="Close"]')
        self.browser.find_element_by_xpath('//*[@aria-label="Close"]').click()

    def set_max_fail_login(self,count):
        """
        Установка значения параметра "Максимальное количество попыток неуспешных входов"

        :param str count: новое значение параметра

        :return: Ничего не возвращает. Результат - удачная установка нового значения
        """
        BasePage.ждать_пока_элемент_отсутсвует(self, *AuthorizationServiceLocators.MAX_FAIL_LOGIN_COUNT_INPUT)
        input = self.browser.find_element(*AuthorizationServiceLocators.MAX_FAIL_LOGIN_COUNT_INPUT)
        try:
            input.clear()
        except:
            pass
        input.send_keys(count)
    def set_login_block_time(self,time):
        """
        Установка значения параметра "Период блокировки входа в комплекс (в секундах)"

        :param str time: новое значение параметра

        :return: Ничего не возвращает. Результат - удачная установка нового значения
        """
        BasePage.ждать_пока_элемент_отсутсвует(self, *AuthorizationServiceLocators.LOGIN_BLOCK_TIME_INPUT)
        input = self.browser.find_element(*AuthorizationServiceLocators.LOGIN_BLOCK_TIME_INPUT)
        try:
            input.clear()
        except:
            pass
        input.send_keys(time)

    def set_check_password(self,value):
        """
        Установка значения параметра "Проверять надежность пароля"

        :param  str value: Новое значение параметра - "Да или "Нет"

        :return: Ничего не возвращает. Результат - устанавливка нового значения
        """
        select_elem = self.browser.find_element(*AuthorizationServiceLocators.CHECK_PASSWORDS)
        Select(select_elem).select_by_visible_text(value)


