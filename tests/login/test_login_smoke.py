import pytest

from src.utilities.credentialsUtil import CredentialUtil
from tests.testBase import TestBase

pytestmark = [pytest.mark.smoke, pytest.mark.login]


class TestLoginSmoke(TestBase):

    @pytest.mark.tcid01
    def test_login_successfully_with_admin(self):
        self.pages.login_page().login_with_admin_user()
        self.pages.my_account_page().verify_user_dashboard_displays()

    @pytest.mark.tcid02
    def test_login_successfully(self):
        user = self.get_user()
        self.logger().debug(f'user credentials: {user}')
        username = CredentialUtil.get_username(user)
        self.pages.login_page().login(user)
        self.pages.my_account_page().verify_user_dashboard_displays(username)
