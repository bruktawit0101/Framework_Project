
from ecomstore.src.pages.Locators.CheckOutPageLocator import CheckOutPageLocator
from ecomstore.src.selenium_extended.SeleniumExtended import SeleniumExtended
from ecomstore.src.utilities.genericUtility import generate_random_email_and_password

class CheckOutPage(CheckOutPageLocator):


    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(driver)

    def input_billing_first_name(self, first_name=None):
        first_name = first_name if first_name else 'Automationfname'
        self.sl.wait_and_input_text(self.BILLING_FIRST_NAME_FIELD, first_name)

    def input_billing_last_name(self, last_name=None):
        last_name = last_name if last_name else 'john'
        self.sl.wait_and_input_text(self.BILLING_LAST_NAME_FIELD, last_name)

    def select_billing_country(self, country=None):
        country = 'United States (US)' if not country else country
        self.sl.wait_and_select_dropdown(self.BILLING_COUNTRY_DROPDOWN, to_select=country, select_by='visible_text')


    def input_billing_street_address1(self, address1=None):
        address1 = address1 if address1 else '123lendel_st'
        self.sl.wait_and_input_text(self.BILLING_STREET_ADDRESS, address1)


    def input_billing_city(self, city=None):
        city = city if city else 'las vegas'
        self.sl.wait_and_input_text(self.BILLING_CITY, city)


    def select_billing_state(self, state=None):
        state = "California" if not state else state
        self.sl.wait_and_select_dropdown(self.BILLING_STATE_DROPDOWN, to_select=state, select_by='visible_text')



    def input_billing_zip_code(self, zip_code=None):
        zip_code = zip_code if zip_code else 89103
        self.sl.wait_and_input_text(self.BILLING_ZIP_CODE, zip_code)

    def input_billing_phone_number(self, phone=None):
        phone = phone if phone else '702-777-7777'
        self.sl.wait_and_input_text(self.BILLING_PHONE_NUMBER, phone)

    def input_billing_email_address(self, email=None):
        if not email:
            rand_email = generate_random_email_and_password()
            email = rand_email['email']
        self.sl.wait_and_input_text(self.BILLING_EMAIL_ADDRESS, email)
        return email


    def fill_billing_info(self, f_name=None, l_name=None, street1=None, city=None, zip_code=None, phone=None, email=None, country=None, state=None):
        self.input_billing_first_name(first_name=f_name)
        self.input_billing_last_name(last_name=l_name)
        self.input_billing_street_address1(address1=street1)
        self.input_billing_city(city=city)
        self.input_billing_zip_code(zip_code=zip_code)
        self.input_billing_phone_number(phone=phone)
        self.input_billing_email_address(email=email)
        self.select_billing_country(country=country)
        self.select_billing_state(state=state)

    def click_place_order_btn(self):
        self.sl.wait_and_click(self.PLACE_ORDER_BTN)


