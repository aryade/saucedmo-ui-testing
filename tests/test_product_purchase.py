import pytest
from playwright.sync_api import Page
from pages.login_page import LoginPage
from pages.product_page import ProductPage
from pages.checkout_page import CheckoutPage

#in this file, we are mainly testing purchase funtions with different scenarios:
#1.purchase products successfully, 2.try to purchase products without adding products to the cart,
#3. purchase products without adding the checkout information and expecting the erroe message

def test_product_purchase_success(page: Page) -> None:
    login_page = LoginPage(page)
    product_page = ProductPage(page)
    checkout_page = CheckoutPage(page)
    login_page.navigate()
    login_page.login("standard_user", "secret_sauce")
    product_page.verify_product_list_title(page)
    product_page.add_first_n_products_to_cart(3)
    product_page.go_to_cart()
    page.get_by_text("Checkout").click()
    checkout_page.fill_checkout_information("User", "Test", "01234")
    checkout_page.finish_checkout()
    checkout_page.verify_order_confirmation("Thank you for your order!")
    page.locator("[data-test=\"back-to-products\"]").click()

def test_product_purchase_with_nothing_in_the_cart(page: Page) -> None: #there is bug in this code.
    login_page = LoginPage(page)
    product_page = ProductPage(page)
    checkout_page = CheckoutPage(page)
    login_page.navigate()
    login_page.login("standard_user", "secret_sauce")
    product_page.verify_product_list_title(page)
    product_page.go_to_cart()
    page.get_by_text("Checkout").click()
    checkout_page.fill_checkout_information("User", "Test", "01234")
    checkout_page.finish_checkout()
    checkout_page.verify_order_confirmation("Thank you for your order!")
    page.locator("[data-test=\"back-to-products\"]").click()

def test_product_purchase_without_adding_checkout_informations(page: Page) -> None:
    login_page = LoginPage(page)
    product_page = ProductPage(page)
    checkout_page = CheckoutPage(page)
    login_page.navigate()
    login_page.login("standard_user", "secret_sauce")
    product_page.verify_product_list_title(page)
    product_page.add_first_n_products_to_cart(3)
    product_page.go_to_cart()
    page.get_by_text("Checkout").click()
    checkout_page.continue_without_adding_informations()


    expected_error_message = "Error: First Name is required"
    assert checkout_page.get_checkout_error_message() == expected_error_message