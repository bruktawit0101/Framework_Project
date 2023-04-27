import pytest
from LocalHost_store.src.pages.MyAccountSignedOut import MyAccountSignedOut
from LocalHost_store.src.pages.MyAccountSignedIn import MyAccountSignedIn

 feature/branch20230418

pytestmarks = [pytest.mark.fe, pytest.mark.regression, pytest.mark.smoke, pytest.mark.my_account]
@pytest.mark.usefixtures("init_driver")

class TestUserValidLogin:
    @pytest.mark.smoke

@pytest.mark.usefixtures("init_driver")

class TestUserValidLogin:

 master
    @pytest.mark.qactcid1
    def test_user_valid_login(self):


        my_account_o = MyAccountSignedOut(self.driver)
        my_account_I = MyAccountSignedIn(self.driver)
        my_account_o.go_to_my_account()
        my_account_o.input_login_username('QAtestusername@gmail.com')
        my_account_o.input_login_password('Regpassword@1')
        my_account_o.click_on_login_btn()
 feature/branch20230418
        my_account_I.verify_user_is_signed_in()

        breakpoint()

        my_account_I.verify_user_signed_in()

 master
