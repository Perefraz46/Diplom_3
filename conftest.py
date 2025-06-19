import pytest
from selenium import webdriver
from data import Data
from methods.auth_service import AuthService
from methods.user_service import UserService


@pytest.fixture(params=['chrome', 'firefox'])
def driver(request):
    browser = None
    if request.param == 'chrome':
        browser = webdriver.Chrome()
        browser.set_window_size(1920, 1080)
    elif request.param == 'firefox':
        browser = webdriver.Firefox()
        browser.set_window_size(1920, 1080)
    yield browser
    browser.quit()


@pytest.fixture
def create_user():
    user_data = Data.generate_user()
    UserService.register_user(user_data)
    yield user_data
    token = AuthService.get_auth_token(user_data)
    UserService.delete_user(token)
