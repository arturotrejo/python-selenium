from selenium.webdriver import Keys

from pages.base_page import BasePage
from utils.check_actions import is_element_present
from utils.selenium_selectors import css, xpath


class HomePage(BasePage):
    CLOSE_SEARCH_ICON = css('[data-testid="Close-icon"]')
    MERCHANT_NAMES = xpath('//*[@id="merchants_table_header"]/following-sibling::*//div/p')
    MERCHANT_TAB = xpath('//div[text()="Comercios"]')
    NO_RESULTS_LABEL = xpath('//p[text()="No encontramos resultados para"]')
    RESULTS = css('#results-component img')
    RESULTS_FOR_LABEL = xpath('//p[contains(text(), "Resultados para")]')
    SEARCH_BAR = css('.searchbar-text-2024')
    SEARCH_PRODUCTS_BAR = css('input[placeholder="Busca productos o comercios"]')


    def search_item_from_home(self, item):
        self.wait_for_element_to_be_visible(self.SEARCH_BAR)
        self.send_keys(self.SEARCH_BAR, item + Keys.RETURN)


    def search_item_from_results(self, item):
        self.click_element_if_present(self.CLOSE_SEARCH_ICON)
        self.wait_for_element_to_be_visible(self.SEARCH_PRODUCTS_BAR)
        self.send_keys(self.SEARCH_PRODUCTS_BAR, item + Keys.RETURN)


    def switch_to_merchant_tab(self):
        self.wait_for_element_to_be_visible(self.MERCHANT_TAB)
        self.click(self.MERCHANT_TAB)


    def verify_results_are_listed(self, searched_item = None):
        if searched_item:
            self.wait_for_element_to_have_text(self.RESULTS_FOR_LABEL, searched_item)
        else:
            self.wait_for_element_to_be_visible(self.RESULTS)

        results = self.get_elements(self.RESULTS)
        assert len(results) >= 1


    def verify_no_results_are_found(self):
        assert is_element_present(self.driver, self.NO_RESULTS_LABEL)


    def verify_merchant_is_listed(self, expected_merchant_name):
        self.switch_to_merchant_tab()
        self.wait_for_element_to_be_visible(self.MERCHANT_NAMES)

        actual_merchants = self.get_elements(self.MERCHANT_NAMES)
        actual_merchants_names = {merchant.text.lower() for merchant in actual_merchants}

        assert expected_merchant_name in actual_merchants_names
