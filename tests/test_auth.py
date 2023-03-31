import allure

from base.driver_class import Driver
from pages.login_page import LoginPage


def test_auth():
    driver = Driver().get_driver()

    login = LoginPage(driver)
    login.authorization()

