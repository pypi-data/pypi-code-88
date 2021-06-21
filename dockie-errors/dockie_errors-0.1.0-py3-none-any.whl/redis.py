"""Module that defines the Dockie redis errors
"""
from dockie_errors import DockieBadGatewayError


class DockieRedisConnectionError(DockieBadGatewayError):
    """Dockie Redis Connection Error Class"""
    error_code = 1400
    message = 'There was a redis connection issue'

    def __init__(self, error_context=None, more_info=None, exc_info=True):
        super().__init__(self.error_code, self.message, error_context, more_info, exc_info)
