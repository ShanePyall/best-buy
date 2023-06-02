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
        # Returns total quantity of all items in store
        total = 0
        for product in self.product_list:
            total += int(product.quantity)
        return total

    def get_all_products(self):
        # Returns a list of products that are active
        active_products = []
        for item in self.product_list:
            if item.is_active():
                active_products.append(item.name)
        return active_products

    def order(self, shopping_list):
        # Checks if there is enough product to sell, returns total price.
        item, qnt = shopping_list
        total_price = item.buy(qnt)
        if total_price == 0.0:
            message = "Quantity entered is larger than what is in stock"
        elif type(total_price) is str:
            return 0, total_price
        else:
            message = "Product added to your list!"
        return total_price, message
