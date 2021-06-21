"""Module that defines the dockie celery errors
"""
from http import HTTPStatus

from dockie_errors import DockieError


class DockieCeleryError(DockieError):
    """Dockie Celery Error"""
    http_code = HTTPStatus.INTERNAL_SERVER_ERROR
    error_code = 1100
    message = 'Something wrong with celery.'

    def __init__(self, error_context=None, more_info=None, exc_info=True):
        super().__init__(self.http_code, self.error_code, self.message, error_context, more_info, exc_info)
