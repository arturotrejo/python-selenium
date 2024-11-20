from pages.base_page import BasePage
from utils.enums import Button
from utils.selenium_selectors import xpath, css, generic_button


class DriverCitiesPage(BasePage):
    CITIES_FOOTER_BUTTON = css("[aria-label='Footer links'] a[href='/driver/cities']")
    SEARCH_FIELD = xpath("//input[@data-testid='SearchInput']")
    SEARCH_OPTION = xpath("//ul[@role='listbox']/li[@role='option']")
    PHONE_FIELD = xpath("//input[@data-testid='phone']")
    AGREE_TO_TERMS_CHECKBOX = css("input[name='tos']")
    APPLY_TO_DRIVER_BUTTON = generic_button(Button.APPLY_TO_DRIVE)

    def go_to_cities_page(self):
        self.driver.find_element(*self.CITIES_FOOTER_BUTTON).click()

    def search_and_select_city(self, city_name):
        city_option = xpath(f"//*[contains(text(), '{city_name}')]")
        self.type_text(self.SEARCH_FIELD, city_name)
        self.driver.find_element(*self.SEARCH_OPTION).find_element(*city_option).click()

    def enter_phone_number_and_apply(self, phone_number):
        self.wait_for_element_to_be_visible(self.PHONE_FIELD)
        self.driver.find_element(*self.PHONE_FIELD).send_keys(phone_number)
        self.driver.find_element(*self.AGREE_TO_TERMS_CHECKBOX).click()
        self.driver.find_element(*self.APPLY_TO_DRIVER_BUTTON).click()
