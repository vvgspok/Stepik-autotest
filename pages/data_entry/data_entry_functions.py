from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from pages.base_page import BasePage
from pages.authorization_service.admin.authorization_service_locators import AuthorizationServiceLocators
from pages.data_entry.data_entry_locators import DataEntryLocators


class DataEntry:
    """Заготовка под парсинг данных с Ввода данных. Сейчас умеет собирать названия панелей по мастерам в json"""
    def __init__(self, page):
        self.nav_tabs_elems = page.find_elements(*DataEntryLocators.NAVIGATION_TABS_ELEMENTS_SUCCESS)
        self.browser = page

    def nav_tabs(self):
        """объекты мастеров из шапки"""
        return self.nav_tabs_elems

    def nav_tab_name(self, elem):
        """:return: название мастера"""
        return elem.text.strip()

    def go_to_master(self, master_name: str):
        """Перемещает в другой мастер нажатием его названия в Визарде"""
        locator = DataEntryLocators.WIZARD_MASTER
        locator = [locator[0], locator[1].replace("<MASTER_NAME>", master_name)]
        btn = self.browser.find_element(*locator)
        btn.click()

    def go_to_step(self, step_data_key: str):
        """Переход на шаг"""
        locator = DataEntryLocators.STEP
        locator = [locator[0], locator[1].replace("STEP_KEY", step_data_key)]
        f = open("locators.txt", "a")
        f.write(str(locator) + "\t")
        f.close()
        btn = self.browser.find_element(*locator)
        btn.click()

    def steps(self) -> dict:
        """:return: dict названия шагов: обьект кнопки шага"""
        steps = {}
        for i in self.browser.find_elements(*DataEntryLocators.WIZARD_STEP):
            data_key = i.get_attribute("data-key")
            steps[data_key] = i

        for i in self.browser.find_elements(*DataEntryLocators.WIZARD_STEP_DISABLED):
            data_key = i.get_attribute("data-key")
            steps[data_key] = False

        active_step = self.browser.find_element(*DataEntryLocators.WIZARD_STEP_ACTIVE)
        active_step_key = active_step.get_attribute("data-key")
        steps[active_step_key] = active_step

        return steps

    def panels(self) -> dict:
        """:return: словарь название панели: содержание элементов панели (текстовые поля, чекбоксы и т.д.)"""
        panels = {}
        for panel in self.browser.find_elements(*DataEntryLocators.PANELS_NAMES):
            panel_name = panel.text
            if panel_name:
                table = self.parse_table(panel_name)
                panels[panel_name] = self.parse_text_fields(panel_name) | self.parse_checkboxes(panel_name) | self.parse_radio_buttons(panel_name) | table
        return panels

    def parse_text_fields(self, panel_title: str) -> dict:
        """:return: словарь id: содержание текстового поля"""
        d = {}
        loc = [*DataEntryLocators.TEXT_FIELDS]
        loc = [loc[0], loc[1].replace("<PANEL_TITLE>", panel_title.strip())]
        loc_large_fields = [*DataEntryLocators.LARGE_TEXT_FIELDS]
        loc_large_fields = [loc_large_fields[0], loc_large_fields[1].replace("<PANEL_TITLE>", panel_title.strip())]
        for field in (self.browser.find_elements(*loc) + self.browser.find_elements(*loc_large_fields)):
            id = field.get_attribute("id")
            if id:
                try:
                    if field.get_attribute("style") == "display: none;":
                        continue
                finally:
                    d[id] = field.get_attribute("value")
        return d

    def parse_checkboxes(self, panel_title: str) -> dict:
        """:return: словарь id: состояние чебокса"""
        d = {}
        loc = [*DataEntryLocators.CHECKBOXES]
        loc = [loc[0], loc[1].replace("<PANEL_TITLE>", panel_title.strip())]
        for checkbox in self.browser.find_elements(*loc):
            id = checkbox.get_attribute("id")
            if id:
                try:
                    if checkbox.get_attribute("style") == "display: none;":
                        continue
                finally:
                    d[id] = (True if checkbox.get_attribute("checked") else False)
        return d

    def parse_radio_buttons(self, panel_title: str) -> dict:
        """:return: словарь name: состояние радиокнопки (нажата - True, иначе False)"""
        d = {}
        loc = [*DataEntryLocators.RADIO_BUTTONS]
        loc = [loc[0], loc[1].replace("<PANEL_TITLE>", panel_title.strip())]
        for radio in self.browser.find_elements(*loc):
            name = radio.get_attribute("name")
            if name:
                try:
                    if radio.get_attribute("style") == "display: none;":
                        continue
                finally:
                    if radio.is_selected():
                        d[name] = radio.get_attribute("value")
        return d

    def parse_table(self, panel_title: str) -> dict:
        """:return: словарь {table: {содержание в таблице по строкам (BasePage.Table.get_table_by_name)}}
         если таблица есть в панели, иначе пустой словарь"""
        try:
            table = BasePage.Table.get_table_by_name(self, panel_title.strip())
            d = {"table": dict(table.get_value())}
            return d
        finally:
            return {}
