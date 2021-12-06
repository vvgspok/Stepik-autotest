from selenium import webdriver
import time
import math

def calc(x, y):
    return str(int(x) + int(y))
try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_id("num1")
    x = input1.text
    input2 = browser.find_element_by_id("num2")
    y = input2.text
    summa = calc(x, y)
    print("Сумма двух чисел = ", summa)

    from selenium.webdriver.support.ui import Select
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(summa)
    browser.find_element_by_css_selector("button.btn").click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()