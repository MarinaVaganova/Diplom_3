import allure


@allure.feature('Основной функционал')
class TestMainPage:
    @allure.title('Проверка перехода по клику на "Конструктор"')
    def test_click_to_go_constructor(self, driver, main_page):
        main_page.click_on_button_order_feed()
        main_page.click_on_button_constructor()
        assert 'Соберите бургер' in main_page.get_text_constructor_title()

    @allure.title('Проверка перехода по клику на "Лента заказов"')
    def test_click_to_go_order_feed(self, driver, main_page, feed_page):
        main_page.click_on_button_order_feed()
        assert 'Лента заказов' in feed_page.get_text_on_orders_feed_title()

    @allure.title('Проверка отображения окна "Детали ингредиента"')
    def test_displaying_modal_window_ingredient_detail(self, driver, main_page):
        main_page.click_on_ingredient()
        assert main_page.check_displaying_ingredient_details()

    @allure.title('Проверка закрытия окна "Детали ингредиента" кликом по крестику')
    def test_close_modal_window_ingredient_detail(self, driver, main_page):
        main_page.click_on_ingredient()
        main_page.close_ingredient_details()
        assert main_page.check_not_displaying_ingredient_details()

    @allure.title('Проверка увеличения каунтера при добавлении ингредиента в заказ')
    def test_increasing_counter_when_adding_ingredient(self, driver, main_page):
        main_page.drag_and_drop_ingredient_to_order()
        assert main_page.get_count_of_ingredients_in_order() == '2'

    @allure.title('Проверка, что залогиненный пользователь может оформить заказ')
    def test_auth_user_can_place_order(self, driver, new_user_tokens, main_page):
        main_page.click_on_button_login_to_account()
        main_page.drag_and_drop_ingredient_to_order()
        main_page.click_on_button_place_order()
        assert main_page.check_displaying_of_confirmation_order_placement()