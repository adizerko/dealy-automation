import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver

from data import FIRST_NAME, LAST_NAME, EMAIL, PASSWORD, NEW_PASSWORD
from pages.account_information_page import AccountInformationPage
from pages.home_page import HomePage
from pages.login_page import LoginPage


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()

    yield driver
    driver.quit()

@pytest.fixture
def login(driver: WebDriver):
    login_page = LoginPage(driver)
    login_page.open_login_page()
    login_page.login()

    return HomePage(driver)

@pytest.fixture
def account_information_page(login: HomePage):
    account_page = login.header.go_to_account_page()
    account_information_page = account_page.go_to_account_information_page()

    yield account_information_page

    account_information_page.set_first_name(FIRST_NAME)
    account_information_page.set_last_name(LAST_NAME)
    account_information_page.set_email(EMAIL)
    account_information_page.set_old_password()
    account_information_page.click_on_save_button()

@pytest.fixture
def account_address_page(login: HomePage):
    account_page = login.header.go_to_account_page()
    account_address_page = account_page.go_to_account_address_page()

    return account_address_page

