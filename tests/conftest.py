import os

import pytest

from clients.account_client import AccountClient
from pages.demoqa.bookstore_page import BookstorePage
from pages.home_page import HomePage
from pages.sign_up_page import SignUpPage
from utils.webdriver_helpers import get_webdriver


@pytest.fixture(scope='session')
def config():
    configs = {
        'base_url': os.getenv('BASE_URL'),
        'bookstore_url': os.getenv('BOOKSTORE_URL'),
        'browser': os.getenv('BROWSER'),
        'marketplace_url': os.getenv('MARKETPLACE_URL'),
    }
    return configs

@pytest.fixture()
def driver(config):
    driver = get_webdriver(config['browser'])
    driver.maximize_window()
    driver.get(config['base_url'])
    yield driver
    driver.quit()

@pytest.fixture()
def home_page(driver):
    return HomePage(driver)

@pytest.fixture()
def sign_up_page(driver):
    return SignUpPage(driver)

@pytest.fixture()
def bookstore(driver, config):
    page = BookstorePage(driver)
    page.driver.get(f'{config['bookstore_url']}/login')
    return page, AccountClient(config['bookstore_url'])
