from clients.base_client import BaseClient
from utils.client_helpers import get_auth_payload
from utils.paths import Account


class AccountClient(BaseClient):
    def __init__(self, base_url):
        api_url = base_url + Account.api_url
        super().__init__(api_url)


    def generate_login_cookies(self, user_name, password):
        payload = get_auth_payload(user_name, password)

        generate_token_response = self.request.post(Account.generate_token, payload)
        login_response = self.request.post(Account.login, payload)

        expires = generate_token_response.as_dict['expires'].replace(':', '%3A')
        token = login_response.as_dict['token']
        user_id = login_response.as_dict['userId']

        return expires, token, user_id
