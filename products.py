class Product:

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True

    def get_quantity(self):
        return float(quantity)

    def set_quantity(self, quantity):
        self.quantity = quantity

    def is_active(self):
        return self.active

    def active(self):
        self.active = True

    def deactivate(self):
        self.active = False

    def show(self):
        return f'{self.name}, Price: {self.price}, Quantity: {self.quantity}'

    def buy(self, quantity):
        total_price = 0
        total_price += (self.price * quantity)
        return total_price
