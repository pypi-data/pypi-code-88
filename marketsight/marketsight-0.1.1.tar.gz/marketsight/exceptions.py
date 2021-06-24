"""
##########################
marketsight.exceptions
##########################

Implements the exceptions that can be raised by the **MarketSight API Library**.

"""
from typing import Optional
from validator_collection import validators

from marketsight._compat import json


class MarketSightError(Exception):
    """Base error produced by the **MarketSight API Library**."""

    _status_code = None

    def __init__(self, *args, **kwargs):
        """
        :param message: The human-readable message to display.
        :type message: :class:`str <python:str>`

        :param status_code: The numerical status code to report to the user.
        :type status_code: :class:`int <python:int>`

        :returns: The exception object
        :rtype: :class:`MarketSightError` or subclass as applicable

        """
        if self.status_code is None:
            self.status_code = kwargs.get("status_code")

        self.message = kwargs.get("message")

        super(MarketSightError, self).__init__(*args, **kwargs)

    def __repr__(self) -> str:
        return "%s(%s, status_code = %s)" % (
            self.error_type,
            self.message,
            self.status_code,
        )

    @classmethod
    def from_exception(cls, error):
        """Raise a :class:`MarketSightError` by converting from a different
        :class:`Exception <python:Exception>`.

        :param error: The original exception that was raised.
        :type error: :exc:`Exception <python:Exception>`

        :raises MarketSightError:
        """
        if isinstance(error, MarketSightError):
            raise error

        if not isinstance(error, Exception):
            try:
                status_code, error_type, message = parse_http_error(error)
            except AttributeError:
                ValueError(
                    "MarketSightError.from_exception() expects an Exception. "
                    "Received %s" % error.__class__.__name__
                )

            raise error_type(message)

        status_code = getattr(error, "status_code", None)
        message = getattr(error, "message", None)

        if not message:
            message = error.args[0]

        if error.__class__.__name__ not in ERROR_TYPES:
            raise error

        error_type = ERROR_TYPES[error.__class__.__name__]

        try:
            raise error_type(message)
        except error_type as raised_error:
            raised_error.status_code = status_code
            raised_error.message = message

            raise raised_error

    @property
    def error_type(self) -> str:
        """Exception class name of the error.

        :rtype: :class:`str <python:str>`
        """
        return self.__class__.__name__

    @property
    def status_code(self) -> Optional[int]:
        """The HTTP status code returned by the
        :term:`Dynata Reporting & Analytics API`.

        :rtype: :class:`int <python:int>` / :obj:`None <python:None>`

        """
        return self._status_code

    @status_code.setter
    def status_code(self, value):
        self._status_code = validators.int(value, allow_empty = True)

    @property
    def message(self) -> Optional[str]:
        """A human-readable message that provides information about the error.

        :rtype: :class:`str <python:str>` / :obj:`None <python:None>`

        """
        return self._message

    @message.setter
    def message(self, value):
        self._message = validators.string(value, allow_empty = True)

    def to_dict(self) -> dict:
        """Create a :class:`dict <python:dict>` representation of the error.

        :rtype: :class:`dict <python:dict>`

        Example:

        .. code-block:: python

          >>> MarketSightError('Something went wrong.', status_code = 500).to_dict()
          {
              'status_code': 500,
              'message': 'Something went wrong.',
              'error_type': 'MarketSightError'
          }
        """

        return {
            "status_code": self.status_code,
            "error_type": self.error_type,
            "message": self.message,
        }

    def to_json(self) -> str:
        """Create a JSON :class:`str <python:str>` representation of the error.

        :rtype: :class:`str <python:str>`

        Example:

        .. code-block:: python

          >>> MarketSightError('Something went wrong.', status_code = 500).to_json()
          '{
              "status_code": 500,
              "message": "Something went wrong.",
              "error_type": "MarketSightError"
          }'

        """
        return json.dumps(self.to_dict())

    @classmethod
    def from_dict(cls, dict_object: dict):
        """Create a :class:`MarketSightError` instance from a supplied
        :class:`dict <python:dict>`.

        .. note::

          This will actually return a different exception based on the
          ``error_type`` and ``status_code`` properties.

        :param dict_object: The :class:`dict <python:dict>` from which to create
          the :class:`MarketSIghtError` object.
        :type dict_object: :class:`dict <python:dict>`

        :returns: A :class:`MarketSightError` instance.
        :rtype: :class:`MarketSightError`

        """
        status_code = dict_object.get("status_code", None)
        message = dict_object.get("message", None)
        error_type = dict_object.get("error_type", None)
        if not error_type or error_type not in ERROR_TYPES:
            error_type = DEFAULT_ERROR_CODES.get(
                status_code, "MarketSightError"
            )

        return ERROR_TYPES[error_type](
            message=message, status_code=status_code, error_type=error_type
        )

    @classmethod
    def from_json(cls, json_string: str):
        """Create a :class:`MarketSightError` instance from a JSON string.

        :param json_string: The JSON payload.
        :type json_string: :class:`str <python:str>`

        :returns: A :class:`MarketSightError` instance.
        :rtype: :class:`MarketSightError`

        """
        json_obj = json.loads(json_string)

        return cls.from_dict(json_obj)


class HelperError(MarketSightError):
    """Error produced when an API Client Instance was instantiated without a
    proper :class:`Helper <marketsight.application_api.Helper>` instance or
    subclass."""
    status_code = 500


class BindingError(MarketSightError):
    """Error produced when the MarketSight Client-side Library has an incorrect API
    binding.
    """

    status_code = 500


class InternalAPIError(MarketSightError):
    """Error produced when the MarketSight API returns a ``Status Code: 500``.

    This error indicates that there was an internal error (unhandled exception)
    produced by the MarketSight API.
    """

    status_code = 500


class RequestPayloadError(MarketSightError):
    """Error produced when the MarketSight API returns a ``Status Code: 400``.

    This error indicates that the MarketSight API was unable to correctly interpret
    the request's JSON payload.
    """

    status_code = 400


class AuthenticationError(MarketSightError):
    """Error produced when the MarketSight API returns a ``Status Code: 401``.

    This error indicates that the authentication credentials provided with the
    request failed.
    """

    status_code = 401


class AuthorizationError(MarketSightError):
    """Error produced when the MarketSight API returns a ``Status Code: 403``.

    This error indicates that the authenticated user does not have permission to
    perform the requested action.

    """

    status_code = 403


class ResourceNotFoundError(MarketSightError):
    """Error produced when the MarketSight API returns a ``Status Code: 404``.

    This error indicates that the MarketSight API was unable to find an
    indicated resource.
    """

    status_code = 404


class ConflictError(MarketSightError):
    """Error produced when the MarketSight API returns a ``Status Code: 409``.

    This error indicates that the MarketSight API was unable to fulfill the request
    because the requested operation produced a conflict between two or more
    resources.
    """

    status_code = 409


class DuplicateRecordError(ConflictError):
    pass


class MissingAPIKeyError(AuthenticationError):
    """Error produced when there is no API key available for authentication.
    """


class HTTPConnectionError(MarketSightError):
    """Error produced when the MarketSight Library is unable to connect to the API, but
    did not time out.
    """

    status_code = 500


class HTTPTimeoutError(HTTPConnectionError):
    """Error produced when the API times out or returns a ``Status Code: 504``.

    This error indicates that the underlying API timed out and did not return a result.
    """

    status_code = 504


class SSLError(MarketSightError):
    """Error produced when an SSL certificate cannot be verified, returns a
    ``Status Code: 495``.
    """

    status_code = 495


def parse_http_error(status_code, http_response):
    """Return the error based on the ``http_response`` received.

    :param http_response: The HTTP response that was retrieved.

    :returns: Tuple with:

      * the status code received,
      * the error type received,
      * the error message received
    """
    error_type = DEFAULT_ERROR_CODES[status_code]
    message = None
    try:
        error_type = http_response.get("error_type", error_type)
        message = http_response.get("message", message)
    except AttributeError:
        message = http_response

    error_type = ERROR_TYPES[error_type]

    return status_code, error_type, message


# pylint: disable=R1711
def check_for_errors(status_code, http_response=None):
    """Raise an error based on the ``status_code`` received.

    :param status_code: The status code whose error should be returned.
    :type status_code: :class:`int <python:int>`

    :param http_response: The HTTP response object that will be parsed to determine
      the message.

    :returns: :obj:`None <python:None>` if no error matches ``status_code``
    :raises MarketSightError: or a sub-type thereof based on ``status_code``

    """
    if status_code in DEFAULT_ERROR_CODES:
        status_code, error_type, message = parse_http_error(
            status_code, http_response
        )
        raise error_type(message)

    return None


# pylint: enable=R1711

DEFAULT_ERROR_CODES = {
    500: "InternalAPIError",
    400: "RequestPayloadError",
    401: "AuthenticationError",
    403: "AuthorizationError",
    404: "ResourceNotFoundError",
    409: "ConflictError",
    504: "HTTPTimeoutError",
    495: "SSLError",
}

ERROR_TYPES = {
    "InternalAPIError": InternalAPIError,
    "RequestPayloadError": RequestPayloadError,
    "AuthenticationError": AuthenticationError,
    "AuthorizationError": AuthorizationError,
    "ResourceNotFoundError": ResourceNotFoundError,
    "ConflictError": ConflictError,
    "HTTPTimeoutError": HTTPTimeoutError,
    "SSLError": SSLError,
    "InvalidURLError": BindingError,
    "DownloadError": InternalAPIError,
    "ResponseTooLargeError": InternalAPIError,
    "HTTPConnectionError": HTTPConnectionError,
    "URLError": BindingError,
    "ValueError": InternalAPIError,
    "DuplicateRecordError": DuplicateRecordError,
}
