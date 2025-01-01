from pages.base_page import BasePage
from utils.check_actions import is_element_present
from utils.enums import Messages
from utils.selenium_selectors import css, xpath


class SignUpPage(BasePage):
    EMAIL_FIELD = css("[name='email']")
    PASSWORD_FIELD = css("[name='password']")
    SIGN_UP_BUTTON = css("#buttonRegistroId")
    INVALID_PHONE_NUMBER_MESSAGE = xpath(f"//*[@data-testid='core-ui-text'][.='{Messages.INVALID_PHONE_NUMBER_MESSAGE}']")

    def create_account(self, email, password):
        self.wait_for_element_to_be_visible(self.EMAIL_FIELD)
        self.driver.find_element(*self.EMAIL_FIELD).send_keys(email)
        self.driver.find_element(*self.PASSWORD_FIELD).send_keys(password)
        self.driver.find_element(*self.SIGN_UP_BUTTON).click()

    def verify_invalid_phone_number_message_is_displayed(self):
        assert is_element_present(self.driver, self.INVALID_PHONE_NUMBER_MESSAGE)