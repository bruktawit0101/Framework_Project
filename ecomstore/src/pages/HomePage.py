
from LocalHost_store.src.pages.Locators.HomePageLocators import HomePageLocators
from LocalHost_store.src.selenium_extended.SeleniumExtended import SeleniumExtended
from LocalHost_store.src.configs.MainConfigs import MainConfigs

class HomePage(HomePageLocators):

    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)

    def go_to_homepage(self):
        home_url = MainConfigs.get_base_url()
        self.driver.get(home_url)

    def click_first_add_to_cart_button(self):
        self.sl.wait_and_click(self.ADD_TO_CART_BTN)







