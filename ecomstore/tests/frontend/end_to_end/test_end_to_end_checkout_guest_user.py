
import pytest
from LocalHost_store.src.pages.HomePage import HomePage
from LocalHost_store.src.pages.Header import Header
from LocalHost_store.src.pages.CartPage import CartPage
from LocalHost_store.src.configs.MainConfigs import MainConfigs
from LocalHost_store.src.pages.CheckOutPage import CheckOutPage
from LocalHost_store.src.pages.OrderReceivedPage import OrderReceivedPage




@pytest.mark.usefixtures("init_driver")
class TestEndToEndCheckOutGuestUser:

   @pytest.mark.qactcid3
   def test_end_to_end_checkout_guest_user(self):

       home_page = HomePage(self.driver)
       header = Header(self.driver)
       cart_page = CartPage(self.driver)
       checkout_page = CheckOutPage(self.driver)
       order_received = OrderReceivedPage(self.driver)


       #go to home page
       home_page.go_to_homepage()

       #add first item to cart
       home_page.click_first_add_to_cart_button()

       #wait until cart item count 1
       header.wait_until_cart_item_count(1)

       #click cart btn on header
       header.click_cart_on_the_right_header()

       #verify there are items in the cart

       product_names = cart_page.get_all_product_names_in_cart()

       assert len(product_names) == 1, f"Expected 1 product in the cart but found {len(product_names)}"

       #apply coupon
       #click apply coupon button
       coupon_code = MainConfigs.get_coupon_code('FREE_COUPON')
       cart_page.apply_coupon(coupon_code)

       #verfiy coupon applyed

       # success_message = 'Coupon code applied successfully.'
       # cart_page.verfiy_coupon_applyed(success_message)

       #proceed to checkoout
       cart_page.click_on_proceed_to_checkout_btn()

       checkout_page.fill_billing_info()

       checkout_page.click_place_order_btn()

       order_received.verify_order_received_page_loaded()

       order_number = order_received.get_order_number()

       print(order_number)

       breakpoint()





