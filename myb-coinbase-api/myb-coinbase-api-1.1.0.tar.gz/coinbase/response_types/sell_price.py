from .currency_price import CurrencyPrice


class SellPrice(CurrencyPrice):

    def __init__(self, price):
        super().__init__(price)
