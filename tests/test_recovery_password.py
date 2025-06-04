import allure


@allure.feature('Восстановление пароля')
class TestRecoveryPassword:
    @allure.title('Проверка перехода по кнопке "Восстановить пароль"')
    def test_go_to_page_recover_password(self, driver, main_page, recovery_page):
        main_page.click_on_button_login_to_account()
        recovery_page.opening_password_recovery_page()
        assert recovery_page.check_displaying_of_input_email()

    @allure.title('Проверка ввода почты и клика по кнопке "Восстановить"')
    def test_enter_email_and_click_restore_button(self, driver, main_page, recovery_page):
        main_page.click_on_button_login_to_account()
        recovery_page.opening_password_recovery_page()
        recovery_page.send_email()
        recovery_page.click_on_recovery_button()
        assert recovery_page.check_displaying_of_password_input_field()

    @allure.title('Проверка, что при нажатии кнопки показать/скрыть пароль отображается')
    def test_click_on_show_password_button_visible_password(self, driver, main_page, recovery_page):
        main_page.click_on_button_login_to_account()
        recovery_page.opening_password_recovery_page()
        recovery_page.send_email()
        recovery_page.click_on_recovery_button()
        recovery_page.send_password()
        recovery_page.click_on_show_password_button()
        assert recovery_page.check_password_visible()