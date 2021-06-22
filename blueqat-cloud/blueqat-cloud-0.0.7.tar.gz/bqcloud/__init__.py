"""`bqcloud` is Blueqat cloud API client library for Python."""
from ._version import __version__
from .api import create_api, load_api, register_api
from .device import Device
