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
    search = True
    while search:
        try:
          browser.find_element_by_css_selector(".loading")
          time.sleep(0.5)
        except:
            search = False


    element = browser.find_elements_by_xpath("//*[contains(@class,'infosystems-table')]//tbody//tr[1]/td")
    for i in element:
        print(i.text)

finally:
    time.sleep(3)
    browser.quit()
