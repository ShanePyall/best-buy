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
        return float(self.quantity)

    def set_quantity(self, quantity):
        # Re-assigns a new value for products quantity
        self.quantity = quantity
        if self.quantity <= 0:
            self.deactivate()

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
        if quantity > self.quantity:
            return 0.0
        total_price = self.price * quantity
        self.set_quantity(self.quantity - quantity)
        return total_price


class NonStockedProduct(Product):
    # Creates a Product with values for non-physical products.
    def __init__(self, name, price, quantity=0):
        super().__init__(name, price, quantity)
        self.quantity = 0

    def show(self):
        return f'{self.name}, Price: {self.price}'

    def buy(self, quantity):
        return self.price * quantity


class LimitedProduct(Product):
    # Creates a Product which can only be purchased a limited number of times per order
    def __init__(self, name, price, quantity, maximum):
        super().__init__(name, price, quantity)
        self.maximum = int(maximum)

    def show(self):
        return f'{self.name}, Price: {self.price}, Quantity: {self.quantity}, maximum: {self.maximum}'

    def buy(self, quantity):
        try:
            if quantity > self.maximum:
                raise ValueError
            return super().buy(quantity)
        except ValueError:
            return f"This product is limited to {self.maximum} per order"
