from behave import *


@given('Open out of stock page')
def open_out_of_stock_page(context):
    context.app.out_stock_page.open_our_of_stock_page()


@then ("Verify User can sees 'Out of Stock', Add to Cart and Checkout buttons are not shown")
def verify_user_sees_OutofStock(context):
    pass

def verify_Add_to_Cart_not_shown(context):
    pass

def verify_Checkout_buttons_not_shown(context):
    pass