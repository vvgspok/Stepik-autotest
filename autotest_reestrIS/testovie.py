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




finally:
    time.sleep(1)
    browser.quit()