
import pytest
from ecomstore.src.api_helpers.CustomersAPIHelper import CustomersAPIHelper

@pytest.mark.customers
@pytest.mark.tcid30
@pytest.mark.qactcid9
def test_get_all_customers():

    customers_helper = CustomersAPIHelper()
    rs_api = customers_helper.call_create_customers()

    assert rs_api, f"Response of list all customers is empty."



