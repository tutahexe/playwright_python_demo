import pytest


@pytest.mark.ui
def test_successful_auth(ui):
    ui.steps.authorization.login_with_user(ui.user, ui.password)
    assert ui.pages.shop_page.menu_button.is_visible() is True \
           and ui.pages.login_page.user_name.is_hidden() is True, "Failed to authorize "


@pytest.mark.ui
def test_failed_auth(ui):
    ui.steps.authorization.login_with_user(ui.user, "wrong_password")
    assert ui.pages.login_page.error_label.is_visible() is True \
           and ui.pages.login_page.user_name.is_visible() is True, "Authorized with invalid credentials"


@pytest.mark.ui
def test_failed_auth_label(ui):
    ui.steps.authorization.login_with_user(ui.user, "wrong_password")
    assert ui.pages.login_page.error_label.text_content() == \
           "Epic sadface: Username and password do not match any user in this service"
