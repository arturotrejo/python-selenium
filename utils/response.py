from dataclasses import dataclass


@dataclass
class Response:
    headers: dict
    status_code: int
    as_dict: object

    def verify_status_code_is(self, status_code):
        assert self.status_code == status_code, f'Status Code is {self.status_code} when it was expected {status_code}'


    def verify_is_not_empty(self, key = None):
        response = self.as_dict[key] if key else self.as_dict
        assert len(response) > 0, 'Response is empty'


    def get_content(self, key):
        return self.as_dict[key]