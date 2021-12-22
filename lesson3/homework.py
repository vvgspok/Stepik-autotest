from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
import time
import math
from selenium import webdriver

@pytest.fixture(scope="function")
def browser():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()

@pytest.mark.parametrize('link', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
class TestLogin:
    def test_guest_should_see_login_link(self, browser, link):
        link = f"https://stepik.org/lesson/{link}/step/1"
        browser.get(link)
        browser.implicitly_wait(10)
        input_pole = browser.find_element_by_xpath("//*[@class='ember-text-area ember-view textarea string-quiz__textarea']")
        answer = math.log(int(time.time()))
        input_pole.send_keys(str(answer))
        button = WebDriverWait(browser, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@class='submit-submission']"))
        )
        button.click()
        cor = browser.find_element_by_xpath("//*[@class='smart-hints__hint']")
        cor_text = cor.text
        assert "Correct!" == cor_text

#pytest -s -v homework.py