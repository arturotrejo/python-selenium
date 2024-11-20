from pages.base_page import BasePage
from utils.check_actions import is_element_present
from utils.enums import Button, Messages
from utils.selenium_selectors import css, xpath, generic_button


class DriveWithLyftPage(BasePage):
    FIRST_NAME_FIELD = css("[name='firstName']")
    LAST_NAME_FIELD = css("[name='lastName']")
    EMAIL_FIELD = css("[name='email']")
    INVALID_PHONE_NUMBER_MESSAGE = xpath(f"//*[@data-testid='core-ui-text'][.='{Messages.INVALID_PHONE_NUMBER_MESSAGE}']")
    SUBMIT_BUTTON = generic_button(Button.SUBMIT)

    def apply_to_drive(self, first_name, last_name, email):
        self.wait_for_element_to_be_visible(self.FIRST_NAME_FIELD)
        self.driver.find_element(*self.FIRST_NAME_FIELD).send_keys(first_name)
        self.driver.find_element(*self.LAST_NAME_FIELD).send_keys(last_name)
        self.driver.find_element(*self.EMAIL_FIELD).send_keys(email)
        self.driver.find_element(*self.SUBMIT_BUTTON).click()

    def verify_invalid_phone_number_message_is_displayed(self):
        assert is_element_present(self.driver, self.INVALID_PHONE_NUMBER_MESSAGE)