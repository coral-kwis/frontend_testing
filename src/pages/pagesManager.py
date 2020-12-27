from src.pages.homePage import HomePage
from src.pages.loginPage import LoginPage
from src.pages.myAccountPage import MyAccountPage


class PagesManager(object):
    def __init__(self, driver):
        self.driver = driver
        self.home_obj = None
        self.login_obj = None
        self.my_account_obj = None

    def home_page(self):
        if not self.home_obj:
            self.home_obj = HomePage(self.driver)
        return self.home_obj

    def login_page(self):
        if not self.login_obj:
            self.login_obj = LoginPage(self.driver)
        return self.login_obj

    def my_account_page(self):
        if not self.my_account_obj:
            self.my_account_obj = MyAccountPage(self.driver)
        return self.my_account_obj
