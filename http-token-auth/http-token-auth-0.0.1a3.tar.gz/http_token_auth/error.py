class ExpiredError(Exception):
    """Base token expire error.
    """
    pass


class TokenExpiredError(ExpiredError):
    """Raised when auth token has expired.
    """
    pass


class SessionExpiredError(ExpiredError):
    """Raised when refresh token has expired.
    """
    pass


class SessionError(Exception):
    """Raised when operating on an invalid session state.
    """
    pass
