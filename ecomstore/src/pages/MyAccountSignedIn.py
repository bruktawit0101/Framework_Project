
from ecomstore.src.pages.Locators.MyAccountSignedInLocator import MyAccountSignedInLocators
from ecomstore.src.selenium_extended.SeleniumExtended import SeleniumExtended

class MyAccountSignedIn(MyAccountSignedInLocators):
    endpoint = '/my_account/'

    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)

    def verify_user_is_signed_in(self):
       '''
       Verifies user is digned by check the 'logout' is visible
       on the left navigation bar.
       :return:
       '''
       self.sl.wait_until_element_is_visible(self.LEFT_NAV_LOGOUT_BTN)



