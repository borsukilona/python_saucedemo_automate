import time
import allure

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base
from base.menu_class import Menu
from utilities.logger import Logger


class LoginPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    user_name = '//input[@id="user-name"]'
    password = '//input[@id="password"]'
    login_button = '//input[@id="login-button"]'

    login_warning = '//h3[@data-test="error"]'

    # Getters

    def get_user_name(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.user_name)))

    def get_password(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.password)))

    def get_login_button(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.login_button)))

    def get_login_warning_message(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.login_warning)))

    # Actions

    def input_user_name(self, username):
        self.get_user_name().send_keys(username)
        print(f"Input login: {username}")

    def input_password(self, pwd):
        self.get_password().send_keys(pwd)
        print(f"Input password: {pwd}")

    def click_login_button(self):
        self.get_login_button().click()
        print("Click login button")

    # Methods

    # Authorize

    def authorization(self):
        with allure.step("Authorization"):
            Logger.add_start_step(method='authorization')
            self.open_url()
            self.input_user_name("standard_user")
            self.input_password("secret_sauce")
            self.click_login_button()
            self.assert_text(self.get_page_title(), "Products")
            Logger.add_end_step(url=self.get_current_url(), method='authorization')

    # Error messages when logging in

    def check_wrong_login(self):
        with allure.step("Authorization with wrong Username / Password"):
            Logger.add_start_step(method='check_wrong_login')
            self.input_user_name("wrong_username")
            self.input_password("secret_sauce")
            self.click_login_button()
            self.assert_text(self.get_login_warning_message(),
                             "Epic sadface: Username and password do not match any user in this service")
            self.driver.refresh()
            self.input_user_name("standard_us")
            self.input_password("wrong_password")
            self.click_login_button()
            self.assert_text(self.get_login_warning_message(),
                             "Epic sadface: Username and password do not match any user in this service")
            Logger.add_end_step(url=self.get_current_url(), method='check_wrong_login')

    def check_no_username_login(self):
        with allure.step("Authorization witn empty Username"):
            Logger.add_start_step(method='check_no_username_login')
            self.input_user_name("")
            self.input_password("secret_sauce")
            self.click_login_button()
            self.assert_text(self.get_login_warning_message(),
                             "Epic sadface: Username is required")
            Logger.add_end_step(url=self.get_current_url(), method='check_no_username_login')

    def check_no_password_login(self):
        with allure.step("Authorization with empty Password"):
            Logger.add_start_step(method='check_no_password_login')
            self.input_user_name("standard_user")
            self.input_password("")
            self.click_login_button()
            self.assert_text(self.get_login_warning_message(),
                             "Epic sadface: Password is required")
            Logger.add_end_step(url=self.get_current_url(), method='check_no_password_login')

    def check_blocked_user_login(self):
        with allure.step("Authorization with Locked User"):
            Logger.add_start_step(method='check_blocked_user_login')
            self.input_user_name("locked_out_user")
            self.input_password("secret_sauce")
            self.click_login_button()
            self.assert_text(self.get_login_warning_message(),
                             "Epic sadface: Sorry, this user has been locked out.")
            Logger.add_end_step(url=self.get_current_url(), method='check_blocked_user_login')

    # Login with different users

    def authorize_with_credentials(self, username, pwd):
        with allure.step(f"Authorization with credentials: {username}, {pwd}"):
            Logger.add_start_step(method='authorize_with_credentials')
            self.input_user_name(username)
            self.input_password(pwd)
            self.click_login_button()
            Logger.add_end_step(url=self.get_current_url(), method='authorize_with_credentials')

    def authorize_with_dif_users(self):
        with allure.step("Authorization with different system users one by one"):
            Logger.add_start_step(method='authorize_with_dif_users')
            login_names = {1: 'standard_user',
                           2: 'locked_out_user',
                           3: 'problem_user',
                           4: 'performance_glitch_user'}

            password_all = 'secret_sauce'

            for i in range(1, len(login_names) + 1):
                self.open_url()

                self.authorize_with_credentials(login_names.get(i), password_all)
                print(f'Login with {login_names.get(i)}')
                print(f'URL after authorization try: {self.get_current_url()}')
                time.sleep(2)

                if self.get_current_url() == 'https://www.saucedemo.com/':
                    self.assert_text(self.get_login_warning_message(),
                                     'Epic sadface: Sorry, this user has been locked out.')
                    print(f'Warning message "{self.get_login_warning_message().text}" displayed')
                    self.driver.refresh()
                    time.sleep(2)
                else:
                    menu = Menu(self.driver)
                    menu.logout()
                    print(f'Logout with {login_names.get(i)}')
            Logger.add_end_step(url=self.get_current_url(), method='authorize_with_dif_users')

    # Clear the login inputs

    def clear_auth_inputs(self):
        with allure.step("Clear username / password fields"):
            Logger.add_start_step(method='clear_auth_inputs')
            self.get_user_name().clear()
            self.get_password().clear()
            Logger.add_end_step(url=self.get_current_url(), method='clear_inputs')













