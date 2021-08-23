from selenium.webdriver.common.by import By
from pages.base_page import BasePage

PLUSBUTTON = (By.CSS_SELECTOR, '.plus.button')
ADD_TO_CART = (By.CSS_SELECTOR, '.cart button')
BOX = (By.CSS_SELECTOR, ".input-text")
CART = (By.CSS_SELECTOR, '.cart-icon strong')


class ProductPage(BasePage):
    def click_on_plus(self):
        self.find_element(*PLUSBUTTON).click()

    def input_amount_items(self, amount):
        e = self.driver.find_element(*BOX)
        e.clear()
        e.send_keys(amount)

    def get_cart_text(self):
        self.get_text(*CART)

    def get_box_value(self):
        self.find_element(*BOX).get_attribute('value')




