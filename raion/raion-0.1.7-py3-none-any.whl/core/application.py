from fastapi import FastAPI
from raion import __app_version__, __app_name__
from raion.routing.Routing import Routing
from raion.core import paths
import importlib

class Application(FastAPI):

    def bootstrap(self, path: str = None):
        self.title   = __app_name__
        self.version = __app_version__
        
        self.routing()

        return self

    def routing(self):
        Routing.init(self)
        
        self.dynamic_routing()

    def dynamic_routing(self):
        for module in paths.list_dir(paths.ROUTES_PATH):
            importlib.import_module(f"routes.{module}")