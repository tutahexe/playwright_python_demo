from Pages.login_page import LoginPage
from Pages.main_page import MainPage
from Steps.authorization_steps import AuthorizationSteps


class UI:
    def __init__(self, page, context, user, password, url):
        self.ui = self
        self.page = page
        self.context = context
        self.user = user
        self.url = url
        self.password = password
        self.pages = Pages(self)
        self.steps = Steps(self)
        self.page = page


class Pages:
    def __init__(self, ui):
        self.login_page = LoginPage(ui)
        self.main_page = MainPage(ui)


class Steps:
    def __init__(self, ui):
        self.authorization = AuthorizationSteps(ui)
