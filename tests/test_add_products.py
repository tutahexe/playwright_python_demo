import random
import pytest


@pytest.mark.ui
def test_cart_amount_label(ui):
    ui.steps.authorization.login_with_user(ui.user, ui.password)
    total_amount_of_items = ui.steps.shop.get_items_amount()
    test_amount = random.randint(1, total_amount_of_items)
    for i in range(test_amount):
        ui.steps.shop.add_to_cart_by_index(i)
    cart_amount = ui.steps.shop.get_cart_badge_amount()
    assert cart_amount == test_amount
