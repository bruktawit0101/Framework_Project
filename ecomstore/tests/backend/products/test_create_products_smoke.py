
import pytest
from ecomstore.src.utilities.genericUtility import generate_random_string
from ecomstore.src.api_helpers.ProductsAPIHelper import ProductsAPIHelper
from ecomstore.src.dao.products_deo import ProductsDao

pytestmark = [pytest.mark.products, pytest.mark.smoke, pytest.mark.BE]

@pytest.mark.tcid26
@pytest.mark.qactcid10
def test_create_1_simple_product():

    # generate some data
    payload = dict()
    payload['name'] = generate_random_string(20)
    payload['type'] = 'simple'
    payload['regular_price'] = '10.99'

    # make a call
    products_rs = ProductsAPIHelper().call_create_product(payload)

    # verify the response is not empty
    assert products_rs, f"Create product api response is empty. payload: {payload}"
    assert products_rs['name'] == payload['name'], f"Create product api call response has" \
                                                   f"unexpected name. Expected: {payload['name']}, Actual: {products_rs['name']}"
    # verify the product exists in db
    product_id = products_rs['id']
    db_product = ProductsDao().get_product_by_id(product_id)

    assert payload['name'] == db_product[0]['post_title'], f"Create product, title in db does not match" \
                                                           f"title in api. DB: {db_product(0)['post_title']}, API: {payload['name']}"





