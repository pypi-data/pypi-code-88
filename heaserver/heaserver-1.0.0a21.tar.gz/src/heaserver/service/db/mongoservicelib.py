from ..appproperty import HEA_DB
from .. import response
from ..heaobjectsupport import new_heaobject
from heaobject.error import DeserializeException
from aiohttp.web import Request, Response
from typing import Type
from heaobject.root import HEAObject


async def get(request: Request, mongodb_collection: str) -> Response:
    """
    Gets the HEA object with the specified id.
    :param request: the HTTP request. Required.
    :param mongodb_collection: the Mongo collection name. Required.
    :return: a Response with the requested HEA object or Not Found.
    """
    result = await request.app[HEA_DB].get(request, mongodb_collection, var_parts='id')
    return await response.get(request, result)


async def get_by_name(request: Request, mongodb_collection: str) -> Response:
    """
    Gets the HEA object with the specified name.
    :param request: the HTTP request. Required.
    :param mongodb_collection: the Mongo collection name. Required.
    :return: a Response with the requested HEA object or Not Found.
    """
    result = await request.app[HEA_DB].get(request, mongodb_collection, var_parts='name')
    return await response.get(request, result)


async def get_all(request: Request, mongodb_collection: str) -> Response:
    """
    Gets all HEA objects.
    :param request: the HTTP request. Required.
    :param mongodb_collection: the Mongo collection name. Required.
    :return: a Response with a list of HEA object dicts.
    """
    result = await request.app[HEA_DB].get_all(request, mongodb_collection)
    return await response.get_all(request, result)


async def post(request: Request, mongodb_collection: str, type_: Type[HEAObject]) -> Response:
    """
    Posts the provided HEA object.
    :param request: the HTTP request.
    :param mongodb_collection: the Mongo collection name. Required.
    :param type_: The HEA object type. Required.
    :return: a Response object with a status of Created and the object's URI in the
    """
    try:
        obj = await new_heaobject(request, type_)
        result = await request.app[HEA_DB].post(request, obj, mongodb_collection)
        return await response.post(request, result, mongodb_collection)
    except DeserializeException:
        return response.status_bad_request()


async def put(request: Request, mongodb_collection: str, type_: Type[HEAObject]) -> Response:
    """
    Updates the HEA object with the specified id.
    :param request: the HTTP request. Required.
    :param mongodb_collection: the Mongo collection name. Required.
    :param type_: The HEA object type. Required.
    :return: a Response object with a status of No Content or Not Found.
    """
    try:
        obj = await new_heaobject(request, type_)
        if request.match_info['id'] != obj.id:
            return response.status_bad_request()
        result = await request.app[HEA_DB].put(request, obj, mongodb_collection)
        return await response.put(result.matched_count if result else False)
    except DeserializeException:
        return response.status_bad_request()


async def delete(request: Request, mongodb_collection: str) -> Response:
    """
    Deletes the HEA object with the specified id.
    :param request: the HTTP request. Required.
    :param mongodb_collection: the Mongo collection name. Required.
    :return: No Content or Not Found.
    """
    result = await request.app[HEA_DB].delete(request, mongodb_collection)
    return await response.delete(result.deleted_count if result else False)
