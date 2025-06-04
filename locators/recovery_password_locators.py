from selenium.webdriver.common.by import By


class RecoveryPasswordLocators:
    # Кнопка "Восстановить пароль"
    RECOVER_PASSWORD_BUTTON = By.XPATH, '//a[text() = "Восстановить пароль"]'

    # Поле ввода Email
    EMAIL_INPUT_FIELD = (By.CLASS_NAME, 'input__textfield')

    # Кнопка "Восстановить"
    RECOVER_BUTTON = (By.CLASS_NAME, 'button_button__33qZ0')

    # Поле ввода пароля
    PASSWORD_INPUT_FIELD = (By.CSS_SELECTOR, '.input_type_password .input__textfield')

    # Кнопка для отображения пароля
    SHOW_PASSWORD_BUTTON = (By.CSS_SELECTOR, '.input__icon')

    # Пароль отображается
    PASSWORD_VISIBLE = (By.XPATH, "//input[@name='Введите новый пароль' and @type='text']")

    # Пароль скрыт
    PASSWORD_INVISIBLE = (By.XPATH, "//input[@name='Введите новый пароль' and @type='password']")