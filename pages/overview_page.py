import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base
from pages.cart_page import CartPage
from utilities.logger import Logger


class OverviewPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    finish_button = '//button[@id="finish"]'

    total_sum = '//div[@class="summary_subtotal_label"]'

    # Getters

    def get_finish_button(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.finish_button)))

    def get_total_sum(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.total_sum)))

    # Actions

    def click_finish_button(self):
        self.get_finish_button().click()
        print('Finish button clicked')

    # Methods

    def finish_purchase(self):
        with allure.step("Click FINISH on Overview page"):
            Logger.add_start_step(method='finish_purchase')
            self.get_current_url()
            self.click_finish_button()
            self.assert_text(self.get_page_title(), 'Checkout: Complete!')
            Logger.add_end_step(url=self.get_current_url(), method='finish_purchase')

    def check_total(self):
        with allure.step("If total sum of the purchase in Overview page corresponds with the total sum of the "
                         "purchase in the Cart"):
            Logger.add_start_step(method='check_total')
            value_total_sum = self.get_total_sum().text
            print(f'Total sum is {value_total_sum.split()[2]}')
            cart = CartPage(self.driver)
            assert value_total_sum.split()[2].replace("$", '') == str(cart.cart_price_sum()), \
                "Product price from Cart doesn't correspond to the total sum"
            print(f'---{value_total_sum.split()[2].replace("$", "")} == {str(cart.cart_price_sum())}---')
            print("---Price Cart == Total sum PASSED---")
            Logger.add_end_step(url=self.get_current_url(), method='check_total')















