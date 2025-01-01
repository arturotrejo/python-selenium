
def test_driver_sign_up_with_invalid_phone_number(driver, cities_page, drive_with_lyft_page):
    city_name = "San Francisco"
    invalid_phone_number = "999999999"
    first_name = "Arturo"
    last_name = "Trejo"
    email = "qa@lyft.com"

    cities_page.go_to_cities_page()
    cities_page.search_and_select_city(city_name)
    cities_page.enter_phone_number_and_apply(invalid_phone_number)
    drive_with_lyft_page.apply_to_drive(first_name, last_name, email)
    drive_with_lyft_page.verify_invalid_phone_number_message_is_displayed()
def test_sign_up_with_existing_email(home_page, sign_up_page):
    existing_email = "a.trejog@hotmail.com"
    password = 'Monkey123'

    home_page.click_create_account_button()
    sign_up_page.create_account(existing_email, password)
