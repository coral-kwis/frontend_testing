from assertpy import assert_that
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait as wait

from src.commons import constants


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver

    # WAIT
    def wait_for_element_visiable(self, tuple_selector, timeout=constants.TIMEOUT):
        return wait(self.driver, timeout).until(EC.visibility_of_element_located(tuple_selector))

    def wait_for_element_invisiable(self, tuple_selector, timeout=constants.TIMEOUT):
        return wait(self.driver, timeout).until(EC.invisibility_of_element_located(tuple_selector))

    def wait_for_element_clickable(self, tuple_selector, timeout=constants.TIMEOUT):
        return wait(self.driver, timeout).until(EC.element_to_be_clickable(tuple_selector))

    def wait_for_element_presence(self, tuple_selector, timeout=constants.TIMEOUT):
        return wait(self.driver, timeout).until(EC.presence_of_element_located(tuple_selector))

    def wait_for_all_elements_presence(self, tuple_selector, timeout=constants.TIMEOUT):
        return wait(self.driver, timeout).until(EC.presence_of_all_elements_located(tuple_selector))

    # SELENIUM API
    def find_element(self, tuple_selector):
        return self.driver.find_element(*tuple_selector)  # *tuple_selector: Unpacking list into 2 arguments

    def click_element(self, tuple_selector):
        self.wait_for_element_clickable(tuple_selector).click()

    def type_text(self, tuple_selector, text):
        ele = self.wait_for_element_visiable(tuple_selector)
        ele.clear()
        ele.send_keys(text)

    def select_option_by_visible_text_in_ddl(self, tuple_selector, text):
        select = Select(self.wait_for_element_visiable(tuple_selector))
        select.select_by_visible_text(text)

    def select_option_by_value_in_ddl(self, tuple_selector, value):
        select = Select(self.wait_for_element_visiable(tuple_selector))
        select.select_by_value(value)

    def override_timeout(self, timeout):
        self.driver.implicitly_wait(timeout)

    # ACTION CHAINS
    def hover_to_element(self, tuple_selector):
        ActionChains(self.driver).move_to_element(self.wait_for_element_visiable(tuple_selector)).perform()

    # JAVASCRIPT
    def move_to_element_by_js(self, tuple_selector):
        self.driver.execute_script('arguments[0].scrollIntoView(true);', self.wait_for_element_visiable(tuple_selector))

    # ASSERT
    def assert_element_text(self, tuple_selector, element_text):
        ele = self.wait_for_element_visiable(tuple_selector)
        assert_that(ele.text).is_equal_to(element_text)

    def is_visible(self, tuple_selector):
        return bool(self.wait_for_element_visiable(tuple_selector))

    def is_invisible(self, tuple_selector):
        return bool(self.wait_for_element_invisiable(tuple_selector))

    def is_exist(self, tuple_selector, timeout=constants.SHORT_TIMEOUT):
        is_exist = True
        try:
            self.override_timeout(timeout)
            self.find_element(tuple_selector)
        except NoSuchElementException:
            is_exist = False
        self.override_timeout(constants.TIMEOUT)
        return is_exist
