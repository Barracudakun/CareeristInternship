from behave import *
from selenium.webdriver.common.by import By

firstItem = (By.CSS_SELECTOR, '.product-title a')
ADD_TO_CART = (By.CSS_SELECTOR, '.cart button')

@given('Open Gettop page')
def open_main_page(context):
    # context.driver.get('https://gettop.us/')
    context.app.main_page.open_main()


@when('Click on the first item from LATEST PRODUCTS ON SALE')
def click_firstItem_on_lastProductOnSale(context):
    # context.driver.find_element(By.CSS_SELECTOR, '.product-title a').click()
    context.find_element(*firstItem).click()



@when('Click on ADD TO CART')
def click_on_ADD_TO_CART(context):
    # context.driver.find_element(By.CSS_SELECTOR, '.cart button').click()
    context.find_element(*ADD_TO_CART).click()

@then('Verify " {selected_item} has been added to your cart" confirmation upon adding items to cart')
def verify_add_product_to_cart(context, selected_item):
    actual_text = context.driver.find_element(By.CSS_SELECTOR, '.message-container').text
    assert actual_text == "{selected item} has been added to your cart", \
        f'Expected "{selected_item} has been added to your cart", but got {actual_text}'
