
from ecomstore.src.pages.Locators.HeaderLocators import HeaderLocators
from ecomstore.src.selenium_extended.SeleniumExtended import SeleniumExtended

class Header(HeaderLocators):

    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(driver)

    def click_cart_on_the_right_header(self):
        self.sl.wait_and_click(self.HEADER_RIGHT_CART)
    def wait_until_cart_item_count(self, count):
        # expected_text = str(count) + 'item'
        expected_text = f"{str(count)} item"
        self.sl.wait_until_element_contains_text(self.CART_ITEM_COUNT, expected_text)