from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class DriverCitiesPage(BasePage):
    CITIES_FOOTER_BUTTON = (By.CSS_SELECTOR, "[aria-label='Footer links'] a[href='/driver/cities']")
    SEARCH_FIELD = (By.XPATH, "//input[@data-testid='SearchInput']")
    SEARCH_OPTION = (By.XPATH, "//ul[@role='listbox']/li[@role='option']")
    PHONE_FIELD = (By.XPATH, "//input[@data-testid='phone']")
    AGREE_TO_TERMS_CHECKBOX = (By.CSS_SELECTOR, "input[name='tos']")
    APPLY_TO_DRIVER_BUTTON = (By.XPATH, "//button//span[text()='Apply to drive']")

    def go_to_cities_page(self):
        self.driver.find_element(*self.CITIES_FOOTER_BUTTON).click()

    def search_and_select_city(self, city_name):
        city_option = (By.XPATH, f"//*[contains(text(), '{city_name}')]")
        self.type_text(self.SEARCH_FIELD, city_name)
        self.driver.find_element(*self.SEARCH_OPTION).find_element(*city_option).click()

    def enter_phone_number_and_apply(self, phone_number):
        self.wait_for_element_to_be_visible(self.PHONE_FIELD)
        self.driver.find_element(*self.PHONE_FIELD).send_keys(phone_number)
        self.driver.find_element(*self.AGREE_TO_TERMS_CHECKBOX).click()
        self.driver.find_element(*self.APPLY_TO_DRIVER_BUTTON).click()
