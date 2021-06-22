# coding: utf-8
from pywss.ctx import Ctx as _Ctx
from pywss.route import Route, _RouteMap


class Ctx(_Ctx):

    def __init__(self, environ: dict, handlers: tuple, urlParams: dict, queryParams: dict):
        pass


class Client:

    def __init__(self, routeMap: _RouteMap):
        self.routeMap = routeMap

    def get(self, route, params=None or {}, headers=None or {}, data=None, json=None):
        pass


def testApp(app: Route) -> Client:
    client = Client(app.routeMap)
    return client


def application(environ, start_response):
    pass
