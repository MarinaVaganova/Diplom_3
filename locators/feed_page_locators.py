from selenium.webdriver.common.by import By


class FeedPageLocators:
    # Заказ в разделе "В работе"
    ORDER_IN_PROGRESS = (By.XPATH, '//ul[contains(@class, "OrderFeed_orderListReady")]/li')

    # Номер заказа в разделе "В работе"
    ORDER_NUMBER_IN_PROGRESS = (By.XPATH, '//ul[contains(@class, '
                                             '"OrderFeed_orderListReady")]/li[contains(@class, '
                                             '"text_type_digits-default")]')

    # Счетчик "Выполнено за все время"
    COUNTER_COMPLETED_ALL_TIME = (By.XPATH, '//p[text()="Выполнено за все время:"]/following-sibling::p')

    # Счетчик "Выполнено за сегодня"
    COUNTER_COMPLETED_TODAY = (By.XPATH, '//p[text()="Выполнено за сегодня:"]/following-sibling::p')

    # Заголовок ленты заказов
    ORDERS_FEED_TITLE = (By.XPATH, '//div[contains(@class, "OrderFeed_orderFeed")]/h1')

    # Раздел c заказами
    ORDERS_FEED_LIST = (By.XPATH, '//ul[contains(@class, "OrderFeed_list")]')

    # Номер заказа в ленте (нужно подставить id заказа)
    ORDER_NUMBER_BY_ID = (By.XPATH, './/*[text()="{order_id}"]')

    # Карточка заказа в ленте
    ORDER_CARD_IN_ORDER_FEED = (By.XPATH, '//li[contains(@class, "OrderHistory_listItem")][1]')

    # Заголовок окна с деталями заказа
    ORDER_DETAILS_MODAL_WINDOW_TITLE = (By.XPATH, '//section[contains(@class, "Modal_modal_opened")]//div[contains(@class, '
                                      '"Modal_orderBox")]//h2')

    # Окно с деталями заказа
    ORDER_DETAILS_MODAL_WINDOW = (By.XPATH, '//section[contains(@class, "Modal_modal_opened")]//div[contains'
                             '(@class, "Modal_orderBox")]')