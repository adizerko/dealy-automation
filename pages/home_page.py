from components.header import HeaderComponent
from curl import MAIN_PAGE_URL
from pages.base_page import BasePage


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.header = HeaderComponent(driver, self)

    def open_home_page(self) -> None:
        self.open(MAIN_PAGE_URL)



