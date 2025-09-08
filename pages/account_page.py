import allure
from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.login_page import LoginPage


class AccountPage(BasePage):
    # Логотип компании
    DEALY_LOGO = By.XPATH, "//img[@alt='Dealy']"

    # Имя пользователя
    PROFILE_NAME = By.XPATH, "//span[contains(text(), 'Ivan Ivanov')]"

    # Ссылка в левом меню на страницу профиля
    PROFILE_LINK = By.CSS_SELECTOR, "a.c-account-sidebar__link.c-account-sidebar__heading"

    # Ссылка в левом меню на страницу историю заказов
    ORDER_HISTORY_LINK = By.ID, "history-link"

    # Ссылка в левом меню на страницу личную информация
    INFORMATION_LINK = By.ID, "identity - link"

    # Ссылка в левом меню на страницу добавления адреса
    ADD_FIRST_ADDRESS_LINK = By.ID, "address-link"

    # Ссылка в левом меню на страницу ваучеры
    VOUCHERS_LINK = By.ID, "discounts-link"

    # Ссылка в левом меню на получение персональных данных
    PERSONAL_DATA_LINK = By.ID, "psgdpr-link"

    # Ссылка в левом меню выхода из аккаунта
    LOGOUT_LINK = By.XPATH, "//a[@href='https://dealy.com/?mylogout=']"

    # Ссылка возврата на главную страницу
    BACK_TO_STORE_LINK = By.XPATH, "//span[text()='Back to store']"

    @allure.step("Кликнуть на ссылку профиля")
    def click_on_profile_link(self):
        self.click_on_element(self.PROFILE_LINK)

    @allure.step("Кликнуть на кнопку в левом меню 'Order history and details'")
    def click_on_order_history_link(self):
        self.click_on_element(self.ORDER_HISTORY_LINK)

    @allure.step("Кликнуть на кнопку в левом меню 'Add first address'")
    def click_on_add_address_link(self):
        self.click_on_element(self.ADD_FIRST_ADDRESS_LINK)

    @allure.step("Кликнуть на кнопку в левом меню 'Vouchers'")
    def click_on_vouchers_link(self):
        self.click_on_element(self.VOUCHERS_LINK)

    @allure.step("Кликнуть на кнопку в левом меню 'GDPR - Personal data'")
    def click_on_personal_data_link(self):
        self.click_on_element(self.PERSONAL_DATA_LINK)

    @allure.step("Кликнуть на кнопку в левом меню 'Logout'")
    def click_on_logout_link(self):
        self.click_on_element(self.LOGOUT_LINK)

    @allure.step("Кликнуть на кнопку 'Back to store'")
    def click_on_back_to_store(self):
        self.click_on_element(self.BACK_TO_STORE_LINK)

    @allure.step("Проверка успешно выхода из аккаунт")
    def is_logout_in(self):
        return bool(self.wait_for_element(LoginPage.SIGN_IN_BUTTON))