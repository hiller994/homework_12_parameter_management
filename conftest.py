import os
from random import choices

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options #Options нужен для кастомного брауера
from selene import Browser, Config
from dotenv import load_dotenv #наверное нужно для вытягивания секретов из jenkins

from utils import attach


#параметризация
#до всех фикстур используем python hook
#и мы используем hook, который добавляет опции

#Вид бразуера
'''
def pytest_addoption(parser):
    parser.addoption( #через парсер зачитываем наши опции
        '--browser', #выбор браузера
        help='Браузер, в котором будут запущены тесты', #если мы не заполнил или неправильно, это нам подскажет
        choices=['firefox', 'chrome'], #какие браузеры
        default='chrome' #по дефолту
    )
'''

#Версия браузера

DEFAULT_BROWSER_VERSION = "100.0" #константа для дефолтной версии браузера


def pytest_addoption(parser):
    parser.addoption( #через парсер зачитываем наши опции
        '--browser_version', #выбор версии браузера
        default='100.0' #по дефолту
    )

#нужна для секретных данных
@pytest.fixture(scope='session', autouse=True)
def load_env():
    load_dotenv() #помещает переменные в окружение и мы их зачитываем в os.getenv


@pytest.fixture(scope='function') #autouse=True нужен, чтобы не указывать руками фикстуру в тестах
def setup_browser(request):
    #browser_name = request.config.getoption('--browser')
    browser_version = request.config.getoption('--browser_version')
    browser_version = browser_version if browser_version != "" else DEFAULT_BROWSER_VERSION #это защитит от того, что не заполнили параметр

    #driver_options = webdriver.ChromeOptions()
    # driver_options.add_argument('--headless')  #скрыть браузер
    #driver_options.page_load_strategy = 'eager'
    #browser.config.driver_options = driver_options  # сам запуск|
    #browser.config.window_height = 1920  # высота браузера
    #browser.config.window_width = 1080  # ширина браузера
    #browser.config.base_url = 'https://demoqa.com'

    #запуск браузер селеноид
    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome", # browser_name вместо хрома
        "browserVersion": browser_version, #вместо "100.0"
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }


    options.capabilities.update(selenoid_capabilities)


    login = os.getenv('LOGIN') #os забирает перенные из окружен
    password = os.getenv('PASSWORD')
    driver = webdriver.Remote(
        command_executor=f"https://{login}:{password}@selenoid.autotests.cloud/wd/hub",
        options=options
    )
    browser = Browser(Config(driver=driver)) #мы создаем свой объект браузера. В классе браузера передаем конструктор Config, в конструктор Config передаем наш driver
    #browser.config.driver = driver

    yield browser #фикстура возвращает браузер

    # если код упадет, attach сработает
    attach.add_logs(browser)
    attach.add_html(browser)
    attach.add_video(browser)
    attach.add_screenshot(browser)

    browser.quit()
'''
    options = Options()
    selenoid_capabilities = {
        "browserName": "opera",
        #"browserVersion": "100.0",
        "browserVersion": "106.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }
    options.capabilities.update(selenoid_capabilities)
    driver = webdriver.Remote(
        command_executor=f"https://user1:1234@selenoid.autotests.cloud/wd/hub",
        options=options
    )

    browser = Browser(Config(driver))
    yield browser

    browser.quit()
'''