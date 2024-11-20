from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class DriverCitiesPage(BasePage):
    CITIES_FOOTER_BUTTON = (By.XPATH, "//h2[text()='DRIVER']//ancestor::div/ul//span[@data-testid='core-ui-text'][.='Cities']")
    SEARCH_FIELD = (By.XPATH, "//input[@data-testid='SearchInput']")
    FIRST_SEARCH_OPTION = (By.XPATH, "//ul[@role='listbox']/li[@role='option']//span")

    def go_to_cities_page(self):
        self.driver.find_element(*self.CITIES_FOOTER_BUTTON).click()

    def search_and_select_city(self, city_name):
        self.type_text(self.SEARCH_FIELD, city_name)
        self.driver.find_element(*self.FIRST_SEARCH_OPTION).click()
