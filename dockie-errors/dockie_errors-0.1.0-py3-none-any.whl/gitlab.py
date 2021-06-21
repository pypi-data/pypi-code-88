"""Module that defines the Dockie gitlab errors
"""

from dockie_errors import DockieBadGatewayError, DockieResourceNotFoundError


class DockieGitlabConnectionError(DockieBadGatewayError):
    """Dockie Gitlab Connection Error"""
    error_code = 1300
    message = 'Gitlab connection error'

    def __init__(self, error_context=None, more_info=None, exc_info=True):
        super().__init__(self.error_code, self.message, error_context, more_info, exc_info)


class DockieGitlabAuthenticationError(DockieBadGatewayError):
    """Dockie Gitlab Authentication Error"""
    error_code = 1301
    message = 'Unable to authenticate in gitlab. Check gitlab token.'

    def __init__(self, error_context=None, more_info=None, exc_info=True):
        super().__init__(self.error_code, self.message, error_context, more_info, exc_info)


class DockieGitlabGroupNotFound(DockieResourceNotFoundError):
    """Dockie Gitlab Group Not Found Error"""
    error_code = 1302
    message = 'Gitlab Group is not found.'

    def __init__(self, error_context=None, more_info=None, exc_info=True):
        super().__init__(self.error_code, self.message, error_context, more_info, exc_info)
