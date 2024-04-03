import pytest


@pytest.mark.ui
def test_successful_auth(ui):
    ui.steps.authorization.login_with_user(ui.user, ui.password)
    assert ui.pages.main_page.menu_button.is_visible() is True and ui.pages.login_page.user_name.is_hidden() is True, \
        "Failed to authorize "
