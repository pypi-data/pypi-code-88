class CurrencyPrice:

    def __init__(self, price):
        self.amount = float(price.get('amount'))
        self.currency = price.get('currency')
