class InvalidTokenException(Exception):
    """Exception to be raised for tokens which do not pass validation."""


class NoPrivateKeyException(Exception):
    """
    Exception to be raised when an attempt is made to decode
    an encrypted token without access to a private key.
    """
