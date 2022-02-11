import json
import os
import time
from datetime import datetime

from pages.base_page import BasePage
from collections import defaultdict
from pages.public_page.public_page_locators import RegisterLocators
from selenium import webdriver

class RegisterCheckFunctions(BasePage):

    def set_select2_value(self,element,value):
        element.click()
        self.find_element_by_xpath('//div[@class = "select2-result-label" and contains(.,"' + value + '")]').click()
    def get_active_step(self):
        tabs = self.browser.find_elements_by_css_selector(".block-section.enter-register-data.item")
        for inx, tab in enumerate(tabs):
            str = tab.get_attribute("class").find("active")
            if (str > 0):
                index = inx + 1
        return index
    # Проверка справок
    def check_helpblock(self, locator, value):
        """
        Проверка корректности текста справки

        :param str locator: Локатор элемента справки
        :param str value: Ожидаемое значение
        :return: В случае не совпадение возникает исключение
        """
        elements = self.browser.find_elements(*locator)
        helpblock=""
        for element in elements:
         try:
             helpblock = helpblock + " " + element.text
         except:
             helpblock = helpblock + ""
        helpblock = helpblock.strip()
        assert helpblock == value, "Некорректнаыя подсказка. \nОжидается"+helpblock+" .Фактически"+value

    class FirstStep():
        def import_data(self):
            elements = []
            ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
            with open(os.path.join(ROOT_DIR, 'register_data.json'), encoding="utf-8") as f:
                pars = json.load(f)
                for lines in pars["step1"]:
                    dict_data = defaultdict(dict)
                    for type in pars["step1"][0]:
                        if (type != "validation"):
                            dict_data[type]["input"] = lines[type]["input"].replace("_data_", datetime.now().strftime(
                                "%d%m%Y%H%M%S"))
                            dict_data[type]["help_message"] = lines[type]["help_message"]
                        else:
                            dict_data[type] = lines[type]
                    elements.append(dict_data)
            return elements
        #Установка значений
        def set_fullname(self,value):
            """
            Установка значения "ФИО" на первом шаге регистрации

            :param value: Устанавливаемое значение

            :return:
            """
            try:
                full_name = self.browser.find_element(*RegisterLocators.FULL_USERNAME_FORMGROUP)
            except:
                assert False, "Отсутствует поле ввода ФИО"
            try:
                BasePage.FormGroup(full_name).set_value(value)
            except:
                assert False, "Не удалось установить ФИО сотрудника"

        def set_org_type(self,value):
            org_type = self.browser.find_element(*RegisterLocators.ORGANIZATION_TYPE_FORMGROUP)
            BasePage.FormGroup(org_type).set_value(value)
        def set_username(self,value):
             username =  self.browser.find_element(*RegisterLocators.USERNAME_FORMGROUP)
             BasePage.FormGroup(username).set_value(value)

        def set_inn(self, value):
            inn =  self.browser.find_element(*RegisterLocators.INN_FORMGROUP)
            BasePage.FormGroup(inn).set_value(value)

        def set_phone(self, value):
            phone =  self.browser.find_element(*RegisterLocators.PHONE_FORMGROUP)
            BasePage.FormGroup(phone).set_value(value)

        def set_email(self, value):
            email = self.browser.find_element(*RegisterLocators.EMAIL_FORMGROUP)
            BasePage.FormGroup(email).set_value(value)
        # Переход на следующий шаг
        def go_to_next_step(self):
            index = RegisterCheckFunctions.get_active_step(self)
            for inx in 1, 2, 3:
                index = RegisterCheckFunctions.get_active_step(self)
                if (index == 1):
                    try:
                        self.browser.find_element(*RegisterLocators.BTN_STEP1_NEXT).click()
                        time.sleep(0.5)
                    except:
                        pass
                index = RegisterCheckFunctions.get_active_step(self)
            BasePage.ожидание_прогрузки_страницы(self)
            time.sleep(1)
            try:
                while True:
                    self.browser.find_element_by_xpath("//div[contains(.,'Разрешенные символы')]")
                    time.sleep(0.5)
            except:
                pass
    class SecondStep():
        def import_data(self):
            elements = []
            ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
            with open(os.path.join(ROOT_DIR, 'register_data.json'), encoding="utf-8") as f:
                pars = json.load(f)
                for lines in pars["step2"]:
                    dict_data = defaultdict(dict)
                    dict_data["prepare"]["org_type"] = lines["prepare"]["org_type"]
                    dict_data["data"]["region"] = lines["data"]["region"]
                    dict_data["data"]["activity"] = lines["data"]["activity"]
                    dict_data["helpblock"]["region"] = lines["helpblock"]["region"]
                    dict_data["helpblock"]["activity"] = lines["helpblock"]["activity"]
                    dict_data["validation"] = lines["validation"]
                    elements.append(dict_data)
                return elements
        def set_region(self,value):
            if (value != ""):
                select2 = self.browser.find_element(*RegisterLocators.REGION_FORMGROUP)
                BasePage.FormGroup(select2).set_value(value)
                # select2 = self.browser.find_element(*RegisterLocators.SELECT_REGION)
                # RegisterCheckFunctions.set_select2_value(self.browser, select2, value)
        def set_activity(self,value):
            if (value != ""):
                select2 = self.browser.find_element(*RegisterLocators.ACTIVITY_FORMGROUP)
                BasePage.FormGroup(select2).set_value(value)
                # select2 = self.browser.find_element(*RegisterLocators.SELECT_ACTIVITY)
                # RegisterCheckFunctions.set_select2_value(self.browser, select2, value)

        def go_to_next_step(self):
            index = RegisterCheckFunctions.get_active_step(self)
            for inx in 1, 2, 3:
                index = RegisterCheckFunctions.get_active_step(self)
                if (index == 2):
                    try:
                        self.browser.find_element(*RegisterLocators.BTN_STEP2_NEXT).click()
                        time.sleep(0.5)
                    except:
                        pass
                index = RegisterCheckFunctions.get_active_step(self)
            BasePage.ожидание_прогрузки_страницы(self)
            time.sleep(1)

        def go_to_prev_step(self):
            index = RegisterCheckFunctions.get_active_step(self)
            for inx in 1, 2, 3:
                index = RegisterCheckFunctions.get_active_step(self)
                if (index == 2):
                    try:
                        self.browser.find_elements(*RegisterLocators.BTN_PREV_STEP)[0].click()
                        time.sleep(0.5)
                    except:
                        pass
                index = RegisterCheckFunctions.get_active_step(self)
            BasePage.ожидание_прогрузки_страницы(self)
            time.sleep(1)
    class ThirdStep():
        def import_data(self):
            elements = []
            ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
            with open(os.path.join(ROOT_DIR, 'register_data.json'), encoding="utf-8") as f:
                pars = json.load(f)
                for lines in pars["step3"]:
                    dict_data = defaultdict(dict)
                    dict_data["data"]["password1"] = lines["data"]["password1"]
                    dict_data["data"]["password2"] = lines["data"]["password2"]
                    dict_data["data"]["promocode"] = lines["data"]["promocode"]
                    dict_data["data"]["agreement"] = lines["data"]["agreement"]
                    dict_data["data"]["copy_data"] = lines["data"]["copy_data"]

                    dict_data["helpblock"]["password1"] = lines["helpblock"]["password1"]
                    dict_data["helpblock"]["password2"] = lines["helpblock"]["password2"]
                    dict_data["helpblock"]["promocode"] = lines["helpblock"]["promocode"]
                    dict_data["helpblock"]["agreement"] = lines["helpblock"]["agreement"]
                    elements.append(dict_data)
                return elements
        def go_to_next_step(self):
            try:
                self.browser.find_element(*RegisterLocators.BTN_STEP3_NEXT).click()
                time.sleep(0.5)
            except:
                pass
            BasePage.ожидание_прогрузки_страницы(self)
        def go_to_prev_step(self):
            index = RegisterCheckFunctions.get_active_step(self)
            for inx in 1,2,3:
                index = RegisterCheckFunctions.get_active_step(self)
                if (index == 3):
                    try:
                        self.browser.find_elements(*RegisterLocators.BTN_PREV_STEP)[1].click()
                        time.sleep(1)
                    except:
                        pass
                index = RegisterCheckFunctions.get_active_step(self)
            BasePage.ожидание_прогрузки_страницы(self)
            time.sleep(1)
        def set_password1(self,value):
            password_setted = "False"
            while (password_setted == "False"):
                try:
                    password1 = self.browser.find_element(*RegisterLocators.INPUT_PASSWORD1)
                    password1.click()
                    password1.send_keys(value)
                    password_setted = "True"
                except:
                    pass
        def set_password2(self,value):
            password_setted = "False"
            while (password_setted == "False"):
                try:
                    password2 = self.browser.find_element(*RegisterLocators.INPUT_PASSWORD2)
                    password2.click()
                    password2.send_keys(value)
                    password_setted = "True"
                except:
                    pass

        def set_promocode(self, value):
            promocode_setted = "False"
            while (promocode_setted == "False"):
                try:
                    promocode = self.browser.find_element(*RegisterLocators.INPUT_PROMOCODE)
                    promocode.clear()
                    promocode.click()
                    promocode.send_keys(value)
                    promocode_setted = "True"

                except:
                    pass

        def set_agreement(self, value):

            """
            КОСТЫЛЬ!
            """
            # У флага нет состояния checked. Установка флага определяется по наличию псевдоэлемента "after"
            # Аналогично для флага промокода. В случае определния более лакончиного метода (добавления свойства checked) - изменить и там и там (базовый метод выделять пока смысла не вижу)
            script = "return window.getComputedStyle(document.querySelector('#id_user_agreement + span'),'::after').getPropertyValue('content')"
            script_result = self.browser.execute_script(script).strip()
            if (script_result == "none"):
                state = "False"
            else:
                state = "True"
            if (state != value):
                self.browser.find_element(*RegisterLocators.CHECKBOX_USER_AGREEMENT).click()
                time.sleep(1)
                #Скролл для активизации кнопки "Принять условия" выполняется путем поиска последней строки соглашения
                try:
                    self.browser.find_element_by_xpath("//li[contains(.,'Если для Пользователя неприемлемы')]").click()
                    button = self.browser.find_element_by_xpath("//button[contains(.,'Принять условия')]")
                    button.click()
                    time.sleep(1)
                except:
                    pass

        def set_copy_data(self,value):
            # У флага нет состояния checked. Установка флага определяется по наличию псевдоэлемента "after"
            # Аналогично для флага согласий. В случае определния более лакончиного метода (добавления свойства checked) - изменить и там и там (базовый метод выделять пока смысла не вижу)
            script = "return window.getComputedStyle(document.querySelector('#id_need_copy_data + span'),'::after').getPropertyValue('content')"
            script_result = self.browser.execute_script(script).strip()
            if (script_result == "none"):
                state = "False"
            else:
                state = "True"
            if (state != value):
                self.browser.find_element(*RegisterLocators.CHECKBOX_NEED_COPY_DATA).click()
    class CheckData():
        def import_data(self):
            elements = []
            ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
            with open(os.path.join(ROOT_DIR, 'register_data.json'), encoding="utf-8") as f:
                pars = json.load(f)
                for lines in pars["check_data"]:
                    dict_data = defaultdict(dict)
                    dict_data["org_type"] = lines["org_type"]
                    dict_data["full_name"] = lines["full_name"]
                    dict_data["email"] = lines["email"].replace("_data_", datetime.now().strftime("%d%m%Y%H%M%S"))
                    dict_data["username"] = lines["username"].replace("_data_", datetime.now().strftime("%d%m%Y%H%M%S"))
                    dict_data["phone"] = lines["phone"]
                    dict_data["inn"] = lines["inn"]

                    dict_data["region"] = lines["region"]
                    dict_data["activity"] = lines["activity"]

                    dict_data["password1"] = lines["password1"]
                    dict_data["password2"] = lines["password2"]
                    dict_data["promocode"] = lines["promocode"]
                    dict_data["copy_data"] = lines["copy_data"]
                    dict_data["agreement"] = lines["agreement"]
                    elements.append(dict_data)
                    time.sleep(1) #Для генерации уникальныъ datetime.now(Выполняется слишком быстро и генерирует идентичные логины)
                return elements

        def registration(self,dictionary):
            RegisterCheckFunctions.FirstStep.set_org_type(self,dictionary["prepare"]["org_type"])
            RegisterCheckFunctions.FirstStep.set_fullname(self,dictionary["prepare"]["full_name"])
            RegisterCheckFunctions.FirstStep.set_email(self,dictionary["prepare"]["email"])
            # RegisterCheckFunctions.FirstStep.set_username(self, dictionary["prepare"]["username"])
            RegisterCheckFunctions.FirstStep.set_phone(self, dictionary["prepare"]["phone"])
            RegisterCheckFunctions.FirstStep.set_inn(self, dictionary["prepare"]["inn"])
            RegisterCheckFunctions.FirstStep.go_to_next_step(self)
            RegisterCheckFunctions.SecondStep.set_region(self, dictionary["prepare"]["region"])
            RegisterCheckFunctions.SecondStep.set_activity(self, dictionary["prepare"]["activity"])
            RegisterCheckFunctions.SecondStep.go_to_next_step(self)
            RegisterCheckFunctions.ThirdStep.set_password1(self, dictionary["prepare"]["password1"])
            RegisterCheckFunctions.ThirdStep.set_password2(self, dictionary["prepare"]["password2"])
            RegisterCheckFunctions.ThirdStep.set_promocode(self, dictionary["prepare"]["promocode"])
            RegisterCheckFunctions.ThirdStep.set_copy_data(self, dictionary["prepare"]["copy_data"])
            RegisterCheckFunctions.ThirdStep.set_agreement(self,"True")

            RegisterCheckFunctions.ThirdStep.go_to_next_step(self)
            try:
                while True:
                    self.browser.find_element_by_xpath("//h5[contains(.,'Мы настраиваем Ваш профиль')]")
                    self.browser.find_element_by_xpath("//p[contains(.,'Осталось совсем чуть-чуть')]")
            except:
                pass



class Регистрация:
    def set_select2_value(self,element,value):
        element.click()
        self.find_element_by_xpath('//div[@class = "select2-result-label" and contains(.,"' + value + '")]').click()
    def get_active_step(self):
        tabs = self.browser.find_elements_by_css_selector(".block-section.enter-register-data.item")
        for inx, tab in enumerate(tabs):
            str = tab.get_attribute("class").find("active")
            if (str > 0):
                index = inx + 1
        return index
    # Проверка справок
    def check_helpblock(self, locator, value):
           elements = self.browser.find_elements(*locator)
           helpblock=""
           for element in elements:
             try:
                 helpblock = helpblock + " " + element.text
             except:
                 helpblock = helpblock + ""
           helpblock = helpblock.strip()
           assert helpblock == value, "Некорректнаыя подсказка. \nОжидается"+helpblock+" .Фактически"+value

    class Первый_шаг():
        def Импорт_данных(self):
            elements = []
            ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
            with open(os.path.join(ROOT_DIR, 'register_data.json'), encoding="utf-8") as f:
                pars = json.load(f)
                for lines in pars["step1"]:
                    dict_data = defaultdict(dict)
                    for type in pars["step1"][0]:
                        if (type != "validation"):
                            dict_data[type]["input"] = lines[type]["input"].replace("_data_", datetime.now().strftime(
                                "%d%m%Y%H%M%S"))
                            dict_data[type]["help_message"] = lines[type]["help_message"]
                        else:
                            dict_data[type] = lines[type]
                    elements.append(dict_data)
            return elements
        #Установка значений
        class ФИО:
            def Установить(self,value):
                RegisterCheckFunctions.FirstStep.set_fullname(self,value)
            def Проверить_справку(self,value):
                RegisterCheckFunctions.check_helpblock(self, RegisterLocators.HELPBLOCK_FULL_USERNAME,value)
        class Тип_оргназиации:
            def Установить(self,value):
                RegisterCheckFunctions.FirstStep.set_org_type(self,value)
            def Проверить_справку(self,value):
                RegisterCheckFunctions.check_helpblock(self, RegisterLocators.HELPBLOCK_ORGANIZATION_TYPE,value)
        class Логин:
            def Установить(self,value):
                 RegisterCheckFunctions.FirstStep.set_username(self,value)
            def Проверить_справку(self, value):
                RegisterCheckFunctions.check_helpblock(self, RegisterLocators.HELPBLOCK_USERNAME, value)
        class ИНН:
            def Установить(self, value):
                RegisterCheckFunctions.FirstStep.set_inn(self,value)
            def Проверить_справку(self, value):
                RegisterCheckFunctions.check_helpblock(self, RegisterLocators.HELPBLOCK_INN, value)
        class Телефон:
            def Установить(self, value):
                RegisterCheckFunctions.FirstStep.set_phone(self,value)
            def Проверить_справку(self, value):
                RegisterCheckFunctions.check_helpblock(self, RegisterLocators.HELPBLOCK_PHONE, value)
        class Email:
            def Установить(self, value):
                RegisterCheckFunctions.FirstStep.set_email(self,value)
            def Проверить_справку(self, value):
                RegisterCheckFunctions.check_helpblock(self, RegisterLocators.HELPBLOCK_EMAIL, value)
        # Переход на следующий шаг
        def Следующий_шаг(self):
            index = RegisterCheckFunctions.get_active_step(self)
            for inx in 1, 2, 3:
                index = RegisterCheckFunctions.get_active_step(self)
                if (index == 1):
                    try:
                        self.browser.find_element(*RegisterLocators.BTN_STEP1_NEXT).click()
                        time.sleep(0.5)
                    except:
                        pass
                index = RegisterCheckFunctions.get_active_step(self)
            BasePage.ожидание_прогрузки_страницы(self)
            time.sleep(1)
            try:
                while True:
                    self.browser.find_element_by_xpath("//div[contains(.,'Разрешенные символы')]")
                    time.sleep(0.5)
            except:
                pass

    class Второй_шаг():
        def import_data(self):
            elements = []
            ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
            with open(os.path.join(ROOT_DIR, 'register_data.json'), encoding="utf-8") as f:
                pars = json.load(f)
                for lines in pars["step2"]:
                    dict_data = defaultdict(dict)
                    dict_data["prepare"]["org_type"] = lines["prepare"]["org_type"]
                    dict_data["data"]["region"] = lines["data"]["region"]
                    dict_data["data"]["activity"] = lines["data"]["activity"]
                    dict_data["helpblock"]["region"] = lines["helpblock"]["region"]
                    dict_data["helpblock"]["activity"] = lines["helpblock"]["activity"]
                    dict_data["validation"] = lines["validation"]
                    elements.append(dict_data)
                return elements
        class Регион:
            def Установить(self,value):
                if (value != ""):
                    select2 = self.browser.find_element(*RegisterLocators.REGION_FORMGROUP)
                    RegisterCheckFunctions.set_select2_value(self.browser, select2, value)

            def Проверить_справку(self, value):
                RegisterCheckFunctions.check_helpblock(self, RegisterLocators.HELPBLOCK_REGION, value)

        class Сфера:
            def Установить(self,value):
                if (value != ""):
                    select2 = self.browser.find_element(*RegisterLocators.SELECT_ACTIVITY)
                    RegisterCheckFunctions.set_select2_value(self.browser, select2, value)

            def Проверить_справку(self, value):
                RegisterCheckFunctions.check_helpblock(self, RegisterLocators.HELPBLOCK_ACTIVITY, value)

        def Следующий_шаг(self):
            index = RegisterCheckFunctions.get_active_step(self)
            for inx in 1, 2, 3:
                index = RegisterCheckFunctions.get_active_step(self)
                if (index == 2):
                    try:
                        self.browser.find_element(*RegisterLocators.BTN_STEP2_NEXT).click()
                        time.sleep(0.5)
                    except:
                        pass
                index = RegisterCheckFunctions.get_active_step(self)
            BasePage.ожидание_прогрузки_страницы(self)
            time.sleep(1)
        def Предыдущий_шаг(self):
            index = RegisterCheckFunctions.get_active_step(self)
            for inx in 1, 2, 3:
                index = RegisterCheckFunctions.get_active_step(self)
                if (index == 2):
                    try:
                        self.browser.find_elements(*RegisterLocators.BTN_PREV_STEP)[0].click()
                        time.sleep(0.5)
                    except:
                        pass
                index = RegisterCheckFunctions.get_active_step(self)
            BasePage.ожидание_прогрузки_страницы(self)
            time.sleep(1)
    class Третий_шаг():
        def import_data(self):
            elements = []
            ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
            with open(os.path.join(ROOT_DIR, 'register_data.json'), encoding="utf-8") as f:
                pars = json.load(f)
                for lines in pars["step3"]:
                    dict_data = defaultdict(dict)
                    dict_data["data"]["password1"] = lines["data"]["password1"]
                    dict_data["data"]["password2"] = lines["data"]["password2"]
                    dict_data["data"]["promocode"] = lines["data"]["promocode"]
                    dict_data["data"]["agreement"] = lines["data"]["agreement"]
                    dict_data["data"]["copy_data"] = lines["data"]["copy_data"]

                    dict_data["helpblock"]["password1"] = lines["helpblock"]["password1"]
                    dict_data["helpblock"]["password2"] = lines["helpblock"]["password2"]
                    dict_data["helpblock"]["promocode"] = lines["helpblock"]["promocode"]
                    dict_data["helpblock"]["agreement"] = lines["helpblock"]["agreement"]
                    elements.append(dict_data)
                return elements
        def Завершить_регистрацию(self):
            try:
                self.browser.find_element(*RegisterLocators.BTN_STEP3_NEXT).click()
                time.sleep(0.5)
            except:
                pass
            BasePage.ожидание_прогрузки_страницы(self)
        def Предыдущий_шаг(self):
            index = RegisterCheckFunctions.get_active_step(self)
            for inx in 1,2,3:
                index = RegisterCheckFunctions.get_active_step(self)
                if (index == 3):
                    try:
                        self.browser.find_elements(*RegisterLocators.BTN_PREV_STEP)[1].click()
                        time.sleep(1)
                    except:
                        pass
                index = RegisterCheckFunctions.get_active_step(self)
            BasePage.ожидание_прогрузки_страницы(self)
            time.sleep(1)
        class Придумайте_пароль:
            def Установить(self,value):
                password1 = self.browser.find_element(*RegisterLocators.PASSWORD1_FORMGROUP)
                BasePage.FormGroup(password1).set_value(value)

            def Проверить_справку(self, value):
                RegisterCheckFunctions.check_helpblock(self, RegisterLocators.HELPBLOCK_PASSWORD1, value)

        class Повторите_пароль:
            def Установить(self,value):
                password2 = self.browser.find_element(*RegisterLocators.PASSWORD2_FORMGROUP)
                BasePage.FormGroup(password2).set_value(value)
            def Проверить_справку(self, value):
                RegisterCheckFunctions.check_helpblock(self, RegisterLocators.HELPBLOCK_PASSWORD2, value)

        class У_меня_есть_промокод:
            def Установить(self, value):
                promocode = self.browser.find_element(*RegisterLocators.PROMOCODE_FORMGROUP)
                BasePage.FormGroup(promocode).set_value(value)
            def Проверить_справку(self, value):
                RegisterCheckFunctions.check_helpblock(self, RegisterLocators.HELPBLOCK_PROMOCODE, value)

        class Я_принимаю_условия:
            def Установить(self, value):

                check_box =  self.browser.find_element(*RegisterLocators.USER_AGREEMENT_FORMGROUP)
                current_value = BasePage.FormGroup(check_box).get_value()
                if current_value != eval(value):
                    BasePage.FormGroup(check_box).set_value(eval(value))
                    self.browser.implicitly_wait(10)
                    #Скролл для активизации кнопки "Принять условия" выполняется путем поиска последней строки соглашения
                    modal_window = True
                    while modal_window:
                        try:
                             self.browser.find_element_by_xpath("//button[contains(.,'Принять условия')]")
                             self.browser.find_element_by_xpath("//li[contains(.,'Если для Пользователя неприемлемы')]")
                             self.browser.find_element_by_xpath("//li[contains(.,'Если для Пользователя неприемлемы')]").click()
                             self.browser.find_element_by_xpath("//button[contains(.,'Принять условия')]").click()
                             time.sleep(1)
                             modal_window = False
                             self.browser.implicitly_wait(0)
                        except:
                            pass
            def Проверить_справку(self, value):
                RegisterCheckFunctions.check_helpblock(self, RegisterLocators.HELPBLOCK_USER_AGREEMENT, value)

        class Хочу_получить_предзаполненный_профиль:
            def Установить(self,value):
                check_box = self.browser.find_element(*RegisterLocators.NEED_COPY_DATA_FORMGROUP)
                current_value = BasePage.FormGroup(check_box).get_value()
                if current_value != eval(value):
                    BasePage.FormGroup(check_box).set_value(eval(value))


    class CheckData():
        def import_data(self):
            elements = []
            ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
            with open(os.path.join(ROOT_DIR, 'register_data.json'), encoding="utf-8") as f:
                pars = json.load(f)
                for lines in pars["check_data"]:
                    dict_data = defaultdict(dict)
                    dict_data["prepare"]["org_type"] = lines["prepare"]["org_type"]
                    dict_data["prepare"]["full_name"] = lines["prepare"]["full_name"]
                    dict_data["prepare"]["email"] = lines["prepare"]["email"].replace("_data_", datetime.now().strftime("%d%m%Y%H%M%S"))
                    dict_data["prepare"]["username"] = lines["prepare"]["username"].replace("_data_", datetime.now().strftime("%d%m%Y%H%M%S"))
                    dict_data["prepare"]["phone"] = lines["prepare"]["phone"]
                    dict_data["prepare"]["inn"] = lines["prepare"]["inn"]

                    dict_data["prepare"]["region"] = lines["prepare"]["region"]
                    dict_data["prepare"]["activity"] = lines["prepare"]["activity"]

                    dict_data["prepare"]["password1"] = lines["prepare"]["password1"]
                    dict_data["prepare"]["password2"] = lines["prepare"]["password2"]
                    dict_data["prepare"]["promocode"] = lines["prepare"]["promocode"]
                    dict_data["prepare"]["copy_data"] = lines["prepare"]["copy_data"]

                    elements.append(dict_data)
                return elements
        def registration(self,dictionary):
            RegisterCheckFunctions.FirstStep.set_org_type(self,dictionary["prepare"]["org_type"])
            RegisterCheckFunctions.FirstStep.set_fullname(self,dictionary["prepare"]["full_name"])
            RegisterCheckFunctions.FirstStep.set_email(self,dictionary["prepare"]["email"])
            # RegisterCheckFunctions.FirstStep.set_username(self, dictionary["prepare"]["username"])
            RegisterCheckFunctions.FirstStep.set_phone(self, dictionary["prepare"]["phone"])
            RegisterCheckFunctions.FirstStep.set_inn(self, dictionary["prepare"]["inn"])
            RegisterCheckFunctions.FirstStep.go_to_next_step(self)
            RegisterCheckFunctions.SecondStep.set_region(self, dictionary["prepare"]["region"])
            RegisterCheckFunctions.SecondStep.set_activity(self, dictionary["prepare"]["activity"])
            RegisterCheckFunctions.SecondStep.go_to_next_step(self)
            RegisterCheckFunctions.ThirdStep.set_password1(self, dictionary["prepare"]["password1"])
            RegisterCheckFunctions.ThirdStep.set_password2(self, dictionary["prepare"]["password2"])
            RegisterCheckFunctions.ThirdStep.set_promocode(self, dictionary["prepare"]["promocode"])
            RegisterCheckFunctions.ThirdStep.set_copy_data(self, dictionary["prepare"]["copy_data"])
            RegisterCheckFunctions.ThirdStep.set_agreement(self,"True")

            RegisterCheckFunctions.ThirdStep.go_to_next_step(self)
            try:
                while True:
                    self.browser.find_element_by_xpath("//h5[contains(.,'Мы настраиваем Ваш профиль')]")
                    self.browser.find_element_by_xpath("//p[contains(.,'Осталось совсем чуть-чуть')]")
            except:
                pass