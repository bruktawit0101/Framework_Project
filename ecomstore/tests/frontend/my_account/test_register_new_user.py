
from ecomstore.src.pages.MyAccountSignedOut import MyAccountSignedOut
from ecomstore.src.pages.MyAccountSignedIn import MyAccountSignedIn
import pytest
from ecomstore.src.utilities.genericUtility import generate_random_email_and_password

pytestmarks = [pytest.mark.fe, pytest.mark.regression, pytest.mark.smoke, pytest.mark.my_account]
@pytest.mark.usefixtures("init_driver")
class TestRegisterNewUser:

    @pytest.mark.qactcid2
    def test_register_valid_new_user(self):
        '''
        Test is verify a valid user can register to the site.
        It generates a random email and password then registers the user.
        :return:
        '''

        my_acct = MyAccountSignedOut(self.driver)
        my_acct_sin = MyAccountSignedIn(self.driver)
        # go to my account page
        my_acct.go_to_my_account()

        random_info = generate_random_email_and_password()
        # input register email
        my_acct.input_register_email(random_info["email"])
        # input register password
        my_acct.input_register_password(random_info["password"])
        # click on register button
        my_acct.click_register_button()
        # VERIFY USER IS REGISTERED
        my_acct_sin.verify_user_is_signed_in()

        breakpoint()




