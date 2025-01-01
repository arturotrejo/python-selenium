import os

import pytest

from pages.drive_with_lyft_page import DriveWithLyftPage
from pages.driver_cities_page import DriverCitiesPage
from pages.home_page import HomePage
from pages.sign_up_page import SignUpPage
from utils.webdriver_helpers import get_webdriver


@pytest.fixture(scope='session')
def config():
    configs = {
        'base_url': os.getenv('BASE_URL'),
        'browser': os.getenv('BROWSER')
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
def cities_page(driver):
    return DriverCitiesPage(driver)
def home_page(driver):
    return HomePage(driver)

@pytest.fixture()
def drive_with_lyft_page(driver):
    return DriveWithLyftPage(driver)
def sign_up_page(driver):
    return SignUpPage(driver)
