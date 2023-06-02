import products

class Store:
    # Creates new object as Store, receives a list of products to contain.

    def __init__(self, product_list):
        # Store must have at-least a list when defined.
        self.product_list = product_list

    def add_product(self, product):
        # Adds product to list
        self.product_list.append(product)

    def remove_product(self, product):
        # Removes product for stores list
        self.product_list.remove(product)

    def get_total_quantity(self):
        # Returns total quanity of all items in store
        total = 0
        for product in self.product_list:
            total += int(product.quantity)
        return total

    def get_all_products(self):
        # Returns a list of products that are active
        active_products = []
        for item in self.product_list:
            if products.Product.is_active(item) == True:
                active_products.append(item.name)
        return active_products

    def order(self, shopping_list):
        # Returns total price of an item multiplied by its quantity
        total_price = 0
        for list_pos, qnt in shopping_list:
            num = self.product_list[int(list_pos) - 1]
            if num.quantity < int(qnt):
                return total_price, "Quantity larger than what exists"
            if num.quantity <= 0:
                num.deactivate()

            num.quantity -= int(qnt)
            total_price += int(num.price * int(qnt))
        return total_price, "Product added to your list!"
