from pages.base_page import BasePage
from utils.check_actions import is_element_present
from utils.selenium_selectors import css
from utils.session_helpers import set_up_session_cookies


class BookstorePage(BasePage):
    LOGGED_IN_MESSAGE = css('#loading-label')

    def login_with_cookies(self, expires, token, user_id, username):
        set_up_session_cookies(self.driver, expires, token, user_id, username)

    def verify_login_is_successful(self):
        self.reload_page()
        assert is_element_present(self.driver, self.LOGGED_IN_MESSAGE)
