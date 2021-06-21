"""Module that defines the Dockie request errors
"""

from dockie_errors import DockieBadRequestError


class DockieRequestValidationError(DockieBadRequestError):
    """Dockie Validation Request Body Error"""
    error_code = 1500
    message = 'There was an issue while validating the request body'

    def __init__(self, error_context=None, more_info=None, exc_info=True):
        super().__init__(self.error_code, self.message, error_context, more_info, exc_info)
