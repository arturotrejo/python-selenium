from selenium.webdriver.common.by import By


def xpath(selector: str):
    return By.XPATH, selector

def css(selector: str):
    return By.CSS_SELECTOR, selector
