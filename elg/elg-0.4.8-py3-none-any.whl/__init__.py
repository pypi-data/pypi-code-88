__version__ = "0.4.8"

import importlib.util

_docker_available = importlib.util.find_spec("docker") is not None
_docker_available = importlib.util.find_spec("flask") is not None
_docker_available = importlib.util.find_spec("flask_json") is not None
_requests_toolbelt_available = importlib.util.find_spec("requests_toolbelt") is not None


from .authentication import Authentication
from .benchmark import Benchmark
from .catalog import Catalog
from .corpus import Corpus
from .entity import Entity
from .pipeline import Pipeline
from .provider import Provider
from .service import Service

if _docker_available and _docker_available and _docker_available and _requests_toolbelt_available:
    from .flask_service import FlaskService
