# 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
import time
from collections import defaultdict

import pytest
from selenium import webdriver
import urllib3
# from manager.manager_base import МенеджерСайта
from pages.base_page import BasePage
#from dictionary.dict_functions import DictionaryFunctions
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common import keys
import os


@pytest.mark.usefixtures("prepare")
class TestGeneral:
    def test_step1(self):

        self.browser.get(self.common_address + "cabinet/main_wizard/personal_data_crypto_standalone/#step/common")
        BasePage.ожидание_прогрузки_страницы(self)

        # Проверка кол-ва шагов на странице

        #len_step = len(self.browser.find_elements_by_xpath("//*[@class='step-name']"))
        #assert len_step == 5, "Кол-во шагов != 5"

        field_inn = self.browser.find_element_by_xpath("//*[@id='id_inn']")  # ИНН
        field_kpp = self.browser.find_element_by_xpath("//*[@id='id_kpp']")  # КПП
        field_ogrn = self.browser.find_element_by_xpath("//*[@id='id_ogrn']")  # ОГРН
        field_short = self.browser.find_element_by_xpath("//*[@id='id_short_name_0']")  # Краткое наименование организации
        field_full = self.browser.find_element_by_xpath("//*[@id='id_full_name_0']")  # Полное наименование организации
        field_disease = self.browser.find_element_by_xpath("//*[@id='id_symbol_0']")  # Условное сокращение
        field_org_type = self.browser.find_element_by_xpath("//*[@id='id_kind']")  # Тип организации
        field_name_doc = self.browser.find_element_by_xpath("//*[@id='id_charter']")  # Наименование и реквизиты учредительного документа
        field_activity_licenses = self.browser.find_element_by_xpath("//*[@class='select2-search-choice ui-sortable-handle']")  # Лицензии на вид деятельности
        field_checkbox_off_website = self.browser.find_element_by_xpath("//*[@id='id_has_website']")  # Есть официальный сайт
        field_locality = self.browser.find_element_by_xpath("//*[@id='id_locality']")  # Населённый пункт
        field_legal_index = self.browser.find_element_by_xpath("//*[@id='id_legal_address_0']")  # Юридический адрес
        field_legal_address = self.browser.find_element_by_xpath("//*[@id='id_legal_address_1']")  # Юридический адрес
        field_actual_index = self.browser.find_element_by_xpath("//*[@id='id_actual_address_0']")  # Фактический адрес
        field_actual_address = self.browser.find_element_by_xpath("//*[@id='id_actual_address_1']")  # Фактический адрес
        field_mailing_index = self.browser.find_element_by_xpath("//*[@id='id_mailing_address_0']")  # Почтовый адрес
        field_mailing_address = self.browser.find_element_by_xpath("//*[@id='id_mailing_address_1']")  # Почтовый адрес
        field_email = self.browser.find_element_by_xpath("//*[@id = 'id_email']")  # Адрес электронной почты
        field_checkbox_department = self.browser.find_element_by_xpath("//*[@id='id_has_departments']")  # Есть структурные подразделения

        field_inn = field_inn.get_attribute("value")

        print("\n",field_inn)
        #field_inn = field_inn.get_attribute("readonly")
        #print(field_inn)

        field_kpp = field_kpp.get_attribute("value")
        print(field_kpp)

        field_ogrn = field_ogrn.get_attribute("value")
        print(field_ogrn)

        field_short = field_short.get_attribute("value")
        print(field_short)

        field_full = field_full.get_attribute("value")
        print(field_full)

        field_disease = field_disease.get_attribute("value")
        print(field_disease)

        print(field_org_type.text)

        field_name_doc = field_name_doc.get_attribute("value")
        print(field_name_doc)

        print(field_activity_licenses.text)

        field_checkbox_off_website = field_checkbox_off_website.get_attribute("value")
        print(field_checkbox_off_website)

        field_locality = field_locality.get_attribute("value")
        print(field_locality)

        field_legal_index = field_legal_index.get_attribute("value")
        print(field_legal_index)

        field_legal_address = field_legal_address.get_attribute("value")
        print(field_legal_address)

        field_actual_index = field_actual_index.get_attribute("value")
        print(field_actual_index)

        field_actual_address = field_actual_address.get_attribute("value")
        print(field_actual_address)

        field_mailing_index = field_mailing_index.get_attribute("value")
        print(field_mailing_index)

        field_mailing_address = field_mailing_address.get_attribute("value")
        print(field_mailing_address)

        field_email = field_email.get_attribute("value")
        print(field_email)

        field_checkbox_department = field_checkbox_department.get_attribute("value")
        print(field_checkbox_department)

    def test_step2(self):
        self.browser.get(self.common_address + "cabinet/main_wizard/personal_data_crypto_standalone/#step/structure")
        BasePage.ожидание_прогрузки_страницы(self)
        '''
        """Загрузка файла"""
        name_file = 'SP.xlsx'
        BasePage.file_upload(self, name_file)
        '''
        """Проверка на обязательное поле"""

        WebDriverWait(self.browser, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@class='btn btn-sm btn-success']"))
        ).click()

        WebDriverWait(self.browser, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@class='btn btn-sm btn-success']"))
        ).click()

        obligatory_field_name = WebDriverWait(self.browser, 100).until(
            EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Это поле обязательно.')]"))).text
        assert obligatory_field_name == "Это поле обязательно.", f'Сообщение "{obligatory_field_name}" не появилось'
        """Добавление структурного подразделения"""
        field_name_SP = self.browser.find_element_by_xpath("//*[@id='id_name']")
        field_name_SP.send_keys("Наименование СП")
        checkbox_filial = self.browser.find_element_by_xpath("//*[@id='id_affiliate']").click()

        WebDriverWait(self.browser, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@class='btn btn-sm btn-success']"))
        ).click()

        obligatory_field_kpp = WebDriverWait(self.browser, 100).until(
            EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Для филиала необходимо указать КПП')]"))).text
        assert obligatory_field_kpp == "Для филиала необходимо указать КПП", f'Сообщение "{obligatory_field_kpp}" не появилось'
        field_kpp = self.browser.find_element_by_xpath("//*[@id='id_kpp']")
        field_kpp.send_keys("КПП тестовый")

        WebDriverWait(self.browser, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@class='btn btn-sm btn-success']"))
        ).click()
        obligatory_field_kpp = WebDriverWait(self.browser, 100).until(
            EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Разрешённые символы: цифры')]"))).text
        assert obligatory_field_kpp == "Разрешённые символы: цифры", f'Сообщение "{obligatory_field_kpp}" не появилось'
        newfield_kpp = self.browser.find_element_by_xpath("//*[@id='id_kpp']")
        newfield_kpp.clear()
        newfield_kpp.send_keys("123456789")

        WebDriverWait(self.browser, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@class='btn btn-sm btn-success']"))
        ).click()
        BasePage.select_row(self)
        time.sleep(5)

    def test_step3(self):
        self.browser.get(self.common_address + "cabinet/main_wizard/personal_data_crypto_standalone/#step/employees")
        BasePage.ожидание_прогрузки_страницы(self)
        '''   
        """
        Загрузка файла
        """
        name_file = 'worker.xlsx'
        BasePage.file_upload(self, name_file)
        BasePage.file_upload(self, name_file, delete=True)
        '''
        # len_fio = self.browser.find_elements_by_xpath("//*[contains(@class, 'employeestable ')]/tbody/tr")
        # print(len(len_fio))

        table = BasePage.Table.get_table_by_name(self, "Сотрудники организации")
        rows = table.search_record_by_value("ФИО СОТРУДНИКА", "Петрова Елена Николаевна")

        s = 1


    def test_step4(self):
        self.browser.get(self.common_address + "cabinet/main_wizard/personal_data_crypto_standalone/#step/crypto-access-std")
        BasePage.ожидание_прогрузки_страницы(self)

        '''
        Ответственный пользователь криптосредств
        '''
        # add_OPK = self.browser.find_element_by_xpath("//*[@class='btn btn-info']")
        #  add_OPK.click()

        '''
        Перечень лиц, имеющих доступ в помещения, содержащие криптосредства, 
        в том числе допущенных к работе с криптосредствами         
        '''
        add_access = self.browser.find_element_by_xpath("//*[@class='btn btn-sm btn-success']")
        add_access.click()
        time.sleep(5)
        l = self.browser.find_elements_by_xpath("//*[contains(@class, 'selectmultiplepersonaccesstable ')]/tbody/tr")

        add_all_fio = WebDriverWait(self.browser, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Выбрать всех')]"))
        )
        add_all_fio.click()


    def test_step5(self):
        self.browser.get(self.common_address + "cabinet/main_wizard/personal_data_crypto_standalone/#step/rooms_vaults")
        BasePage.ожидание_прогрузки_страницы(self)
        """
        Загрузка файла
        """
        name_file = 'cabinet.xls'
        BasePage.file_upload(self, name_file)
