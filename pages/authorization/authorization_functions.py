import json
import os
import time
from collections import defaultdict

from pages.authorization.authorization_locators import AuthorizationLocators
from pages.base_page import BasePage
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.firefox.webdriver import WebDriver


class AuthorizationFunctions(BasePage):

    def import_data(self):
        elements = []
        ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
        with open(os.path.join(ROOT_DIR, 'user_data.json'), encoding="utf-8") as f:
            elements = json.load(f)
        return elements
    def go_to_login(self):
        try:
            self.browser.find_element(*AuthorizationLocators.ENTER_BTN).click()
        except:
            assert False, "Не удалось перейти на страницу авторизации"
        BasePage.ожидание_прогрузки_страницы(self)
    def login_by_service_auth(self):
        """
        Авторизация пользователя через сервис авторизации

        :return: Ничего не возвращает. Результат выполнения - тык по ссылку "Войти через сервис авторизации"
        """
        try:
            BasePage.ждать_пока_элемент_отсутсвует(self, *AuthorizationLocators.SERVICE_AUTH)
            self.browser.find_element(*AuthorizationLocators.SERVICE_AUTH).click()
            BasePage.ожидание_прогрузки_страницы(self)
        except:
            assert False, "Не удалось авторизоваться через сервис авторизации - ссылка не доступна или отсутсвует"
    def logout(self):
        """
        Деавторизация пользователя

        :return: Ничего не возвращает. Результат выполнения - деавторизация пользователя из АльфаДок, сервиса авторизации и почтового сервиса
        """
        self.browser.get(self.common_address+"/accounts/logout")
        BasePage.ожидание_прогрузки_страницы(self)
        self.browser.get(self.autorization_service_address+"/Account/LogoutProfile")
        BasePage.ожидание_прогрузки_страницы(self)
        self.browser.get(self.mail_service_address+"/accounts/logout")
        BasePage.ожидание_прогрузки_страницы(self)
    def login(self,login,password):
        """
        Авторизация пользователя. Функция универсально для АльфаДок, почтового сервиса, сервиса авторизации

        :param str login: логин пользователя

        :param str password: пароль пользователя

        :return: Ничего не возвращает. Результат выполнения -  авторизация пользователя
        """
        BasePage.ждать_пока_элемент_отсутсвует(self, *AuthorizationLocators.LOGIN_INPUT)
        # В ряде случае очистка пустого поля ввода приводит к ошибке. Возможно костыль?
        try:
            self.browser.find_element(*AuthorizationLocators.LOGIN_INPUT).clear()
        except:
            pass
        try:
            self.browser.find_element(*AuthorizationLocators.PASSWORD_INPUT).clear()
        except:
            pass

        try:
            self.browser.find_element(*AuthorizationLocators.LOGIN_INPUT).send_keys(login)
        except:
            assert False, "Поле ввода логина недоступно или отсутствует"
        try:
            self.browser.find_element(*AuthorizationLocators.PASSWORD_INPUT).send_keys(password)
        except:
            assert False, "Поле ввода пароля недоступно или отсутствует"

        try:
            self.browser.find_element(*AuthorizationLocators.LOGIN_SUBMIT).click()
        except:
            assert False, "Команда авторизации недоступна или отсутствует"
        BasePage.ожидание_прогрузки_страницы(self)
    def get_alert_message(self):
        """
        Получение сообщения об ошибке при авторизации. Для проверки отсутсвия ошибки проверять с пустым значением

        :return: Возвращает текст ошибки или "", если ошибки нет
        """
        current_message = ""
        try:
            alert = self.browser.find_element(*AuthorizationLocators.ALERT_MESSAGE)
            current_message = alert.text
        except:
            pass
        return current_message
    def reset_password(self):
        """
        Сброс пароля пользователя

        :return: Возвращает текст сообщения, возникшее по выполнению сброса
        """

        try:
            self.browser.find_element_by_xpath("//*[contains(@class,'login__recovery-password-btn')]").click()
        except:
            assert False, "Команда восстановления пароля недоступна или отсутствует"
        searching = True
        while searching:
            try:
                window = self.browser.find_element_by_xpath("//*[contains(@class,'alert-modal modal fade show')]")
                searching = False
            except:
                time.sleep(1)

        try:
            window_text = window.find_element_by_xpath("//*[contains(@class,'modal-dialog-centered')]//*[@class='modal-body']//span").text
        except:
            assert False, "Не удалось получить текст модального окна"
        try:
            self.browser.find_element_by_xpath("//*[contains(@class,'alert-modal__close-btn')]").click()
        except:
            assert False, "Команда 'Закрыть' модального окна недоступно или отсутствует на странице"
        return window_text


