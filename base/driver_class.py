from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service


class Driver:

    def get_driver(self):
        options = Options()
        options.add_experimental_option("excludeSwitches",
                                    ['enable-logging'])  # это чтоб говна в консоли не было при запуске тестов
        options.add_experimental_option("detach",
                                    True)  # это чтоб не браузер не закрывался сразу как отработает тест, ибо бесить
        path = 'C:\\Users\\Ilona\\Documents\\Resources\\chromedriver.exe'
        service = Service(path)
        driver = webdriver.Chrome(options=options, service=service)
        return driver




