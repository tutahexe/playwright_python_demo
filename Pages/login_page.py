class LoginPage:
    def __init__(self, ui):
        self.user_name = ui.page.locator("#user-name")
        self.password = ui.page.locator("#password")
        self.login_button = ui.page.locator("#login-button")
