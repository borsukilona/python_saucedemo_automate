import allure

from base.driver_class import Driver
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.login_page import LoginPage
from pages.main_product_page import MainPage


@allure.description('Test error messages when checkout')
def test_error_message_checkout():
    driver = Driver().get_driver()

    login = LoginPage(driver)
    login.open_url()
    login.authorization()

    main = MainPage(driver)
    main.select_product_and_go_to_cart(1)

    cart = CartPage(driver)
    cart.click_checkout()

    checkout = CheckoutPage(driver)
    checkout.check_no_firstname_checkout()
    driver.refresh()

    checkout.check_no_lastname_checkout()
    driver.refresh()

    checkout.check_no_postalcode_checkout()
    driver.refresh()




