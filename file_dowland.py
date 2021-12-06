from selenium import webdriver
import time
import os
try: 
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_xpath("//*[@name='firstname']")
    input1.send_keys("Вова")
    input2 = browser.find_element_by_xpath("//*[@name='lastname']")
    input2.send_keys("Волков")
    input3 = browser.find_element_by_xpath("//*[@name='email']")
    input3.send_keys("test@mail.ru")



    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')
    print(current_dir)
    print(file_path)
    element = browser.find_element_by_name("file")
    element.send_keys(file_path)

    button = browser.find_element_by_css_selector("button.btn")
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()