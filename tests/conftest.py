import os
import time

import pytest

from src.configs.hosts_config import UI_HOST
from src.pages.pagesManager import PagesManager
from src.utilities.driverUtil import DriverUtil

driver = None


def pytest_addoption(parser):
    # “store”: store this option’s argument (default).
    parser.addoption('--browser', action='store', default='')


@pytest.fixture(scope='function')
def setup(request, config_browser):
    global driver
    browser = request.config.getoption('browser')
    if not browser:
        browser = config_browser
    driver = DriverUtil.init_driver(browser)
    request.cls.driver = driver
    pages = PagesManager(driver)
    request.cls.pages = pages
    yield
    driver.close()


@pytest.fixture(scope='session')
def config_browser():
    return UI_HOST['browser']


@pytest.fixture(params=['chromeheadless', 'firefox', 'edge'], scope='session')
def browser(request):
    return request.param


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])
    if report.when == 'call' or report.when == 'setup':
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            # wasxfail: @pytest.mark.xfail & run failed
            # report.failed: run failed
            report_dir = os.path.dirname(item.config.option.htmlpath)
            time_string = time.asctime().replace(':', ' ')
            file_name = f'{item.originalname}_{time_string}.png'
            file_path = os.path.join(report_dir, file_name)
            driver.get_screenshot_as_file(file_path)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:325px;height=225px;"' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra
