from selenium.webdriver.common.by import By


class AccountPageLocators:
    # Кнопка "Войти"
    LOGIN_BUTTON = (By.XPATH, '//button[text()="Войти"]')

    # Кнопка "Зарегистрироваться"
    REGISTER_BUTTON = By.XPATH, '//a[text() = "Зарегистрироваться"]'

    # Раздел "Профиль" в ЛК
    PROFILE_SECTION = (By.XPATH, '//a[@href = "/account/profile"]')

    # Кнопка "Выход" в ЛК
    LOGOUT_BUTTON = (By.XPATH, '//button[@type = "button"]')

    # "В этом разделе вы можете изменить свои персональные данные"
    SECTION_DESCRIPTION = (By.XPATH, '//p[contains(@class, "Account_text")]')

    # Раздел "История заказов" в ЛК
    ORDER_HISTORY_SECTION = (By.XPATH, '//a[@href = "/account/order-history"]')

    # Карточка заказа в разделе "История заказов"
    ORDER_CARD_IN_HISTORY_SECTION = (By.XPATH, '//*[contains(@class, "OrderHistory_listItem")]')

    # Номер заказа в карточке заказа в разделе "История заказов"
    ORDER_CARD_NUMBER_IN_HISTORY_SECTION = (By.XPATH, '(//div[contains(@class, "OrderHistory_textBox")]'
                               '/p[contains(@class, "text_type_digits-default")])[1]')

    # Название бургера в карточке заказа в разделе "История заказов"
    ORDER_CARD_TITLE_IN_HISTORY_SECTION = (By.XPATH, '//*[contains(@class, "OrderHistory_listItem")]//h2')