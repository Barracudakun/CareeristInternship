from pages.base_page import BasePage
from selenium.webdriver.common.by import By

firstItem = (By.CSS_SELECTOR, '.product-title a')

class MainPage(BasePage):
    def open_main(self):
        self.open_url('https://gettop.us/')

    def click_firstItem_on_lastProductOnSale(self):
        self.click(*firstItem)