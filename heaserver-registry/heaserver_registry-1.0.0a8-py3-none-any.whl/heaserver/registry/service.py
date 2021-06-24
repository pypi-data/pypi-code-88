"""
The HEA Registry Service provides a table of all currently active HEA microservices. Microservices each have an unique
component name field, and the name may be used to get other information about the microservice including its base URL
to make REST API calls.
"""

from heaserver.service import response, appproperty
from heaserver.service.runner import init_cmd_line, routes, start, web
from heaserver.service.db import mongo, mongoservicelib
from heaserver.service.wstl import builder_factory, action
from heaobject.registry import Component, Property

MONGODB_COMPONENT_COLLECTION = 'components'

MONGODB_PROPERTIES_COLLECTION = 'properties'


@routes.get('/components/{id}')
@action('heaserver-registry-component-open', path='/components/{id}')
async def get_component(request: web.Request) -> web.Response:
    """
    Gets the component with the specified id.
    :param request: the HTTP request.
    :return: the requested component or Not Found.
    """
    return await mongoservicelib.get(request, MONGODB_COMPONENT_COLLECTION)


@routes.get('/components/byname/{name}')
async def get_component_by_name(request: web.Request) -> web.Response:
    """
    Gets the component with the specified id.
    :param request: the HTTP request.
    :return: the requested component or Not Found.
    """
    return await mongoservicelib.get_by_name(request, MONGODB_COMPONENT_COLLECTION)


@routes.get('/components/bytype/{type}')
async def get_component_by_type(request: web.Request) -> web.Response:
    """
    Gets the component that serves resources of the specified HEA object type.
    :param request: the HTTP request.
    :return: the requested component or Not Found.
    """
    result = await request.app[appproperty.HEA_DB].get(request,
                                                       MONGODB_COMPONENT_COLLECTION,
                                                       mongoattributes={'resources': {
                                                           '$elemMatch': {'resource_type_name': {
                                                               '$in': [request.match_info['type']]}}}})
    return await response.get(request, result)


@routes.get('/components')
@routes.get('/components/')
@action('heaserver-registry-component-open', path='/components/{id}')
async def get_all_components(request: web.Request) -> web.Response:
    """
    Gets all components.
    :param request: the HTTP request.
    :return: all components.
    """
    return await mongoservicelib.get_all(request, MONGODB_COMPONENT_COLLECTION)


@routes.get('/components/{id}/properties')
@action(name='heaserver-registry-component-properties-form', path='/components/{id}')
async def get_component_properties_form(request: web.Request) -> web.Response:
    """
    Gets the component with the specified id, including a template for editing the folder's properties.
    :param request: the HTTP request.
    :return: the requested component or Not Found.
    """
    return await mongoservicelib.get(request, MONGODB_COMPONENT_COLLECTION)


@routes.get('/components/{id}/duplicator')
@action(name='heaserver-registry-component-duplicator-form', path='/components/{id}/duplicator')
async def get_component_duplicate_form(request: web.Request) -> web.Response:
    """
    Gets a form template for duplicating the requested component.

    :param request: the HTTP request. Required.
    :return: the requested form, or Not Found if the requested component was not found.
    """
    return await mongoservicelib.get(request, MONGODB_COMPONENT_COLLECTION)


@routes.post('/components')
@routes.post('/components/')
async def post_component(request: web.Request) -> web.Response:
    """
    Posts the provided component.
    :param request: the HTTP request.
    :return: a Response object with a status of Created and the object's URI in the
    """
    return await mongoservicelib.post(request, MONGODB_COMPONENT_COLLECTION, Component)


@routes.put('/components/{id}')
async def put_component(request: web.Request) -> web.Response:
    """
    Updates the component with the specified id.
    :param request: the HTTP request.
    :return: a Response object with a status of No Content or Not Found.
    """
    return await mongoservicelib.put(request, MONGODB_COMPONENT_COLLECTION, Component)


@routes.delete('/components/{id}')
async def delete_component(request: web.Request) -> web.Response:
    """
    Deletes the component with the specified id.
    :param request: the HTTP request.
    :return: No Content or Not Found.
    """
    return await mongoservicelib.delete(request, MONGODB_COMPONENT_COLLECTION)


@routes.get('/properties/{id}')
async def get_property(request: web.Request) -> web.Response:
    """
    Gets the property with the specified id.
    :param request: the HTTP request.
    :return: the requested component or Not Found.
    """
    return await mongoservicelib.get(request, MONGODB_PROPERTIES_COLLECTION)


@routes.get('/properties/byname/{name}')
async def get_property_by_name(request: web.Request) -> web.Response:
    """
    Gets the property with the specified id.
    :param request: the HTTP request.
    :return: the requested component or Not Found.
    """
    return await mongoservicelib.get_by_name(request, MONGODB_PROPERTIES_COLLECTION)


@routes.get('/properties')
@routes.get('/properties/')
async def get_all_properties(request: web.Request) -> web.Response:
    """
    Gets all properties.
    :param request: the HTTP request.
    :return: all components.
    """
    return await mongoservicelib.get_all(request, MONGODB_PROPERTIES_COLLECTION)


@routes.post('/properties')
@routes.post('/properties/')
async def post_property(request: web.Request) -> web.Response:
    """
    Posts the provided property.
    :param request: the HTTP request.
    :return: a Response object with a status of Created and the object's URI in the
    """
    return await mongoservicelib.post(request, MONGODB_PROPERTIES_COLLECTION, Property)


@routes.put('/properties/{id}')
async def put_property(request: web.Request) -> web.Response:
    """
    Updates the property with the specified id.
    :param request: the HTTP request.
    :return: a Response object with a status of No Content or Not Found.
    """
    return await mongoservicelib.put(request, MONGODB_PROPERTIES_COLLECTION, Property)


@routes.delete('/properties/{id}')
async def delete_property(request: web.Request) -> web.Response:
    """
    Deletes the property with the specified id.
    :param request: the HTTP request.
    :return: No Content or Not Found.
    """
    return await mongoservicelib.delete(request, MONGODB_PROPERTIES_COLLECTION)


def main() -> None:
    config = init_cmd_line(description='Registry of HEA services, HEA web clients, and other web sites of interest',
                           default_port=8080)
    start(db=mongo.Mongo, wstl_builder_factory=builder_factory(__package__), config=config)
