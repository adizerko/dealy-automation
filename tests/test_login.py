import allure
from selenium.webdriver.remote.webdriver import WebDriver

from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.account_page import AccountPage


@allure.feature("Авторизация")
class TestLogin:

    @allure.story("Пользователь может войти с корректными данными")
    @allure.title("Тест успешного входа в систему")
    def test_login(self, driver: WebDriver) -> None:
        home_page = HomePage(driver)
        home_page.open_home_page()

        login_page: LoginPage = home_page.header.go_to_login_page()
        login_page.set_email()
        login_page.set_password()
        login_page.click_on_sign_in_button()

        assert login_page.is_logged_in()  # добавили вызов метода

    @allure.story("Пользователь может выйти из аккаунта")
    @allure.title("Тест выхода пользователя из профиля")
    def test_logout(self, login: HomePage, driver: WebDriver) -> None:
        home_page: HomePage = login
        account_page: AccountPage = home_page.header.go_to_account_page()
        account_page.click_on_logout_link()

        assert account_page.is_logout_in()
