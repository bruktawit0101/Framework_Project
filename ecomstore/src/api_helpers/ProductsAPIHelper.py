
from ecomstore.src.utilities.wooAPIUtility import WooAPIUtility

class ProductsAPIHelper:

    def __init__(self):
        self.woo_api_utility = WooAPIUtility()

    def call_create_product(self, payload):
        return self.woo_api_utility.post('products', params=payload, expected_status_code=201)

