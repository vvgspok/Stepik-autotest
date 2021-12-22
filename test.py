from selenium import webdriver
import time
import math
answer = math.log(int(time.time()))
try:
    link = "https://stepik.org/lesson/236895/step/1"
    browser = webdriver.Chrome()
    browser.get(link)
    browser.implicitly_wait(10)
    input_pole = browser.find_element_by_xpath("//*[@class='ember-text-area ember-view textarea string-quiz__textarea']")

    input_pole.send_keys(str(answer))
    button = browser.find_element_by_xpath("//*[@class='submit-submission']")
    button.click()
    cor = browser.find_element_by_xpath("//*[@class='smart-hints__hint']")
    cor_text = cor.text
    assert "Correct!" == cor_text
finally:
    time.sleep(3)
    browser.quit()