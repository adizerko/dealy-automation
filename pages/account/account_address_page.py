from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from helper import Generation
from pages.base_page import BasePage


class AccountAddressPage(BasePage):
    PROFILE_NAME = By.XPATH, "//span[@class='u-font-weight-bold']"
    FIRST_NAME_INPUT = By.NAME, "firstname"
    LAST_NAME_INPUT = By.NAME, "lastname"
    COMPANY_INPUT = By.NAME, "company"
    ADDRESS_INPUT = By.NAME, "address1"
    ADDRESS_COMPLEMENT_INPUT = By.NAME, "address2"
    POSTAL_CODE_INPUT = By.NAME, "postcode"
    CITY_INPUT = By.NAME, "city"
    COUNTRY_SELECT = By.NAME, "id_country"
    PHONE_NUMBER_INPUT = By.NAME, "phone_mobile"
    ALIAS_INPUT = By.NAME, "alias"
    SAVE_BUTTON = By.CSS_SELECTOR, "button.btn.btn-primary.form-control-submit"
    UPDATE_SUCCESS_MESSAGE = By.XPATH, "//li[text()='Address successfully added!']"

    def set_first_name(self):
        self.send_keys_to_input(self.FIRST_NAME_INPUT, Generation.first_name())

    def set_last_name(self):
        self.send_keys_to_input(self.LAST_NAME_INPUT, Generation.last_name())

    def set_company(self):
        self.send_keys_to_input(self.COMPANY_INPUT, Generation.company())

    def set_address(self):
        self.send_keys_to_input(self.ADDRESS_INPUT, Generation.address())

    def set_address_complement(self):
        self.send_keys_to_input(self.ADDRESS_COMPLEMENT_INPUT, Generation.address_complement())

    def set_postal_code(self):
        self.send_keys_to_input(self.POSTAL_CODE_INPUT, Generation.postal_code())

    def set_city(self):
        self.send_keys_to_input(self.CITY_INPUT, Generation.city())

    def click_on_country_select(self):
        self.click_on_element(self.COUNTRY_SELECT)

    def select_country(self, country: str):
        self.get_select_by_visible_text(self.COUNTRY_SELECT, country)

    def set_phone(self):
        self.send_keys_to_input(self.PHONE_NUMBER_INPUT, Generation.phone())

    def is_update_success_message_displayed(self) -> bool:
        success_message = self.get_text(self.UPDATE_SUCCESS_MESSAGE)

        return success_message == "Address successfully added!"

    def click_on_button_save(self):
        self.click_on_element(self.SAVE_BUTTON)




