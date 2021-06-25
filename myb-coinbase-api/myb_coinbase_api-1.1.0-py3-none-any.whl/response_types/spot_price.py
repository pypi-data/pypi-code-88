from .currency_price import CurrencyPrice


class SpotPrice(CurrencyPrice):

    def __init__(self, price):
        super().__init__(price)
