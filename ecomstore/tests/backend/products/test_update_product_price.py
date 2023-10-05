import random
import pytest
from ecomstore.src.dao.products_deo import ProductsDao
from ecomstore.src.api_helpers.ProductsAPIHelper import ProductsAPIHelper

pytestmark = [pytest.mark.products, pytest.mark.beregression]

@pytest.mark.tcid61
@pytest.mark.qatcid13

def test_update_regular_price_should_update_price():
    """
    Verifies updating the 'regular_price' field should automatically update the 'price' field.
    :return:
    """
    # create helper objects and get random product from db
    product_helper = ProductsAPIHelper()
    product_db = ProductsDao()
    filters = {'on_sale': False, 'per_page': 100}
    random_products = product_helper.call_list_products(filters)

    if random_products:
        selected_products = random.choice(random_products)
        product_id = selected_products['id']

    else:
        random_products = product_helper.call_list_products()
        selected_products = random.choice(random_products)
        product_id = selected_products['id']
        product_helper.call_update_product(product_id, {'sale_price': ''})


   # make the update to 'regular_price'

    new_price = str(random.randint(10, 100))+ '.' + str(random.randint(10, 99))
    payload = dict()
    payload['regular_price'] = new_price

    rs_update = product_helper.call_update_product(product_id, payload=payload)

    # verify the response has the 'price' and 'regular_price' has updated and 'sale_price' is not updated
    assert rs_update['price'] == new_price, f"Update product api call response. Updating the 'regular_price' did not " \
                                            f"update the 'price' field. price field actual value {rs_update['price']}," \
                                            f"but expected: {new_price}"

    assert rs_update[
               'regular_price'] == new_price, f"Update product api call response. Updating the 'regular_price' did not " \
                                              f"update in the response. Actual response 'regular_price'={rs_update['price']}," \
                                              f"but expected: {new_price}"

    rs_product = product_helper.call_retrieve_product(product_id)

    assert rs_product['price'] == new_price, f"Update product api call response. Updating the 'regular_price' did not " \
                                    f"Update the 'price' field. Price field actual value {rs_product['price']}, "\
                                    f"but expected: {new_price}"
    assert rs_update['regular_price'] == new_price,f"Update product api call response. Updating the 'regular_price' did not " \
                                    f"Update. Actual 'regular_price'= {rs_product['price']}, "\
                                    f"but expected: {new_price}"