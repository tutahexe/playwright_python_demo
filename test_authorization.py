from playwright.sync_api import Page


def test_successful_auth(page: Page):
    page.goto("")
    page.locator("#user-name").fill("standard_user")
    page.locator("#password").fill("secret_sauce")
    page.locator("#login-button").click()
    assert page.locator("#react-burger-menu-btn").is_visible() is True, "Failed to authorize"
