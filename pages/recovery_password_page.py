import allure

from pages.base_page import BasePage
from locators.recovery_password_locators import RecoveryPasswordLocators
from helpers import *


class RecoveryPasswordPage(BasePage):
    @allure.step('Открытие страницы восстановления пароля')
    def opening_password_recovery_page(self):
        self.wait_visibility_of_element(RecoveryPasswordLocators.RECOVER_PASSWORD_BUTTON)
        self.click_on_element(RecoveryPasswordLocators.RECOVER_PASSWORD_BUTTON)

    @allure.step('Проверка отображения поля email')
    def check_displaying_of_input_email(self):
        return self.check_element_display(RecoveryPasswordLocators.EMAIL_INPUT_FIELD)

    @allure.step('Ввод email для восстановления пароля')
    def send_email(self):
        self.wait_visibility_of_element(RecoveryPasswordLocators.EMAIL_INPUT_FIELD)
        email = create_random_email()
        self.entering_value_input_field(RecoveryPasswordLocators.EMAIL_INPUT_FIELD, email)

    @allure.step('Нажатие на кнопку "Восстановить"')
    def click_on_recovery_button(self):
        self.wait_visibility_of_element(RecoveryPasswordLocators.RECOVER_BUTTON)
        self.click_on_element(RecoveryPasswordLocators.RECOVER_BUTTON)

    @allure.step('Проверка отображения поля "Пароль"')
    def check_displaying_of_password_input_field(self):
        self.wait_visibility_of_element(RecoveryPasswordLocators.PASSWORD_INPUT_FIELD)
        return self.check_element_display(RecoveryPasswordLocators.PASSWORD_INPUT_FIELD)

    @allure.step('Ввод пароля')
    def send_password(self):
        self.wait_visibility_of_element(RecoveryPasswordLocators.PASSWORD_INPUT_FIELD)
        passwd = create_random_password()
        self.entering_value_input_field(RecoveryPasswordLocators.PASSWORD_INPUT_FIELD, passwd)

    @allure.step('Нажатие на кнопку для отображения пароля')
    def click_on_show_password_button(self):
        self.wait_visibility_of_element(RecoveryPasswordLocators.SHOW_PASSWORD_BUTTON)
        self.click_on_element(RecoveryPasswordLocators.SHOW_PASSWORD_BUTTON)

    @allure.step('Проверка отображения пароля после нажатия кнопки')
    def check_password_visible(self):
        return self.check_element_display(RecoveryPasswordLocators.PASSWORD_VISIBLE)