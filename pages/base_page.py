from selenium.common import NoSuchElementException
from selenium.webdriver.remote.webdriver import WebDriver
from time import sleep

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from utils.enums import WaitTimes


class BasePage:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def reload_page(self):
        self.driver.refresh()

    def wait_for_element_to_be_visible(self, element, timeout: WaitTimes = WaitTimes.WEB_ELEMENT_TIMEOUT):
        WebDriverWait(self.driver, timeout.value).until(expected_conditions.presence_of_element_located(element))

    def type_text(self, element, text):
        for char in text:
            self.driver.find_element(*element).send_keys(char)
            sleep(.05)
