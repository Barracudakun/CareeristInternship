# Created by yingxuyao at 8/4/21
Feature: Adding to cart

  Scenario: User can add product to cart
    Given Open Gettop page
    When Click on the first item from LATEST PRODUCTS ON SALE
    And Click on ADD TO CART
    Then Verify “MacBook Pro 13-inch” has been added to your cart." confirmation upon adding items to cart


  Scenario: User can click - and + to modify amount of items to add to cart, upon adding to cart, correct amount of items shown
  in the cart
    Given Open Gettop page
    When Click on the first item from LATEST PRODUCTS ON SALE
    And Click on PLUSBUTTON
    And Click on ADD TO CART
    Then Verify correct amount of items shown in the cart


  Scenario: User can type in amount of items to add to cart, upon adding to cart, correct amount of items shown in the cart
    Given Open Gettop page
    When Click on the first item from LATEST PRODUCTS ON SALE
    And Type in {amount} of items to add to cart
    And Click on ADD TO CART
    Then Verify correct amount of items shown in the cart


  Scenario: User can click through multiple products by clicking back and forward arrows over “You may also like” text
#   (see https://gettop.us/product/macbook-pro-16/ )
    Given Open Given page
    Then Verify User can click through multiple products by clicking back and forward arrows


  Scenario: If product is out of stock, user sees "Out of Stock", Add to Cart and Checkout buttons are not shown
#    (https://gettop.us/product/land-tee-jack-jones/)
    Given Open out of stock page
    Then Verify User can sees 'Out of Stock', Add to Cart and Checkout buttons are not shown
