import pytest
from playwright.sync_api import Page
from pages.login_page import LoginPage
from pages.product_page import ProductPage

# here we are sorted products by price low to high (ascending order) and high to low(descending order)
#and verify that the products are sorted correctly

def test_sorted_products_with_ascending_order(page: Page) -> None:
    login_page = LoginPage(page)
    product_page = ProductPage(page)
    login_page.navigate()
    login_page.login("standard_user", "secret_sauce")
    product_page.sort_products_by_prices_ascending_order()
    assert product_page.are_prices_sorted_ascending()

def test_sorted_products_with_descending_order(page: Page) -> None:
    login_page = LoginPage(page)
    product_page = ProductPage(page)
    login_page.navigate()
    login_page.login("standard_user", "secret_sauce")
    product_page.sort_products_by_prices_descending_order()
    assert product_page.are_prices_sorted_descending()