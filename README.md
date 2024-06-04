# Brief description of the testing
The test automation is done with Python and Playwright. Playwright allows us to interact with the UI elements.

# Environment setup
 Setup the python virtual environments and install playwright and pytest plugins. This assumes that the python is already installed in the system.

    python3 -m venv .venv
    source .venv/bin/activate

    pip install pytest-playwright
    playwright install

The source code is divided in to two main directories. The pages directory contains the functions that interacts with the webpage and traverses thru the pages. The tests directory has all the test cases that check and validates the various test scenarios.

- tests
    Testing is done with three files in the 'tests'folder.
    1.test_login.py = In this file,we are mainly testing three scenarios: 1.login with standard user, 2.login with lockedout user and expecting the error message, and 3.login with invalid user.
    2.test_product_purchase.py = In this file, we are mainly testing purchase functions with different scenarios: 1.purchase products successfully, 2.try to purchase products without adding products to the cart, 3. purchase products without adding the checkout information and expecting the erroe message
    3.test_product_listing_sorted_order.py = In this file, we mainly focused on the sorted products by price from low to high, and sorted products by price from high to low

- conftest.py(file)
    It is the file to set up fixtures for playwright.

- pytest.ini
    file to configure the pytest


# Executing the tests
Goto to the tests folder in the source code and execute

    pytest
