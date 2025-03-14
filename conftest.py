import os
from random import choices

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options #Options нужен для кастомного брауера
from selene import Browser, Config
from dotenv import load_dotenv #наверное нужно для вытягивания секретов из jenkins

from utils import attach


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


@pytest.fixture(scope='function')
def setup_browser(request):
    #browser_name = request.config.getoption('--browser')
    browser_version = request.config.getoption('--browser_version')
    browser_version = browser_version if browser_version != "" else DEFAULT_BROWSER_VERSION #это защитит от того, что не заполнили параметр

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
    browser = Browser(Config(driver=driver))

    yield browser #фикстура возвращает браузер

    # если код упадет, attach сработает
    attach.add_logs(browser)
    attach.add_html(browser)
    attach.add_video(browser)
    attach.add_screenshot(browser)

    browser.quit()
