from selenium import webdriver
from selenium.webdriver.common import keys
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
    browser.get("http://rc.alfa-doc.ru/cabinet/infosystem_registry/infosystem_registry/infosystem_registry/#step/registry")
    l = browser.find_elements_by_xpath("//*[@class='table-hover table has-fixed-columns infosystems-table table-bordered table-condensed']/tbody/tr[1]/td")
    for i in l:
        # выводим содержимое заголовка
        print(i.text)

finally:
    time.sleep(3)
    browser.quit()