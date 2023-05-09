from ecomstore.src.pages.Locators.CartPageLocators import CartPageLocators
from ecomstore.src.selenium_extended.SeleniumExtended import SeleniumExtended

class CartPage(CartPageLocators):

    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(driver)

    def get_all_product_names_in_cart(self):
        product_name_elements = self.sl.Wait_and_get_elements(self.PRODUCT_NAME_IN_CART)
        # product_names = [i.text for i in product_name_elements]
        product_names = []
        for i in product_name_elements:
            product_name = i.text
            product_names.append(product_name)
            return product_names

    def input_coupon(self, coupon_code):
        self.sl.wait_and_input_text(self.COUPON_FIELD, str(coupon_code))

    def click_apply_coupon(self):
        self.sl.wait_and_click(self.APPLY_COUPON_BTN)

    def apply_coupon(self, coupon_code):
        self.input_coupon(coupon_code)
        self.click_apply_coupon()


    def verify_coupon_applied(self, success_message):
        self.sl.wait_until_text_visible(self.COUPON_SUCCESS_MESSAGE, success_message)
        pass
    def click_on_proceed_to_checkout_btn(self):
        self.sl.wait_and_click(self.PROCEED_TO_CHECKOUT_BTN)