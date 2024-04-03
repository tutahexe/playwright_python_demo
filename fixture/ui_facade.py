from Pages.base_page import BasePage


class UI:
    def __init__(self, page, context, user, password, url):
        self.page = page
        self.context = context
        self.user = user
        self.password = password
        self.base_url = url
