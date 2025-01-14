import requests

from utils.response import Response


class APIRequest:
    def __init__(self, api_url, headers):
        self.api_url = api_url
        self.base_headers = headers


    def get(self, path, json=None, data=None, headers=None):
        url = self.api_url + path
        request_headers = headers or self.base_headers

        response = requests.get(url, headers=request_headers, data=data, json=json)
        response.raise_for_status()

        return self.__process_response(response)


    def post(self, path, json=None, data=None, headers=None):
        url = self.api_url + path
        request_headers = headers or self.base_headers

        response = requests.post(url, headers=request_headers, data=data, json=json)
        response.raise_for_status()

        return self.__process_response(response)


    @staticmethod
    def __process_response(response):
        headers = response.headers
        status_code = response.status_code
        as_dict = response.json()

        return Response(headers, status_code, as_dict)
