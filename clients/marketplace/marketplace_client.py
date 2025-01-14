from clients.base_client import BaseClient
from utils.paths import Products


class Marketplace(BaseClient):
    def __init__(self, base_url):
        api_url = base_url + Products.api_url
        super().__init__(api_url)


    def get_all_products(self):
        return self.request.get(Products.products_list)
