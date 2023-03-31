import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base
from utilities.logger import Logger


class CheckoutPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    first_name = '//input[@id="first-name"]'
    last_name = '//input[@id="last-name"]'
    postal_code = '//input[@id="postal-code"]'

    continue_button = '//input[@id="continue"]'
    cancel_button = '//button[@id="cancel"]'

    # Getters

    def get_first_name(self):
        return WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, self.first_name)))

    def get_last_name(self):
        return WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, self.last_name)))

    def get_postal_code(self):
        return WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, self.postal_code)))

    def get_continue_button(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.continue_button)))

    def get_cancel_button(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.cancel_button)))

    # Actions

    def input_first_name(self, name):
        self.get_first_name().send_keys(name)
        print(f'Input first name: {name}')

    def input_last_name(self, lastname):
        self.get_last_name().send_keys(lastname)
        print(f'Input last name: {lastname}')

    def input_postal_code(self, code):
        self.get_postal_code().send_keys(code)
        print(f'Input postal code: {code}')

    def click_continue_button(self):
        self.get_continue_button().click()
        print('Continue checkout button clicked')

    def click_cancel_button(self):
        self.get_cancel_button().click()
        print('Cancel checkout button clicked')

    # Methods

    def continue_checkout(self):
        with allure.step("Continue checkout: fill in the fields and continue"):
            Logger.add_start_step(method='continue_checkout')
            self.get_current_url()
            self.input_first_name('Ilona')
            self.input_last_name('Borsuk')
            self.input_postal_code('220047')
            self.click_continue_button()
            self.assert_text(self.get_page_title(), 'Checkout: Overview')
            Logger.add_end_step(url=self.get_current_url(), method='continue_checkout')

    def cancel_checkout_filled_in(self):
        with allure.step("Cancel checkout process: form fields are filled in"):
            Logger.add_start_step(method='cancel_checkout_filled_in')
            self.get_current_url()
            self.input_first_name('Ilona')
            self.input_last_name('Borsuk')
            self.input_postal_code('220047')
            self.click_cancel_button()
            self.assert_text(self.get_page_title(), 'Your Cart')
            Logger.add_end_step(url=self.get_current_url(), method='cancel_checkout_filled_in')

    def cancel_checkout_empty(self):
        with allure.step("Cancel checkout process: form fields are empty"):
            Logger.add_start_step(method='cancel_checkout_empty')
            self.get_current_url()
            self.click_cancel_button()
            self.assert_text(self.get_page_title(), 'Your Cart')
            Logger.add_end_step(url=self.get_current_url(), method='cancel_checkout_empty')













