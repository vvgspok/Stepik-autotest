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

        field_inn = self.browser.find_element_by_xpath("//*[@id='id_inn']")
        field_kpp = self.browser.find_element_by_xpath("//*[@id='id_kpp']")
        field_ogrn = self.browser.find_element_by_xpath("//*[@id='id_ogrn']")
        field_short = self.browser.find_element_by_xpath("//*[@id='id_short_name_0']")
        field_full = self.browser.find_element_by_xpath("//*[@id='id_full_name_0']")
        field_disease = self.browser.find_element_by_xpath("//*[@id='id_symbol_0']")
        field_org_type = self.browser.find_element_by_xpath("//*[@id='id_kind']")
        field_name_doc = self.browser.find_element_by_xpath("//*[@id='id_charter']")
        field_activity_licenses = self.browser.find_element_by_xpath("//*[@class='select2-search-choice ui-sortable-handle']")
        field_checkbox_off_website = self.browser.find_element_by_xpath("//*[@id='id_has_website']")
        field_locality = self.browser.find_element_by_xpath("//*[@id='id_locality']")
        field_legal_index = self.browser.find_element_by_xpath("//*[@id='id_legal_address_0']")
        field_legal_address = self.browser.find_element_by_xpath("//*[@id='id_legal_address_1']")
        field_actual_index = self.browser.find_element_by_xpath("//*[@id='id_actual_address_0']")
        field_actual_address = self.browser.find_element_by_xpath("//*[@id='id_actual_address_1']")
        field_mailing_index = self.browser.find_element_by_xpath("//*[@id='id_mailing_address_0']")
        field_mailing_address = self.browser.find_element_by_xpath("//*[@id='id_mailing_address_1']")
        field_checkbox_department = self.browser.find_element_by_xpath("//*[@id='id_has_departments']")


        field_inn = field_inn.get_attribute("value")
        print("\n",field_inn)

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

        field_checkbox_department = field_checkbox_department.get_attribute("value")
        print(field_checkbox_department)

        '''
        input_kpp = self.browser.find_element_by_xpath("//*[@class='form-group kpp-group']//*[@class='form-control']")
        input_kpp.clear()
        input_kpp.send_keys("123456789")

        input_ogrn = self.browser.find_element_by_xpath(
            "//*[@class='form-group required ogrn-group']//*[@class='form-control']")
        input_ogrn.clear()
        input_ogrn.send_keys("6053066791167")

        input_locality = self.browser.find_element_by_xpath(
            "//*[@class='form-group required locality-group']//*[@class='form-control']")
        input_locality.clear()
        input_locality.send_keys("Тест_Москва")

        input_legal_index = self.browser.find_element_by_xpath("//*[@id='id_legal_address_0']")
        input_legal_index.clear()
        input_legal_index.send_keys("123456")

        input_legal_address = self.browser.find_element_by_xpath("//*[@id='id_legal_address_1']")
        input_legal_address.clear()
        input_legal_address.send_keys("Чебоксары", enter)
        '''

        time.sleep(2)

