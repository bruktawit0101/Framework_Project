
from ecomstore.src.pages.Locators.MyAccountSignedOutLocator import MyAccountSignedOutLocators
# from LocalHost_store.src.helpers.Config_helpers import get_base_url
from ecomstore.src.selenium_extended.SeleniumExtended import SeleniumExtended

class MyAccountSignedOut(MyAccountSignedOutLocators):

    endpoint = '/my-account/'

    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)


    def go_to_my_account(self):
        base_url = ('http://localhost:8888/quicksite/')
        my_account_url = base_url + self.endpoint
        self.driver.get(my_account_url)

    def input_login_username(self, username):
        self.sl.wait_and_input_text(self.USERNAME_FIELD, username)

    def input_login_password(self, password):
        self.sl.wait_and_input_text(self.PASSWORD_FIELD, password)

    def click_on_login_btn(self):
        self.sl.wait_and_click(self.LOGIN_BUTTON)

    def input_register_email(self, email):
        self.sl. wait_and_input_text(self.REGISTER_EMAIL, email)

    def input_register_password(self, password):
        self.sl.wait_and_input_text(self.REGISTER_PASSWORD, password)

    def click_register_button(self):
        self.sl.wait_and_click(self.REGISTER_BTN)



