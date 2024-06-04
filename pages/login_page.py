from playwright.sync_api import Page

class LoginPage:  #locators in the login page
    def __init__(self, page: Page):
        self.page = page
        self.username_input = page.get_by_placeholder("Username")
        self.password_input = page.get_by_placeholder("Password")
        self.login_button = page.get_by_text("Login")
        self.error_message_locator = page.locator("[data-test=\"error\"]")

    def navigate(self):  #navigate to the webpage
        self.page.goto("https://www.saucedemo.com")


    def login(self, username: str, password: str): #fill the login page
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()

    def get_login_error_message(self): #login with wrong or invalid or lockedout user :error message will pop-up
        return self.error_message_locator.text_content()