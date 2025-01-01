from utils.request import APIRequest


class BaseClient:
    def __init__(self):

        self.request = APIRequest()

        self.headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }
