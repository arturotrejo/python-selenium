from time import sleep

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from utils.check_actions import is_element_present
from utils.enums import WaitTimes


class BasePage:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def reload_page(self):
        self.driver.refresh()

    def wait_for_element_to_be_visible(self, element, timeout: WaitTimes = WaitTimes.WEB_ELEMENT_TIMEOUT):
        WebDriverWait(self.driver, timeout.value).until(expected_conditions.visibility_of_element_located(element))

    def wait_for_element_to_have_text(self, element, text, timeout: WaitTimes = WaitTimes.WEB_ELEMENT_TIMEOUT):
        WebDriverWait(self.driver, timeout.value).until(expected_conditions.text_to_be_present_in_element(element, text))

    def type_text(self, element, text):
        for char in text:
            self.send_keys(element, char)
            sleep(.05)

    def click_element_if_present(self, element):
        if is_element_present(self.driver, element, WaitTimes.SHORT_TIMEOUT):
            self.click(element)

    def click(self, element):
        self.driver.find_element(*element).click()

    def send_keys(self, element, text):
        self.driver.find_element(*element).send_keys(text)

    def get_elements(self, element):
        return self.driver.find_elements(*element)
