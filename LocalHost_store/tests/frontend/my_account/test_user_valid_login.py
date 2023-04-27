import pytest
from LocalHost_store.src.pages.MyAccountSignedOut import MyAccountSignedOut
from LocalHost_store.src.pages.MyAccountSignedIn import MyAccountSignedIn
# from LocalHost_store.src.helpers.generic_helpers import generate_random_email_and_password
@pytest.mark.usefixtures("init_driver")

class TestUserValidLogin:

    @pytest.mark.qactcid1
    def test_user_valid_login(self):


        my_account_o = MyAccountSignedOut(self.driver)
        my_account_I = MyAccountSignedIn(self.driver)
        my_account_o.go_to_my_account()
        my_account_o.input_login_username('QAtestusername@gmail.com')
        my_account_o.input_login_password('Regpassword@1')
        my_account_o.click_on_login_btn()
        my_account_I.verify_user_signed_in()

