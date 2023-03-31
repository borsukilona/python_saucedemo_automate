import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base
from utilities.logger import Logger


class FinishPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    # Getters

    # Methods

    def do_finish_screen(self):
        with allure.step("Making screenshot of the finish page (after 'buy product' process finished)"):
            Logger.add_start_step(method='do_finish_screen')
            self.get_current_url()
            self.assert_url('https://www.saucedemo.com/checkout-complete.html')
            self.assert_text(self.get_page_title(), 'Checkout: Complete!')
            self.make_screenshot()
            Logger.add_end_step(url=self.get_current_url(), method='do_finish_screen')














