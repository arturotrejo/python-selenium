
def test_sign_up_with_existing_email(home_page, sign_up_page):
    existing_email = "a.trejog@hotmail.com"
    password = 'Monkey123'

    home_page.click_create_account_button()
    sign_up_page.create_account(existing_email, password)

def test_login_via_api(bookstore):
    bookstore_page, api = bookstore

    username = 'atrejog'
    password = 'TestingWithR3n@t@'

    expires, token, user_id = api.generate_login_cookies(username, password)
    bookstore_page.login_with_cookies(expires, token, user_id, username)
    bookstore_page.verify_login_is_successful()
