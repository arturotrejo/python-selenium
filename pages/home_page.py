from pages.base_page import BasePage
from utils.selenium_selectors import css


class HomePage(BasePage):
    NAVBAR_CREATE_ACCOUNT_BUTTON = css(".navbar-ctas a[href*='/registro']")

    def click_create_account_button(self):
        self.driver.find_element(*self.NAVBAR_CREATE_ACCOUNT_BUTTON).click()
