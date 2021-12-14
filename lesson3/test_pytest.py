import pytest
from selenium import webdriver


def test_abs1():
    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_css_selector("[placeholder='Input your first name']")
    input1.send_keys("Вова")
    input2 = browser.find_element_by_css_selector("[placeholder='Input your last name']")
    input2.send_keys("Волков")
    input3 = browser.find_element_by_xpath("//*[@class='form-control third']")
    input3.send_keys("test@mail.ru")

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    welcome_text_elt = browser.find_element_by_tag_name("h1").text
    assert "Congratulations! You have successfully registered!" == welcome_text_elt
    browser.quit()


def test_abs2():
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_css_selector("[placeholder=['Input your first name']")
    input1.send_keys("Вова")
    input2 = browser.find_element_by_css_selector("[placeholder='Input your last name']")
    input2.send_keys("Волков")
    input3 = browser.find_element_by_xpath("//*[@class='form-control third']")
    input3.send_keys("test@mail.ru")

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    welcome_text_elt = browser.find_element_by_tag_name("h1").text
    assert "Congratulations! You have successfully registered!" == welcome_text_elt
    browser.quit()


if __name__ == "__main__":
    pytest.main()
