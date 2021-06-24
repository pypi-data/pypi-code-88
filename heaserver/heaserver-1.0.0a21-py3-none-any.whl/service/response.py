"""
Functions that create HTTP responses. The returned response object will have the following attributes:
status: an integer HTTP status code. Will never be None.
body: the body of the response as a byte array. May be None.
text: the body of the response as a str. May be None.
charset: the response's character set. May be None.
headers: a header name -> header value mapping. May be None.
content_type: the response's content type.
"""
from aiohttp import web, hdrs
from heaserver.service import requestproperty, appproperty
from heaserver.service.representor import factory as representor_factory
from yarl import URL
import logging
import copy
from typing import Union, List, Optional, Dict, Any


def status_not_found(body: bytes = None) -> web.Response:
    """
    Returns a newly created Response object with status code 404 and an optional body.
    :param body: the body of the message, typically an explanation of what was not found.
    :return: Response with a 404 status code.
    """
    return web.HTTPNotFound(body=body)


def status_bad_request(body: bytes = None) -> web.Response:
    """
    Returns a newly created Response object with status code 400 and an optional body.
    :param body: the body of the message, typically an explanation of why the request is bad.
    :return: Response with a 400 status code.
    """
    return web.HTTPBadRequest(body=body)


def status_created(base_url: Union[URL, str], resource_base: str, inserted_id: str) -> web.Response:
    """
    Returns a newly created Response object with status code 201 and the Location header set.

    :param base_url: the service's base URL (required).
    :param resource_base: the common base path fragment for all resources of this type (required).
    :param inserted_id: the id of the newly created object (required).

    :return: Response with a 201 status code and the Location header set to the URL of the created object.
    """
    if inserted_id is None:
        raise ValueError('inserted_id cannot be None')
    return web.HTTPCreated(headers={hdrs.LOCATION: str(URL(base_url) / resource_base / str(inserted_id))})


def status_ok(body: bytes, content_type: str = 'application/json') -> web.Response:
    """
    Returns a newly created Response object with status code 201, the provided Content-Type header, and the provided
    body.
    :param body: the body of the response.
    :param content_type: the content type of the response (default is application/json).
    :return: a Response object with a 200 status code.
    """
    if content_type is not None:
        return web.HTTPOk(headers={hdrs.CONTENT_TYPE: content_type}, body=body)
    else:
        return web.HTTPOk(body=body)


def status_no_content() -> web.Response:
    """
    Returns a newly created Response object with status code 204.
    :return: a Response object with a 204 status code.
    """
    return web.HTTPNoContent()


async def get(request: web.Request, data: Optional[Dict[str, Any]]) -> web.Response:
    """
    Handle a get request by attribute.

    :param request: the HTTP request (required).
    :param data: a HEA object dict. May be None.
    :return: a Response object, with status code 200, containing a body containing the object in name-value pair (NVP)
    JSON.
    """
    if data:
        return await _handle_get_result(request, data)
    else:
        return web.HTTPNotFound()


async def get_from_wstl(request: web.Request, run_time_doc: Dict[str, Any]) -> web.Response:
    """
    Handle a get request that returns a run-time WeSTL document. Any actions in the document are added to the
    request's run-time WeSTL documents, and the href of the action is prepended by the service's base URL. The actions
    in the provided run-time document are expected to have a relative href.

    :param request: the HTTP request (required).
    :param run_time_doc: a run-time WeSTL document containing data.
    :return: a Response object with a body containing the object in a JSON array of name-value pair (NVP) objects.
    """
    return await _handle_get_result_from_wstl(request, run_time_doc)


async def get_all_from_wstl(request: web.Request, run_time_docs: List[Dict[str, Any]]) -> web.Response:
    """
    Handle a get all request that returns one or more run-time WeSTL documents. Any actions in the documents are added
    to the request's run-time WeSTL documents, and the href of the action is prepended by the service's base URL. The
    actions in the provided run-time document are expected to have a relative href.

    :param request: the HTTP request (required).
    :param run_time_docs: a list of run-time WeSTL documents containing data.
    :return: a Response object with a body containing the object in a JSON array of name-value pair (NVP) objects.
    """
    return await _handle_get_result_from_wstl(request, run_time_docs)


async def get_all(request: web.Request, data: List[Dict[str, Any]]) -> web.Response:
    """
    Handle a get request.

    :param request: the HTTP request (required).
    :param data: a list of HEA object dicts.
    :return: a Response object with a body containing the object in a JSON array of name-value pair (NVP) objects.
    """
    return await _handle_get_result(request, data)


async def post(request: web.Request, result: Optional[str], resource_base: str) -> web.Response:
    """
    Handle a post request.

    :param request: the HTTP request (required).
    :param result: the id of the POST'ed HEA object, or None if the POST failed due to a bad request.
    :param resource_base: the common base path fragment for all resources of this type (required).
    :return: a Response with Created status code and the URL of the created object, or a Response with a Bad Request
    status code if the result is None.
    """
    if result:
        return await _handle_post_result(request, resource_base, result)
    else:
        return web.HTTPBadRequest()


async def put(result: bool) -> web.Response:
    """
    Handle the result from a put request.

    :param result: whether any objects were updated.
    :return: a Response object with status code 203 (No Content) or 404 (Not Found).
    """
    if result:
        return web.HTTPNoContent()
    else:
        return web.HTTPNotFound()


async def delete(result: bool) -> web.Response:
    """
    Handle the result from a delete request.

    :param result: whether any objects were deleted.
    :return: a Response object with status code 203 (No Content) or 404 (Not Found).
    """
    if result:
        return web.HTTPNoContent()
    else:
        return web.HTTPNotFound()


async def _handle_get_result(request: web.Request, data: Union[Dict[str, Any], List[Dict[str, Any]]]) -> web.Response:
    """
    Handle the result from a get request. Returns a Response object, the body of which will always contain a list of
    JSON objects.

    :param request: the HTTP request object. Cannot be None.
    :param data: the retrieved HEAObject(s) as a dict or a list of dicts, with each dict representing a
    HEAObject with its attributes as name-value pairs.
    :return: a Response object, either a 200 status code and the requested JSON object in the body, or status code 404
    (Not Found).
    """
    _logger = logging.getLogger(__name__)
    if data is not None:
        wstl_builder = request[requestproperty.HEA_WSTL_BUILDER]
        wstl_builder.data = data if isinstance(data, list) else [data]
        wstl_builder.href = str(request.url)
        return await _handle_get_result_from_wstl(request, wstl_builder())
    else:
        return web.HTTPNotFound()


async def _handle_get_result_from_wstl(request: web.Request,
                                       run_time_docs: Union[Dict[str, Any], List[Dict[str, Any]]]) -> web.Response:
    """
    Handle a get or get all request that returns one or more run-time WeSTL documents. Any actions in the documents are
    added to the request's run-time WeSTL documents, and the href of the action is prepended by the service's base URL.
    The actions in the provided run-time documents are expected to have a relative href.

    :param request: the HTTP request object. Cannot be None.
    :param run_time_doc: a list of run-time WeSTL documents containing data
    :return: a Response object, either a 200 status code and the requested JSON objects in the body, or status code 404
    (Not Found).
    """
    _logger = logging.getLogger(__name__)
    _logger.debug('Run-time WeSTL document is %s', run_time_docs)
    if run_time_docs is not None:
        representor = representor_factory.from_accepts_header(request.headers[hdrs.ACCEPT])
        _logger.debug('Using %s output format', representor)
        body = await representor.formats(request, run_time_docs)
        _logger.debug('Response body is %s', body)
        return status_ok(body=body, content_type=representor.MIME_TYPE)
    else:
        return web.HTTPNotFound()


async def _handle_post_result(request: web.Request, resource_base: str, inserted_id: str) -> web.Response:
    """
    Handle the result from a post request.

    :param request: the HTTP request object (required).
    :param resource_base: the common base path fragment for all resources of this type (required).
    :param inserted_id: the id of the newly created object (required).
    :return: a Response object with status code 201 (Created).
    """
    return status_created(request.app[appproperty.HEA_COMPONENT], resource_base, inserted_id)
