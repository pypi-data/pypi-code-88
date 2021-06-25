from .currency_price import CurrencyPrice


class BuyPrice(CurrencyPrice):

    def __init__(self, price):
        super().__init__(price)
