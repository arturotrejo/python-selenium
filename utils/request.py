import requests

from utils.response import Response


class APIRequest:
    def get(self, url, headers, data = None, json = None):
        response = requests.get(url, headers=headers, data=data, json=json)
        response.raise_for_status()
        return self.__process_response(response)


    def post(self, url, headers, data = None, json = None):
        response = requests.post(url, headers=headers, data=data, json=json)
        response.raise_for_status()
        return self.__process_response(response)


    @staticmethod
    def __process_response(response):
        headers = response.headers
        status_code = response.status_code
        as_dict = response.json()

        return Response(headers, status_code, as_dict)
