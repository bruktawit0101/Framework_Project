
from ecomstore.src.utilities.dbUtility import DbUtility
import random
import logging as logger

class ProductsDao:

    def __init__(self):
        self.db_helper = DbUtility()
        self.database = self.db_helper.database
        self.table_prefix = self.db_helper.table_prefix

    def get_random_products_from_db(self, qty=1):
        """
        Get a random product from db.
        :params qty: number of products to get
        :return:
        """
        logger.info(f"Getting random products from db qty={qty}")
        sql = """SELECT ID, post_title, post_name FROM
        quicksitedb.wp_posts WHERE post_type=
        "product" LIMIT 5000;"""
        rs_sql = self.db_helper.execute_select(sql)
        logger.debug(f"found{len(rs_sql)} random products from DB.")

        return random.sample(rs_sql, int(qty))

    def get_product_by_id(self, product_id):
        sql = f"""SELECT * FROM {self.database}.{self.table_prefix}posts 
              WHERE ID = {product_id};"""

        return self.db_helper.execute_select(sql)




