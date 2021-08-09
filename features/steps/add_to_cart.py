from behave import *
from selenium.webdriver.common.by import By


@given(u'Open Gettop page')
def open_main_page(context):
    context.driver.get('https://gettop.us/')


@when(u'Click on the first item from LATEST PRODUCTS ON SALE')
def click_firstItem_on_lastProductOnSale(context):
    context.driver.find_element(By.CSS_SELECTOR, '.product-title a').click()



@when(u'Click on ADD TO CART')
def click_on_ADDTOCART(context):
    context.driver.find_element(By.CSS_SELECTOR, '.cart button').click()


@then(u'Verify user can add product to cart')
def verify_add_product_to_cart(context):

