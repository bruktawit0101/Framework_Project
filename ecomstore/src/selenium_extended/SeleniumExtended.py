from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException, TimeoutException
from selenium.webdriver.support.ui import Select


class SeleniumExtended:

    def __init__(self, driver):
        self.driver = driver
        self.default_timeout = 20

    def wait_and_input_text(self, locator, text, timeout=None):
        timeout = timeout if timeout else self.default_timeout
        WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        ).send_keys(text)

    def wait_and_click(self, locator, timeout=None):
        timeout = timeout if timeout else self.default_timeout
        WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        ).click()

    def wait_until_element_contains_text(self, locator, text, timeout=None):
        timeout = timeout if timeout else self.default_timeout
        WebDriverWait(self.driver, timeout).until(
            EC.text_to_be_present_in_element(locator, text),
            message=f"Element with locator = {locator}, does not contain text.'{text}', after waiting {timeout}")


    def wait_until_element_is_visible(self, locator_or_element, timeout=None):
        timeout = timeout if timeout else self.default_timeout

        if isinstance(locator_or_element, tuple):
            elem = WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator_or_element),
                message=f"element{locator_or_element} not found after timeout{timeout}"
            )

        else:
            import selenium.webdriver.remote.webelement
            if isinstance(locator_or_element, selenium.webdriver.remote.webelement.WebElement):
                elem = WebDriverWait(self.driver, timeout).until(
                    EC.visibility_of(locator_or_element),
                    message=f"element{locator_or_element} not found after timeout{timeout}"
                )
            else:
                raise TypeError(f"The locator to check visibility must be a 'tuple' or a 'WebElement' ")

        return elem

    def Wait_and_get_elements(self, locator, timeout=None, err=None):
        timeout = timeout if timeout else self.default_timeout
        err = err if err else f'unable to get elements located by "{locator}".'\
                              f'after timeout {timeout}'
        try:
            elements = WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_all_elements_located(locator)
            )
        except TimeoutException:
            raise TimeoutException(err)


        return elements

    def wait_and_select_dropdown(self, locator, to_select, select_by='visible_text'):
        # """
        #
        #
        # :param Locator:
        # :param to_select:
        # :param select_by: Options are 'visible_text', 'index', 'value'
        # :return:
        # """
        select_element = self.wait_until_element_is_visible(locator)
        select = Select(select_element)
        if select_by.lower() == 'visible_text':
            select.select_by_visible_text(to_select)
        elif select_by.lower() == 'index':
            select.select_by_index(to_select)
        elif select_by.lower() == 'value':
            select.select_by_value(to_select)
        else:
            raise Exception(f"invalid option for 'to_select' parameter. Valid values are 'visible_text', 'index' or 'value'")


    def wait_and_get_text(self, locator, timeout=None):
        timeout = timeout if timeout else self.default_timeout
        elm = self.wait_until_element_is_visible(locator, timeout)
        element_text = elm.text

        return element_text




