from selenium import webdriver
import time

try:

    log = "vvgspok7890"
    pas = "jkl28mn170797"

    link = "http://rc.alfa-doc.ru/accounts/login/"
    browser = webdriver.Chrome()
    browser.get(link)
    # browser.implicitly_wait(5)
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
    search = True
    while search:
        try:
            browser.find_element_by_css_selector(".loading")
            time.sleep(0.5)
        except:
            search = False

    # нажатие всех кнопко Развернуть
    # all_buttons = browser.find_elements_by_xpath("//*[@class='cell-expand-text' and contains(.,'развернуть') and not(@style='display: none;')]")
    # for expand in all_buttons:
    #   expand.click()
    column_N = browser.find_elements_by_xpath("(//th[@class='col-fixed nowrap row_number tight-column'])[1]")
    column_N_text = column_N[0].text
    assert "№ П/П" == column_N_text, f"Нет колонки {column_N_text}"

    column_K = browser.find_elements_by_xpath("(//th[@class='nowrap card_infosystem tight-column'])[1]")

    column_IS = browser.find_elements_by_xpath("(//th[@class='orderable sortable name'])[1]")
    #column_IS_text = column_IS[0].text
   # assert "НАИМЕНОВАНИЕ ИС" == column_IS_text, f"Нет колонки {column_IS_text}"

    column_PK = browser.find_elements_by_xpath("(//th[@class='software_by_rate'])[1]")
    column_PK_text = column_PK[0].text
    assert "ПРОГРАММНЫЕ КОМПЛЕКСЫ" == column_PK_text, f"Нет колонки {column_PK_text}"

    column_Location = browser.find_elements_by_xpath("(//th[@class='get_rooms'])[1]")
    column_Location_text = column_Location[0].text
    assert "МЕСТО РАСПОЛОЖЕНИЯ" == column_Location_text, f"Нет колонки {column_Location_text}"

    column_YZ = browser.find_elements_by_xpath("(//th[@class='protection_level'])[1]")
    column_YZ_text = column_YZ[0].text
    assert "УРОВЕНЬ ЗАЩИЩЁННОСТИ ПДН" == column_YZ_text, f"Нет колонки {column_YZ_text}"

    column_KZ = browser.find_elements_by_xpath("(//th[@class='protection_class'])[1]")
    column_KZ_text = column_KZ[0].text
    assert "КЛАСС ЗАЩИЩЁННОСТИ ГИС" == column_KZ_text, f"Нет колонки {column_KZ_text}"

    column_K3 = browser.find_elements_by_xpath("(//th[@class='significance'])[1]")
    column_K3_text = column_K3[0].text
    assert "КАТЕГОРИЯ ЗНАЧИМОСТИ" == column_K3_text, f"Нет колонки {column_K3_text}"

    column_AT = browser.find_elements_by_xpath("(//th[@class='validation_state_verbose'])[1]")
    column_AT_text = column_AT[0].text
    assert "СВЕДЕНИЯ ОБ АТТЕСТАЦИИ" == column_AT_text, f"Нет колонки {column_AT_text}"

    element3 = browser.find_elements_by_xpath("//*[contains(@class,'infosystems-table')]//tbody//tr[1]/td[3]")
    for i3 in element3:
        print("НАИМЕНОВАНИЕ ИС = ", i3.text)
    print("---------------------")

    element4 = browser.find_elements_by_xpath("//*[contains(@class,'infosystems-table')]//tbody//tr[1]/td[4]")
    for i4 in element4:
        print("ПРОГРАММНЫЕ КОМПЛЕКСЫ = ", i4.text)
    print("---------------------")

    element5 = browser.find_elements_by_xpath("//*[contains(@class,'infosystems-table')]//tbody//tr[1]/td[5]")
    for i5 in element5:
        print("МЕСТО РАСПОЛОЖЕНИЯ = ", i5.text)
    print("---------------------")

    element6 = browser.find_elements_by_xpath("//*[contains(@class,'infosystems-table')]//tbody//tr[1]/td[6]")
    for i6 in element6:
        print("УРОВЕНЬ ЗАЩИЩЁННОСТИ ПДН = ", i6.text)
    print("---------------------")

    element7 = browser.find_elements_by_xpath("//*[contains(@class,'infosystems-table')]//tbody//tr[1]/td[7]")
    for i7 in element7:
        print("КЛАСС ЗАЩИЩЁННОСТИ ГИС = ", i7.text)
    print("---------------------")

    element8 = browser.find_elements_by_xpath("//*[contains(@class,'infosystems-table')]//tbody//tr[1]/td[8]")
    for i8 in element8:
        print("КАТЕГОРИЯ ЗНАЧИМОСТИ = ", i8.text)
    print("---------------------")

    element9 = browser.find_elements_by_xpath("//*[contains(@class,'infosystems-table')]//tbody//tr[1]/td[9]")
    for i9 in element9:
        print("СВЕДЕНИЯ ОБ АТТЕСТАЦИИ = ", i9.text)
    print("---------------------")

    # browser.get("http://rc.alfa-doc.ru/cabinet/main_wizard/company_details/#step/aims")


finally:
    time.sleep(3)
    browser.quit()
