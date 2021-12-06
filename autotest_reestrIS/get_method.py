from selenium import webdriver
import time



try:

    log = "vvgspok7890" #
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
    browser.get("http://rc.alfa-doc.ru/cabinet/company_reports/company_reports/company_reports/#step/infosystems")
    l = browser.find_elements_by_xpath("//*[@class='tableFloatingHeaderOriginal]").text
    print(l)

    # добавил измменения
finally:
    time.sleep(3)
    browser.quit()