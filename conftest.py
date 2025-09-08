import pytest
from selenium import webdriver

from pages.account_page import AccountPage
from pages.home_page import HomePage
from pages.login_page import LoginPage
from curl import LOGIN_URL, PROFILE_PAGE_URL


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()

    yield driver
    driver.quit()

@pytest.fixture
def login(driver):
    login_page = LoginPage(driver)
    login_page.open_login_page()
    login_page.login()

    return HomePage(driver)