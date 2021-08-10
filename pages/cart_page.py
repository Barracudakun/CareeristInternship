from pages.base_page import BasePage


class Cart(BasePage):
    def cart(self):
        self.open_url('https://gettop.us/cart/')
