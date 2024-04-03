from pages.login_page import LoginPage
from pages.shop_page import ShopPage
from steps.authorization_steps import AuthorizationSteps
from steps.shop_steps import ShopSteps


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
        self.shop_page = ShopPage(ui)


class Steps:
    def __init__(self, ui):
        self.authorization = AuthorizationSteps(ui)
        self.shop = ShopSteps(ui)
