from pages.authorization_service.user_profile.user_profile_locators import UserProfileLocators
from pages.base_page import BasePage


class UserProfileFunctions(BasePage):
    save_button = None
    change_password_button = None
    logout_button = None
    lastname_input = None
    name_input = None
    middlename_input = None
    snils_input = None
    domainname_input = None
    email_input = None

    def __init__(self, page):
        """
        Конструктор класса UserProfileFunctions.

        :param page: объект класса WebElement, относительно которого выполняется поиск элементов (например browser)
        """
        self.save_button = page.find_element(*UserProfileLocators.SAVE_BUTTON)
        self.change_password_button = page.find_element(*UserProfileLocators.CHANGE_PASSWORD_BUTTON)
        self.logout_button = page.find_element(*UserProfileLocators.LOGOUT_BUTTON)
        self.lastname_input = page.find_element(*UserProfileLocators.LASTNAME_INPUT)
        self.name_input = page.find_element(*UserProfileLocators.NAME_INPUT)
        self.middlename_input = page.find_element(*UserProfileLocators.MIDDLENAME_INPUT)
        self.snils_input = page.find_element(*UserProfileLocators.SNILS_INPUT)
        self.domainname_input = page.find_element(*UserProfileLocators.DOMAINNAME_INPUT)
        self.email_input = page.find_element(*UserProfileLocators.EMAIL_INPUT)

    def save_settings(self):
        """
        Сохранение настроек пользователя

        :return: Ничего не возвращает. Результат - сохранение настроек
        """
        self.save_button.click()
    def logout(self):
        """
        Деавторизация пользователя

        :return: Ничего не возвращает. Результат - деавторизация пользователя
        """
        self.logout_button.click()
    def change_password(self,old_password,new_password):
        """
        Изменение пароля пользователя

        :param str old_password: Значение старого пароля

        :param str new_password: Значение нового пароля

        :return: Ничего не возвращает. Результат - изменение пароля
        """
        old_password_input = self.browser.find_element_by_xpath("//*[@name='OldPassword']")
        new_password_input = self.browser.find_element_by_xpath("//*[@name='NewPassword']")
        new_password_repeat_input = self.browser.find_element_by_xpath("//*[@name='NewPasswordRepeat']")
        submit_button = self.browser.find_element_by_xpath("//button[contains(.,'Сохранить изменение')]")
        try:
            old_password_input.clear()
        except:
            pass

        try:
            new_password_input.clear()
        except:
            pass
        try:
            new_password_repeat_input.clear()
        except:
            pass
        old_password_input.send_keys(old_password)
        new_password_input.send_keys(new_password)
        new_password_repeat_input.send_keys(new_password)
        submit_button.click()
    def set_lastname(self,value):
        """
        Изменение фамилии пользователя

        :param str value: новое значение фамилии

        :return: Ничего не возвращает. Результат выполнения - установка нового значения фамилии
        """
        try:
            self.lastname_input.clear()
        except:
            pass
        self.lastname_input.send_keys(value)
    def set_name(self, value):
        """
        Изменение имени пользователя

        :param str value: новое значение имени

        :return: Ничего не возвращает. Результат выполнения - установка нового значения имени
        """
        try:
            self.name_input.clear()
        except:
            pass
        self.name_input.send_keys(value)
    def set_middlename(self, value):
        """
        Изменение отчества пользователя

        :param str value: новое значение отчества

        :return: Ничего не возвращает. Результат выполнения - установка нового значения отчества
        """
        try:
            self.middlename_input.clear()
        except:
            pass
        self.middlename_input.send_keys(value)
    def set_domainname(self, value):
        """
        Изменение доменного имени пользователя

        :param str value: новое значение доменного имени

        :return: Ничего не возвращает. Результат выполнения - установка нового значения доменного имени
        """
        try:
            self.domainname_input.clear()
        except:
            pass
        self.domainname_input.send_keys(value)
    def set_snils(self, value):
        """
        Изменение СНИЛСа пользователя

        :param str value: новое значение имени

        :return: Ничего не возвращает. Результат выполнения - установка нового значения СНИЛСа
        """
        try:
            self.snils_input.clear()
        except:
            pass
        self.snils_input.send_keys(value)

    def set_email(self, value):
        """
        Изменение e-mail пользователя

        :param str value: новое значение e-mail

        :return: Ничего не возвращает. Результат выполнения - установка нового значения e-mail
        """
        try:
            self.email_input.clear()
        except:
            pass
        self.email_input.send_keys(value)
