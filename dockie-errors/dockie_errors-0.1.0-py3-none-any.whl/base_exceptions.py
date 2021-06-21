"""Custom exception module"""
from http import HTTPStatus
import logging

logger = logging.getLogger(__name__)


class DockieBaseException(Exception):
    """Base class for exceptions in this module."""


class DockieError(DockieBaseException):
    """Error base class for Dockie Projects"""

    def __init__(self, http_code, error_code, message, error_context=None, more_info=None, exc_info=True):

        self.http_code = http_code
        self.error_code = error_code
        self.message = message
        self.error_context = error_context
        self.more_info = 'There are no more information available.' if more_info is None else more_info

        # Make sure every exception is logged
        # If exc_info is an instance of an exception, the stack trace of that exception will be logged
        # If exc_info is True, the stack trace of this exception will be logged
        logger.error(self, exc_info=exc_info)

        super().__init__(self.http_code, self.error_code, self.message, self.error_context, self.more_info)

    def __str__(self):
        full_message = self.message
        if self.error_context:
            full_message = f'{full_message} | Error context: {self.error_context}'
        if self.more_info:
            full_message = f'{full_message} | More info: {self.more_info}'

        return full_message

    def to_dict(self):
        """Converts the error information into a dict"""
        result = dict()
        result['message'] = self.message
        result['httpCode'] = self.http_code
        result['errorCode'] = self.error_code
        result['errorContext'] = self.error_context
        result['moreInfo'] = self.more_info

        return result


class DockieBadRequestError(DockieError):
    """Dockie base class for Bad Request Error"""
    def __init__(self, error_code=1000, message=None, error_context=None, more_info=None, exc_info=True):
        super().__init__(HTTPStatus.BAD_REQUEST, error_code, message, error_context, more_info, exc_info)


class DockiePermissionDeniedError(DockieError):
    """Dockie base class for Permission Denied Error"""
    def __init__(self, error_code=1020, message=None, error_context=None, more_info=None, exc_info=True):
        super().__init__(HTTPStatus.FORBIDDEN, error_code, message, error_context, more_info, exc_info)


class DockieResourceNotFoundError(DockieError):
    """Dockie base class for Resource Not Found Error"""
    def __init__(self, error_code=1004, message=None, error_context=None, more_info=None, exc_info=True):
        super().__init__(HTTPStatus.NOT_FOUND, error_code, message, error_context, more_info, exc_info)


class DockieResourceConflictError(DockieError):
    """Dockie base class for Conflict Error"""
    def __init__(self, error_code=1009, message=None, error_context=None, more_info=None, exc_info=True):
        super().__init__(HTTPStatus.CONFLICT, error_code, message, error_context, more_info, exc_info)


class DockieBadGatewayError(DockieError):
    """Dockie base class for Bad Gateway Error"""
    def __init__(self, error_code=5002, message=None, error_context=None, more_info=None, exc_info=True):
        super().__init__(HTTPStatus.BAD_GATEWAY, error_code, message, error_context, more_info, exc_info)


class DockieNotAllowedError(DockieError):
    """Dockie base class for Not Allowed Error"""
    def __init__(self, error_code=4005, message=None, error_context=None, more_info=None, exc_info=True):
        super().__init__(HTTPStatus.METHOD_NOT_ALLOWED, error_code, message, error_context, more_info, exc_info)


class DockieNotImplementedError(DockieError):
    """Dockie base class for Not Implemented Error"""
    def __init__(self, error_code=5001, message=None, error_context=None, more_info=None, exc_info=True):
        super().__init__(HTTPStatus.NOT_IMPLEMENTED, error_code, message, error_context, more_info, exc_info)
