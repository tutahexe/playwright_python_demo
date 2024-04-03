class ShopPage:
    def __init__(self, ui):
        self.ui = ui
        self.menu_button = ui.page.locator("#react-burger-menu-btn")
        self.all_price_labels = ui.page.locator(".inventory_item_price")
        self.sort_dropdown = ui.page.locator(".product_sort_container")
        self.inventory_items = ui.page.locator(".inventory_item")
        self.cart_badge_amount = ui.page.locator(".shopping_cart_badge")

    def get_add_to_cart_item_by_index(self, index):
        return self.ui.page.locator(".btn_inventory").nth(index)
