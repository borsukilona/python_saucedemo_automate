import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base
from utilities.logger import Logger


class CartPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    checkout_button = '//button[@id="checkout"]'

    cart_sum = '//div[@class="inventory_item_price"]'

    # Getters

    def get_checkout_button(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.checkout_button)))

    def get_cart_prices(self):
        return self.driver.find_elements(by=By.XPATH, value=self.cart_sum)

    # Actions

    def click_checkout(self):
        self.get_checkout_button().click()
        print('Checkout button clicked')

    # Methods

    # Make checkout

    def go_to_checkout(self):
        with allure.step("Go to checkout form"):
            Logger.add_start_step(method='go_to_checkout')
            self.get_current_url()
            self.click_checkout()
            self.assert_text(self.get_page_title(), 'Checkout: Your Information')
            Logger.add_end_step(url=self.get_current_url(), method='go_to_checkout')

    # Get cart price of the product by product number

    def get_cart_price_of_product(self, product_number_price):
        with allure.step(f"Product N{product_number_price} price displayed in the cart"):
            Logger.add_start_step(method='get_cart_price_of_product')
            for i in range(len(self.get_cart_prices())):
                if product_number_price == i:
                    print(f'Product N{product_number_price} = {self.get_cart_prices()[i].text}')
                    return self.get_cart_prices().text
            Logger.add_end_step(url=self.get_current_url(), method='get_cart_price_of_product')

    # Count cart sum

    def cart_price_sum(self):
        with allure.step("Calculate total sum of product prices from the cart"):
            Logger.add_start_step(method='cart_price_sum')
            prices = []

            for i in range(len(self.get_cart_prices())):
                prices.append(float(self.get_cart_prices()[i].text.replace('$', '')))

            cart_sum = sum(prices)
            print(f'Cart sum is {cart_sum}')

            [print(f'Product N{i+1} = ${el}') for i, el in enumerate(prices)]
            Logger.add_end_step(url=self.get_current_url(), method='cart_price_sum')

            return cart_sum











