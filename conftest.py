import requests
import pytest

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from pages.account_page import AccountPage
from pages.main_page import MainPage
from pages.feed_page import FeedPage
from pages.recovery_password_page import RecoveryPasswordPage
from urls import URLs
from helpers import *


@pytest.fixture(params=[webdriver.Chrome, webdriver.Firefox], ids=['chrome','firefox'], scope='function')
def driver(request):
    if request.param == webdriver.Chrome:
        chrome_options = Options()
        chrome_options.add_argument('--window-size=1920,1080')
        chrome_options.add_argument('--incognito')
        driver = webdriver.Chrome(options=chrome_options)
    elif request.param == webdriver.Firefox:
        firefox_options = webdriver.FirefoxOptions()
        firefox_options.add_argument('--width=1920')
        firefox_options.add_argument('--height=1080')
        profile = FirefoxProfile()
        profile.set_preference('browser.privatebrowsing.autostart', True)
        firefox_options.profile = profile
        driver = webdriver.Firefox(options=firefox_options)
    driver.get(URLs.MAIN_PAGE)
    yield driver
    driver.quit()

@pytest.fixture
def create_and_delete_new_user():
    payload = {
        'email': create_random_email(),
        'password': create_random_password(),
        'name': create_random_name()
    }
    response = requests.post(URLs.USER_REGISTRATION, data=payload)
    response_body = response.json()
    yield payload, response_body
    token = response_body['accessToken']
    requests.delete(URLs.USER_DELETE, headers={'Authorization': token})

#@pytest.fixture
#def create_user():
    #email = create_random_email()
    #password = create_random_password()
    #name = create_random_name()
    #return email, password, name

@pytest.fixture
def create_and_delete_user_and_order(create_and_delete_new_user):
    token = create_and_delete_new_user[1]['accessToken']
    headers = {'Authorization': token}
    payload = {'ingredients': [
            '61c0c5a71d1f82001bdaaa6d','61c0c5a71d1f82001bdaaa74','61c0c5a71d1f82001bdaaa6f'
        ]}
    response_body = requests.post(URLs.ORDER_CREATE, data=payload, headers=headers)
    yield token, response_body
    requests.delete(URLs.USER_DELETE, headers={'Authorization': token})

@pytest.fixture
def new_user_tokens(driver, create_and_delete_new_user):
    driver.get(URLs.MAIN_PAGE)
    user_data = create_and_delete_new_user[1]
    token = user_data.get('accessToken')
    token_refresh = user_data.get('refreshToken')
    driver.execute_script(f'window.localStorage.setItem("accessToken", "{token}");')
    driver.execute_script(f'window.localStorage.setItem("refreshToken", "{token_refresh}");')

@pytest.fixture
def account_page(driver):
    return AccountPage(driver)

@pytest.fixture
def main_page(driver):
    return MainPage(driver)

@pytest.fixture
def feed_page(driver):
    return FeedPage(driver)

@pytest.fixture
def recovery_page(driver):
    return RecoveryPasswordPage(driver)