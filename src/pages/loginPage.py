from selenium.webdriver.common.by import By

from src.pages.commonPage import CommonPage
from src.utilities.credentialsUtil import CredentialUtil


class LoginPage(CommonPage):
    username_tbx = (By.ID, 'username')
    password_tbx = (By.ID, 'password')
    login_btn = (By.NAME, 'login')

    def type_username(self, username):
        self.type_text(self.username_tbx, username)

    def type_password(self, password):
        self.type_text(self.password_tbx, password)

    def click_login_btn(self):
        self.click_element(self.login_btn)

    def login_with_admin_user(self):
        admin_user = CredentialUtil.get_admin_username()
        admin_pwd = CredentialUtil.get_admin_password()
        self.click_my_account_lnk()
        self.type_username(admin_user)
        self.type_password(admin_pwd)
        self.click_login_btn()

    def login(self, user):
        self.click_my_account_lnk()
        self.type_username(CredentialUtil.get_username(user))
        self.type_password(CredentialUtil.get_password(user))
        self.click_login_btn()
