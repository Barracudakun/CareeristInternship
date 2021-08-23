from behave import *
from pages.product_page import ProductPage
from selenium.webdriver.common.by import By
# PLUSBUTTON = (By.CSS_SELECTOR, '.plus.button')
# ADD_TO_CART = (By.CSS_SELECTOR, '.cart button')
# BOX = (By.CSS_SELECTOR, ".input-text")
# CART = (By.CSS_SELECTOR, '.cart-icon strong')

@when('Click on PLUSButton')
def click_on_plus(context):
    context.app.product_page.click_on_plus()

# @when('Type in {amount} of items to add to cart')
# # how do i put different amounts of numbers in the cart to verity?
# def input_amount_items(context, amount):
#     context.app.product_page.input_amount_items(10)


@then('Verify correct amount of items shown in the cart')
def correct_amount_items_in_cart(context):
    actual_number = context.app.product_page.get_box_value()
    cart_number = context.app.product_page.get_cart_text()
    assert actual_number == cart_number, f'Expected {cart_number}, but got {actual_number}'
