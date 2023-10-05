from ecomstore.src.dao.products_deo import ProductsDao
from ecomstore.src.api_helpers.ProductsAPIHelper import ProductsAPIHelper
import pytest
import logging as logger

<<<<<<< HEAD
pytestmarks = [pytest.mark.regression, pytest.mark.beregression, pytest.mark.besmoke, pytest.mark.customers]
=======
pytestmark = [pytest.mark.products, pytest.mark.smoke, pytest.mark.beregression]
>>>>>>> fb3a5983d89754f1c31ab3174a634ddfdbbf94b1

@pytest.mark.tcid25
@pytest.mark.qactcid11
def test_get_product_by_id():

    # get product that exist from db

    product_deo = ProductsDao()
    random_product = product_deo.get_random_products_from_db()
    product_id = random_product[0]['ID']
    product_name = random_product[0]['post_name']
    product_title = random_product[0]['post_title']

    logger.info(f"Test product id: {product_id}")

    # make product call with api
    product_helper = ProductsAPIHelper()
    rs_api = product_helper.call_list_product_by_id(product_id)


    # verify
    assert rs_api['id'] == product_id, f"Get product call. Id in request doesn't much id in response"
    assert rs_api['slug'] == product_name, f"rs_api post "
    assert rs_api['name'] == product_title, f"{product_title}doesn't mach the actual"
