from playwright.sync_api import Page

class CheckoutPage:     #checkout page locators
    def __init__(self, page: Page):
        self.page = Page
        self.first_name_input = page.locator("[data-test=\"firstName\"]")
        self.last_name_input = page.locator("[data-test=\"lastName\"]")
        self.postal_code_input = page.locator("[data-test=\"postalCode\"]")
        self.continue_button = page.locator("[data-test=\"continue\"]")
        self.finish_button = page.locator("[data-test=\"finish\"]")
        self.confirmation_message_locator = page.locator("[data-test=\"complete-header\"]")
        self.error_message_locator = page.locator("[data-test=\"error\"]")

    def fill_checkout_information(self, first_name: str, last_name: str, postal_code: str): #fill the details in checkout page
        self.first_name_input.fill(first_name)
        self.last_name_input.fill(last_name)
        self.postal_code_input.fill(postal_code)
        self.continue_button.click()

    def continue_without_adding_informations(self): #continue button in the checkout page
        self.continue_button.click()

    def finish_checkout(self):  #finish button in the checkout page
        self.finish_button.click()

    def verify_order_confirmation(self, expected_message: str): #verifying the order confirmed with success message
        assert self.confirmation_message_locator.text_content() == expected_message

    def get_checkout_error_message(self): #verifying the error message comes after click 'continue' without adding any checkout informations in the form.
        return self.error_message_locator.text_content()
