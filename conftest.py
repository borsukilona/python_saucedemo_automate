import io
import os

import allure
import pytest
from allure_commons.types import AttachmentType
import pyautogui

from base.driver_class import Driver
driver = Driver().get_driver()


@pytest.fixture()  # будет применяться для каждой функции в модуле, где укажем
def set_up():
    print('Start test')
    yield  # here will be our test work
    print('Finish test')


@pytest.fixture(scope="module")  # будет применяться для всего модуля целиком
def set_group():
    print('Enter system')
    yield  # here will be our test work
    print('Exit system')


'''
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport():
    outcome = yield
    rep = outcome.get_result()
    if rep.failed:
        allure.attach(driver.get_screenshot_as_png(),
                      name="Screenshot",
                      attachment_type=allure.attachment_type.PNG)
'''
