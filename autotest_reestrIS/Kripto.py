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
from selenium.webdriver.support.ui import Select
import os

@pytest.mark.usefixtures("prepare")
class TestGeneral():
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
        """
        Загрузка списка структурных подразделений из файла 
        """
        self.browser.find_element_by_xpath("//*[@class='btn btn-sm btn-default']").click()
        current_dir = os.path.abspath(os.path.dirname(__file__))
        file_path = os.path.join(current_dir, 'SP.xlsx')
        element = WebDriverWait(self.browser, 10).until(
        EC.presence_of_element_located((By.ID, "id_upload_file")))
        element.send_keys(file_path)
        try:
                WebDriverWait(self.browser, 10).until(
                EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Загружен файл')]")))
        except Exception as e:
            assert False, "Файл не загружается;" + e
        self.browser.find_element_by_xpath("//*[@class='modal-content']//*[@class='btn btn-sm btn-success']").click()



    def test_step3(self):
        self.browser.get(self.common_address + "cabinet/main_wizard/personal_data_crypto_standalone/#step/employees")
        BasePage.ожидание_прогрузки_страницы(self)
        """
        Загрузка списка сотрудников из файла
        """
        self.browser.find_element_by_xpath("//*[@class='btn btn-sm btn-default']").click()
        current_dir = os.path.abspath(os.path.dirname(__file__))
        file_path = os.path.join(current_dir, 'worker.xlsx')
        element = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.ID, "id_upload_file")))
        element.send_keys(file_path)
        try:
            WebDriverWait(self.browser, 10).until(
                EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Загружен файл')]")))
        except Exception as e:
            assert False, "Файл не загружается;" + e
        self.browser.find_element_by_xpath("//*[@class='modal-content']//*[@class='btn btn-sm btn-success']").click()

    def test_step4(self):
        self.browser.get(self.common_address + "cabinet/main_wizard/personal_data_crypto_standalone/#step/crypto-access-std")
        BasePage.ожидание_прогрузки_страницы(self)

    def test_step5(self):
        self.browser.get(self.common_address + "cabinet/main_wizard/personal_data_crypto_standalone/#step/rooms_vaults")
        BasePage.ожидание_прогрузки_страницы(self)

