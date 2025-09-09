import allure

from helper import Generation
from pages.account_information_page import AccountInformationPage


@allure.epic("Информация аккаунта")
@allure.feature("Управление профилем")
class TestAccountInformation:

    @allure.story("Изменение имени")
    @allure.title("Тест изменения имени в аккаунте")
    def test_change_name(self, account_information_page: AccountInformationPage) -> None:
        new_first_name: str = Generation.first_name()
        account_information_page.set_first_name(new_first_name)
        account_information_page.set_old_password()
        account_information_page.click_on_save_button()

        assert account_information_page.is_update_success_message_displayed()
        assert new_first_name in account_information_page.get_displayed_name()

    @allure.story("Изменение фамилии")
    @allure.title("Тест изменения фамилии в аккаунте")
    def test_change_last_name(self, account_information_page: AccountInformationPage) -> None:
        new_last_name: str = Generation.last_name()
        account_information_page.set_last_name(new_last_name)
        account_information_page.set_old_password()
        account_information_page.click_on_save_button()

        assert account_information_page.is_update_success_message_displayed()
        assert new_last_name in account_information_page.get_displayed_last_name()

    @allure.story("Изменение email")
    @allure.title("Тест изменения email в аккаунте")
    def test_change_email(self, account_information_page: AccountInformationPage) -> None:
        new_email: str = Generation.email()
        account_information_page.set_email(new_email)
        account_information_page.set_old_password()
        account_information_page.click_on_save_button()

        email_value = account_information_page.get_email_value()
        print(email_value)
        assert email_value == new_email
        assert account_information_page.is_update_success_message_displayed()

    @allure.story("Подписка на рассылку")
    @allure.title("Тест изменения подписки на рассылку")
    def test_change_newsletter(self, account_information_page: AccountInformationPage) -> None:
        account_information_page.set_old_password()
        account_information_page.click_on_newsletter_checkbox_label()
        account_information_page.click_on_save_button()
        assert account_information_page.is_update_success_message_displayed()

        account_information_page.refresh_account_page()
        assert account_information_page.is_newsletter_checked()
