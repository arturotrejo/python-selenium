from requests import status_codes


def test_get_all_products(marketplace):
    response = marketplace.get_all_products()
    response.verify_status_code_is(status_codes.codes.ok)
    response.verify_is_not_empty('products')
