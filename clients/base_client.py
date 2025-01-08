from utils.request import APIRequest


class BaseClient:
    def __init__(self, base_url):

        self.base_headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }

        self.request = APIRequest(base_url, self.base_headers)
