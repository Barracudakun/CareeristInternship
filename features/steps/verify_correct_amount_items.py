from behave import *
from selenium.webdriver.common.by import By
PLUSBUTTON = (By.CSS_SELECTOR, '.plus.button')
ADD_TO_CART = (By.CSS_SELECTOR, '.cart button')
BOX = (By.CSS_SELECTOR, ".input-text")
CART = (By.CSS_SELECTOR, '.cart-icon strong')

@when('Click on PLUSButton')
def click_on_plus(context):
    context.app.main_page.find_element(*PLUSBUTTON).click()


# @then('Verify correct amount of items shown in the cart')
# def correct_amount_items_in_cart(context):
#     actual_number = context.app.main_page.get_text(*BOX)
#
#     cart_number = context.app.main_page.get_text(*CART)
#     assert actual_number == cart_number, f'Expected {cart_number}, but got {actual_number}'

@then('Verify correct amount of items shown in the cart')
def correct_amount_items_in_cart(context):
    actual_number = context.driver.find_element(*BOX).get_attribute('value')
    cart_number = context.app.main_page.get_text(*CART)
    assert actual_number == cart_number, f'Expected {cart_number}, but got {actual_number}'
