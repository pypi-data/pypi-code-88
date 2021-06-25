"""
API response utilities
"""
from abc import ABC, abstractmethod
from enum import Enum
from json import dumps
from typing import NamedTuple, Any, Union, List, Optional
from ckf_api_toolkit.core import Actor, UseCase
from ckf_api_toolkit.tools.error_handling import get_trace
from ckf_api_toolkit.tools.logger import Logger, LogLevel


class ResponseCode(Enum):
    """Enum representing HTTP response codes"""
    OK = 200
    REDIRECT = 300
    REDIRECT_PERMANENT = 301
    REDIRECT_TEMP = 302
    BAD_REQUEST = 400
    UNAUTHORIZED = 401
    FORBIDDEN = 403
    NOT_FOUND = 404
    ALREADY_EXISTS = 409
    ERROR = 500
    NOT_IMPLEMENTED = 501


class ApiResponseException(Exception):
    """Class to wrap a response exception from an API

    Attributes:
        status_code (Union[ResponseCode, int]): The status code for this response. Can use builtin ResponseCode Enum
             or a custom integer
        message (str): The message for this exception
    """
    status_code: Union[ResponseCode, int]
    message: str

    def __init__(self, status_code: Union[ResponseCode, int], message: str):
        """Inits APIResponseException with status_code and message"""
        self.status_code = status_code
        self.message = message


class ApiSuccessResponseBody:
    """Class for a successful response body

    Attributes:
        data (Any): The data returned in the response body
        message (Optional[str]): the message returned with the response
    """
    data: Any
    message: Optional[str]

    def __init__(self, *, data: Optional[Any] = None, message: Optional[str] = None):
        self.data = data or {}
        self.message = message

    def append_data(self, data: Any, data_key: str):
        """Append the given data with the data key. Will overwrite existing data if not a dictionary.

        Args:
            data (Any): The data to append
            data_key (str): The key for the data
        """
        if not self.data or type(self.data) is not dict:
            self.data = {}
        self.data[data_key] = data

    def set_data(self, data: Any):
        """Set the body data to the given data

        Args:
            data (Any): The data to set
        """
        self.data = data


class ApiErrorResponseBody(NamedTuple):
    """NamedTuple for an error response body"""
    error: str


# noinspection PyUnresolvedReferences
class Header(NamedTuple):
    """NamedTuple for an HTTP Header

    Attributes:
        key (str): The key for the header
        value (str): The value for the header
    """
    key: str
    value: str


class ApiResponseFactory(ABC):
    """Abstract class to be implemented for specific API responses

    Attributes:
        return_trace (bool): Whether to log a trace of the response return
        status_code (int): The status code of the response
        body (Union[ApiSuccessResponseBody, ApiErrorResponseBody]): The response body of the request
    """
    return_trace: bool
    status_code: int
    body: Union[ApiSuccessResponseBody, ApiErrorResponseBody]

    def __init__(self, *, return_trace=False):
        """Inits ApiResponseFactory with an empty body

        Keyword Args:
            return_trace (bool): include any exception traces in the API Response (default is False)
        """
        self.return_trace = return_trace
        self.body = ApiSuccessResponseBody()

    @abstractmethod
    def get_response(self) -> dict:
        """Return the response as a dictionary

        To be implemented by the child class"""
        pass

    @abstractmethod
    def add_header(self, header: Header):
        """Add a header to the API Response

        To be implemented by the child class

        Args:
            header (Header): Header object containing the key and value to add
        """
        pass

    @property
    def is_error(self) -> bool:
        """Return whether this response is an error or not

        Returns:
            (bool) Whether the response is an error or not
        """
        return type(self.body) is ApiErrorResponseBody

    @property
    def body_dict(self) -> dict:
        """Returns a dictionary of the response body

        Returns:
            (dict) The response body
        """
        if self.is_error:
            # noinspection PyProtectedMember
            return self.body._asdict()
        else:
            return vars(self.body)

    def set_error(self, error_code: Union[ResponseCode, int], message: str):
        """Set the error code and message for this response

        Args:
            error_code (Union[ResponseCode, int]): The error code for this response. Can use builtin ResponseCode Enum
                or a custom integer
            message (str): The message for this response
        """
        self.body = ApiErrorResponseBody(message)

        if type(error_code) is ResponseCode:
            self.status_code = error_code.value
        elif type(error_code) is int:
            self.status_code = error_code

    def set_exception(self, error: Union[Exception, ApiResponseException]):
        """Set the exception for this response

        Args:
            error (Union[Exception, ApiResponseException]): The error to set
        """
        if self.return_trace:
            trace = get_trace()
            Logger().log(LogLevel.debug, trace, title="Returning Exception Trace in Response")
            error_object = {
                'trace': trace,
                'error': str(error),
            }
            message = dumps(error_object)
        else:
            message = "Internal server error."

        if isinstance(error, ApiResponseException):
            self.set_error(error.status_code, error.message)
        else:
            self.set_error(ResponseCode.ERROR, message)

    def set_success(self, operation_name: str, *, response_code: ResponseCode = ResponseCode.OK):
        """Set the successful response code and operation name for this response

        Args:
            operation_name (str): The operation name to use
            response_code (ResponseCode): The response code to return
        """
        self.body = ApiSuccessResponseBody(
            message=f"Operation successful: {operation_name}.",
        )
        self.status_code = response_code.value

    def add_to_response_data(self, data: Any, data_key: str):
        """Add the given data to the response with the given key if the response is a success response

        Args:
            data (Any): The data to add
            data_key (str): The key for the data
        """
        if type(self.body) is ApiSuccessResponseBody:
            self.body.append_data(data, data_key)

    def set_response_data(self, data: any):
        """
        Set the full response data object to the given data if the response is a success response

        Args:
            data (Any): The data to set
        """
        if type(self.body) is ApiSuccessResponseBody:
            self.body.set_data(data)

    def set_response_from_actor(self, actor: Actor, use_case: UseCase, data_key: Optional[str] = None, *,
                                suppress_data=False, headers: Optional[List[Header]] = None):
        """Runs a use case on an actor, and set success for the use case along with response data

        Args:
            actor (Actor): The actor to operate
            use_case (UseCase): The use case to run
            data_key (Optional[str]): the data key to add response data to - will set the entire response data to the
             given data if not provided
            suppress_data (bool): Prevent the returned data from being added to the response, but preserve success/error
             state information.
            headers (List[Header]): List of Header objects to add to the response
        """
        data = actor.run_use_case(use_case)

        self.set_success(use_case.name)
        if not suppress_data:
            if data_key:
                self.add_to_response_data(data, data_key)
            else:
                self.set_response_data(data)

        if headers:
            for header in headers:
                self.add_header(header)
