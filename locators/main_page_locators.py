from selenium.webdriver.common.by import By


class MainPageLocators:
    # Кнопка "Конструктор"
    CONSTRUCTOR_BUTTON = (By.XPATH, '//p[text() = "Конструктор"]')

    # Кнопка "Лента заказов"
    ORDER_FEED_BUTTON = (By.XPATH, '//p[text()="Лента Заказов"]/parent::a/parent::li')

    # Кнопка "Личный кабинет"
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, '//p[text()="Личный Кабинет"]/parent::a')

    # Кнопка "Войти в аккаунт"
    LOGIN_TO_ACCOUNT_BUTTON = By.XPATH, './/button[text() = "Войти в аккаунт"]'

    # Заголовок раздела "Конструктор"
    CONSTRUCTOR_HEADING = (By.XPATH, '//section[contains(@class, "BurgerIngredients_ingredients")]/h1')

    # Заголовок раздела "Булки"
    BUNS_HEADING = (By.XPATH, '//span[text() = "Булки"]')

    # Заголовок раздела "Соусы"
    SAUCES_HEADING = (By.XPATH, '//span[text() = "Соусы"]')

    # Заголовок раздела "Начинки"
    FILLINGS_HEADING = (By.XPATH, '//span[text() = "Начинки"]')

    # Активный раздел конструктора
    ACTIVE_SECTION_SELECTOR = (By.XPATH, ('//div[@class = '
                                          '"tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect"]'))

    # Ингредиент
    INGREDIENT = (By.XPATH, '(.//p[@class="BurgerIngredient_ingredienttextyp3dH"])[1]')

    # Ингредиент "Флюоресцентная булка R2-D3"
    BUN_R2_D3 = (By.XPATH, './/*[@alt="Флюоресцентная булка R2-D3"]')

    # Заголовок окна "Детали ингредиента"
    INGREDIENT_DETAIL_WINDOW_TITLE = (By.XPATH, '//h2[contains(@class, "Modal_modal__title") and contains(text(), "Детали")]')

    # Кнопка для закрытия окна "Детали ингредиента"
    INGREDIENT_DETAIL_CLOSE_BUTTON = (By.XPATH, '//section[contains(@class, '
                                                '"Modal_modal_opened")]//button[contains(@class, "close")]')

    # Блок для формирования бургера из ингредиентов
    BURGER_CONSTRUCTOR_BASKET = (By.XPATH, '//section[contains(@class, "BurgerConstructor_basket")]')

    # Состав заказа в корзине
    ORDER_CONTENTS_BASKET = (By.CSS_SELECTOR, '.constructor-element_pos_top .constructor-element__row')

    # Счетчик количества ингредиентов в заказе
    COUNTER_INGREDIENTS_IN_ORDER = (By.XPATH, "//p[@class='counter_counter__num__3nue1']")

    # Кнопка "Оформить заказ"
    PLACE_ORDER_BUTTON = (By.XPATH, '//button[text()="Оформить заказ"]')

    # Окно подтверждения заказа
    CONFIRMATION_ORDER_PLACEMENT = (By.XPATH, '//section[contains(@class, "Modal_modal_opened")]/div[contains'
                                             '(@class, "Modal_modal__container")]')

    # Номер заказа в окне подтверждения
    NUMBER_ORDER_IN_CONFIRMATION_WINDOW = (By.XPATH, '//section[contains(@class, "Modal_modal_opened")]//h2')

    # Кнопка для закрытия окна подтвержденного заказа
    CONFIRMATION_ORDER_CLOSE_BUTTON = (By.CSS_SELECTOR, ".Modal_modal__close_modified__3V5XS")