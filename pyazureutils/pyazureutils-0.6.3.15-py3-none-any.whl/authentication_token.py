from requests.auth import AuthBase
class TokenAuth(AuthBase):
    """Authentication object for token based authentication (e.g. Azure IoT Central)

    :param AuthBase: Parent class
    :type AuthBase: Class of type AuthBase.
    """

    def __init__(self, token):
        self.token = token

    def __eq__(self, other):
        return self == other

    def __ne__(self, other):
        return not self == other

    def __call__(self, r):
        r.headers['Authorization'] = self.token
        return r

class BearerAuth(AuthBase):
    def __init__(self, token):
        self.token = token
    def __call__(self, r):
        r.headers["authorization"] = "Bearer " + self.token
        return r