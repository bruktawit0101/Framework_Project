from ecomstore.src.configs.MainConfigs import MainConfigs
from ecomstore.src.utilities.credentialUtility import CredentialUtility
from woocommerce import API
import logging as logger

class WooAPIUtility:
    def __init__(self):

        wc_creds = CredentialUtility.get_woo_api_keys()

        self.base_url = MainConfigs.get_base_url()

        self.wcapi = API(
            url=self.base_url,
            consumer_key=wc_creds["woo_key"],
            consumer_secret=wc_creds["wc_secret"],
            version="wc/v3"
        )

    def assert_status_code(self):
        assert self.status_code == self.expected_status_code, f"if bad status code."\
          f"Expected {self.expected_status_code}, Actual status code: {self.status_code},"\
          f"URL: {self.url}, Response Json: {self.rs_json}"

    def post(self, wc_endpoint, params=None, expected_status_code=200):

        rs_api = self.wcapi.post(wc_endpoint, data=params)


        self.status_code = rs_api.status_code
        self.expected_status_code = expected_status_code
        self.rs_json = rs_api.json()
        self.endpoint = wc_endpoint
        self.url = rs_api.url
        self.assert_status_code()

        logger.debug(f"POST API response: {self.rs_json}")

        return self.rs_json






