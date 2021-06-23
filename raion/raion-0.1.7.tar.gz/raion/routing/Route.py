
from raion import routing
from typing import Any
from .Routing import Routing

routing = Routing()
class Route:
    
    @classmethod
    def get(self, path, controller = None, **kwargs: Any):
        return routing.add_route(path=path, method="GET", controller=controller, **kwargs)
