import time
import urllib.request
import allure
import requests
from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from .main_settings import Global_Profile, MAIN_URL


def f_logging(driver, tariff):
    try:
        driver.get(MAIN_URL)
        driver.find_element_by_link_text("Войти").click();
        # print(step, ") С лендинга нажали на 'Войти");step += 1
        driver.find_element_by_link_text("Войти через сервис авторизации Charon").click()
        # print(step, ") Нажали на Войти через сервис авторизации");step += 1

        login, password = Global_Profile(tariff)

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "id_password")))
        time.sleep(0.5)
        driver.find_element_by_id("id_username").send_keys(login)

        time.sleep(0.5)

        driver.find_element_by_id("id_password").send_keys(password)
        time.sleep(0.5)
        # print(step,") Ввели логин и пароль");step += 1
        driver.find_element_by_class_name("btn").click()
        # print(step,") Нажали на кнопку 'Войти'");step += 1
        # print("+++++Yes Connect =)\t")
        time.sleep(0.5)

    except Exception as err:
        print(err, "\n")
    finally:
        return driver


def get_alfadoc_cookies(USERNAME, PASSWORD):
    """
    Авторизация через запрос и получение Cookie (для использования в браузере)
    """
    LOGIN_URL = "https://id.npc-ksb.ru/account/login/"
    if MAIN_URL == "https://alfa-doc.ru/":
        ENDPOINT_URL = 'http://alfa-doc.ru/accounts/oidc/authenticate/'
    elif MAIN_URL == "http://rc.alfa-doc.ru/":
        ENDPOINT_URL = 'http://rc.alfa-doc.ru/accounts/oidc/authenticate/'
    else:
        print("MAIN_URL не задан в условии")
        exit(1)

    client = requests.session()
    client.get(LOGIN_URL)

    login_data = {'username': USERNAME, 'password': PASSWORD, 'Button': 'login'}
    headers = {
        'Host': 'id.npc-ksb.ru',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/87.0.4280.141 Safari/537.36',
        # 'Origin': 'https://id.npc-ksb.ru',
        # 'Referer': 'https://id.npc-ksb.ru/account/login/',
    }

    r1 = client.post(LOGIN_URL, data=login_data, headers=headers)
    client.get(ENDPOINT_URL)

    return client.cookies.items()


def проверка_ссылки(link):
    """
    Проверка ссылки на код состояния (=200?)
    """
    # zapros = urllib.request.urlopen(link).getcode()
    # assert zapros == 200, f"Запрос вернул код {zapros} \n {link}"


def screen_allure(browser, step_name):
    """
    Добавление скриншота страницы в allure
    1) драйвер 2) придуманное название шага для скрина
    """
    with allure.step(step_name):
        allure.attach(browser.get_screenshot_as_png(),
                      name='screenshot',
                      attachment_type=AttachmentType.PNG)


def завершение_теста(self):
    self.browser.close()
    self.browser.quit()
