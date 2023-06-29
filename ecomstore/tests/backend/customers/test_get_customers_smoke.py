
import pytest
from ecomstore.src.api_helpers.CustomersAPIHelper import CustomersAPIHelper

pytestmarks = [pytest.mark.regression, pytest.mark.besmoke, pytest.mark.customers]

@pytest.mark.besmoke
@pytest.mark.tcid30
@pytest.mark.qactcid9
def test_get_all_customers():
    """
    Alternate tc name:
        Test getting all customers with API and verify the response is not empty
    :return:
    """

    customers_helper = CustomersAPIHelper()
    rs_api = customers_helper.call_create_customers()

    assert rs_api, f"Response of list all customers is empty."



