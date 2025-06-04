import allure

from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators


class MainPage(BasePage):
    @allure.step('Нажатие на кнопку "Конструктор"')
    def click_on_button_constructor(self):
        self.wait_visibility_of_element(MainPageLocators.CONSTRUCTOR_BUTTON)
        self.click_on_element(MainPageLocators.CONSTRUCTOR_BUTTON)

    @allure.step('Нажатие на кнопку "Лента заказов"')
    def click_on_button_order_feed(self):
        self.wait_visibility_of_element(MainPageLocators.ORDER_FEED_BUTTON)
        self.click_on_element(MainPageLocators.ORDER_FEED_BUTTON)

    @allure.step('Нажатие на кнопку "Личный кабинет')
    def click_on_button_personal_account(self):
        self.wait_visibility_of_element(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)
        self.click_on_element(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)

    @allure.step('Нажатие на кнопку "Войти в аккаунт"')
    def click_on_button_login_to_account(self):
        self.click_on_element(MainPageLocators.LOGIN_TO_ACCOUNT_BUTTON)

    @allure.step('Получение заголовка раздела "Конструктор"')
    def get_text_constructor_title(self):
        return self.get_text_on_element(MainPageLocators.CONSTRUCTOR_HEADING)

    @allure.step('Нажатие на ингредиент')
    def click_on_ingredient(self):
        self.wait_visibility_of_element(MainPageLocators.BUN_R2_D3)
        self.click_on_element(MainPageLocators.BUN_R2_D3)

    @allure.step('Проверка отображения окна "Детали ингредиента"')
    def check_displaying_ingredient_details(self):
        self.wait_visibility_of_element(MainPageLocators.INGREDIENT_DETAIL_WINDOW_TITLE)
        return self.check_element_display(MainPageLocators.INGREDIENT_DETAIL_WINDOW_TITLE)

    @allure.step('Закрытие окна "Детали ингредиента"')
    def close_ingredient_details(self):
        self.wait_visibility_of_element(MainPageLocators.INGREDIENT_DETAIL_CLOSE_BUTTON)
        self.click_on_element(MainPageLocators.INGREDIENT_DETAIL_CLOSE_BUTTON)

    @allure.step('Проверка, что окно "Детали ингредиента" не отображается')
    def check_not_displaying_ingredient_details(self):
        self.wait_for_closing_of_element(MainPageLocators.INGREDIENT_DETAIL_WINDOW_TITLE)
        if not self.check_element_display(MainPageLocators.INGREDIENT_DETAIL_WINDOW_TITLE):
            return True

    @allure.step('Добавление ингредиента в заказ')
    def drag_and_drop_ingredient_to_order(self):
        source_element = MainPageLocators.BUN_R2_D3
        target_element = MainPageLocators.BURGER_CONSTRUCTOR_BASKET
        self.drag_and_drop_element(source_element, target_element)

    @allure.step('Получение количества ингредиентов в заказе')
    def get_count_of_ingredients_in_order(self):
        return self.get_text_on_element(MainPageLocators.COUNTER_INGREDIENTS_IN_ORDER)

    @allure.step('Нажатие на кнопку "Оформить заказ"')
    def click_on_button_place_order(self):
        self.click_on_element(MainPageLocators.PLACE_ORDER_BUTTON)

    @allure.step('Проверка отображения окна о создании заказа')
    def check_displaying_of_confirmation_order_placement(self):
        self.wait_visibility_of_element(MainPageLocators.CONFIRMATION_ORDER_PLACEMENT)
        return self.check_element_display(MainPageLocators.CONFIRMATION_ORDER_PLACEMENT)

    @allure.step('Получение номера в окне о создании заказа')
    def get_number_order_in_confirmation_window(self):
        self.wait_for_element_to_change_text(MainPageLocators.NUMBER_ORDER_IN_CONFIRMATION_WINDOW, '9999')
        return self.get_text_on_element(MainPageLocators.NUMBER_ORDER_IN_CONFIRMATION_WINDOW)

    @allure.step('Закрытие окна о создании заказа')
    def click_on_button_close_confirmation_order(self):
        self.check_element_clickability(MainPageLocators.CONFIRMATION_ORDER_CLOSE_BUTTON)
        self.click_on_element(MainPageLocators.CONFIRMATION_ORDER_CLOSE_BUTTON)