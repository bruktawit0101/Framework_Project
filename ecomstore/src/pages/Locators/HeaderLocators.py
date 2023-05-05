from selenium.webdriver.common.by import By

class HeaderLocators():

    HEADER_RIGHT_CART = (By.ID, 'site-header-cart')
    CART_ITEM_COUNT = (By.CSS_SELECTOR, 'ul#site-header-cart span.count')