from selenium import webdriver

from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService

from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class conexao():

    def __init__(self, browser):
        self.browser = browser



    def selecionaBrowser(self):
        if self.browser == 'Chrome':
            self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        elif self.browser == 'Firefox':
            self.driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

        return self.driver
