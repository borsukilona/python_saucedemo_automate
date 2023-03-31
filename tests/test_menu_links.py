import time

import allure
import pytest

from base.driver_class import Driver
from base.menu_class import Menu
from pages.login_page import LoginPage
from pages.main_product_page import MainPage


def test_link_about():
    driver = Driver().get_driver()

    print("Start test")

    login = LoginPage(driver)
    login.authorization()

    menu = Menu(driver)
    menu.choose_about()

    driver.close()

    print("Finish test")


def test_link_logout():
    driver = Driver().get_driver()

    print("Start test")

    login = LoginPage(driver)
    login.authorization()

    menu = Menu(driver)
    menu.logout()

    driver.close()

    print("Finish test")


def test_link_items():
    driver = Driver().get_driver()

    print("Start test")

    login = LoginPage(driver)
    login.authorization()

    main = MainPage(driver)
    main.select_product_and_go_to_cart(0)

    menu = Menu(driver)
    menu.choose_all_items()


def test_link_reset():
    driver = Driver().get_driver()

    print("Start test")

    login = LoginPage(driver)
    login.authorization()

    main = MainPage(driver)
    main.select_products(0, 1, 2)

    menu = Menu(driver)
    menu.choose_reset()









    

