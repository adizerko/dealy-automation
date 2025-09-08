import time

import allure
from selenium.webdriver.common.by import By

import curl
from pages.base_page import BasePage
from data import EMAIL, PASSWORD
from curl import PROFILE_PAGE_URL
from pages.registration_page import RegistrationPage


class LoginPage(BasePage):

    # Поле ввода email
    EMAIL_INPUT = By.NAME, "email"

    # Поле ввода password
    PASSWORD_INPUT = By.NAME, "password"

    # Кнопка показать/скрыть password
    SHOW_PASSWORD_BUTTON = By.CSS_SELECTOR, "button[data-action='show-password']"

    # Ссылка возврата на главную страницу
    BACK_TO_STORE_LINK = By.XPATH, "//span[text()='Back to store']"

    # Кнопка войти в систему
    SIGN_IN_BUTTON = By.ID, "submit-login"

    # Кнопка зарегистрироваться
    CREATE_ACCOUNT_BUTTON = By.CSS_SELECTOR, "a[data-link-action='display-register-form']"

    # Логотип компании
    DEALY_LOGO = By.XPATH, "//img[@alt='Dealy']"

    def open_login_page(self):
        self.open(curl.LOGIN_URL)

    @allure.step("Ввод данных в поле email")
    def set_email(self):
        self.send_keys_to_input(self.EMAIL_INPUT, EMAIL)

    @allure.step("Ввод данных в поле password")
    def set_password(self):
        self.send_keys_to_input(self.PASSWORD_INPUT, PASSWORD)

    @allure.step("Кликаем на кнопку SIGN IN")
    def click_on_sign_in_button(self):
        self.click_on_element(self.SIGN_IN_BUTTON)

    @allure.step("Заходим в аккаунт")
    def login(self):
        self.set_email()
        self.set_password()
        self.click_on_sign_in_button()

    @allure.step("Ожидаем загрузки страницы профиля")
    def wait_for_page_to_load(self):
        self.wait_for_url_site(PROFILE_PAGE_URL)

    @allure.step("Проверка успешного входа в аккаунт")
    def is_logged_in(self):
        current_url = self.get_current_url()
        expected_url = PROFILE_PAGE_URL

        return current_url == expected_url

    def go_to_registration_page(self):
        self.click_on_element(self.CREATE_ACCOUNT_BUTTON)
        return RegistrationPage(self.driver)

