from behave import *
from selenium.webdriver.common.by import By
PLUS = (By.CSS_SELECTOR, '.plus.button')
ADD_TO_CART = (By.CSS_SELECTOR, '.cart button')

@when('Click on "PLUS"')
def click_on_plus(context):
    context.find_element(*PLUS).click()


@when('Click on ADDTOCART')
def click_on_ADDTOCART(context):
    context.find_element(*ADD_TO_CART).click()


@then('Verify correct amount of items shown in the cart')
def correct_amount_items_in_cart(context):
    actual_items = context.get_text()
    cart_items = contex

