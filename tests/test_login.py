import pytest
from playwright.sync_api import Page
from pages.login_page import LoginPage
from pages.product_page import ProductPage

 #In this test,we are mainly testing three scenarios: 1.login with standard user, 2.login with lockedout user, 3.login with invalid user.
def test_login_with_standard_user(page: Page) -> None:
    login_page = LoginPage(page)
    product_page = ProductPage(page)
    login_page.navigate()
    login_page.login("standard_user", "secret_sauce")

    assert product_page.verify_product_list_title(page)

def test_login_with_locked_out_user(page: Page) -> None:
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login("locked_out_user", "secret_sauce")

    expected_error_message = "Epic sadface: Sorry, this user has been locked out."
    assert login_page.get_login_error_message() == expected_error_message

def test_login_with_invalide_user(page: Page) -> None:
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login("User1", "secret_sauce")

    expected_error_message = "Epic sadface: Username and password do not match any user in this service"
    assert login_page.get_login_error_message() == expected_error_message