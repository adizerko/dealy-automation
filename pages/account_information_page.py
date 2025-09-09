from selenium.webdriver.common.by import By

from curl import ACCOUNT_INFORMATION_PAGE
from pages.base_page import BasePage
from data import PASSWORD, NEW_PASSWORD


class AccountInformationPage(BasePage):
    PROFILE_NAME = By.XPATH, "//span[@class='u-font-weight-bold']"
    FIRST_NAME_INPUT = By.NAME, "firstname"
    LAST_NAME_INPUT = By.NAME, "lastname"
    EMAIL_INPUT = By.NAME, "email"
    PASSWORD_INPUT = By.NAME, "password"
    NEW_PASSWORD_INPUT = By.NAME, "new_password"
    NEWSLETTER_INPUT = By.NAME, "newsletter"
    NEWSLETTER_LABEL = By.XPATH, "//input[@name='newsletter']/following-sibling::label"
    SAVE_BUTTON = By.XPATH, "//button[@data-link-action='save-customer']"
    UPDATE_SUCCESS_MESSAGE = By.XPATH, "//li[(text()='Information successfully updated.')]"

    def open_account_personal_page(self) -> None:
        self.open(ACCOUNT_INFORMATION_PAGE)

    def set_first_name(self, new_first_name) -> None:
        self.send_keys_to_input(self.FIRST_NAME_INPUT, new_first_name)

    def set_last_name(self, new_last_name) -> None:
        self.send_keys_to_input(self.LAST_NAME_INPUT, new_last_name)

    def set_email(self, new_email) -> None:
        self.send_keys_to_input(self.EMAIL_INPUT, new_email)

    def set_old_password(self) -> None:
        self.send_keys_to_input(self.PASSWORD_INPUT, PASSWORD)

    def set_new_password(self, new_password) -> None:
        self.send_keys_to_input(self.NEW_PASSWORD_INPUT, new_password)

    def click_on_newsletter_checkbox(self):
        self.click_on_element(self.NEWSLETTER_INPUT)

    def click_on_newsletter_checkbox_label(self):
        self.click_on_element(self.NEWSLETTER_LABEL)

    def click_on_save_button(self) -> None:
        self.click_on_element(self.SAVE_BUTTON)

    def get_displayed_name(self) -> str:
        save_first_name = self.get_text(self.PROFILE_NAME)
        return save_first_name

    def get_displayed_last_name(self) -> str:
        save_last_name = self.get_text(self.PROFILE_NAME)
        return save_last_name

    def get_email_value(self) -> str:
        email_value = self.get_value_element(self.EMAIL_INPUT)
        return email_value

    def is_newsletter_checked(self) -> bool:
        return self.is_checkbox_checked(self.NEWSLETTER_INPUT)

    def is_update_success_message_displayed(self) -> bool:
        success_message = self.get_text(self.UPDATE_SUCCESS_MESSAGE)

        return success_message == "Information successfully updated."

    def refresh_account_page(self) -> None:
        self.refresh_page()


