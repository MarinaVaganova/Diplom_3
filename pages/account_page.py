import allure

from pages.base_page import BasePage
from locators.account_page_locators import AccountPageLocators


class AccountPage(BasePage):
    @allure.step('Ожидание прогрузки кнопки "Войти"')
    def wait_visibility_of_login_button(self):
        self.wait_visibility_of_element(AccountPageLocators.LOGIN_BUTTON)

    @allure.step('Проверка отображения кнопки "Войти"')
    def check_displaying_of_login_button(self):
        return self.check_element_display(AccountPageLocators.LOGIN_BUTTON)

    @allure.step('Нажатие на раздел "История заказов"')
    def click_on_order_history_section(self):
        self.click_on_element(AccountPageLocators.ORDER_HISTORY_SECTION)

    @allure.step('Ожидание прогрузки текста описания раздела')
    def wait_visibility_of_section_description(self):
        self.wait_visibility_of_element(AccountPageLocators.SECTION_DESCRIPTION)

    @allure.step('Проверка отображения описания раздела')
    def check_displaying_of_section_description(self):
        return self.check_element_display(AccountPageLocators.SECTION_DESCRIPTION)

    @allure.step('Нажатие на кнопку "Выйти"')
    def click_on_logout_button(self):
        self.click_on_element(AccountPageLocators.LOGOUT_BUTTON)

    @allure.step('Ожидание прогрузки карточки заказа')
    def wait_visibility_of_order_card(self):
        self.wait_visibility_of_element(AccountPageLocators.ORDER_CARD_IN_HISTORY_SECTION)

    @allure.step('Получение информации из карточки заказа')
    def get_text_of_order_card_title(self):
        return self.get_text_on_element(AccountPageLocators.ORDER_CARD_TITLE_IN_HISTORY_SECTION)

    @allure.step('Получение номера заказа из карточки')
    def get_number_of_order_card(self):
        return self.get_text_on_element(AccountPageLocators.ORDER_CARD_NUMBER_IN_HISTORY_SECTION)