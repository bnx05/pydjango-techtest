import os

import pytest
from pyvirtualdisplay import Display
from selenium import webdriver

from page_objects.admin_login_page import AdminLoginPage

ADMIN_LOGIN_URL = os.getenv('ADMIN_LOGIN_URL', 'http://127.0.0.1:8000/admin/login')
USERNAME = os.getenv('USERNAME')
PASSWORD = os.getenv('PASSWORD')


def set_browser():
    selected_browser = os.getenv('BROWSER', 'chrome').lower()
    headless = os.getenv('HEADLESS', False)

    if headless:
        print("Using local headless browser")
        display = Display(visible=0, size=(1400, 1000))
        display.start()

    if selected_browser == 'chrome':
        print("Using Chrome")
        wd = webdriver.Chrome()
    elif selected_browser == 'firefox':
        print("Using Firefox")
        wd = webdriver.Firefox()
    else:
        raise Exception("{} not yet supported! Please select either Chrome or Firefox".format(selected_browser))

    wd.maximize_window()

    return wd


@pytest.fixture
def browser(request):
    with set_browser() as browser:
        yield browser


@pytest.fixture
def login_to_django_admin(browser):
    admin_login = AdminLoginPage(browser)
    browser.get(ADMIN_LOGIN_URL)
    admin_login.login_to_admin(username=USERNAME, password=PASSWORD)
