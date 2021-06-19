from typing import Dict, Optional

from us_libraries.constants import http_code


class ServiceException(Exception):

    def __init__(self, message: Optional[str] = "Service Error", status_code: int = http_code.GENERAL_SERVICE_ERROR_CODE):
        self.status_code = status_code
        self.message = message

    def get_status_code(self) -> int:
        return self.status_code

    def to_dict(self) -> Dict:
        dto = {
            "status_code": self.status_code,
            "message": self.message,
            "success": False
        }
        return dto


class ValidationException(ServiceException):
    def __init__(self, message: Optional[str] = None):
        super().__init__(message or 'Invalid value', http_code.VALIDATION_ERROR_CODE)


class RecordNotFoundException(ServiceException):
    def __init__(self, message: Optional[str] = None):
        super().__init__(message or 'Record not found', http_code.NOT_FOUND_ERROR_CODE)


class MethodNotAllowedException(ServiceException):
    def __init__(self, message: Optional[str] = None):
        super().__init__(message or 'Method Not Allowed', http_code.METHOD_NOT_ALLOWED_ERROR_CODE)


class BadGatewayException(ServiceException):
    def __init__(self, message: Optional[str] = None):
        super().__init__(message or 'Bad Gateway', http_code.BAD_GATEWAY_ERROR_CODE)


class GatewayTimeoutException(ServiceException):
    def __init__(self, message: Optional[str] = None):
        super().__init__(message or 'Gateway Timeout', http_code.GATEWAY_TIMEOUT_ERROR_CODE)


class ServiceUnavailableException(ServiceException):
    def __init__(self, message: Optional[str] = None):
        super().__init__(message or 'Service Unavailable', http_code.SERVICE_NOT_AVAILABLE_ERROR_CODE)


class ServiceErrorException(ServiceException):
    def __init__(self, message: Optional[str] = None):
        super().__init__(message or 'An Error occurred in the Service', http_code.GENERAL_SERVICE_ERROR_CODE)
