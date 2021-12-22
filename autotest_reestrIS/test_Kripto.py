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

    # Переход в мастер опроса
    browser.get("http://rc.alfa-doc.ru/cabinet/main_wizard/company_details/#step/common")

    try:
        while True:
            browser.find_element_by_css_selector(".loading")
            time.sleep(0.5)
    except:
        pass
    enter = u'\ue007'
    input_KPP = browser.find_element_by_xpath("//*[@class='form-group kpp-group']//*[@class='form-control']")
    input_KPP.send_keys("123456789")
    input_OGRN = browser
    input_OGRN = browser.find_element_by_xpath("//*[@class='form-group required ogrn-group']//*[@class='form-control']")
    input_OGRN.clear()
    input_OGRN.send_keys("6053066791167")

    input_locality = browser.find_element_by_xpath("//*[@class='form-group required locality-group']//*[@class='form-control']")
    input_locality.clear()
    input_locality.send_keys("Тест_Москва")

    input_legal_index = browser.find_element_by_xpath("//*[@id='id_legal_address_0']")
    input_legal_index.clear()
    input_legal_index.send_keys("123456")

    input_legal_address = browser.find_element_by_xpath("//*[@id='id_legal_address_1']")
    input_legal_address.clear()
    input_legal_address.send_keys("Чебоксары", enter)



    field_actual_address = browser.find_element_by_xpath("//*[@id='id_mailing_address_0']")


finally:
    time.sleep(5)
    browser.quit()