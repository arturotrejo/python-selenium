from clients.base_client import BaseClient


class AccountClient(BaseClient):
    def __init__(self, bookstore_url):
        super().__init__()
        self.account_url = f'{bookstore_url}/Account/v1'

    def generate_login_cookies(self, user_name, password):
        generate_token_url = f'{self.account_url}/GenerateToken'
        login_url = f'{self.account_url}/Login'

        payload = {'userName': user_name, 'password': password}

        generate_token_response = self.request.post(generate_token_url, json=payload, headers=self.headers)
        login_response = self.request.post(login_url, json=payload, headers=self.headers)

        expires = generate_token_response.as_dict['expires'].replace(':', '%3A')
        token = login_response.as_dict['token']
        user_id = login_response.as_dict['userId']

        return expires, token, user_id
