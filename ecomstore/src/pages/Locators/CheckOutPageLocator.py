from selenium.webdriver.common.by import By

class CheckOutPageLocator():


    BILLING_FIRST_NAME_FIELD = (By.ID, 'billing_first_name')

    BILLING_LAST_NAME_FIELD = (By.ID, 'billing_last_name')

    BILLING_COUNTRY_DROPDOWN = (By.ID, 'billing_country')

    BILLING_STREET_ADDRESS = (By.ID, 'billing_address_1')

    BILLING_CITY = (By.ID, 'billing_city')

    BILLING_STATE_DROPDOWN = (By.ID, 'billing_state')

    BILLING_ZIP_CODE = (By.ID, 'billing_postcode')

    BILLING_PHONE_NUMBER = (By.ID, 'billing_phone')

    BILLING_EMAIL_ADDRESS = (By.ID, 'billing_email')

    PLACE_ORDER_BTN = (By.ID, 'place_order')



