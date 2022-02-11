import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from pages.authorization.authorization_functions import AuthorizationFunctions,AuthorizationLocators
#from pages.base_page import BasePage


@pytest.fixture(scope = "session", autouse="True")
def prepare(request,platform,username,password,system_name):
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    browser = webdriver.Chrome(chrome_options=options)
    if platform == "RC":
        common_address = "http://rc.alfa-doc.ru/"
        autorization_service_address = "https://id.npc-ksb.ru/"
        mail_service_address = "https://mail.npc-ksb.ru/"
    if platform == "CI":
        common_address = "http://alfadoc.dev.ksb.local/"
        autorization_service_address = "http://id.dev.ksb.local"
        mail_service_address = "http://postman.dev.ksb.local/"

    browser.get(common_address)
    browser.find_element(*AuthorizationLocators.ENTER_BTN).click()
    browser.find_element(*AuthorizationLocators.SERVICE_AUTH).click()

    try:
        while True:
            browser.find_element(By.CSS_SELECTOR, ".loading")
            time.sleep(0.5)
    except:
        pass

    try:
        while True:
            browser.find_element(By.CSS_SELECTOR, ".loading")
            time.sleep(0.5)
    except:
        pass

    try:
        browser.find_element(*AuthorizationLocators.LOGIN_INPUT).send_keys(username)
    except:
        assert False, "Поле ввода логина недоступно или отсутствует"
    try:
        browser.find_element(*AuthorizationLocators.PASSWORD_INPUT).send_keys(password)
    except:
        assert False, "Поле ввода пароля недоступно или отсутствует"

    try:
        browser.find_element(*AuthorizationLocators.LOGIN_SUBMIT).click()
    except:
        assert False, "Команда авторизации недоступна или отсутствует"
    try:
        while True:
            browser.find_element(By.CSS_SELECTOR, ".loading")
            time.sleep(0.5)
    except:
        pass



    session = request.node
    for item in session.items:
        cls = item.getparent(pytest.Class)
        setattr(cls.obj,"browser",browser)
        setattr(cls.obj,"common_address",common_address)
        setattr(cls.obj,"autorization_service_address",autorization_service_address)
        setattr(cls.obj,"mail_service_address",mail_service_address)
        setattr(cls.obj,"username",username)
        setattr(cls.obj,"password",password)
        setattr(cls.obj,"system_name",system_name)

    yield
    browser.close()

def pytest_addoption(parser):
    """Declaring the command-line options for test run"""
    parser.addoption('--platform',
                     default='RC',
                     help='host options: "staging", "production", or your own host for local testing')
    parser.addoption('--username',
                         # default='user_without_manager')
                         default='vvgspok')
    parser.addoption('--password',
                         default='jkl28mn170797')
                         # default='user_without_manager')
    parser.addoption('--system_name',
                     default='Информационная система «Обращения граждан»')

@pytest.fixture(scope = "session")
def platform(request):
    platform = request.config.getoption('--platform')
    yield platform

@pytest.fixture(scope = "session")
def username(request):
    username = request.config.getoption('--username')
    yield username

@pytest.fixture(scope = "session")
def password(request):
    password = request.config.getoption('--password')
    yield password

@pytest.fixture(scope = "session")
def system_name(request):
    system_name = request.config.getoption('--system_name')
    yield system_name