from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_xpath("//*[@id='treasure']")
    num = x_element.get_attribute("valuex")
    print("Значение сундука =", num)
    x = num
    y = calc(x)

    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)
    check = browser.find_element_by_css_selector("[type='checkbox']").click()
    radio = browser.find_element_by_xpath("//*[@id='robotsRule']").click()
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(50)
    # закрываем браузер после всех манипуляций
    browser.quit()