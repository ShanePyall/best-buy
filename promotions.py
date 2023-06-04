# Only 1 promotion per product at a given time.
from abc import ABC


class Promotion(ABC):
    def __init__(self, discount_text, percent=0):
        self.discount_text = discount_text
        self.percent = percent

    def apply_promotion(self, product, quantity):
        # Returns price(Float) after discount is applied
        return float


class SecondHalfPrice(Promotion):
    # Makes every 2nd of the same product 1/2 price.
    def __init__(self, discount_text):
        super().__init__(discount_text)

    def apply_promotion(self, product, quantity):
        if quantity % 2 == 0:
            price_post_discount = (product.price * quantity) * 0.75
        else:
            price_post_discount = ((product.price * (quantity - 1)) * 0.75) + product.price
        return price_post_discount


class ThirdOneFree(Promotion):
    # Makes the 3rd for every 3 of the same products free.
    def __init__(self, discount_text):
        super().__init__(discount_text)

    def apply_promotion(self, product, quantity):
        if quantity % 3 == 0:
            price_post_discount = (product.price * ((quantity / 3) * 2))

        elif quantity % 3 == 1:
            if quantity - 1 > 0:
                price_post_discount = (product.price * (((quantity - 1) / 3) * 2)) + product.price
            else:
                price_post_discount = product.price * quantity

        else:
            if quantity - 2 > 0:
                price_post_discount = ((product.price * (((quantity - 2) / 3) * 2)) + (product.price * 2))
            else:
                price_post_discount = product.price * quantity

        return price_post_discount


class PercentDiscount(Promotion):
    # Applies a manual discount given by user.
    def __int__(self, discount_text, percent):
        super().__init__(discount_text, percent)

    def apply_promotion(self, product, quantity):
        return (product.price * quantity) * (1 - (self.percent / 100))
