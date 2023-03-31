import allure

from base.driver_class import Driver
from pages.login_page import LoginPage


@allure.description('Test error messages while login')
def test_error_login_message():
    driver = Driver().get_driver()

    print("Start test")

    login = LoginPage(driver)

    login.open_url()

    login.check_wrong_login()
    driver.refresh()

    login.check_no_password_login()
    driver.refresh()

    login.check_no_username_login()
    driver.refresh()

    login.check_blocked_user_login()
    driver.refresh()

    driver.close()

    print("Finish test")


@allure.description('Test login with different users one by one')
def test_login_with_users():
    driver = Driver().get_driver()

    print("Start test")

    login = LoginPage(driver)
    login.authorize_with_dif_users()

    driver.close()

    print("Finish test")


