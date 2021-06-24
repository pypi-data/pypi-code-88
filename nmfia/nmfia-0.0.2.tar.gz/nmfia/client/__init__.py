from nmfia.calc.cvt_bond import _ConvertibleBondCalculator
from nmfia.client.connect import _NmConnect


class NmClient:
    def __init__(
            self,
            app_key,
            app_secret,
            connect_timeout=None):
        """
        constructor for NmClient
        :param app_key: access key id
        :param app_secret: access key secret
        :param connect_timeout: connect timeout
        """
        self._app_key = app_key
        self._app_secret = app_secret
        self._connect_timeout = connect_timeout

        self._conn = _NmConnect(app_key, app_secret)
        self._conn.verify_account()

    def create_convertible_bond_calculator(self):
        """
        get instance of ConvertibleBondCalculator
        :return: ConvertibleBondCalculator()
        """
        instance = _ConvertibleBondCalculator(self._conn)
        return instance

