from behave import *
from time import sleep
#
@when('Type in {amount} of items to add to cart')
# how do i put different amounts of numbers in the cart to verity?
def input_amount_items(context, amount):
    context.app.product_page.input_amount_items(10)
    sleep(3)

