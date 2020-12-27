from selenium.webdriver.common.by import By

from src.pages.commonPage import CommonPage
from src.utilities.credentialsUtil import CredentialUtil


class MyAccountPage(CommonPage):
    user_dashboard_str = 'Hello {} (not {}? Log out)'

    user_dashboard_txt = (By.XPATH, '//div[contains(@class,"MyAccount-content")]//p')

    def verify_user_dashboard_displays(self, username=None):
        if not username:
            username = CredentialUtil.get_admin_username()
        self.assert_element_text(self.user_dashboard_txt, self.user_dashboard_str.format(username, username))
