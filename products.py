class Product:
    # Creates new object as Product, after receiving: name, price, quantity.

    def __init__(self, name, price, quantity):
        # Creates the bare minimum for product, activates on creation.
        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True

    def get_quantity(self):
        # Returns quantity of selected product.
        return float(quantity)

    def set_quantity(self, quantity):
        # Re-assigns a new value for products quantity
        self.quantity = quantity

    def is_active(self):
        # Returns products active status
        return self.active

    def active(self):
        # Actives product
        self.active = True

    def deactivate(self):
        # de-activates product
        self.active = False

    def show(self):
        # Returns string of products values.
        return f'{self.name}, Price: {self.price}, Quantity: {self.quantity}'

    def buy(self, quantity):
        # Returns price of product
        total_price = 0
        total_price += (self.price * quantity)
        return total_price
