class AuthorizationSteps:
    def __init__(self, ui):
        self.page = ui.page
        self.ui = ui

    def login_with_user(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.ui.pages.login_page.login_button.click()

    def enter_username(self, username):
        self.ui.pages.login_page.user_name.fill(username)

    def enter_password(self, password):
        self.ui.pages.login_page.password.fill(password)
