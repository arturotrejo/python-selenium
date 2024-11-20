from selenium.webdriver.common.by import By

from utils.check_actions import is_element_present


def test_driver_sign_up_with_invalid_phone_number(driver, cities_page):
    city_name = "San Francisco"
    invalid_phone_number = "999999999"
    first_name = "Arturo"
    last_name = "Trejo"
    email = "qa@lyft.com"

    # San Francisco screen locators
    phone_field = (By.XPATH, "//input[@data-testid='phone']")
    agree_to_terms_checkbox = "//input[@data-testid='core-ui-checkbox']"
    apply_to_driver_button = "//button//span[text()='Apply to drive']"

    #Sing-Up screen locators
    first_name_field = (By.CSS_SELECTOR, "[name='firstName']")
    last_name_field = "[name='lastName']"
    email_field = "[name='email']"
    invalid_phone_number_message = (By.XPATH, "//*[@data-testid='core-ui-text'][.='Error submitting form: Please enter a valid phone number.']")
    submit_button = "//button//span[text()='Submit']"

    cities_page.go_to_cities_page()
    cities_page.search_and_select_city(city_name)

    is_element_present(driver, phone_field)
    driver.find_element(*phone_field).send_keys(invalid_phone_number)
    driver.find_element(By.XPATH, agree_to_terms_checkbox).click()
    driver.find_element(By.XPATH, apply_to_driver_button).click()

    # Fill form
    is_element_present(driver, first_name_field)
    driver.find_element(*first_name_field).send_keys(first_name)
    driver.find_element(By.CSS_SELECTOR, last_name_field).send_keys(last_name)
    driver.find_element(By.CSS_SELECTOR, email_field).send_keys(email)
    driver.find_element(By.XPATH, submit_button).click()

    is_element_present(driver, invalid_phone_number_message)
    assert driver.find_element(*invalid_phone_number_message).is_displayed()

