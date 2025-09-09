import time

import allure
from selenium.webdriver.chrome.webdriver import WebDriver

from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.registration_page import RegistrationPage


@allure.feature("Регистрация")
class TestRegistration:

    @allure.story("Пользователь может зарегистрироваться")
    @allure.title("Тест успешной регистрации нового пользователя")
    def test_registration(self, driver: WebDriver) -> None:
        home_page = HomePage(driver)
        home_page.open_home_page()
        login_page: LoginPage = home_page.header.go_to_login_page()
        registration_page: RegistrationPage = login_page.go_to_registration_page()
        registration_page.set_first_name()
        registration_page.set_last_name()
        registration_page.set_email()
        registration_page.set_password()
        registration_page.click_on_save_button()

        assert registration_page.is_registration_successful()

