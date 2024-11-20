from selenium.common import TimeoutException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from utils.enums import WaitTimes

def is_element_present(driver, element, timeout: WaitTimes = WaitTimes.WEB_ELEMENT_TIMEOUT):
    try:
        WebDriverWait(driver, timeout.value).until(expected_conditions.presence_of_element_located(element))
        return True
    except TimeoutException:
        return False