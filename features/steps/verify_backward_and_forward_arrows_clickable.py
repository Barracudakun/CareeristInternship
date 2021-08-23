from behave import *




@given('Open Given page')
def open_given_page(context):
    context.app.given_page.open_url('https://gettop.us/product/macbook-pro-16/')

#
# @when('Click forward arrow')
# def click_forward_arrow(context):
#     pass
#     #text = context.get_product_title()

@then('Verify User can click through multiple products by clicking back and forward arrows')
def verity_clicking_back_and_forward_arrows(context):
    product_list = []
    text = context.app.given_page.get_product_title()
    product_list.append(text)
    context.app.given_page.click_forward_arrows()
    text = context.app.given_page.get_product_title()
    product_list.append(text)
    context.app.given_page.click_back_arrows()
    context.app.given_page.click_back_arrows()
    text = context.app.given_page.get_product_title()
    product_list.append(text)
    print(product_list)






# GEt to the 16-inch page
# Get the the product text into  a list
# CLick Forward arrow
# Append the second product to the list
# CLick back arrow twice
# Append the third product to the list
# len(set(prod_list)) > 1
