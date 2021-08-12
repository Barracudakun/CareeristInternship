# Created by yingxuyao at 8/4/21
Feature: Adding to cart
  Background:
   Given Open Gettop page
   When Click on the first item from LATEST PRODUCTS ON SALE

  Scenario: User can add product to cart
    And Click on ADD TO CART
    Then Verify " ... have been added to your cart" confirmation upon adding items to cart


  Scenario: User can click - and + to modify amount of items to add to cart, upon adding to cart, correct amount of items shown
  in the cart
    And Click on '+'
    And Click on ADD TO CART
    Then Verify correct amount of items shown in the cart


  Scenario: User can type in amount of items to add to cart, upon adding to cart, correct amount of items shown in the cart
    And Type in amount of items to add to cart
    Then Verify correct amount of items shown in the cart


  Scenario: User can click through multiple products by clicking back and forward arrows over “You may also like” text
    And Click on clicking back and forward arrows
    Then Verify  “You may also like” text



