from behave import *
from selenium.webdriver.common.by import By
from time import sleep

firstItem = (By.CSS_SELECTOR, '.product-title a')
ADD_TO_CART = (By.CSS_SELECTOR, '.cart button')
# SelectedProduct = (By.CSS_SELECTOR, '.product-title')


@given('Open Gettop page')
def open_main_page(context):
    # context.driver.get('https://gettop.us/')
    context.app.main_page.open_main()
    sleep(3)

@when('Click on the first item from LATEST PRODUCTS ON SALE')
def click_firstItem_on_lastProductOnSale(context):
    # context.driver.find_element(By.CSS_SELECTOR, '.product-title a').click()
    selected_item = context.app.main_page.find_element(*firstItem)
    selected_item.click()
    sleep(3)


@when('Click on ADD TO CART')
def click_on_ADD_TO_CART(context):
    # context.driver.find_element(By.CSS_SELECTOR, '.cart button').click()
    context.app.main_page.find_element(*ADD_TO_CART).click()
    sleep(3)

@then('Verify “MacBook Pro 13-inch” has been added to your cart." confirmation upon adding items to cart')
def verify_add_product_to_cart(context):
    # selected_item = context.app.main_page.get_text(*SelectedProduct)
    actual_text = context.app.main_page.find_element(By.CSS_SELECTOR, '.message-container').text
    # actual_text = actual_text.replace('"', '')
    # actual_text = actual_text[:actual_text.find("has")]
    #assert actual_text == "{selected_item} has been added to your cart", f'Expected "{selected_item} has been added to your cart", but got {actual_text}'
    assert actual_text == '“MacBook Pro 13-inch” has been added to your cart.', f'Expected text, but got {actual_text}'
    sleep(3)