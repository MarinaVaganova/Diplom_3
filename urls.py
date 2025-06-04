class URLs:
    MAIN_PAGE = 'https://stellarburgers.nomoreparties.site'
    ACCOUNT_PAGE = f'{MAIN_PAGE}/account/profile'
    ORDER_HISTORY_PAGE = f'{MAIN_PAGE}/account/order-history'
    FEED_PAGE = f'{MAIN_PAGE}/feed'
    LOGIN_PAGE = f'{MAIN_PAGE}/login'
    FORGOT_PASSWORD_PAGE = f'{MAIN_PAGE}/forgot-password'
    RESET_PASSWORD_PAGE = f'{MAIN_PAGE}/reset-password'

    # Ручки API
    USER_REGISTRATION = f'{MAIN_PAGE}/api/auth/register'
    USER_DELETE = f'{MAIN_PAGE}/api/auth/user'
    ORDER_CREATE = f'{MAIN_PAGE}/api/orders'