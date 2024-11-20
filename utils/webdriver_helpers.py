from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager


def get_webdriver(browser):
    """
    :param browser:
    :return: webdriver of the selected browser
    """
    driver_map = {
        'chrome': get_chrome_driver,
        'edge': get_edge_driver,
        'firefox': get_firefox_driver
    }
    return driver_map.get(browser, get_chrome_driver)()

def get_chrome_driver():
    chrome_options = ChromeOptions()
    chrome_options.add_argument("--ignore-certificate-errors")

    chrome_driver = webdriver.Chrome(
        service = ChromeService(ChromeDriverManager().install()),
        options = chrome_options
    )
    return chrome_driver

def get_edge_driver():
    edge_options = EdgeOptions()
    edge_options.add_argument("--ignore-certificate-errors")

    edge_driver = webdriver.Edge(
        service = EdgeService(EdgeChromiumDriverManager().install()),
        options = edge_options
    )
    return edge_driver

def get_firefox_driver():
    firefox_options = FirefoxOptions()
    firefox_options.accept_insecure_certs = True

    firefox_driver = webdriver.Firefox(
        service = FirefoxService(GeckoDriverManager().install()),
        options = firefox_options
    )
    return firefox_driver
