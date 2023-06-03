# Only 1 promotion per product at a given time.

class Promotion:
    def __init__(self, discount_text):
        self.discount_text = discount_text


class SecondHalfPrice(Promotion):
    # Makes every 2nd of the same product 1/2 price.
    def __init__(self, discount_text):
        super().__init__(self)
    pass


class ThirdOneFree(Promotion):
    # Makes the 3rd for every 3 of the same products free.
    def __int__(self, discount_text):
        super().__init__(self)
    pass


class PercentDiscount(Promotion):
    # Applies a manual discount given by user.
    def __int__(self, discount_text, percent=0):
        super().__init__(self)
    pass
