
from ecomstore.src.utilities.dbUtility import DbUtility

class CustomerDao(object):

    def __init__(self):
        self.db_helper = DbUtility()

    def get_customer_by_email(self, email):
        sql = f"""SELECT * FROM quicksitedb.wp_users
         WHERE user_email = '{email}';"""

        rs_sql = self.db_helper.execute_select(sql)

        return rs_sql





