import datetime
import time

import allure
from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utilities.logger import Logger


class Base:

    # URL

    base_url = 'https://www.saucedemo.com/'

    # Common Locators

    page_title = '//span[@class="title"]'

    # Methods

    def __init__(self, driver):
        self.driver = driver

    """
    Method: open url
    """

    def open_url(self):
        with allure.step("Open test url and maximize window"):
            Logger.add_start_step(method='open_url')
            self.driver.get(self.base_url)
            self.driver.maximize_window()
            self.get_current_url()
            Logger.add_end_step(url=self.get_current_url(), method='open_url')

    """
    Method: get current url
    """

    def get_current_url(self):
        with allure.step("Get current URL and return it"):
            get_url = self.driver.current_url
            print(f"Current URL: {get_url}")
            return get_url

    """
    Method: get page title
    """

    def get_page_title(self):
        with allure.step("Get page tite and return it"):
            Logger.add_start_step(method='get_page_title')
            title = WebDriverWait(self.driver, 30).until(
                EC.visibility_of_element_located((By.XPATH, self.page_title)))
            print(f"Current page title: '{title.text}'")
            Logger.add_end_step(url=self.get_current_url(), method='get_page_title')
            return title

    """
    Method: making screenshot and save it locally 
    """

    def make_screenshot(self):
        with allure.step("Make screenshot"):
            Logger.add_start_step(method='make_screenshot')
            now_date = datetime.datetime.utcnow().strftime("%Y.%m.%d.%H.%M.%S")
            name_screenshot = f'screenshot{now_date}.png'
            time.sleep(2)
            self.driver.save_screenshot(f"C:\\Users\\Ilona\\Documents\\main_project\\screen\\{name_screenshot}")
            print('---Screenshot made---')
            Logger.add_end_step(url=self.get_current_url(), method='make_screenshot')

    """
        Method: Make screenshot and send it to Allure report
        """

    def take_allure_screenshot(self):
        now_date = datetime.datetime.utcnow().strftime("%Y.%m.%d.%H.%M.%S")
        name_screenshot = f'screenshot{now_date}.png'
        time.sleep(2)
        allure.attach(self.driver.get_screenshot_as_png(),
                      name=name_screenshot,
                      attachment_type=allure.attachment_type.PNG)

    """
    Method: assert page text
    """

    def assert_text(self, text, result):
        with allure.step("Assert actual text with the expected text result"):
            Logger.add_start_step(method='assert_text')
            value_text = text.text
            assert value_text == result, \
                f'Wrong result:' \
                f'\nThe message displayed: "{value_text}"' \
                f'\nThe message expected: "{result}"'
            print(f"Text result: '{result}' --- PASSED")
            Logger.add_end_step(url=self.get_current_url(), method='assert_text')

    """
    Method: assert current URL
    """

    def assert_url(self, result):
        with allure.step("Assert current URL with the expected URL"):
            Logger.add_start_step(method='assert_url')
            get_url = self.driver.current_url
            assert get_url == result, \
                f'Wrong result:' \
                f'\nCurrent URL: "{self.get_current_url()}"' \
                f'\nURL expected: "{result}"'
            print(f"Current URL result: '{result}' --- PASSED")
            Logger.add_end_step(url=self.get_current_url(), method='assert_url')

    """
    Method: If the element exists on page
    """

    def check_exists_by_xpath(self, xpath):
        with allure.step("Check if an element exists / could be found on the page"):
            Logger.add_start_step(method='check_exists_by_xpath')
            try:
                WebDriverWait(self.driver, 30).until(
                    EC.visibility_of_element_located((By.XPATH, xpath)))
            except NoSuchElementException:
                print("No such element on the page - No Such Element Exception")
                return False
            except TimeoutException:
                print("No such element on the page - Timeout Exception")
                return False
            print("Element exists - TRUE")
            Logger.add_end_step(url=self.get_current_url(), method='check_exists_by_xpath')
            return True











