
import logging as logger
from ecomstore.src.utilities.wooAPIUtility import WooAPIUtility

class ProductsAPIHelper:

    def __init__(self):
        self.woo_api_utility = WooAPIUtility()

    def call_create_product(self, payload):
        return self.woo_api_utility.post('products', params=payload, expected_status_code=201)

    def call_list_product_by_id(self, product_id):
        return self.woo_api_utility.get(f"products/{product_id}")

    def call_list_products(self, payload):

        #if max number of products per page is not provided then use the max to reduce number of calls
        # if not payload:
        #     payload = {'per_page': 100}
        # elif 'per_page' not in payload.keys():
        #     payload['per_page'] = 100

        return self.woo_api_utility.get('products', params=payload, return_headers=True)
        # rs_api = self.woo_api_utility.get('products', params=payload, return_headers=True)
        # total_number_of_pages = rs_api['headers']['X-WP-TotalPages']

        # all_products = []
        # all_products.extend(rs_api['response_json']) # since the first page is fetched use that
        #
        # for i in range(2, int(total_number_of_pages) + 1): # start from 2 because this will be used for page number and page 1 is fetched already
        #
        #     logger.debug(f"List products page number: {i}")
        #
        #     payload['page'] = i
        #     rs_api = self.woo_api_utility.get('products', params=payload, return_headers=True)
        #     all_products.extend(rs_api['response_json'])
        #
        #     return all_products


