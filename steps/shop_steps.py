class ShopSteps:
    def __init__(self, ui):
        self.page = ui.page
        self.ui = ui

    def add_to_cart_by_index(self, index):
        self.ui.pages.shop_page.get_add_to_cart_item_by_index(index).click()

    def get_items_amount(self):
        return len(self.ui.pages.shop_page.inventory_items.all_inner_texts())

    def get_cart_badge_amount(self):
        return int(self.ui.pages.shop_page.cart_badge_amount.inner_text())
