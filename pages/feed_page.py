import allure

from pages.base_page import BasePage
from locators.feed_page_locators import FeedPageLocators


class FeedPage(BasePage):
    @allure.step('Получение номера последнего заказа в разделе "В работе"')
    def get_order_number_in_progress(self):
        return self.get_text_on_element(FeedPageLocators.ORDER_NUMBER_IN_PROGRESS)

    @allure.step('Получение текста заголовка раздела заказов')
    def get_text_on_orders_feed_title(self):
        return self.get_text_on_element(FeedPageLocators.ORDERS_FEED_TITLE)

    @allure.step('Нажатие на первый (последний) заказ в ленте')
    def click_on_order_card_in_order_feed(self):
        self.wait_visibility_of_element(FeedPageLocators.ORDER_CARD_IN_ORDER_FEED)
        self.click_on_element(FeedPageLocators.ORDER_CARD_IN_ORDER_FEED)

    @allure.step('Получение текста заголовка окна с деталями заказа')
    def get_text_on_order_details_modal_title(self):
        return self.get_text_on_element(FeedPageLocators.ORDER_DETAILS_MODAL_WINDOW_TITLE)

    @allure.step('Получение количества заказов, выполненных за все время')
    def get_counter_completed_all_time(self):
        self.find_element_on_page(FeedPageLocators.COUNTER_COMPLETED_ALL_TIME)
        return self.get_text_on_element(FeedPageLocators.COUNTER_COMPLETED_ALL_TIME)

    @allure.step('Получение количества заказов, выполненных за сегодня')
    def get_counter_completed_today(self):
        self.find_element_on_page(FeedPageLocators.COUNTER_COMPLETED_TODAY)
        return self.get_text_on_element(FeedPageLocators.COUNTER_COMPLETED_TODAY)

    @allure.step('Проверка наличия номера заказа в списке ленты')
    def check_id_order_in_feed(self, order_id):
        locator = FeedPageLocators.ORDER_NUMBER_BY_ID
        locator_with_order_id = (locator[0], locator[1].format(order_id=order_id))
        self.find_element_on_page(locator_with_order_id)
        return self.check_element_display(locator_with_order_id)