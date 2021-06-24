
class _NmConnect:
    def __init__(self, app_key, app_secret):
        """
        constructor for _NmRequest
        :param app_key:
        :param app_secret:
        """
        self._app_key = app_key
        self._app_secret = app_secret

    def verify_account(self):
        """
        检查app key有效性
        :return: None
        """
        pass
