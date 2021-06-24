from nmfia.client.request import _NmRequest


class _ConvertibleBondCalculator(_NmRequest):
    def __init__(self, conn):
        super().__init__(conn)

    def get(self):
        return "something"
