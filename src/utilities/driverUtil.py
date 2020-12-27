from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

from src.commons import constants
from src.configs.hosts_config import UI_HOST


class DriverUtil(object):
    @staticmethod
    def init_driver(browser):
        if browser == 'chrome':
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_experimental_option("excludeSwitches", ["enable-automation", "load-extension"])
            chrome_options.add_experimental_option(
                'prefs', {
                    'credentials_enable_service': False,
                    'profile': {
                        'password_manager_enabled': False
                    }
                })
            driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
        elif browser == 'chromeheadless':
            chrome_options = webdriver.ChromeOptions()
            chrome_options.headless = True
            driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
        elif browser == 'firefox':
            driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        elif browser == 'edge':
            driver = webdriver.Edge(EdgeChromiumDriverManager().install())
        else:
            raise Exception(f'{browser} is not a supported browser')
        driver.get(UI_HOST[constants.ENV]['host'])
        driver.maximize_window()
        driver.implicitly_wait(constants.TIMEOUT)
        return driver
