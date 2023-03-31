import pytest
import allure

from base.driver_class import Driver
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.login_page import LoginPage
from pages.main_product_page import MainPage
from pages.overview_page import OverviewPage
from pages.finish_page import FinishPage


# @pytest.mark.run(order=3)
@allure.description('Test "buy one product"')
def test_buy_one_product(set_up, set_group):
    driver = Driver().get_driver()

    print("Start test")

    login = LoginPage(driver)
    login.authorization()

    product = MainPage(driver)
    product.select_product_and_go_to_cart(0)  # you can choose one product to add to the cart and go to the cart further

    checkout = CartPage(driver)
    checkout.go_to_checkout()
    
    make_checkout = CheckoutPage(driver)
    make_checkout.continue_checkout()

    overview = OverviewPage(driver)
    overview.finish_purchase()

    finish = FinishPage(driver)
    finish.do_finish_screen()

    driver.close()

    print("Finish test")

# запустить конкретный тест (терминал): python -m pytest -svk test_buy_product_3
# отчет allure загрузить на сервер:
# 1. в терминале пайчарма: python -m pytest --alluredir=test_results/ tests/test_buy_product.py
# 2. в командной строке компа перейти в директорию проекта: cd C:\Users\Ilona\Documents\main_project
# 3. затем в той же командной строке: allure serve test_results


@allure.description('Test "buy several product"')
def test_buy_several_products(set_up):
    driver = Driver().get_driver()

    print("Start test")

    login = LoginPage(driver)
    login.authorization()

    product = MainPage(driver)
    product.select_products(0, 1)  # you can choose several products here and add them to the cart one by one
    product.get_cart().click()

    checkout = CartPage(driver)
    checkout.go_to_checkout()

    make_checkout = CheckoutPage(driver)
    make_checkout.continue_checkout()

    overview = OverviewPage(driver)
    overview.check_total()

    overview.finish_purchase()

    finish = FinishPage(driver)
    finish.do_finish_screen()

    driver.close()

    print("Finish test")

