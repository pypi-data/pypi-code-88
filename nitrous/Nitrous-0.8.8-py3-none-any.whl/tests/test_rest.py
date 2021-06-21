# coding: utf-8

from json import dumps, loads

import cherrypy
from turbogears import controllers, expose, redirect, view
from turbogears.testutil import make_app, start_server, stop_server
from turbogears.util import simplify_http_accept_header
from webtest import Upload

import pytest
import datetime

import cherrypy
from turbogears import controllers, expose, flash, identity, redirect, visit
from turbogears.rest import RESTContainer, RESTResource



class Root(controllers.RootController):
    """The root controller of the application."""

    def __init__(self):
        self.df = DynamicFormController()
        self.jecho = Echoer()

    @expose()
    def index(self):
        return dict(now=datetime.datetime.now())


@RESTContainer('DynamicFormResource')
class DynamicFormController:
    @expose()
    def POST(self, type):
        print('POST', type)
        return {}


class DynamicFormResource(RESTResource):
    def __init__(self, id, parent_container=None):
        self.id = id

    @expose()
    def GET(self):
        return getattr(cherrypy.request, 'json', 'NOATTR')

    @cherrypy.tools.json_in()
    @expose()
    def PUT(self):
        print('PUT', self.id)
        print(cherrypy.request.json)


class Echoer(RESTResource):
    @expose()
    def GET(self):
        return getattr(cherrypy.request, 'json', 'NOATTR')

    @cherrypy.tools.json_in()
    @expose()
    def POST(self):
        return cherrypy.request.json


@pytest.fixture
def app():
    return make_app(Root)


def test_resource_get_should_not_have_json_attribute(app):
    response = app.get('/df/123')

    assert response.body == b'"NOATTR"'


def test_resource_get_should_not_have_json_attribute_after_put(app):
    app.put('/df/12345', content_type='application/json', params=dumps({}))
    response = app.get('/df/123')

    assert response.body == b'"NOATTR"'


def test_echoer_json_in_should_reflect_supplied_json(app):
    json = {'a': 'json', 'y_u_no': None}
    response = app.post('/jecho', content_type='application/json', params=dumps(json))

    assert json == response.json


def test_echo_resource_get_should_not_have_json_attribute(app):
    response = app.get('/jecho')

    assert response.body == b'"NOATTR"'


# COREBT-14067
def test_cp_json_in_tool_should_not_pollute_parent_config(app):
    app.post('/df', params={'type': 'A'})
    app.put('/df/12345', content_type='application/json', params=dumps({}))

    # before fix, this fails with 415 Unsupported Media Type
    app.post('/df', params={'type': 'A'})
