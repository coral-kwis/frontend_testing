from selenium.webdriver.common.by import By

from src.pages.basePage import BasePage


class CommonPage(BasePage):
    my_account_lnk = (By.CSS_SELECTOR, 'div .header-login a')

    def click_my_account_lnk(self):
        self.click_element(self.my_account_lnk)


