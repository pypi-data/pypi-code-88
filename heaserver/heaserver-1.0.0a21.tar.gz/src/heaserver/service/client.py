from aiohttp import ClientSession, hdrs, web
from heaobject import root
from heaobject.registry import Component, Property
from heaserver.service import appproperty
from heaserver.service.representor import nvpjson
from yarl import URL
from typing import Optional, Union, Dict, Type, TypeVar
import logging


async def get_dict(app, url, headers=None) -> Optional[dict]:  # type: ignore[return]
    """
    Co-routine that gets a dict from a HEA service that returns JSON.

    :param app: the aiohttp application context (required).
    :param url: The URL (str or URL) of the resource (required).
    :param headers: optional dict of headers.
    :return: the dict populated with the resource's content, None if no such resource exists, or another HTTP
    status code if an error occurred.
    """
    _logger = logging.getLogger(__name__)
    async with ClientSession(connector=app[appproperty.HEA_CONNECTOR], connector_owner=False) as session:
        async with session.get(url, headers=headers) as response:
            if response.status == 200:
                result = await response.json()
                _logger.debug('Client returning %s', result)
                result_len = len(result);
                if result_len != 1:
                    raise ValueError(f'Result from {url} has {result_len} values')
                return result[0] if isinstance(result, list) else result
            elif response.status == 404:
                return None
            else:
                response.raise_for_status()


HEAObjectType = TypeVar('HEAObjectType', bound=root.HEAObject)


async def get(app: web.Application, url: Union[URL, str], obj: Union[HEAObjectType, Type[HEAObjectType]], headers: Optional[Dict[str, str]] = None) -> Optional[HEAObjectType]:    # type: ignore[return]
    """
    Co-routine that gets a HEAObject from a HEA service.

    :param app: the aiohttp application context (required).
    :param url: The URL (str or URL) of the resource (required).
    :param obj: the HEAObject type to populate with the resource's content, or a HEAObject instance. If a type or type
    name, this function will attempt to create an instance using the type's no-arg constructor.
    :param headers: optional dict of headers. Attempts to set the Accept header will be ignored. The service will
    always receive Accepts: application/json.
    :return: the HEAObject populated with the resource's content, None if no such resource exists, or another HTTP
    status code if an error occurred.
    """
    _logger = logging.getLogger(__name__)
    if isinstance(obj, str):
        obj = root.type_for_name(obj)
    if isinstance(obj, type) and issubclass(obj, root.HEAObject):
        obj_ = obj()
    elif isinstance(obj, root.HEAObject):
        obj_ = obj
    else:
        raise TypeError('obj must be an HEAObject instance, an HEAObject type, or an HEAObject type name')
    headers_ = dict(headers) if headers else {}
    headers_[hdrs.ACCEPT] = nvpjson.MIME_TYPE
    async with ClientSession(connector=app[appproperty.HEA_CONNECTOR], connector_owner=False) as session:
        async with session.get(url, headers=headers_) as response:
            if response.status == 200:
                result = await response.json()
                _logger.debug('Client returning %s', result)
                result_len = len(result);
                if result_len != 1:
                    raise ValueError(f'Result from {url} has {result_len} values')
                obj_.from_dict(result[0])
                return obj_
            elif response.status == 404:
                return None
            else:
                response.raise_for_status()


async def post(app: web.Application, url: Union[URL, str], data: root.HEAObject, headers: Dict[str, str] = None) -> str:    # type: ignore[return]
    """
    Coroutine that posts a HEAObject to a HEA service.

    :param app: the aiohttp application context (required).
    :param url: the The URL (str or URL) of the resource (required).
    :param data: the HEAObject (required).
    :param headers: optional dict of headers.
    :return: the URL string in the response's Location header.
    """
    async with ClientSession(connector=app[appproperty.HEA_CONNECTOR], connector_owner=False, json_serialize=root.json_dumps) as session:
        async with session.post(url, json=data, headers=headers) as response:
            if response.status == 201:
                return response.headers['Location']
            else:
                response.raise_for_status()


async def put(app: web.Application, url: Union[URL, str], data: root.HEAObject, headers: Dict[str, str] = None) -> None:
    """
    Coroutine that updates a HEAObject.

    :param app: the aiohttp application context (required).
    :param url: the The URL (str or URL) of the resource (required).
    :param data: the HEAObject (required).
    :param headers: optional dict of headers.
    """
    async with ClientSession(connector=app[appproperty.HEA_CONNECTOR], connector_owner=False, json_serialize=root.json_dumps) as session:
        async with session.put(url, json=data, headers=headers) as response:
            response.raise_for_status()


async def delete(app: web.Application, url: Union[URL, str], headers: Dict[str, str] = None) -> None:
    """
    Coroutine that deletes a HEAObject.

    :param app: the aiohttp application context (required).
    :param url: the URL (str or URL) of the resource (required).
    :param headers: optional dict of headers.
    """
    _logger = logging.getLogger(__name__)
    async with ClientSession(connector=app[appproperty.HEA_CONNECTOR], connector_owner=False) as session:
        _logger.debug('Deleting %s', str(url))
        async with session.delete(url, headers=headers) as response:
            response.raise_for_status()


async def get_component_by_name(app: web.Application, name: str) -> Optional[Component]:
    """
    Gets the Component with the given name from the HEA registry service.
    :param app: the aiohttp app.
    :param name: the component's name.
    :return: a Component instance or None (if not found).
    """
    return await get(app, URL(app[appproperty.HEA_REGISTRY]) / 'components' / 'byname' / name, Component)


async def get_resource_url(app: web.Application, type_or_type_name: Union[str, Type[root.HEAObject]]) -> Optional[str]:
    """
    Gets the resource URL corresponding to the HEA object type from the HEA registry service.
    :param app: the aiohttp app.
    :param type_or_type_name: the HEAObject type or type name of the resource.
    :return: a URL string or None (if not found).
    """
    if isinstance(type_or_type_name, str) and root.is_heaobject_type(type_or_type_name):
        type__ = type_or_type_name
    elif isinstance(type_or_type_name, type) and issubclass(type_or_type_name, root.HEAObject):
        type__ = type_or_type_name.get_type_name()
    else:
        raise TypeError('type_or_type_name must be an HEAObject type')
    component: Optional[Component] = await get(app, URL(app[appproperty.HEA_REGISTRY]) / 'components' / 'bytype' / type__, Component)
    return component.get_resource_url_by_type(type__) if component is not None else None


async def get_property(app: web.Application, name: str) -> Optional[Property]:
    """
    Gets the Property with the given name from the HEA registry service.
    :param app: the aiohttp app.
    :param name: the property's name.
    :return: a Property instance or None (if not found).
    """
    return await get(app, URL(app[appproperty.HEA_REGISTRY]) / 'properties' / 'byname' / name, Property)


