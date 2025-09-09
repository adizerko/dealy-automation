import allure

from helper import Generation
from pages.account.account_address_page import AccountAddressPage

@allure.epic("Информация аккаунта")
@allure.feature("Адреса пользователя")
class TestAccountAddress:

    @allure.story("Добавление нового адреса")
    @allure.title("Тест добавления адреса со всеми полями")
    def test_add_address_with_all_fields(self, account_address_page: AccountAddressPage) -> None:
        account_address_page.set_first_name()
        account_address_page.set_last_name()
        account_address_page.set_company()
        account_address_page.set_address()
        account_address_page.set_address_complement()
        account_address_page.set_postal_code()
        account_address_page.set_city()
        account_address_page.select_country(Generation.country())
        account_address_page.set_phone()
        account_address_page.click_on_button_save()

        assert account_address_page.is_update_success_message_displayed()
