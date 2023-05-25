
from ecomstore.src.utilities.dbUtility import DbUtility
import random
import logging as logger
class CustomerDao(object):


    def __init__(self):
        self.db_helper = DbUtility()
        self.database = self.db_helper.database
        self.table_prefix = self.db_helper.table_prefix

    def get_customer_by_email(self, email):
        sql = f"""SELECT * FROM {self.database}.{self.table_prefix}_users
              WHERE user_email = '{email}';"""

        rs_sql = self.db_helper.execute_select(sql)

        return rs_sql

    def get_random_customer_from_db(self, qty=1):
        sql = f"""SELECT user_email FROM {self.database}.{self.table_prefix}_users 
              ORDER BY id desc LIMIT 1000;"""
        rs_sql = self.db_helper.execute_select(sql)
        logger.debug(f"found{len(rs_sql)} random users from DB.")

        random_emails = random.sample(rs_sql, int(qty))
        return random_emails




