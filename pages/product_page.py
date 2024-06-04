from playwright.sync_api import Page

class ProductPage:  # page locators in the product page
    def __init__(self, page: Page):
        self.page = page
        self.product_list_title = page.locator("span.title")
        self.inventory_items = page.locator("[data-test=\"inventory-item\"]") #.all()
        self.shopping_cart_link = page.locator("[data-test=\"shopping-cart-link\"]")
        self.sort_dropdown = page.locator("[data-test=\"product-sort-container\"]")
        self.inventory_item_prices = page.locator(".inventory_item_price")

    def verify_product_list_title(self, page: Page): #verify the page locator with the page title
        return self.product_list_title.get_by_title("product") #== "product"


    def add_first_n_products_to_cart(self, number_of_products_to_buy: int): #adds a specific number of items to the shoppingcartby iterating over the items and clicking the "Add to cart" button.
        for product in range(number_of_products_to_buy):
            self.inventory_items.nth(product).get_by_text("Add to cart").click()

    def go_to_cart(self):  #add items to the cart
        self.shopping_cart_link.click()

    def sort_products_by_prices_ascending_order(self): # sort items with the dropdown options -here sorted items/products by price from low to high
        self.sort_dropdown.select_option("lohi")

    def sort_products_by_prices_descending_order(self): # sort items with the dropdown options -here sorted items/products by price from high to low
        self.sort_dropdown.select_option("hilo")

    def get_all_prodcuts_prices(self):  #here checking the sorted products prices
        prices = self.inventory_item_prices.all()
        return [float(price.text_content().strip('$')) for price in prices]

    def are_prices_sorted_ascending(self): #verify that the products are sorted by price from low to high
        products_price = self.get_all_prodcuts_prices()
        return products_price == sorted(products_price)

    def are_prices_sorted_descending(self): #verify that the products are sorted by price from high to low
        products_price = self.get_all_prodcuts_prices()
        return products_price == sorted(products_price, reverse=True)
