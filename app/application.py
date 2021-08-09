from pages.cart import Cart

class Application:

    def __init__(self, driver):
        self.driver = driver

        self.cart = Cart(self.driver)

