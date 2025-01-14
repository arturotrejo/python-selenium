import pytest
from jsonschema.exceptions import ValidationError
from requests import codes
from jsonschema import validate


def test_get_all_products(marketplace):
    response = marketplace.get_all_products()
    response.verify_status_code_is(codes.ok)
    response.verify_is_not_empty('products')

def test_products_list_contains_latest_product(marketplace):
    latest_product = 'Cotton Mull Embroidered Dress'
    response = marketplace.get_all_products()
    products = response.get_content('products')
    expected_product = [product for product in products if product['id'] == 20]

    assert len(expected_product) == 1
    assert expected_product[0]['name'] == latest_product

def test_product_schema_is_valid(marketplace):
    product_schema = {
        "type": "object",
        "properties": {
            "id": {"type": "integer"},
            "name": {"type": "string"},
            "price": {"type": "string"},
            "brand": {"type": "string"},
            "category": {
                "type": "object",
                "properties": {
                    "usertype": {
                        "type": "object",
                        "properties": {
                            "usertype": {"type": "string"}
                        },
                        "required": ["usertype"]
                    },
                    "category": {"type": "string"}
                },
                "required": ["usertype", "category"]
            }
        },
        "required": ["id", "name", "price", "brand", "category"]
    }

    response = marketplace.get_all_products()
    products = response.get_content('products')
    for product in products:
        try:
            validate(instance=product, schema=product_schema)
        except ValidationError as e:
            pytest.fail(f'Product {product['id']} did not pass validation: {e}')
