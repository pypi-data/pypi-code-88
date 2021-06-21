"""
Common exceptions you can raise in web applications.


Example
-------
import flask

from wtoolzexceptions import exceptions

app = flask.Flask(__name__)

@app.errorhandler(exceptions.HTTPException)
def handle_it(e):
    res = flask.jsonify(self.to_dict())
    res.status_code = self.http_status_code
    return res

@app.route("/me")
def boom_me():
    raise exceptions.Forbidden()

# When calling /me you will now get 404 status code and JSON response
# as {"error": {"code": "XY", "message": "xy"}}.
"""

HTTP_STATUS_CODES = {
    400: "Bad Request",
    401: "Unauthorized",
    402: "Payment Required",
    403: "Forbidden",
    404: "Not Found",
    405: "Method Not Allowed",
    406: "Not Acceptable",
    407: "Proxy Authentication Required",
    408: "Request Timeout",
    409: "Conflict",
    410: "Gone",
    411: "Length Required",
    412: "Precondition Failed",
    413: "Request Entity Too Large",
    414: "Request URI Too Long",
    415: "Unsupported Media Type",
    416: "Requested Range Not Satisfiable",
    417: "Expectation Failed",
    418: "I'm a teapot",  # NOTE: see RFC 2324
    421: "Misdirected Request",  # NOTE: see RFC 7540
    422: "Unprocessable Entity",
    423: "Locked",
    424: "Failed Dependency",
    426: "Upgrade Required",
    428: "Precondition Required",  # NOTE: see RFC 6585
    429: "Too Many Requests",
    431: "Request Header Fields Too Large",
    449: "Retry With",  # NOTE: proprietary MS extension
    451: "Unavailable For Legal Reasons",
    500: "Internal Server Error",
    501: "Not Implemented",
    502: "Bad Gateway",
    503: "Service Unavailable",
    504: "Gateway Timeout",
    505: "HTTP Version Not Supported",
    507: "Insufficient Storage",
    510: "Not Extended",
}


class HTTPException(Exception):
    http_status_code = None
    code = None
    message = None

    def __init__(self, message=None):
        super(HTTPException, self).__init__()
        if message is not None:
            self.message = message

    @property
    def http_status_name(self):
        return HTTP_STATUS_CODES.get(self.http_status_code, "Unknown Error")

    def to_dict(self):
        return {"error": {"code": self.code, "message": self.message}}

    def __str__(self):
        return repr(self)

    def __repr__(self):
        http_status_code = (
            self.http_status_code
            if self.http_status_code is not None
            else "???"
        )
        return (
            "{}(http_status_code={}, http_status_name={}, "
            "code={}, message={})"
        ).format(
            self.__class__.__name__,
            http_status_code,
            self.http_status_name,
            self.code,
            self.message,
        )


class BadRequest(HTTPException):
    """400 Bad Request

    Raise if sent something the application or server cannot handle.
    """

    http_status_code = 400
    code = "BadRequest"
    message = "Sent a request that this server could not understand."


class Unauthorized(HTTPException):
    """401 Unauthorized

    Raise if the user is not authorized to access a resource.
    """

    http_status_code = 401
    code = "Unauthorized"
    message = (
        "The server could not verify that you are authorized to access "
        "the URL requested."
    )


class Forbidden(HTTPException):
    """403 Forbidden

    Raise if the user doesn't have the permission for the requested
    resource but was authenticated.
    """

    http_status_code = 403
    code = "Forbidden"
    message = (
        "You don't have the permission to access the requested " "resource."
    )


class NotFound(HTTPException):
    """404 Not Found

    Raise if a resource does not exist and never existed.
    """

    http_status_code = 404
    code = "NotFound"
    message = "The requested URL was not found on the server."


# FIXME: Review headers Allow response is needed and what Flask does.
class MethodNotAllowed(HTTPException):
    """405 Method Not Allowed

    Raise if the server used a method the resource does not handle.
    """

    http_status_code = 405
    code = "MethodNotAllowed"
    message = "The method is not allowed for the requested URL."


# REVIEW: Guideline do I need assert this.
class NotAcceptable(HTTPException):
    """406 Not Acceptable

    Raise if the server can't return any content conforming to the
    Accept headers of the client.
    """

    http_status_code = 406
    code = "NotAcceptable"
    message = (
        "The resource identified by the request is only capable of "
        "generating response entities which have content "
        "characteristics not acceptable according to the accept "
        "headers sent in the request."
    )


class RequestTimeout(HTTPException):
    """408 Request Timeout

    Raise to signalize a timeout.
    """

    http_status_code = 408
    code = "RequestTimeout"
    message = (
        "The server closed the network connection because "
        "didn't finish the request within the specified time."
    )


class Conflict(HTTPException):
    """409 Conflict

    Raise to signal that a request cannot be completed because it
    conflicts with the current state on the server.
    """

    http_status_code = 409
    code = "Conflict"
    message = (
        "A conflict happened while processing the request. The "
        "resource might have been modified while the request was being "
        "processed."
    )


class Gone(HTTPException):
    """410 Gone

    Raise if a resource existed previously and went away without new
    location.
    """

    http_status_code = 410
    code = "Gone"
    message = (
        "The requested URL is no longer available on this server and "
        "there is no forwarding address. If you followed a link from a "
        "foreign page, please contact the author of this page."
    )


class LengthRequired(HTTPException):
    """411 Length Required

    Raise if submitted data but no Content-Length header which is
    required for the kind of processing the server does.
    """

    http_status_code = 411
    code = "LengthRequired"
    message = (
        "A request with this method requires a valid Content-Length " "header."
    )


class PreconditionFailed(HTTPException):
    """412 Precondition Failed

    Status http_status_code used in combination with If-Match,
    If-None-Match, or If-Unmodified-Since.
    """

    http_status_code = 412
    code = "PreconditionFailed"
    message = (
        "The precondition on the request for the URL failed positive "
        "evaluation."
    )


class RequestEntityTooLarge(HTTPException):
    """413 Request Entity Too Large

    The status one should return if the data submitted exceeded a
    given limit.
    """

    http_status_code = 413
    code = "RequestEntityTooLarge"
    message = "The data value transmitted exceeds the capacity limit."


class RequestURITooLarge(HTTPException):
    """414 Request URI Too Large

n    Like 413 but for too long URLs.
    """

    http_status_code = 414
    code = "RequestURITooLarge"
    message = (
        "The length of the requested URL exceeds the capacity limit for "
        "this server."
    )


class UnsupportedMediaType(HTTPException):
    """415 Unsupported Media Type

    The status returned if the server is unable to handle the media
    type the client transmitted.
    """

    http_status_code = 415
    code = "UnsupportedMediaType"
    message = (
        "The server does not support the media type transmitted in the "
        "request."
    )


# REVIEW: Content-Range header in orignal implementation.
class RequestedRangeNotSatisfiable(HTTPException):
    """416 Requested Range Not Satisfiable

    The client asked for an invalid part of the file.
    """

    http_status_code = 416
    code = "UnsupportedMediaType"
    message = "The server cannot provide the requested range."


class ExpectationFailed(HTTPException):
    """417 Expectation Failed

    The server cannot meet the requirements of the Expect
    request-header.
    """

    http_status_code = 417
    code = "ExpectationFailed"
    message = (
        "The server could not meet the requirements of the " "Expect header"
    )


class ImATeapot(HTTPException):
    """418 I'm a teapot

    The server should return this if it is a teapot and someone
    attempted to brew coffee with it.
    """

    http_status_code = 418
    code = "ImATeapot"
    message = "This server is a teapot, not a coffee machine."


class UnprocessableEntity(HTTPException):
    """422 Unprocessable Entity

    Used if the request is well formed, but the instructions are
    otherwise incorrect.
    """

    http_status_code = 422
    code = "UnprocessableEntity"
    message = (
        "The request was well-formed but was unable to be followed due "
        "to semantic errors."
    )


class Locked(HTTPException):
    """423 Locked

    Used if the resource that is being accessed is locked.
    """

    http_status_code = 423
    code = "Locked"
    message = "The resource that is being accessed is locked."


class FailedDependency(HTTPException):
    """424 Failed Dependency

    Used if the method could not be performed on the resource because
    the requested action depended on another action and that action
    failed.
    """

    http_status_code = 424
    code = "FailedDependency"
    message = (
        "The method could not be performed on the resource because the "
        "requested action depended on another action and that action "
        "failed."
    )


class PreconditionRequired(HTTPException):
    """428 Precondition Required

    The server requires this request to be conditional, typically to
    prevent the lost update problem, which is a race condition between
    two or more clients attempting to update a resource through PUT or
    DELETE. By requiring each client to include a conditional header
    If-Match or If-Unmodified-Since with the proper value retained
    from a recent GET request, the server ensures that each client has
    at least seen the previous revision of the resource.
    """

    http_status_code = 428
    code = "PreconditionRequired"
    message = (
        "This request is required to be conditional. Try using "
        "If-Match or If-Unmodified-Since."
    )


# REVIEW: Retry header after?
class TooManyRequests(HTTPException):
    """429 Too Many Requests

    The server is limiting the rate at which this user receives
    responses, and this request exceeds that rate. The server may use
    any convenient method to identify users and their request
    rates. The server may include a Retry-After header to indicate how
    long the user should wait before retrying.
    """

    http_status_code = 429
    code = "TooManyRequests"
    message = "This user has exceeded an allotted request count."


class RequestHeaderFieldsTooLarge(HTTPException):
    """431 Request Header Fields Too Large

    The server refuses to process the request because the header
    fields are too large. One or more individual fields may be too
    large, or the set of all headers is too large.
    """

    http_status_code = 431
    code = "RequestHeaderFieldsTooLarge"
    message = "One or more header fields exceeds the maximum size."


class UnavailableForLegalReasons(HTTPException):
    """*451* `Unavailable For Legal Reasons`

    This status code indicates that the server is denying access to
    the resource as a consequence of a legal demand.
    """

    http_status_code = 451
    code = "UnavailableForLegalReasons"
    message = "Unavailable for legal reasons."


class InternalServerError(HTTPException):
    """500 Internal Server Error

    Raise if an internal server error occurred.  This is a good
    fallback if an unknown error occurred in the dispatcher.
    """

    http_status_code = 500
    code = "InternalServerError"
    message = (
        "The server encountered an internal error and was unable to "
        "complete your request."
    )


class NotImplemented(HTTPException):
    """501 Not Implemented

    Raise if the application does not support the action requested by
    the browser.
    """

    http_status_code = 501
    code = "NotImplemented"
    message = (
        "The server does not support the action requested by the browser."
    )


class BadGateway(HTTPException):
    """502 Bad Gateway

    If you do proxying in your application you should return this
    status code if you received an invalid response from the upstream
    server it accessed in attempting to fulfill the request.
    """

    http_status_code = 502
    code = "BadGateway"
    message = (
        "The proxy server received an invalid response from an "
        "upstream server."
    )


class ServiceUnavailable(HTTPException):
    """503 Service Unavailable

    Status code you should return if a service is temporarily
    unavailable.
    """

    http_status_code = 503
    code = "ServiceUnavailable"
    message = (
        "The server is temporarily unable to service your request due "
        "to maintenance downtime or capacity problems."
    )


class GatewayTimeout(HTTPException):
    """504 Gateway Timeout

    Status code you should return if a connection to an upstream
    server times out.
    """

    http_status_code = 504
    code = "GatewayTimeout"
    message = "The connection to an upstream server timed out."


class HTTPVersionNotSupported(HTTPException):
    """505 HTTP Version Not Supported

    The server does not support the HTTP protocol version used in the
    request.
    """

    http_status_code = 505
    code = "HTTPVersionNotSupported"
    message = (
        "The server does not support the HTTP protocol version used in "
        "the request."
    )


default_exceptions = {}
__all__ = ["HTTPException"]


def _find_exceptions():
    for _, obj in globals().items():
        try:
            is_http_exception = issubclass(obj, HTTPException)
        except TypeError:
            is_http_exception = False
        if not is_http_exception or obj.http_status_code is None:
            continue
        __all__.append(obj.__name__)
        old_obj = default_exceptions.get(obj.http_status_code, None)
        if old_obj is not None and issubclass(obj, old_obj):
            continue
        default_exceptions[obj.http_status_code] = obj


_find_exceptions()
del _find_exceptions


class Aborter(object):
    """
    When passed a dict of (code, exception) items it can be used as
    callable that raises exceptions.  If the first argument to the
    callable is an integer it will be looked up in the mapping, if
    it's a WSGI application it will be raised in a proxy exception.

    The rest of the arguments are forwarded to the exception
    constructor.
    """

    # TODO: Review logic and add tests.
    def __init__(self, mapping=None, extra=None):
        if mapping is None:
            mapping = default_exceptions
        self.mapping = dict(mapping)
        if extra is not None:
            self.mapping.update(extra)

    def __call__(self, code, *args, **kwargs):
        if not args and not kwargs and not isinstance(code, int):
            raise HTTPException(response=code)
        if code not in self.mapping:
            raise LookupError("no exception for %r" % code)
        raise self.mapping[code](*args, **kwargs)


_aborter = Aborter()


def ohoh(status, *args, **kwargs):
    """
    Raises an HTTPException for the given status code.

    ohoh(404)  # 404 Not Found
    """
    return _aborter(status, *args, **kwargs)
