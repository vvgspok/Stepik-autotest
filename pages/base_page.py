import time
from collections import defaultdict

import os
import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait

from pages.base_locators import BaseLocators
from .main_functions import проверка_ссылки
from .main_settings import MAIN_URL


class BasePage():
    header = None
    body = None

    def __init__(self, browser, url):
        self.browser = browser
        self.url = url.strip()
        проверка_ссылки(MAIN_URL + self.url)
        self.open_url()
        self.ожидание_прогрузки_страницы()
        self.проверка_на_ошибку_на_странице()

    def attach_screenshot(self, step, name):
        # добавить скриншот к отчёту
        with allure.step(step):
            allure.attach(MAIN_URL + self.url,
                          name=name)
            allure.attach(self.browser.get_screenshot_as_png(),
                          name='screenshot_' + step + '_' + name,
                          attachment_type=AttachmentType.PNG)

    def open_url(self):
        """
        открывает ссылку внутри (авторизированному пользователю)
        :return:
        """
        self.browser: WebDriver
        self.browser.find_element()
        url = MAIN_URL + self.url
        self.browser.get(url)
        self.ожидание_прогрузки_страницы()

    def is_element_present(self, how, what, timeout=5, search_area=None):
        if search_area is None:
            search_area = self.browser
        try:
            WebDriverWait(search_area, timeout).until(EC.presence_of_element_located((how, what)))
            # self.browser.find_element(how, what)
        except:
            try:
                time.sleep(1)
                search_area.find_element(how, what)
            except:
                return False

        return True

    def is_elementS_present(self, how, what, timeout=5):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_all_elements_located((how, what)))
            # self.browser.find_element(how, what)
        except:
            return False
        return True

    def ожидание_прогрузки_страницы(self):
        loadind = True
        try:
            while loadind:
                self.browser.find_element(By.CSS_SELECTOR, ".loading")
                time.sleep(0.5)
        except:
            pass

    def file_upload(self, name_file, delete=False):
        """
        Загрузка файла
        в "name_fail"-передать наименование файла

        Пример вызова функции:
            name_file = 'worker.xlsx' - Передаем наименование файла
            BasePage.file_upload(self, name_file) - Вызов функции
        """
        self.browser.find_element_by_xpath("//*[@class='btn btn-sm btn-default']").click()

        # Ставится чекбокс = "Удалить предыдущие данные перед импортом"
        if delete == True:
            WebDriverWait(self.browser, 5).until(
                EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Удалить предыдущие данные перед импортом')]"))
            ).click()

        current_dir = os.path.abspath(os.path.dirname(__file__))
        file_path = os.path.join(current_dir, name_file)
        element = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.ID, "id_upload_file")))
        element.send_keys(file_path)

        try:
            WebDriverWait(self.browser, 10).until(
                EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Загружен файл')]")))
        except Exception as e:
            assert False, "Файл не загружается;" + e
        self.browser.find_element_by_xpath("//*[@class='modal-content']//*[@class='btn btn-sm btn-success']").click()

        WebDriverWait(self.browser, 30).until(
            EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Операция успешно завершена.')]")))

        button_close = WebDriverWait(self.browser, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@class='btn btn-sm btn-success btn-close']"))
        )
        button_close.click()
        return

    def проверка_url_в_адресной_строке(self, url):
        self.ожидание_прогрузки_страницы()
        current_url = self.browser.current_url
        assert url == current_url, \
            f"""Не та страница
            ♦ Ожидалось: {url}
            ♦ Открылось: {current_url}"""

    def проверка_обновления(self):
        update = True
        while update:
            try:
                self.browser.find_element_by_xpath("//p[contains(.,'Сервис в процессе обновления')]")
                time.sleep(3)
            except:
                update = False

    def check_elements_on_form(self, elements_waiting, elements_reality):
        """
        input:
        elements_waiting - ожидаемые элементы на форме
        elements_reality - элементы на форме после парсинга
        ___________
        входной состав списком (порядок важен)
        пример:
        [
            {
            "form_name": {name: "Добавление приглашения"
            },

            {
            "Имя, Отчество получателя": {
                "required": False,
                "value": "",
                "type": "input",
                }
            },
            {
            "Отправить мне копию письма": {
                "required": True,
                "value": "True",
                "type": "checkbox",
                }
            },
            {
            "Тариф": {
                "required": True,
                "value": "ПДн.Минимум",
                "type": "select2",
                }
            },
        ]
        """
        # Первоначальная проверка на кол-во данных (элементов)
        if len(elements_waiting) != len(elements_reality):
            assert False, f"Кол-во ожидаемых {len(elements_waiting)}, а реальных {len(elements_reality)}"

        # тут проверка
        check = True
        if check:
            return True
        else:
            assert False, "Ожидаемые элементы не соответствуют реальности"

    def проверка_на_ошибку_на_странице(self):
        self.browser: WebDriver
        a = self.browser.get_cookies()
        pass

    def ждать_пока_элемент_отсутсвует(self, how, what, timeout=10):
        '''
        Ожидание, пока элемент отсутствует
        :param how: Метод поиска элемента (BY.XPATH, BY.CSS_SELECTOR и.т.д
        :param what: Локатор, в соответствии с выбранным методом
        :param timeout: Максимальное время ожидания. По умолчанию - 10 секунд
        :return: Не возвращает ничего
        '''
        BasePage.wait_while_element_presented(self, how, what, timeout)

    def wait_while_element_presented(self, how, what, timeout=10):
        '''
        Ожидание, пока элемент отсутствует
        :param how: Метод поиска элемента (BY.XPATH, BY.CSS_SELECTOR и.т.д
        :param what: Локатор, в соответствии с выбранным методом
        :param timeout: Максимальное время ожидания. По умолчанию - 10 секунд
        :return: Не возвращает ничего
        '''
        wait = True
        t_end = time.time() + timeout
        while wait and t_end > time.time():
            try:
                self.browser.find_element(how, what)
                wait = False
            except:
                time.sleep(0.5)
        assert wait == False, "Элемент '" + how + "'-'" + what + "' не появился  в течении заданного таймаута" + str(
            timeout) + " секунд"

    def wait_while_elementS_presented(self, how, what, timeout=10):
        '''
        Ожидание, пока элемент отсутствует
        :param how: Метод поиска элемента (BY.XPATH, BY.CSS_SELECTOR и.т.д
        :param what: Локатор, в соответствии с выбранным методом
        :param timeout: Максимальное время ожидания. По умолчанию - 10 секунд
        :return: Не возвращает ничего
        '''
        wait = True
        t_end = time.time() + timeout
        while wait and t_end > time.time():
            try:
                self.browser.find_element(how, what)
                wait = False
            except:
                time.sleep(0.5)
        assert wait == False, "Элемент '" + how + "'-'" + what + "' не появился  в течении заданного таймаута" + str(
            timeout) + " секунд"

    def ждать_пока_элемент_присутствует(self, how, what, timeout=10):
        '''
        Ожидание, пока элемент присутсвует на странице

                :param how: Метод поиска элемента (BY.XPATH, BY.CSS_SELECTOR и.т.д

                :param what: Локатор, в соответствии с выбранным методом

                :return: Не возвращает ничего
        '''
        BasePage.wait_while_element_disappear(self, how, what, timeout)

    def wait_while_element_disappear(self, how, what, timeout=10):
        '''
        Ожидание, пока элемент присутсвует на странице
        :param how: Метод поиска элемента (BY.XPATH, BY.CSS_SELECTOR и.т.д
        :param what: Локатор, в соответствии с выбранным методом
        :param timeout: Максимальное время ожидания. По умолчанию - 10 секунд
        :return: Не возвращает ничего
        '''
        wait = True
        t_end = time.time() + timeout
        while wait and t_end > time.time():
            try:
                self.browser.find_element(how, what)
                time.sleep(0.5)
            except:
                wait = False
        assert wait == False, "Элемент '" + how + "'-'" + what + "' не пропал в течении заданного таймаута" + str(
            timeout) + " секунд"

    # endregion
    # region Базовые, простые элементы
    class BaseElement:
        value = ""
        name = ""
        element = ""
        element_class = ""

        def set_value(self, value):
            pass

        def get_value(self):
            return self.value

        def clean_value(self):
            pass

    class FormControl(BaseElement):
        def __init__(self, formcontrol):
            """
            Базовый класс для элемента типа FornContril

            :param formcontrol: WebElement класса formgroup

            """

            self.element_class = "form-control"
            self.element = formcontrol
            try:
                self.value = self.element.find_element_by_css_selector("input:nth-child(1)").get_attribute("value")
            except:
                try:
                    self.value = self.element.find_element_by_css_selector(".form-control").text
                except:
                    pass

        def set_value(self, new_value):
            try:
                self.element.find_element_by_css_selector("input").clear()
            except:
                pass
            self.element.find_element_by_css_selector("input").send_keys(new_value)
            self.element.find_element_by_css_selector("input").click()
            try:
                self.value = self.element.find_element_by_css_selector("input:nth-child(1)").get_attribute("value")
            except:
                pass

        def get_value(self):
            return self.value

    class CheckBox(BaseElement):
        def __init__(self, checkbox):
            """
           Базовый класс для элемента типа checkbox

           :param checkbox: WebElement типа formgroup

           """
            self.element_class = "checkbox"
            self.element = checkbox
            self.name = checkbox.find_element_by_css_selector("label span:nth-child(2)").text
            self.value = checkbox.find_element_by_css_selector("input").get_property("checked")

        def set_value(self, new_value):
            if self.value != new_value:
                self.element.find_element_by_css_selector("input").click()
            self.value = self.element.find_element_by_css_selector("input").get_property("checked")

    class RaddioButton(BaseElement):

        # //*[@class='commission form-group']//*[contains(@class,'radio')] - если на форме
        # //*[contains(@class,'form-horizontal')]/*[contains(@class,'form-group')]/div/*[contains(@class,'radio')]//ancestor::*[contains(@class,'panel-body')]/parent::*//*[contains(@class,'panel-title')]//*[contains(@class,'help-link')]
        # - если чисто на панели. Локатор для имени панели от группы

        def __init__(self, raddio):
            """
            Базовый класс для элемента типа raddiobutton

            :param raddio: WebElement типа formgroup

            """
            self.element_class = "radio"
            self.element = raddio
            radios = self.element.find_elements_by_css_selector(".radio")
            try:
                self.value = self.element.find_element_by_xpath(
                    "//*[contains(@class,'radio')]//input[@checked]/following-sibling::span").text
            except:
                self.value = ""
            # Если есть
            try:
                self.name = raddio.find_element_by_xpath("//*[contains(@class,'control-label-required')]").text
            except:
                self.name = "panel-name"

        def set_value(self, new_value):
            if self.value != new_value:
                try:
                   self.element.find_element_by_xpath("//*[contains(@class,'radio')]//input/following-sibling::span[contains(.,'"+new_value+"')]").click()
                except:
                    pass
            try:
                self.value = self.element.find_element_by_xpath(
                    "//*[contains(@class,'radio')]//input[@checked]/following-sibling::span").text
            except:
                pass

    class Select2Chooice(BaseElement):
        def __init__(self, select2chooices):
            """
           Базовый класс для элемента типа select2chooices

           :param select2chooices: WebElement типа formgroup

           """
            self.element_class = "select2-chooice"
            self.element = select2chooices
            array = self.element.find_elements_by_css_selector(".select2-search-choice div")
            self.value = []
            for element in array:
                self.value.append(element.text)

        def set_value(self, new_value):
            try:
                self.element.find_element_by_css_selector(".select2-choices .select2-search-field").click()
                self.element.find_element_by_css_selector(
                    ".select2-choices .select2-search-field .select2-input").send_keys(new_value)
                BasePage.Select2Chooice.wait_searching(self)
                try:
                    self.element.find_element_by_xpath(
                        "//span[contains(.,'" + new_value + "') and @class='select2-match']/parent::*").click()
                except:
                    # Если не нашли значение - очищаем поле ввода по Esc. Возможно костыль?
                    self.element.find_element_by_css_selector(
                        ".select2-choices .select2-search-field .select2-input").send_keys(Keys.ESCAPE)

                array = self.element.find_elements_by_css_selector(".select2-search-choice div")
                self.value = []
                for element in array:
                    self.value.append(element.text)
            except:
                pass

        def clean_value(self):
            values = self.element.find_elements_by_css_selector(".select2-choices .select2-search-choice-close")
            for _value in values:
                _value.click()

        def wait_searching(self):
            """
            Ожидание завершения поиска значения в выпадающем списке
            :return:
            """
            searching = True
            while searching:
                try:
                    WebDriverWait(self.element, 1).until(EC.presence_of_element_located(
                        (By.CSS_SELECTOR, ".select2-choices .select2-search-field .select2-input select2-active")))
                except:
                    searching = False

    class Select2Choosen(BaseElement):
        def __init__(self, select2choosen):
            """
            Базовый класс для элемента типа select2choosen

            :param select2choosen: WebElement типа formgroup

            """
            self.element_class = "select2-choosen"
            self.element = select2choosen
            self.value = self.element.find_element_by_css_selector(".select2-chosen").text

        def set_value(self, new_value):
            self.element.find_element_by_css_selector(".select2-chosen").click()
            try:
                self.element.find_element_by_xpath("//ancestor::body//*[@id='select2-drop']//input").send_keys(
                    new_value)
            except:
                pass
            # В случа
            try:
                self.element.find_element_by_xpath(
                    "//ancestor::body//*[@class = 'select2-result-label' and contains(.,'" + new_value + "')]").click()
            except:
                pass
            BasePage.Select2Choosen.wait_searching(self)
            try:
                self.element.find_element_by_xpath(
                    "//ancestor::body//*[@id='select2-drop']//*[@class='select2-result-label']").click()
            except:
                self.element.find_element_by_xpath("//ancestor::body//*[@id='select2-drop']//input").send_keys(
                    Keys.ESCAPE)
            self.value = self.element.find_element_by_css_selector(".select2-chosen").text

        def wait_searching(self):
            searching = True
            while searching:
                try:
                    WebDriverWait(self.element, 1).until(EC.presence_of_element_located(
                        (By.XPATH, "//ancestor::body//*[@id='select2-drop']//input[contains(@class,'select2-active']")))
                except:
                    searching = False

    class Select(BaseElement):
        def __init__(self, select):
            """
             Базовый класс для элемента типа select

             :param select: WebElement типа formgroup

             """
            self.element_class = "select"
            self.element = select
            try:
                self.value = Select(self.element.find_element_by_css_selector(
                    "select:not([style='display: none;'])")).first_selected_option.text
            except:
                pass

        def set_value(self, value):
            Select(self.element.find_element_by_css_selector(
                "select:not([style='display: none;'])")).select_by_visible_text(value)
            self.value = Select(self.element.find_element_by_css_selector(
                "select:not([style='display: none;'])")).first_selected_option.text

    class Row(BaseElement):
        def __init__(self, row):
            """
            Базовый класс для элемента типа row

            :param row: WebElement типа formgroup

            """
            self.element_class = "row"
            self.element = row
            self.value = defaultdict(dict)
            childs = self.element.find_elements_by_css_selector(".input-group")
            for child in childs:
                data_name = child.find_element_by_css_selector("span").text
                try:
                    value = child.find_element_by_css_selector("input").get_property("value")
                except:
                    value = ""
                self.value[data_name] = value

        def set_value(self, values):
            self.value = defaultdict(dict)
            childs = self.element.find_elements_by_css_selector(".input-group")
            for child, value in zip(childs, values):
                try:
                    child.find_element_by_css_selector("input").clear()
                except:
                    pass
                child.find_element_by_css_selector("input").send_keys(value)
            childs = self.element.find_elements_by_css_selector(".input-group")
            for child in childs:
                data_name = child.find_element_by_css_selector("span").text
                try:
                    value = child.find_element_by_css_selector("input").get_property("value")
                except:
                    value = ""
                self.value[data_name] = value

    class Button(BaseElement):
        def __init__(self, button):
            """
           Базовый класс для элемента типа button

           :param button: WebElement типа formgroup

           """
            self.element_class = "button"
            self.element = button
            try:
                self.name = self.element.find_element_by_css_selector("span")
                self.name = self.name.text.strip()
            except:
                try:
                    self.name = self.element.text
                except:
                    pass

    class DeclensionWidget(BaseElement):
        def __init__(self, widget):
            self.element = widget
            self.element_class = "declensionwidget"

    # endregion
    # region Сложные, составные элементы
    class FormGroup(BaseElement):
        obj = None
        helpblock = ""
        required = ""

        def __init__(self, formGroup):
            """
            Базовый класс для элемента типа formGroup
            По результатам выполнения инициирует объект, соответствующий найденому элементу: ChecBox, RaddioButton и.т.д

            :param formGroup: WebElement типа formgroup

              """
            self.element = formGroup
            element = defaultdict(dict)
            # region Парсинг элементов
            try:
                formGroup.find_element_by_css_selector(".form-control")
                # value = formGroup.find_element_by_css_selector("input:nth-child(1)").get_attribute("value")
                obj = BasePage.FormControl(formGroup)
            except:
                pass
                # region TextArea
                # Многострочный ввод
            try:
                formGroup.find_element_by_css_selector("textarea")
                obj = BasePage.FormControl(formGroup)
            except:
                pass
                # endregion
                # region CheckBox
            try:

                checkboxes = formGroup.find_elements_by_css_selector(".checkbox")
                if (len(checkboxes) > 1):
                    obj = []
                    for checkbox in checkboxes:
                        obj.append(BasePage.CheckBox(checkbox))
                if (len(checkboxes) == 1):
                    obj = BasePage.CheckBox(checkboxes[0])
            except:
                pass
                # endregion
                # region RaddioButtons
                # Радио???
            try:
                formGroup.find_element_by_css_selector(".radio")
                obj = BasePage.RaddioButton(formGroup)
            except:
                pass
                # endregion
                # region Select2Choosen
            try:
                formGroup.find_element_by_css_selector(".select2-chosen")
                obj = BasePage.Select2Choosen(formGroup)
            except:
                pass
                # endregion
                # region Select2Chooices
            try:
                formGroup.find_element_by_css_selector(".select2-choices")
                obj = BasePage.Select2Chooice(formGroup)
            except:
                pass
            try:
                formGroup.find_element_by_css_selector(".select2-choice")
                try:
                    prop = formGroup.find_element_by_css_selector(".select2-choice").get_attribute("tabindex")
                except:
                    prop = formGroup.find_element_by_css_selector(".select2-choice").get_property("tabindex")

                if int(prop) > -1:
                    obj = BasePage.Select2Chooice(formGroup)
            except:
                pass
                # endregion
                # region Select
                # Простой селект. hidden-select валится в except - спец обработка не нужна
            try:
                formGroup.find_element_by_css_selector("select:not([style='display: none;'])")
                obj = BasePage.Select(formGroup)
            except:
                pass
                # endregion
                # region Row
                # группа "Индекс и Адрес", пока что
            try:
                row = formGroup.find_element_by_css_selector(".row")
                obj = BasePage.Row(row)
            except:
                pass
            # endregion
            self.value = obj.value
            self.element_class = obj.element_class
            self.obj = obj
            self.required = self.check_required()

        def get_form_group_by_name(self, name, root=None):
            """
            Поиск formgroup на странице по имени

            :param name: Вхождение имени, по которому организовывается поиск

            :param root: "Корень", источник поиска. Если не указан - то self.browser

            :return: Объект ForGroup
            """
            if root == None:
                root = self.browser
            try:
                formGroups = root.find_elements_by_xpath(
                    "//span[contains(.,'" + name + "')]/ancestor::*[contains(@class,'form-group')]")
                formGroup = root.find_element_by_xpath(
                    "//span[contains(.,'" + name + "')]/ancestor::*[contains(@class,'form-group')]")
                # Костыль
                if len(formGroups) > 1:
                    formGroup = formGroups[len(formGroups) - 1]
            except:
                pass
            try:
                # Попытка поиска RaddioButton без наименования
                formGroup = root.find_element_by_xpath(
                    "//*[contains(@class,'help-link') and contains(.,'" + name + "')]/ancestor::*[contains(@class,'panel panel-theme')]" +
                    "//*[contains(@class,'form-horizontal')]/*[contains(@class,'form-group')]/div/*[contains(@class,'radio')]/ancestor::*[contains(@class,'form-group')]")
            except:
                pass
            obj = BasePage.FormGroup(formGroup)
            return obj

        def get_value(self):
            return self.value

        def get_name(self, formGroup):
            try:
                formGroup_name = formGroup.find_element_by_css_selector(".control-label label span:nth-child(1)").text
                # Текстовое поле
            except:
                formGroup_name = "None"
            return formGroup_name

        def set_value(self, value):
            self.obj.set_value(value)

        def clean_value(self):
            self.obj.clean_value()

        def get_helpblock(self):
            try:
                self.helpblock = self.element.find_element_by_xpath("//*[contains(@class,'help-block')]").text
            except:
                pass
            return self.helpblock

        def check_required(self):
            """
            Проверка оьязательности параметра
            :return:
            """
            try:
                self.element.find_element_by_xpath("//*[contains(@class,'control-label-required')]")
                self.required = "True"
            except:
                self.required = "False"

    class Panel(BaseElement):
        element = None
        header = None
        body = None
        name = ""

        def __init__(self, panel):
            """
            Конструктор класса описывающий элемент типа Panel

            :param panel: WebElement класса panel
            """
            self.element = panel
            self.header = self.element.find_element_by_css_selector(".panel-heading")
            self.body = self.element.find_element_by_css_selector(".panel-body")
            self.name = self.element.find_element_by_css_selector(".panel-heading .panel-title").text

        def сommand(self, name):
            """
            Выполнение команды панели, наименование которой соответствует заданному вхождению

            :param name: Вхождение наименования искомой команды

            :return:
            """
            command = "//*[contains(@class,'btn') and contains(.,'" + name + "') and not(@aria-hidden='true')]"
            action = self.element.find_element_by_xpath(command)
            action.click()

        def get_panel_by_name(self, name):
            """
            Поиск и иинициализация объекта класса Panel по наименования вхождению наименования панели

            :param name: Вхождение наименования искомой панели

            :return: объект типа Panel
            """

            panel = self.browser.find_element_by_xpath(
                "//*[*/@class='panel-title' and contains(.,'" + name + "')]/following-sibling::*[@class='panel-body']/parent::*")
            return BasePage.Panel(panel)
        def search_parametr(self,parametr):
            try:
                element = BasePage.FormGroup.get_form_group_by_name(self, parametr, self.body)
            except:
                assert False, "Панель не содержит параметр '" + parametr + "'"
            return element

    class Table(BaseElement):
        search_element = None
        headers_list = []
        rowspans = []
        undertable = None
        data_element = None
        search_control = None

        def __init__(self, table):
            """
            Конструктор класса, описывающий таблицу

            :param table: WebElement класса table

            """
            self.element = table
            self.value = None
            try:
                self.data_element = self.element.find_element_by_css_selector(".ksb-table-wrapper div table")
            except:
                self.data_element = self.element.find_element_by_css_selector(".table")

            # self.undertable = self.element.find_element_by_css_selector(".ksb-table-container .undertable.table-buttons")
            try:
                self.search_element = self.element.find_element_by_css_selector(".search-control")
            except:
                pass
            BasePage.Table.get_header(self)

        def get_value(self):
            """
            Парсинг таблицы по элементу WebElement переданного в self.element

            :return: Распарсенная таблица в формате словаря "ШАПКА КОЛОНКИ : ЗНАЧЕНИЕ" для каждой строки
            """
            self.value = BasePage.Table.__get_table_data_by_element(self)
            return self.value


        def get_header(self):
            """
            Получение шапки таблицы

            :return: Шапка таблицы в формате массива
            """
            self.headers_list = []
            self.rowspans = []

            headers = self.element.find_elements_by_css_selector(".tableFloatingHeaderOriginal th")
            # Для модальных окон
            if len(headers) == 0:
                headers = self.data_element.find_elements_by_css_selector("th")
            for header in headers:
                if (header.text == ''):
                    data = header.get_attribute("data-name")
                else:
                    data = header.text
                self.headers_list.append(data.strip())
                self.rowspans.append(0)

        def show_all(self):
            """
            Отображение всех элементов таблицы (или 1000, если записей больше 1000)

            :return:
            """
            try:
                self.element.find_element_by_css_selector(".page-control").click()
                time.sleep(2)
                self.element.find_element_by_css_selector("[data-page-size='1000']").click()
                time.sleep(1)
                BasePage.ожидание_прогрузки_страницы(self)
            except:
                pass

        def get_table_by_name(self, name="", root=None):
            """
            Поиск таблицы по наименованию панели, в рамках которой она расположена

            :param name: Наименование искомой панели. Если не указан - возвращает любую первую найденную
            :param root: Место поиска таблицы (например модальное окно). Если не указан - ищет на всей странице
            :return: объект класса Table
            """
            if root == None:
                root = self.browser
            if name != "":
                try:
                    try:
                        table = root.find_element_by_xpath("//*[*/@class='panel-title' and contains(.,'"+name+"')]/following-sibling::*[@class='panel-body']//*[contains(@class,'ksb-table-container')]")
                    except:
                        # Если таблица в разделе
                        try:
                            table = root.find_element_by_xpath("//*[*/@class='panel-title']//a[contains(.,'"+name+"')]//ancestor::*[contains(@class,'panel-title')]/parent::*//*[contains(@class,'tab-pane active')]//*[contains(@class,'ksb-table-container')]")
                        except:
                            # Если таблица в модальном окне
                            table = root.find_element_by_xpath("//*[*/@class='modal-title' and contains(.,'"+name+"')]//ancestor::*[contains(@class,'modal-content')]//*[contains(@class,'ksb-table-container')]")
                except:
                    assert False, "Не удалось найти таблицу '" + name + "'"
            else:
                try:
                    elements =  root.find_elements_by_xpath("//*[contains(@class,'ksb-table-container')]")
                    table = elements[len(elements)-1]
                except:
                    assert False, "Не удалось найти таблицу"
            return BasePage.Table(table)



        def __get_table_cell_data(self, value):
            """
            Парсинг значения ячейкт таблицы

            :param value: объект WebElement соответствующий ячейке таблицы

            :return: Значение ячейки таблицы
            """
            data = None
            try:
                data = value.text
            except:
                pass
                # Частный случай обработки, когда контент - галочка или крестик
            try:
                if value.find_element_by_css_selector(".text-danger"):
                    data = "False"
            except:
                pass
            try:
                if value.find_element_by_css_selector(".text-success"):
                    data = "True"
            except:
                pass

                # Частный случай обработки, когда контент - чекбокс

            try:
                checkbox = value.find_element_by_css_selector(".checkbox")
                element = BasePage.CheckBox(checkbox)
                data = element.value
            except:
                pass
                # Частный случай обработки, когда контент - список элементов
            try:
                stack = value.find_elements_by_css_selector(".list-unstyled li")
                new_data = []
                if len(stack) > 0:
                    # Развернуть список элементов, если можно развернуть
                    try:
                        expand_elem = value.find_element_by_css_selector(".cell-expand-text")
                        if expand_elem.text == 'развернуть':
                            expand_elem.click()
                            expand = True
                            while expand:
                                try:
                                    value.find_element_by_css_selector(".cell-expand-text.disabled")
                                    expand = False
                                except:
                                    pass
                            expand = True
                            while expand:
                                try:
                                    value.find_element_by_css_selector(".cell-expand-text.disabled")
                                except:
                                    expand = False
                    except:
                        pass
                    for stack_element in stack:
                        new_data.append(stack_element.text)
                    data = new_data
            except:
                pass
            return data

        def command(self, command):
            """
            Выполнение команды таблицы по вхождению ее наименования

            :param command: Вхождение наименования команды таблицы

            :return:
            """

            self.element.find_element_by_xpath(
                "//*[contains(@class,'ksb-table-container')]//*[contains(@class,'undertable')]//*[contains(@class,'btn') and contains(.,'" + command + "')]").click()

        def __get_table_data_by_locator(self, how, what):
            """
            Парсинг значений таблицы по ее локатору.

            :param how: Способ поиска локатора

            :param what: Локатор таблицы

            :return: Распарсенная таблица в формате словаря "ШАПКА КОЛОНКИ : ЗНАЧЕНИЕ" для каждой строки
            """
            BasePage.is_element_present(self, how, what)
            element = self.browser.find_element(how, what)
            return BasePage.get_table_by_element(element)

        def __get_table_data_by_element(self):
            """
            Парсинг значений таблицы по элементу self.element

            :return: Распарсенная таблица в формате словаря "ШАПКА КОЛОНКИ : ЗНАЧЕНИЕ" для каждой строки
            """
            try:
                table_element = self.element
                full_table = defaultdict(dict)
                # region Отобразить 1000 элементов
                try:
                    table_element.find_element_by_css_selector(".page-control").click()
                    table_element.find_element_by_css_selector("[data-page-size='1000']").click()
                    BasePage.ожидание_прогрузки_страницы(self)
                    # TO DO Костыль для прогрузки записей? Подумать как допилить, чтобы без тайма ждал прогрузки всего и вся
                    time.sleep(2)
                except:
                    pass
                # endregion
                index = 0
                rows = self.data_element.find_elements_by_css_selector("tbody tr")
                for row in rows:
                    # При закрытии модального окна теряется контекст. Для этого переинцивлизация
                    try:
                        values = row.find_elements_by_css_selector("td")
                    except:
                        row = self.data_element.find_elements_by_css_selector("tbody tr")[index]
                        values = row.find_elements_by_css_selector("td")

                    value_index = 0

                    for self.header_index, self.rowspan in enumerate(self.rowspans):
                        if (self.rowspan > 1):
                            full_table[index][self.headers_list[self.header_index]] = full_table[index - 1][
                                self.headers_list[self.header_index]]
                            self.rowspans[self.header_index] = self.rowspans[self.header_index] - 1
                        else:
                            try:
                                value = values[value_index]

                                # По умолчанию принимается, что контент ячейки - текст
                                data = value.text
                                # Частный случай обработки, когда контент - галочка или крестик
                                try:
                                    if value.find_element_by_css_selector(".text-danger"):
                                        data = "False"
                                except:
                                    pass
                                try:
                                    if value.find_element_by_css_selector(".text-success"):
                                        data = "True"
                                except:
                                    pass

                                    # Частный случай обработки, когда контент - чекбокс

                                try:
                                    checkbox = value.find_element_by_css_selector(".checkbox")
                                    element = BasePage.CheckBox(checkbox)
                                    data = element.value
                                except:
                                    pass
                                # Частный случай обработки, когда контент - список элементов
                                try:

                                    # Развернуть список элементов, если можно развернуть
                                    try:
                                        value.find_element_by_css_selector(".cell-expand-text").click()
                                        expand = True
                                        while expand:
                                            try:
                                                value.find_element_by_css_selector(".cell-expand-text.disabled")
                                                expand = False
                                            except:
                                                pass
                                        expand = True
                                        while expand:
                                            try:
                                                value.find_element_by_css_selector(".cell-expand-text.disabled")
                                            except:
                                                expand = False
                                    except:
                                        pass

                                    stack = value.find_elements_by_css_selector(".list-unstyled li")
                                    new_data = []
                                    if len(stack) > 0:
                                        for stack_element in stack:
                                            new_data.append(stack_element.text)
                                        data = new_data
                                except:
                                    pass

                                # Частный случай обработки, когда контент - кнока "Изменить" или "Ввод данных"
                                try:
                                    buttons_stack = value.find_elements_by_css_selector(".btn-stack-vertical .btn")
                                    if len(buttons_stack) > 0:
                                        buttons = defaultdict(dict)
                                        for button in buttons_stack:
                                            button_obj = BasePage.Button(button)
                                            if (button_obj.name.strip().find('Изменить') > -1
                                                    or button_obj.name.strip().find('Ввод данных') > -1
                                                    or button_obj.name.strip().find('Состав ПК') > -1):
                                                self.headers_list[self.header_index] = "Действие"
                                                buttons.update(
                                                    {button_obj.name: BasePage.get_data_from_window(self, button_obj)})
                                        data = buttons
                                    else:
                                        button = value.find_element_by_css_selector(".btn")
                                        button_obj = BasePage.Button(button)
                                        if (button_obj.name.find('Изменить') > -1
                                                or button_obj.name.find('Ввод данных') > -1
                                                or button_obj.name.find('Состав ПК') > -1):
                                            self.headers_list[self.header_index] = "Действие"
                                            data = BasePage.get_data_from_window(self, button_obj)
                                except:
                                    pass
                            except:
                                pass

                            full_table[index][self.headers_list[self.header_index]] = data
                            try:
                                self.rowspans[self.header_index] = int(value.get_attribute("rowspan"))
                            except:
                                pass
                            value_index = value_index + 1
                            try:
                                value.find_element_by_css_selector(".cell-expand-text").click()
                            except:
                                pass
                    index = index + 1
            except:
                pass
            return full_table

        def get_column_values(self, column_name):
            """
                      Парсинг значений таблицы по элементу self.element

                      :return: Распарсенная таблица в формате словаря "ШАПКА КОЛОНКИ : ЗНАЧЕНИЕ" для каждой строки
                      """
            try:
                table_element = self.element
                full_table = defaultdict(dict)
                # region Отобразить 1000 элементов
                try:
                    table_element.find_element_by_css_selector(".page-control").click()
                    BasePage.is_element_present(self, *(By.CSS_SELECTOR, "[data-page-size='1000']"))
                    table_element.find_element_by_css_selector("[data-page-size='1000']").click()
                    BasePage.ожидание_прогрузки_страницы(self)
                    # TO DO Костыль для прогрузки записей? Подумать как допилить, чтобы без тайма ждал прогрузки всего и вся
                    time.sleep(2)
                except:
                    pass
                # endregion
                index = 0
                rows = self.data_element.find_elements_by_css_selector("tbody tr")
                for row in rows:
                    # При закрытии модального окна теряется контекст. Для этого переинцивлизация
                    try:
                        values = row.find_elements_by_css_selector("td")
                    except:
                        row = self.data_element.find_elements_by_css_selector("tbody tr")[index]
                        values = row.find_elements_by_css_selector("td")

                    value_index = 0

                    for self.header_index, self.rowspan in enumerate(self.rowspans):
                        if column_name == self.headers_list[self.header_index]:
                            if (self.rowspan > 1):
                                full_table[index][self.headers_list[self.header_index]] = full_table[index - 1][
                                    self.headers_list[self.header_index]]
                                self.rowspans[self.header_index] = self.rowspans[self.header_index] - 1
                            else:
                                try:
                                    value = values[self.header_index]

                                    # По умолчанию принимается, что контент ячейки - текст
                                    data = value.text
                                    # Частный случай обработки, когда контент - галочка или крестик
                                    try:
                                        if value.find_element_by_css_selector(".text-danger"):
                                            data = "False"
                                    except:
                                        pass
                                    try:
                                        if value.find_element_by_css_selector(".text-success"):
                                            data = "True"
                                    except:
                                        pass

                                        # Частный случай обработки, когда контент - чекбокс

                                    try:
                                        checkbox = value.find_element_by_css_selector(".checkbox")
                                        element = BasePage.CheckBox(checkbox)
                                        data = element.value
                                    except:
                                        pass
                                    # Частный случай обработки, когда контент - список элементов
                                    try:

                                        # Развернуть список элементов, если можно развернуть
                                        try:
                                            value.find_element_by_css_selector(".cell-expand-text").click()
                                            expand = True
                                            while expand:
                                                try:
                                                    value.find_element_by_css_selector(".cell-expand-text.disabled")
                                                    expand = False
                                                except:
                                                    pass
                                            expand = True
                                            while expand:
                                                try:
                                                    value.find_element_by_css_selector(".cell-expand-text.disabled")
                                                except:
                                                    expand = False
                                        except:
                                            pass

                                        stack = value.find_elements_by_css_selector(".list-unstyled li")
                                        new_data = []
                                        if len(stack) > 0:
                                            for stack_element in stack:
                                                new_data.append(stack_element.text)
                                            data = new_data
                                    except:
                                        pass

                                    # Частный случай обработки, когда контент - кнока "Изменить" или "Ввод данных"
                                    try:
                                        buttons_stack = value.find_elements_by_css_selector(".btn-stack-vertical .btn")
                                        if len(buttons_stack) > 0:
                                            buttons = defaultdict(dict)
                                            for button in buttons_stack:
                                                button_obj = BasePage.Button(button)
                                                if (button_obj.name.strip().find('Изменить') > -1
                                                        or button_obj.name.strip().find('Ввод данных') > -1
                                                        or button_obj.name.strip().find('Состав ПК') > -1):
                                                    self.headers_list[self.header_index] = "Действие"
                                                    buttons.update(
                                                        {button_obj.name: BasePage.get_data_from_window(self, button_obj)})
                                            data = buttons
                                        else:
                                            button = value.find_element_by_css_selector(".btn")
                                            button_obj = BasePage.Button(button)
                                            if (button_obj.name.find('Изменить') > -1
                                                    or button_obj.name.find('Ввод данных') > -1
                                                    or button_obj.name.find('Состав ПК') > -1):
                                                self.headers_list[self.header_index] = "Действие"
                                                data = BasePage.get_data_from_window(self, button_obj)
                                    except:
                                        pass
                                except:
                                    pass

                                full_table[index][self.headers_list[self.header_index]] = data
                                try:
                                    self.rowspans[self.header_index] = int(value.get_attribute("rowspan"))
                                except:
                                    pass
                                value_index = value_index + 1
                    index = index + 1
            except:
                pass
            return full_table

        def search_str(self, str):
            """
            Поиск записи таблицы по вхождения заданной строки. Поиск средствами элемента "Поиск" таблицы
            :param str: Вхождение строки по которой необходимо выполнить поиск
            :return:
            """

            if self.search_element != None:
                input = self.search_element.find_element_by_css_selector("input")
                input.click()
                try:
                    input.clean()
                except:
                    pass

                try:
                    self.search_element.find_element_by_css_selector(".clear-all").click()
                except:
                    pass
                input.send_keys(str)
                input.send_keys(Keys.ENTER)
                time.sleep(1)
                search_in_progress = True
                try:
                    WebDriverWait(self.element, 1).until(EC.presence_of_element_located(
                        (By.CSS_SELECTOR, ".ksb-table-container.loading-spinner.loading")))
                    while search_in_progress:
                        try:
                            self.element.find_element_by_css_selector(".ksb-table-container.loading-spinner.loading")
                            time.sleep(1)
                        except:
                            search_in_progress = False
                except:
                    pass

        def search_record_by_value(self, how, what):
            """
            Поиск записи таблицы по значению в колонке
            :param how: Колонка таблицы, по которой необходимо выполнить поиск
            :param what: Значение, которое неоюходимо найти
            :return: Словарь значений, соответствующий найденной строке. Формат словаря "ШАПКА КОЛОНКИ : ЗНАЧЕНИЕ"
            """

            # region Шапка
            row_array = []
            # endregion
            # region Отобразить 1000 элементов
            # BasePage.Table.show_all(self)
            # endregion
            try:
                search_index = self.headers_list.index(how)
            except:
                assert False, "В таблице нет колонки '" + how + "'"

            tbodys = self.data_element.find_elements_by_css_selector("tbody")
            for tbody in tbodys:

                try:
                    rows = tbody.find_elements_by_css_selector("tr")
                    index = 0
                    for row in rows:
                        row_dict = defaultdict(dict)
                        # При закрытии модального окна теряется контекст. Для этого переинцивлизация
                        try:
                            value = row.find_elements_by_css_selector("td")[search_index]
                        except:
                            row = self.data_element.find_elements_by_css_selector("tbody tr")[index]
                            value = row.find_elements_by_css_selector("td")[search_index]
                        data = BasePage.Table.__get_table_cell_data(self,value)
                        if isinstance(data, list):
                            data_el = data[0]
                            data = data_el
                        if (data == what):
                            values = row.find_elements_by_css_selector("td")
                            cell_index = 0
                            for value in values:
                                data = BasePage.Table.__get_table_cell_data(self, value)
                                row_dict.update({self.headers_list[cell_index]: data})
                                cell_index = cell_index + 1
                            row_dict.update({"element": row})
                            row_dict.update({"row_index": index})
                            row_array.append(row_dict)
                        index = index + 1
                except:
                    pass

            if len(row_array) == 0:
                assert False, "Указанная запись таблицы со значением '"+ what + "' в колонке '"+ how + "' не найдена"
            if len(row_array) == 1:
                return row_array[0]
            if len(row_array) > 1:
                return row_array

        def delete_row(self, cell_dict):
            """
            Удаление строки таблицы (выполнение команды "Удалить")

            :param cell_dict: Словарь значений строки таблицы

            :return:
            """
            index = 0
            for cell in cell_dict:
                if cell.find("remove") > -1:
                    row = self.data_element.find_elements_by_css_selector("tbody tr")[cell_dict["row_index"]]
                    row.find_elements_by_css_selector("td")[index].find_element_by_css_selector("button").click()
                    continue
                else:
                    index = index + 1

        def select_row(self, row_dict):
            """
            Выделение строки таблицы

            :param row_dict: Словарь значений строки таблицы

            :return:
            """
            index = 0
            for cell in row_dict:
                if cell.find("select") > -1:
                    row = self.data_element.find_elements_by_css_selector("tbody tr")[row_dict["row_index"]]
                    row.find_elements_by_css_selector("td")[index].click()
                else:
                    index = index + 1

        def edit_row(self, row_dict):
            """
            Переход в режим редактирования строки таблицы (выполнение команд "Изменить" или "Ввод данных)

            :param row_dict: Словарь значений строки таблицы

            :return:
            """
            index = 0
            for cell in row_dict:
                if cell.find("edit") > -1 or cell.find("Действие") > -1:
                    row = self.data_element.find_elements_by_css_selector("tbody tr")[row_dict["row_index"]]
                    element = row.find_elements_by_css_selector("td")[index].find_element_by_css_selector("button")
                    element.click()
                else:
                    index = index + 1

        def row_command(self, row_dict, command):
            """
            Выполнение команды строки таблицы

            :param row_dict: Словарь значений строки таблицы

            :param command: Вхождение наименования команды строки таблицы

            :return: Клик по найденной команде
            """

            try:
                row_dict["element"].find_element_by_xpath("//button//*[contains(.,'" + command + "')]").click()
            except:
                try:
                    row_dict["element"].find_element_by_xpath("//span[contains(.,'"+command+"')]").click()
                except:
                    assert False, "Команда '"+command +  "' не найдена"
            '''
            elements = row_dict["element"].find_elements_by_xpath("//child::span[contains(.,'" + command + "')]")
            elements2 = row_dict["element"].find_elements_by_xpath("//span[contains(.,'" + command + "')]")
            if len(elements)==0:
                assert False, "Команда '" + command + "' не найдена"
            else:
                element = elements[len(elements) - 1]
                try:
                    element.click()
                except:
                    assert False, "Команда '" + command + "' не найдена"
            '''

    class ModalWindow():
        """
        Появляющаяся Форма с разделением на 3 составные части
        """
        header = None
        body = None
        footer = None
        name = None
        element = None

        def __init__(self, element):
            """
            Конструктор класса описывающий модальное окно
            :param element: WebElement класса .modal-content
            """
            # .modal-content
            self.element = element
            self.header = self.element.find_element_by_css_selector(".modal-header")
            self.name = self.getWindowName()
            self.body = self.element.find_element_by_css_selector(".modal-body")
            self.footer = self.element.find_element_by_css_selector(".modal-footer")

        def getWindowName(self):
            """
            :return: Получение имени модального окна
            """
            return self.header.find_element_by_css_selector(".modal-title").text

        def closeWindow(self):
            """
            Закрытие модального окна

            :return:
            """
            self.header.find_element_by_css_selector("button.close").click()
            BasePage.ModalWindow.wait_window_close(self)

        def searchByHeaderText(self, header_text):
            """
            Поиск модального окна по вхождению заданной строки и получение объекта класса ModalWindow
            :param header_text: Вхождение строки на основе которой необходимо выполнить поиск строк
            :return: Объект класса ModalWindow соответствующий модального окну
            """

            WebDriverWait(self.browser, 10).until(EC.presence_of_element_located(
                (By.XPATH, "//*[*/@class='modal-title' and contains(.,'"+header_text+"')]/parent::*")))
            window = self.browser.find_element_by_xpath("//*[*/@class='modal-title' and contains(.,'"+header_text+"')]/parent::*")
            time.sleep(0.5)
            return BasePage.ModalWindow(window)

        def сommand(self, name):
            """
            Выполнение команды модального окна по вхождению наименования команды
            :param name: Вхождение наименования строки
            :return:
            """
            # Добавить проверку ожидания - после клика команда "заблокирована", ждем
            try:
               xpath = "//*[contains(@class,'btn') and contains(.,'" + name + "') and not(@aria-hidden='true') and not(contains(@class,'disabled')) ]"
               WebDriverWait(self.footer, 3).until(EC.presence_of_element_located(
                   (By.XPATH, xpath)))
            except:
               xpath = "//*[contains(@class,'btn') and contains(.,'" + name + "')]"
               WebDriverWait(self.footer, 3).until(EC.presence_of_element_located(
                   (By.XPATH, xpath)))
            actions = self.footer.find_elements_by_xpath(xpath)
            if (len(actions)>0):
               for action in actions:
                   try:
                       action.click()
                   except:
                       pass
            loading = True
            while loading:
               try:
                   self.element.find_element_by_xpath("//parent::*[contains(@class,'modal-dialog loading')]")
                   time.sleep(1)
               except:
                   loading = False
        def wait_while_command_in_progress(self,name):
            '''
            Ожидание, пока команда выполняется. Индикация выполнения - кнопка команды disable
            :param name: Наименование команды
            :return: Ничего не вовзращает. Задерживает выполнение теста, пока кнопка команды не доступна
            '''
            try:
                xpath = "//*[contains(@class,'btn') and contains(.,'" + name + "') and not(@aria-hidden='true') and not(contains(@class,'disabled')) ]"
                WebDriverWait(self.footer, 15).until(EC.presence_of_element_located(
                    (By.XPATH, xpath)))
            except:
                xpath = "//*[contains(@class,'btn') and contains(.,'" + name + "')]"
                WebDriverWait(self.footer, 3).until(EC.presence_of_element_located(
                    (By.XPATH, xpath)))

        def set_parametr_by_name(self, parametr, value):
            """
            Установка значения параметра модального окна по его наименования
            :param parametr: Вхождение наименования параметра
            :param value: Устанавливаемое значение
            :return:
            """
            element = BasePage.FormGroup.get_form_group_by_name(self, parametr,self.body)
            element.set_value(value)

        def wait_window_close(self):
            """
            Ожидание закрытия модального окна
            :return:
            """
            display = True
            while display:
                try:
                    self.element.find_element_by_css_selector(".modal-body")
                    time.sleep(1)
                except:
                    display = False

        def search_text_in_window(self, text):
            """
            Поиск текста в окне
            :param text: Вхождение строки, которое необходимо найти
            :return: "" или полный текст найденной строки
            """
            try:
                search = self.body.find_element_by_xpath("//p//*[contains(.,'" + text + "')]").text
            except:
                search = None

        def search_parametr(self,parametr):
            try:
                formGroups = self.body.find_elements_by_xpath(
                    "//span[contains(.,'" + parametr + "')]/ancestor::*[contains(@class,'form-group')]")
                formGroup = self.body.find_element_by_xpath(
                    "//span[contains(.,'" + parametr + "')]/ancestor::*[contains(@class,'form-group')]")
                # Костыль
                if len(formGroups) > 1:
                    formGroup = formGroups[len(formGroups) - 1]
            except:
                try:
                    # Попытка поиска RaddioButton без наименования
                    formGroup = self.body.find_element_by_xpath(
                        "//*[contains(@class,'help-link') and contains(.,'" + parametr + "')]/ancestor::*[contains(@class,'panel panel-theme')]" +
                        "//*[contains(@class,'form-horizontal')]/*[contains(@class,'form-group')]/div/*[contains(@class,'radio')]/ancestor::*[contains(@class,'form-group')]")
                except:
                    assert False, "Модальное окно не содержит параметр '" + parametr + "'"
            return BasePage.FormGroup(formGroup)
        
        def upload_file(self, file_path: str):
            """Загрузка файла в модальном окне
            :param file_path: полный путь до загружаемого файла"""
            upload_btn = self.browser.find_element_by_css_selector("input[type=file]")
            upload_btn.send_keys(file_path)
            try:
                # time.sleep(10)
                # success_msg = self.browser.find_element_by_xpath("//*[contains(text(), 'Загружен файл')]")
                # ожидание работает, но на всякий случай оставил в комментарии костыль
                elem = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Загружен файл')]")))
            except Exception as e:
                assert False, "Файл не загружается;" + e

    class найти_элементы_на_странице:
        """
        ищет элементы в переданной области

        input: search_area - область поиска
        return: Ничего не возвращает обратно
        """

        def строка_поиска(self, search_area):
            a = search_area
            print(a)
            assert BasePage.is_element_present(*BaseLocators.search_control, search_area=search_area), \
                "Не найден элемент 'Поисковая строка'"

        def кнопка_фильтр(self, search_area):

            assert BasePage.is_element_present(*BaseLocators.filter_control, search_area=search_area), \
                "Не найден элемент кнопка 'Фильтр'"

        def кнопка_скрытие_столбцов(self, search_area, extra_how=None, extra_what=None):
            """
            extra - дополнительный параметр, по которуму можно найти: CSS, ID
            """
            # Проверка, что есть оба поля extra_how, extra_what (если хотя бы одно заполнено)
            if ((extra_how is None) and (extra_what is not None)) or \
                    ((extra_how is not None) and (extra_what is None)):
                assert False, f"Проверьте:\n" \
                              f"extra_how: {extra_how},\n" \
                              f"extra_what: {extra_what}"

            if (extra_how is None) and (extra_what is None):
                # Стандартный поиск
                assert BasePage.is_element_present(*BaseLocators.column_сontrol, search_area=search_area), \
                    "Не найден элемент кнопка 'Скрытие столбцов'"
                return

            try:
                #
                what = f"//*[contains(@class,'ksb-table-container')]" \
                       f"//*[contains(@class,'btn') and contains(.,'Столбцы') and contains(@{extra_how},'{extra_what}')]"
                assert BasePage.is_element_present(By.XPATH, what=what)
            except Exception as e:
                assert False, f"{e}"

        def таблица(self, search_area):
            assert BasePage.is_element_present(*BaseLocators.ksb_table_wrapper, search_area=search_area), \
                "Не найдена таблица среди элементов"

        def кнопка_под_таблицей(self, search_area, btn_text):
            search_area: WebDriver
            assert search_area.find_element_by_xpath(f"//*[contains(@class,'ksb-table-container')]" \
                                                     f"//*[contains(@class,'undertable')]" \
                                                     f"//*[contains(@class,'btn') and contains(.,'{btn_text}')]")

    class WizardTab:
        element = None  # li
        state = "Не заполнен"
        active = "False"
        name = ""

        def __init__(self, tab):
            """
            Конструктор класса раздела мастера заполнения данных (Ввод данных, Оценка угроз и.т.д)

            :param tab: WebElement класса [.nav.nav-tabs li]

            """

            self.element = tab
            try:
                el_class = self.element.get_attribute("class")
                if el_class.find("disabled") > -1:
                    self.state = "Заблокирован"
                if el_class.find("active") > -1:
                    self.active = "True"
            except:
                pass

            try:
                self.name = self.element.find_element_by_css_selector("a").text
            except:
                pass
            try:
                self.name = self.element.find_element_by_css_selector("a").find_element_by_css_selector("span").text
            except:
                pass

            try:
                self.element.find_element_by_css_selector(".text-success")
                self.state = "Заполнен"
            except:
                pass

        def Найти(self, name):
            """
            Поиск раздела на страинице по вхождению заданного наименования

            :param name: Вхождение наименования раздела по которому будет выполнен поиск

            :return: Объект класса WizardTab
            """
            xpath = "//*[contains(@class,'nav-tabs')]//a[contains(.,'"+name+"')]/parent::*"
            WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.XPATH, xpath)))

            tab = self.browser.find_element_by_xpath(xpath)
            return BasePage.WizardTab(tab)

        def Найти_все_разделы(self):
            wizard_tabs = self.browser.find_elements_by_xpath(
                "//*[contains(@class,'wizard-tabs')]//*[contains(@class,'nav-tabs')]//li")
            obj = []
            for tab in wizard_tabs:
                obj.append(BasePage.WizardTab(tab))
            return obj

        def Перейти(self):
            self.element.click()

        def Убедиться_что_раздел_доступен(self):
            assert self.state != "Заблокирован"

        def Убедиться_что_раздел_недоступен(self):
            assert self.state == "Заблокирован"

        def Убедиться_что_раздел_заполнен(self):
            assert self.state == "Заполнен"

        def Убедиться_что_раздел_незаполнен(self):
            assert self.state == "Не заполнен"

        def Убедиться_что_все_шаги_заполнены(self):
            pass

    class WizardStep:
        element = None  # li
        state = "Заполнен"
        active = "False"
        name = ""

        def __init__(self, step):
            """
            Конструктор класса шага мастера заполнения данных (Ввод данных, Оценка угроз и.т.д)

            :param step: WebElement класса li.wizard-step

            """
            self.element = step
            try:
                el_class = self.element.get_attribute("class")
                if el_class.find("disabled") > -1:
                    self.state = "Заблокирован"
                if el_class.find("has-errors") > -1:
                    self.state = "Не заполнен"

                if el_class.find("active") > -1:
                    self.active = "True"
            except:
                pass

            try:
                self.name = self.element.find_element_by_css_selector(".step-name").text
            except:
                pass

        def Найти(self, name):
            """
            Поиск шага на страинице по вхождению заданного наименования

            :param name: Вхождение наименования шага по которому будет выполнен поиск

                :return: Объект класса WizardStep
                """
            xpath = "//*[contains(@class,'wizard-steps')]//*[@class='step-name' and contains(.,'"+name+"')]/parent::*/parent::*"
            WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.XPATH, xpath)))
            step = self.browser.find_element_by_xpath(xpath)
            return BasePage.WizardStep(step)
        def Найти_все_шаги(self):
            wizard_steps = self.browser.find_elements_by_xpath("//*[contains(@class,'wizard-steps')]//li")
            obj = []
            for step in wizard_steps:
                obj.append(BasePage.WizardStep(step))
            return obj
        def Перейти(self):
            self.element.click()
        def Убедиться_что_шаг_доступен(self):
            assert self.state != "Заблокирован"
        def Убедиться_что_шаг_недоступен(self):
            assert self.state == "Заблокирован"
        def Убедиться_что_шаг_заполнен(self):
            assert self.state == "Заполнен"
        def Убедиться_что_шаг_незаполнен(self):
            assert self.state == "Не заполнен"

    # endregion
    # region Попытки реализовать универсальный парсер страницы

    def parse_page(self):
        page = defaultdict(dict)
        steps = [1]
        # steps = BasePage.get_all_steps(self)
        for step_name in steps:
            # При переходе на новые шаги ссылки на старые теряются. Необходимая мера

            # BasePage.is_element_present(self,By.XPATH,"//*[text()='"+step_name+"']",10)
            # Cкипаем недоступные шаги
            # if steps[step_name] == "Не доступен":
            #    continue
            # self.browser.find_element_by_xpath("//*[text()='"+step_name+"']").click()
            ## self.browser.find_element_by_xpath("//*[text()='Особенности обработки ПДн']").click()
            # BasePage.ожидание_прогрузки_страницы(self)
            panels = BasePage.get_main_panels(self)
            panels_array = []
            panel_parse = defaultdict(dict)
            for panel in panels:
                panel_body = panel.element.find_element_by_css_selector(".panel-body")
                panel_parse.update(BasePage.parse_panel(self,panel))
                # panel_parse = BasePage.parse_panel(self,panel)
                try:
                    child_panels = BasePage.get_child_panels(panel.element)
                    child_panels_parse = defaultdict(dict)
                    for child_panel in child_panels:
                        panel_parse[panel.name].update(BasePage.parse_panel(self,child_panel))
                except:
                    pass

            page.update({step_name : panel_parse})
        return page
    def get_main_panels(self):
        panels = []
        panels_array = self.browser.find_elements_by_css_selector(".wizard-content>.ajax-content :is(form .panel ,.panel):not(.panel-child):not([style='display: none'])")
        for panel in panels_array:
            panel_obj = BasePage.Panel(panel)
            panels.append(panel_obj)
        return panels
    def get_child_panels(panel):
        panels = []
        panels_array = panel.find_elements_by_css_selector(".panel-child:not([style='display: none']")
        for panel in panels_array:
            try:
                panel_obj = BasePage.Panel(panel)
                panels.append(panel_obj)
            except:
                pass
        return panels
    def parse_panel(self,panel):
        panel_parse = defaultdict(dict)
        # Вычленияем из панели все элементы кроме дочек
        panel_elements = panel.element.find_elements_by_css_selector(":not(.panel)")
        try:
            form_gorups = BasePage.get_form_groups(self, panel.element, panel.name)
            panel_parse[panel.name].update({"Данные": form_gorups})
        except:
            pass
        try:
            element = panel.element.find_element_by_css_selector(".ksb-table-container")
            table_obj = BasePage.Table(element)
            table_obj.name = panel.name
            table_obj.value = BasePage.get_table_data_by_element(self,table_obj.element)
            panel_parse[table_obj.name].update({"Таблица": defaultdict(dict)})
            # panel_parse[panel.name]["Таблица"].update({"Элемент": element})
            panel_parse[table_obj.name]["Таблица"].update({"Элемент": table_obj.element})
            # data = BasePage.get_table_data_by_element(self, panel_parse[panel.name]["Таблица"]["Элемент"])
            panel_parse[table_obj.name]["Таблица"].update({"Данные": table_obj.value})
            panel_parse[table_obj.name]["Таблица"].update({"Поиск": table_obj.search_element})
        except:
            pass
        return panel_parse
    def get_data_from_window(self, obj):
        current_url = self.browser.current_url;
        button_dict = defaultdict(dict)
        obj.element.click()
        BasePage.ожидание_прогрузки_страницы(self)
        new_current_url = self.browser.current_url
        time.sleep(1)
        if (current_url != new_current_url):
            self.browser.forward()
            self.browser.back()
            BasePage.ожидание_прогрузки_страницы(self)
            window_data = ""
        else:
            try:
                windows = self.browser.find_elements(By.CSS_SELECTOR, ".modal.in .modal-content")
                window = windows[len(windows) - 1]
                header = window.find_element_by_css_selector(".modal-header .modal-title").text
                form_groups = window.find_elements_by_css_selector("modal-body .form-groups")
                window_data = BasePage.get_form_groups(self, window, header)
                try:
                    table = window.find_element_by_css_selector(".ksb-table-container")
                    window_table = BasePage.get_table_data_by_element(self, table)
                    window_data.update({"Таблица": window_table})
                except:
                    pass
                window.find_element_by_css_selector(".close").click()
                time.sleep(2)
            except:
                pass

        button_dict.update({"Элемент": obj.element})
        button_dict.update({obj.name: window_data})
        return button_dict
    def get_form_groups(self, panel, panel_name=""):
        page = defaultdict(dict)
        try:
            panel_name = panel.find_element_by_css_selector(".panel-title .help-link").text
        except:
            pass

        try:
            formGroups = panel.find_elements_by_css_selector(".form-group")
        except:
            pass

        for formGroup in formGroups:
            try:
                formGroup_name = formGroup.find_element_by_css_selector(".control-label label span:nth-child(1)").text
                # Текстовое поле
            except:
                formGroup_name = "buff"
            # region Парсинг элементов

            try:
                value = formGroup.find_element_by_css_selector("input:nth-child(1)").get_attribute("value")
                page[panel_name].update({formGroup_name: value})
            except:
                pass

            # region TextArea
            # Многострочный ввод
            try:
                value = formGroup.find_element_by_css_selector("textarea")
                page[panel_name].update({formGroup_name: value.text})
            except:
                pass
            # endregion
            # region CheckBox
            try:
                checkboxes = formGroup.find_elements_by_css_selector(".checkbox")
                if (len(checkboxes) > 0):
                    for checkbox in checkboxes:
                        element = BasePage.CheckBox(checkbox)
                        page[panel_name].update({element.name: element.value})
            except:
                pass
            # endregion
            # region RaddioButtons
            # Радио???
            try:
                raddioButton = formGroup.find_element_by_css_selector(".radio")
                raddioButton = BasePage.RaddioButton(formGroup)
                page[panel_name].update({raddioButton.name: raddioButton.value})
            except:
                pass
            # endregion
            # region Select2Choosen
            try:
                select2_chooicen = formGroup.find_element_by_css_selector(".select2-chosen")
                select2_chooicen_obj = BasePage.Select2Choosen(select2_chooicen)
                select2_chooicen_obj.name = formGroup_name
                page[panel_name].update({select2_chooicen_obj.name: select2_chooicen_obj.value})
                continue
            except:
                pass
            # endregion
            # region Select2Chooices
            try:
                select2_chooices = formGroup.find_element_by_css_selector(".select2-choices")
                select2_chooices_obj = BasePage.Select2Chooice(select2_chooices)
                select2_chooices_obj.name = formGroup_name
                page[panel_name].update({select2_chooices_obj.name: select2_chooices_obj.value})
                continue
            except:
                pass
            # endregion
            # region Select
            # Простой селект. hidden-select валится в except - спец обработка не нужна
            try:
                select = formGroup.find_element_by_css_selector("select")
                select_obj = BasePage.Select(select)
                select_obj.name = formGroup_name
                page[panel_name].update({select_obj.name: select_obj.value})
            except:
                pass
            # endregion
            #region Row
            # группа "Индекс и Адрес", пока что
            try:
                row = formGroup.find_element_by_css_selector(".row")
                row_obj = BasePage.Row(row)
                row_obj.name = formGroup_name
                page[panel_name].update({row_obj.name: row_obj.value})
                continue
            except:
                pass
            # endregion

        return page[panel_name]

    # endregion

    class Apps:
        def __init__(self):
            pass

        def open_apps_popup(self):
            """
            Открытие выпадающего меню приложений организации

            :return:
            """
            self.browser.find_element_by_xpath("//*[@class='apps']").click()
            BasePage.ждать_пока_элемент_отсутсвует(self, By.XPATH, "//*[contains(@class,'popover-content')]/*[contains(@class,'tile-menu')]")

        def open_app(self,name):
            BasePage.ждать_пока_элемент_отсутсвует(self, By.XPATH,"//*[contains(@class,'popover-content')]/*[contains(@class,'tile-menu')]")
            try:
                app = self.browser.find_element_by_xpath(
                    "//*[contains(@class,'popover-content')]//*[@class='tile-text' and contains(.,'"+name+"')]")
                app.click()
                BasePage.ждать_пока_элемент_отсутсвует(self,By.XPATH,"//*[contains(@class,'header-toolbar')]//li[contains(.,'"+name+"')]",20)
            except:
                assert False, "Не удалось открыть приложение '"+name+"'"
        def open_stage(self,name):
            try:
                app = self.browser.find_element_by_xpath(
                    "//*[contains(@title,'"+name+"')]")
                app.click()
                BasePage.ожидание_прогрузки_страницы(self)
            except:
                assert False, "Не удалось открыть приложение '"+name+"'"


        def search_app_by_name(self, name):
            """
            Поиск приложения по заданному наименованию

            :param name: Вхождение наименования приложения поиск которого необходимо выполнить

            :return: True | False
            """
            BasePage.ждать_пока_элемент_отсутсвует(self, By.XPATH,
                                                   "//*[contains(@class,'popover-content')]/*[contains(@class,'tile-menu')]")
            menu = self.browser.find_element_by_xpath(
                "//*[contains(@class,'popover-content')]/*[contains(@class,'tile-menu')]")
            menu_main_elements = menu.find_elements_by_xpath(
                "//*[@class='tile-container']//*[@class='tile']//*[@class='tile-text']")
            menu_favorite_elements = menu.find_elements_by_xpath(
                "//*[@class='favorite-tiles-container']//*[@class='tile']//*[@class='tile-text']")
            menu_elements_text = []
            for menu_element in menu_main_elements:
                menu_elements_text.append(menu_element.text)
            for menu_element in menu_favorite_elements:
                menu_elements_text.append(menu_element.text)
            if name in menu_elements_text:
                return True
            else:
                return False

    class UserMenu:
        dropmenu = None
        menu_state = None
        dropdown_menu = None

        def __init__(self, browser):
            """
            Конструктор класса выпадающего списка меню пользователя (аватар)

            :param browser: Страница, в рамках которого будет выполнен поиск элемента
            """
            self.dropmenu = browser.find_element_by_xpath("//*[contains(@class,'dropdown usermenu')]")
            self.menu_state = self.dropmenu.get_attribute("class")
            try:
                self.dropdown_menu = self.dropmenu.find_element_by_xpath("//*[contains(@class,'dropdown-menu')]")
            except:
                pass

        def is_menu_open(self):
            """
            Проверка, что меню пользователя открыто

            :return:
            """
            if self.menu_state.find("open") > -1:
                return True
            else:
                return False

        def open(self):
            """
            Открытие меню пользователя

            :return:
            """
            if self.menu_state.find("open") == -1:
                self.dropmenu.click()

        def check_manager_rules(self):
            """
            Проверка наличия прав менеджера

            :return: True|False
            """
            if self.menu_state.find("open") == -1:
                self.dropmenu.click()
                self.dropdown_menu = self.dropmenu.find_element_by_xpath("//*[contains(@class,'dropdown-menu')]")
                try:
                    self.dropdown_menu.find_element_by_xpath("//a[contains(.,'Менеджер')]")
                    return True
                except:
                    return False

