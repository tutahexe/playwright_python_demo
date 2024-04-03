from playwright.sync_api import Page


class BasePage:

    def __init__(self, page):
        self.page: Page = page

    def go_to(self, url):
        self.page.goto(url, timeout=30000)
        return self.page

    def wait_for_url(self, url):
        self.page.wait_for_url(url)

    def refresh(self):
        return self.page.reload()

    def get_url(self):
        return self.page.url
