"""Module that defines the aws dockie errors
"""
from dockie_errors import DockieBadGatewayError


class DockieAWSConnectionError(DockieBadGatewayError):
    """Dockie AWS Connection Error"""
    error_code = 1000
    message = 'Error accessing AWS {}'

    def __init__(self, error_context=None, more_info=None, exc_info=True):
        super().__init__(self.error_code, self.message, error_context, more_info, exc_info)
