import time

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base
from utilities.logger import Logger


class MainPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    products_add = '//div[@class="pricebar"]/button'
    cart = '//div[@id="shopping_cart_container"]'
    cart_badge = '//span[@class="shopping_cart_badge"]'

    # Getters

    def get_products_add(self):
        return self.driver.find_elements(by=By.XPATH, value=self.products_add)

    def get_cart(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.cart)))

    def get_cart_badge(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.cart_badge)))

    # Actions

    def add_product_to_cart(self, product_number):
        self.get_products_add()[product_number].click()
        print(f'Add product N{product_number+1} to the cart - clicked')

    def enter_cart(self):
        self.get_cart().click()
        print('Cart clicked = entered')

    # Methods

    def select_product_and_go_to_cart(self, product_number):
        with allure.step(f"Select one product N{product_number} and go further to the cart"):
            Logger.add_start_step(method='select_product_and_go_to_cart')
            self.get_current_url()
            self.add_product_to_cart(product_number)
            self.check_exists_by_xpath(self.cart_badge)  # появился ли красный кружок у корзины
            self.assert_text(self.get_cart_badge(), '1')  # соответствует ли число в красном кружке числу выбранных товаров
            time.sleep(3)
            self.enter_cart()
            self.assert_text(self.get_page_title(), 'Your Cart')
            self.assert_url('https://www.saucedemo.com/cart.html')
            Logger.add_end_step(url=self.get_current_url(), method='select_product_and_go_to_cart')

    def select_products(self, *args):
        with allure.step(f"Select several products N {list(args)} and check cart badge value displayed"):
            Logger.add_start_step(method='select_products')
            for product_number in args:
                self.add_product_to_cart(product_number)
            self.check_exists_by_xpath(self.cart_badge)
            self.assert_text(self.get_cart_badge(), str(len(args)))
            Logger.add_end_step(url=self.get_current_url(), method='select_products')





















