
from ecomstore.src.utilities.wooAPIUtility import WooAPIUtility
from ecomstore.src.utilities.genericUtility import generate_random_email_and_password

class CustomersAPIHelper:

    def __init__(self):
        self.woo_api_utility = WooAPIUtility()

    def call_create_customers(self, email=None, password=None, expected_status_code=201, **kwargs):

        if not email:
            ep = generate_random_email_and_password()
            email = ep['email']
        if not password:
            password = 'password1'

        payload = dict()
        payload['email'] = email
        payload['password'] = password
        payload.update(kwargs)

        create_user_json = self.woo_api_utility.post('customers', params=payload, expected_status_code=expected_status_code)
        return create_user_json
