import allure


@allure.feature('Раздел "Лента заказов"')
class TestFeedPage:
    @allure.title('Проверка открытия всплывающего окна с деталями при клике на заказ')
    def test_display_modal_window_order_details(self, driver, main_page, feed_page):
        main_page.click_on_button_order_feed()
        feed_page.click_on_order_card_in_order_feed()
        assert 'бургер' in feed_page.get_text_on_order_details_modal_title()

    @allure.title('Проверка отображения заказов пользователя из "История заказов" в "Лента заказов"')
    def test_display_order_in_feed_page_and_order_history(self, driver, create_and_delete_user_and_order, new_user_tokens, main_page, feed_page, account_page):
        main_page.click_on_button_personal_account()
        account_page.click_on_order_history_section()
        order_number = account_page.get_number_of_order_card()
        main_page.click_on_button_order_feed()
        assert feed_page.check_id_order_in_feed(order_number)

    @allure.title('Проверка увеличения счетчика "Выполнено за все время" при создании нового заказа')
    def test_increase_counter_completed_all_time(self, driver, new_user_tokens, main_page, feed_page):
        main_page.click_on_button_order_feed()
        orders_count_old = feed_page.get_counter_completed_all_time()
        main_page.click_on_button_constructor()
        main_page.click_on_button_login_to_account()
        main_page.drag_and_drop_ingredient_to_order()
        main_page.click_on_button_place_order()
        main_page.check_displaying_of_confirmation_order_placement()
        main_page.get_number_order_in_confirmation_window()
        main_page.click_on_button_close_confirmation_order()
        main_page.click_on_button_order_feed()
        orders_count_new = feed_page.get_counter_completed_all_time()
        assert orders_count_new > orders_count_old

    @allure.title('Проверка увеличения счетчика "Выполнено за сегодня" при создании нового заказа')
    def test_increase_counter_completed_today(self, driver, new_user_tokens, main_page, feed_page):
        main_page.click_on_button_order_feed()
        orders_count_old = feed_page.get_counter_completed_today()
        main_page.click_on_button_constructor()
        main_page.click_on_button_login_to_account()
        main_page.drag_and_drop_ingredient_to_order()
        main_page.click_on_button_place_order()
        main_page.check_displaying_of_confirmation_order_placement()
        main_page.get_number_order_in_confirmation_window()
        main_page.click_on_button_close_confirmation_order()
        main_page.click_on_button_order_feed()
        orders_count_new = feed_page.get_counter_completed_today()
        assert orders_count_new > orders_count_old

    @allure.title('Проверка появления номера заказа в разделе "В работе"')
    def test_display_new_order_in_progress(self, driver, new_user_tokens, main_page, feed_page):
        main_page.click_on_button_login_to_account()
        main_page.drag_and_drop_ingredient_to_order()
        main_page.click_on_button_place_order()
        main_page.check_displaying_of_confirmation_order_placement()
        new_order = main_page.get_number_order_in_confirmation_window()
        main_page.click_on_button_close_confirmation_order()
        main_page.click_on_button_order_feed()
        assert feed_page.get_order_number_in_progress() == '0'+new_order