import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base
from base.driver_class import Driver
from utilities.logger import Logger


class Menu(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    menu_button = '//button[@id="react-burger-menu-btn"]'

    all_items_menu = '//a[@id="inventory_sidebar_link"]'
    logout_menu = '//a[@id="logout_sidebar_link"]'
    about_menu = '//a[@id="about_sidebar_link"]'
    reset_app_set_menu = '//a[@id="reset_sidebar_link"]'

    products_add = '//div[@class="pricebar"]/button'

    # Getters

    def get_menu(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.menu_button)))

    def get_all_items_button(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.all_items_menu)))

    def get_about_button(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.about_menu)))

    def get_logout_button(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.logout_menu)))

    def get_reset_button(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.reset_app_set_menu)))

    def get_products_add(self):
        return self.driver.find_elements(by=By.XPATH, value=self.products_add)

    # Actions

    def click_menu(self):
        self.get_menu().click()
        print("Menu clicked")

    def click_all_items(self):
        self.get_all_items_button().click()
        print("'All Items' clicked")

    def click_about(self):
        self.get_about_button().click()
        print("'About' clicked")

    def click_logout(self):
        self.get_logout_button().click()
        print("'Logout' clicked")

    def click_reset(self):
        self.get_reset_button().click()
        print("'Reset App State' clicked")

    # Methods

    def choose_all_items(self):
        with allure.step("Choose 'All Items' menu point"):
            Logger.add_start_step(method='choose_all_items')
            self.click_menu()
            self.click_all_items()
            self.assert_url('https://www.saucedemo.com/inventory.html')
            Logger.add_end_step(url=self.get_current_url(), method='choose_all_items')

    def choose_about(self):
        with allure.step("Choose 'About' menu point"):
            Logger.add_start_step(method='choose_about')
            self.click_menu()
            self.click_about()
            self.assert_url('https://saucelabs.com/')
            Logger.add_end_step(url=self.get_current_url(), method='choose_about')

    def logout(self):
        with allure.step("Choose 'Logout' menu point"):
            Logger.add_start_step(method='logout')
            self.click_menu()
            self.click_logout()
            self.assert_url('https://www.saucedemo.com/')
            Logger.add_end_step(url=self.get_current_url(), method='logout')

    def choose_reset(self):
        with allure.step("Choose 'Reset App State' menu point and check the state of the page"):
            Logger.add_start_step(method='choose_reset')
            self.click_menu()
            self.click_reset()
            #self.make_screenshot(),
            self.take_allure_screenshot()
            self.check_exists_by_xpath('//span[@class="shopping_cart_badge"]')

            products = self.get_products_add()
            for i in range(len(products)):
                self.assert_text(products[i], 'Add to cart')

            Logger.add_end_step(url=self.get_current_url(), method='choose_reset')











