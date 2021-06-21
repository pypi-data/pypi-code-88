"""Module that defines the Dockie database errors
"""
from http import HTTPStatus

from dockie_errors import DockieError, DockieBadGatewayError


class DockieDatabaseConnectionError(DockieBadGatewayError):
    """Dockie MySql Error class"""
    error_code = 1200
    message = 'There was a mysql connection issue'

    def __init__(self, error_context=None, more_info=None, exc_info=True):
        super().__init__(self.error_code, self.message, error_context, more_info,  exc_info)


class DockieDatabaseUnknownError(DockieError):
    """Dockie Unknown Database Error class"""
    http_code = HTTPStatus.INTERNAL_SERVER_ERROR
    error_code = 1201
    message = 'Something wrong in database'

    def __init__(self, error_context=None, more_info=None, exc_info=True):
        super().__init__(self.http_code, self.error_code, self.message, error_context, more_info, exc_info)
