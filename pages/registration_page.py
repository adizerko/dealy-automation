import curl
from curl import REGISTRATION_URL
from helper import Generation
from pages.base_page import BasePage

from selenium.webdriver.common.by import By

class RegistrationPage(BasePage):
    FIRST_NAME_INPUT = By.NAME, 'firstname'
    LAST_NAME_INPUT = By.NAME, "lastname"
    EMAIL_INPUT = By.NAME, "email"
    PASSWORD_INPUT = By.NAME, "password"
    NEWSLETTER_CHECKBOX = By.NAME, "newsletter"
    SHOW_PASSWORD_BUTTON = By.XPATH, "//button[@data-action='show-password']"
    SAVE_BUTTON = By.CSS_SELECTOR, "button.form-control-submit"
    LOG_IN_INSTEAD = By.XPATH, "//a[text()='Log in instead!']"

    def open_registration_page(self):
        self.open(REGISTRATION_URL)

    def set_first_name(self):
        self.send_keys_to_input(self.FIRST_NAME_INPUT, Generation.first_name())

    def set_last_name(self):
        self.send_keys_to_input(self.LAST_NAME_INPUT, Generation.last_name())

    def set_email(self):
        self.send_keys_to_input(self.EMAIL_INPUT, Generation.email())

    def set_password(self):
        self.send_keys_to_input(self.PASSWORD_INPUT, Generation.password())

    def click_on_save_button(self):
        self.click_on_element(self.SAVE_BUTTON)

    def is_registration_successful(self) -> bool:
        current_url = self.get_current_url()
        expected_url = curl.MAIN_PAGE_URL

        return current_url == expected_url