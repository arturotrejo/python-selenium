
def set_up_session_cookies(driver, expires_value, token_value, user_id_value, user_name):
    cookies = [
        {'name': 'expires', 'value': expires_value, 'path': '/', 'secure': True},
        {'name': 'token', 'value': token_value, 'path': '/', 'secure': True},
        {'name': 'userID', 'value': user_id_value, 'path': '/', 'secure': True},
        {'name': 'userName', 'value': user_name, 'path': '/', 'secure': True}
    ]

    for cookie in cookies:
        driver.add_cookie(cookie)
