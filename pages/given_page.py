from selenium.webdriver.common.by import By
from pages.base_page import BasePage

BACKARROW = (By.CSS_SELECTOR, '#product-sidebar .icon-angle-left')
FORWARDARROW = (By.CSS_SELECTOR, '#product-sidebar .icon-angle-right')
PRODUCTITLE = (By.XPATH, "//h1[@class='product-title product_title entry-title']")

class GivenPage(BasePage):
    def given_page(self):
        self.open_url('https://gettop.us/product/macbook-pro-16/')

    def click_back_arrows(self):
        self.click(*BACKARROW)

    def click_forward_arrows(self):
        self.click(*FORWARDARROW)

    def get_product_title(self):
        self.get_text(*PRODUCTITLE)

