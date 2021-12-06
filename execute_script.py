from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = " http://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x) # считаем X
    #Скролл страницы вниз
    browser.execute_script("window.scrollBy(0, 100);")

    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)
    check = browser.find_element_by_xpath("//*[@id='robotCheckbox']").click()
    radio = browser.find_element_by_xpath("//*[@id='robotsRule']").click()

    button = browser.find_element_by_css_selector("button.btn")
    button.click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(50)
    # закрываем браузер после всех манипуляций
    browser.quit()