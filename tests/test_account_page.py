import allure


@allure.feature('Личный кабинет')
class TestAccountPage:
    @allure.title('Проверка перехода по клику на "Личный кабинет"')
    def test_click_to_go_personal_account(self, driver, new_user_tokens, main_page, account_page):
        main_page.click_on_button_personal_account()
        account_page.wait_visibility_of_section_description()
        assert account_page.check_displaying_of_section_description() is True

    @allure.title('Проверка перехода по клику на "История заказов"')
    def test_click_to_go_order_history(self, driver, new_user_tokens, create_and_delete_user_and_order, main_page, account_page):
        main_page.click_on_button_personal_account()
        account_page.wait_visibility_of_section_description()
        account_page.click_on_order_history_section()
        account_page.wait_visibility_of_order_card()
        assert 'бургер' in account_page.get_text_of_order_card_title()

    @allure.title('Проверка выхода из аккаунта')
    def test_logout_user(self, driver, new_user_tokens, main_page, account_page):
        main_page.click_on_button_personal_account()
        account_page.wait_visibility_of_section_description()
        account_page.click_on_logout_button()
        account_page.wait_visibility_of_login_button()
        assert account_page.check_displaying_of_login_button()