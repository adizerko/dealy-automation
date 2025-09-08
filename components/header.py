import allure
from selenium.webdriver.common.by import By

from pages.account_page import AccountPage
from pages.base_page import BasePage
from pages.login_page import LoginPage


class HeaderComponent:
    LOGO = (By.CSS_SELECTOR, "img[alt='Dealy']")
    SEARCH_INPUT = (By.NAME, "s")
    CART_BUTTON = (By.CSS_SELECTOR, "a[href*='cart']")
    SIGN_IN_BUTTON = (By.CSS_SELECTOR, "a[href*='login']")
    ACCOUNT_BUTTON = By.XPATH, "//a[@href='https://dealy.com/my-account']"

    def __init__(self, driver, base_page: BasePage):
        self.driver = driver
        self.base = base_page

    @allure.step("Клик по логотипу")
    def click_logo(self):
        self.base.click_on_element(self.LOGO)

    @allure.step("Клик по кнопке 'My account'")
    def click_on_my_account_button(self):
        self.base.click_on_element(self.ACCOUNT_BUTTON)

    @allure.step("Переход на страницу профиля")
    def go_to_account_page(self):
        self.base.click_on_element(self.ACCOUNT_BUTTON)
        return AccountPage(self.base.driver)

    @allure.step("Переход на страницу входа")
    def go_to_login_page(self):
        self.base.click_on_element(self.ACCOUNT_BUTTON)
        return LoginPage(self.base.driver)