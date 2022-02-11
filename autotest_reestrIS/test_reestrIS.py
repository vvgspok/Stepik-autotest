from selenium import webdriver
import time

try:

    log = "vvgspok7890"
    pas = "jkl28mn170797"

    link = "http://rc.alfa-doc.ru/accounts/login/"
    browser = webdriver.Chrome()
    browser.get(link)
    reg = browser.find_element_by_xpath("//*[@class='text-center']/a").click()
    login = browser.find_element_by_id("loginInput")
    login.send_keys(log)
    password = browser.find_element_by_id("passwordInput")
    password.send_keys(pas)
    button = browser.find_element_by_xpath("//*[@class='btn btn-primary login__submit-password-btn ']")
    button.click()

    # Переход в Реестр ИС
    browser.get(
        "http://rc.alfa-doc.ru/cabinet/infosystem_registry/infosystem_registry/infosystem_registry/#step/registry")


    try:
        while True:
            browser.find_element_by_css_selector(".loading")
            time.sleep(0.5)
    except:
        pass

    # нажатие всех кнопко Развернуть
    all_buttons = browser.find_elements_by_xpath(
        "//*[@class='cell-expand-text' and contains(.,'развернуть') and not(@style='display: none;')]")
    for expand in all_buttons:
        expand.click()

    column_N = browser.find_element_by_xpath("(//th[@class='col-fixed nowrap row_number tight-column'])[1]")
    column_N_text = column_N.text
    assert "№ П/П" == column_N_text, f"Нет колонки {column_N_text}"

    # column_K = browser.find_element_by_xpath("(//th[@class='nowrap card_infosystem tight-column'])[1]")

    column_IS = browser.find_element_by_xpath("(//th[@class='orderable sortable name'])[1]")
    column_IS_text = column_IS.text
    # assert "НАИМЕНОВАНИЕ ИС" == column_IS_text, f"Нет колонки {column_IS_text}"

    column_PK = browser.find_element_by_xpath("(//th[@class='software_by_rate'])[1]")
    column_PK_text = column_PK.text
    assert "ПРОГРАММНЫЕ КОМПЛЕКСЫ" == column_PK_text, f"Нет колонки {column_PK_text}"

    column_Location = browser.find_element_by_xpath("(//th[@class='get_rooms'])[1]")
    column_Location_text = column_Location.text
    assert "МЕСТО РАСПОЛОЖЕНИЯ" == column_Location_text, f"Нет колонки {column_Location_text}"

    column_YZ = browser.find_element_by_xpath("(//th[@class='protection_level'])[1]")
    column_YZ_text = column_YZ.text
    assert "УРОВЕНЬ ЗАЩИЩЁННОСТИ ПДН" == column_YZ_text, f"Нет колонки {column_YZ_text}"

    column_KZ = browser.find_element_by_xpath("(//th[@class='protection_class'])[1]")
    column_KZ_text = column_KZ.text
    assert "КЛАСС ЗАЩИЩЁННОСТИ ГИС" == column_KZ_text, f"Нет колонки {column_KZ_text}"

    column_K3 = browser.find_element_by_xpath("(//th[@class='significance'])[1]")
    column_K3_text = column_K3.text
    assert "КАТЕГОРИЯ ЗНАЧИМОСТИ" == column_K3_text, f"Нет колонки {column_K3_text}"

    column_AT = browser.find_element_by_xpath("(//th[@class='validation_state_verbose'])[1]")
    column_AT_text = column_AT.text
    assert "СВЕДЕНИЯ ОБ АТТЕСТАЦИИ" == column_AT_text, f"Нет колонки {column_AT_text}"

    # Поиск значений в колонке
    element3 = browser.find_element_by_xpath("//*[contains(@class,'infosystems-table')]//tbody//tr[1]/td[3]")
    element3_text = element3.text
    print(element3_text)
    print("---------------------")

    element4 = browser.find_element_by_xpath("//*[contains(@class,'infosystems-table')]//tbody//tr[1]/td[4]/div")
    element4_text = element4.text
    print(element4_text)
    print("---------------------")

    element5 = browser.find_element_by_xpath("//*[contains(@class,'infosystems-table')]//tbody//tr[1]/td[5]/div")
    element5_text = element5.text
    print(element5_text)
    print("---------------------")

    element6 = browser.find_element_by_xpath("//*[contains(@class,'infosystems-table')]//tbody//tr[1]/td[6]")
    element6_text = element6.text
    print(element6_text)
    print("---------------------")

    element7 = browser.find_element_by_xpath("//*[contains(@class,'infosystems-table')]//tbody//tr[1]/td[7]")
    element7_text = element7.text
    print(element7_text)
    print("---------------------")

    element8 = browser.find_element_by_xpath("//*[contains(@class,'infosystems-table')]//tbody//tr[1]/td[8]")
    element8_text = element8.text
    print(element8_text)
    print("---------------------")

    element9 = browser.find_element_by_xpath("//*[contains(@class,'infosystems-table')]//tbody//tr[1]/td[9]")
    element9_text = element9.text
    print(element9_text)
    print("---------------------")

    # Переход на шаг Цели и способы обработки
    browser.get("http://rc.alfa-doc.ru/cabinet/main_wizard/company_details/#step/aims")

    try:
        while True:
            browser.find_element_by_css_selector(".loading")
            time.sleep(0.5)
    except:
        pass

    find_column_IS = browser.find_element_by_xpath(
        "//*[@class='ksb-table-wrapper']//*[contains(text(),'" + element3_text + "')]")
    find_column_IS_text = find_column_IS.text
    print(find_column_IS_text)
    assert element3_text == find_column_IS_text

    # Переход в ПК
    browser.get("http://rc.alfa-doc.ru/cabinet/main_wizard/company_details/#step/softwares")

    try:
        while True:
            browser.find_element_by_css_selector(".loading")
            time.sleep(0.5)
    except:
        pass

    find_column_PK1 = browser.find_element_by_xpath(
        "//*[contains(@class,'table-hover -table-hover table-body-bordered table-bordered')]//tbody[2]//tr[2]/td[1]")
    find_column_PK1_text = find_column_PK1.text
    print(find_column_PK1_text)

    find_column_PK2 = browser.find_element_by_xpath(
        "//*[contains(@class,'table-hover -table-hover table-body-bordered table-bordered')]//tbody[2]//tr[3]/td[1]")
    find_column_PK2_text = find_column_PK2.text
    print(find_column_PK2_text)

    find_column_PK3 = browser.find_element_by_xpath(
        "//*[contains(@class,'table-hover -table-hover table-body-bordered table-bordered')]//tbody[2]//tr[4]/td[1]")
    find_column_PK3_text = find_column_PK3.text
    print(find_column_PK3_text)

    # Переход в ПДн
    browser.get("http://rc.alfa-doc.ru/cabinet/main_wizard/personal_data/#step/software_parameters")

    try:
        while True:
            browser.find_element_by_css_selector(".loading")
            time.sleep(0.5)
    except:
        pass

    find_column_Y3 = browser.find_element_by_xpath("//*[contains(@class,'table-bordered')]//tbody//tr[1]/td[3]")
    find_column_Y3_text = find_column_Y3.text
    print("УЗ-" + find_column_Y3_text)

    # Переход в ГИС
    browser.get("http://rc.alfa-doc.ru/cabinet/main_wizard/gis/#step/softwares")

    try:
        while True:
            browser.find_element_by_css_selector(".loading")
            time.sleep(0.5)
    except:
        pass

    find_column_KZ = browser.find_element_by_xpath("//*[contains(@class,'table-bordered')]//tbody//tr[1]/td[3]")
    find_column_KZ_text = find_column_KZ.text
    print("К" + find_column_KZ_text)

    # Переход в Аттестацию
    browser.get("http://rc.alfa-doc.ru/cabinet/main_wizard/attestation/#step/infosystem-certification")

    try:
        while True:
            browser.find_element_by_css_selector(".loading")
            time.sleep(0.5)
    except:
        pass

    find_column_AT = browser.find_element_by_xpath("//*[contains(@class,'table-bordered')]//tbody//tr[1]/td[2]")
    find_column_AT_text = find_column_AT.text
    print(find_column_AT_text)

finally:
    #time.sleep(3)
    browser.quit()
