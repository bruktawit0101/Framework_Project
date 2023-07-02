
from ecomstore.src.dao.products_deo import ProductsDao
from ecomstore.src.api_helpers.ProductsAPIHelper import ProductsAPIHelper
import pytest
from datetime import datetime, timedelta


@pytest.mark.regression
class TestListProductsWithFilter(object):

    @pytest.mark.tcid51
    @pytest.mark.qactcid12
    def test_list_products_with_filter_after(self):

        #create data

        x_days_from_today = 7
        after_created_date = datetime.now().replace(microsecond=0) - timedelta(days=x_days_from_today)
        after_created_date = after_created_date.isoformat()


        #make the call with 'after' in the parameter

        data = {"after": after_created_date}

        rs_api = ProductsAPIHelper().call_list_products(payload=data, get_all=True, return_headers=True)

        #get number of products in the response
        headers = rs_api['headers']
        api_products_qty_header = int(headers['X-WP-Total'])
        api_product_qty_count = len(rs_api['response_json'])

        assert api_product_qty_count == api_products_qty_header, f"List product header and actual number of"\
                                                                 f"products does not match. Header: {api_products_qty_header}, Count: {api_product_qty_count}"





        # get data from db
        db_products = ProductsDao().get_products_created_after_given_date(after_created_date)
        db_products_qty = len(db_products)

        #Verfiy the products in DB match the products in api response
        assert int(api_products_qty_header) == db_products_qty, f"List products with filter 'after' returned unexpected number of products." \
                                                                f"Expected: { db_products_qty}, Actual: {api_products_qty_header}"
        # verify the products match using id
        ids_in_api = [i['id'] for i in rs_api['response_json']]
        ids_in_db = [i['ID'] for i in db_products]
        ids_diff = list(set(ids_in_api) - set(ids_in_db))
        assert not ids_diff, f"List of product ids in api response do not match in db."


