import socket
from functools import cache

from requests import Session
from requests.adapters import HTTPAdapter
from urllib3.connection import HTTPConnection
from urllib3.connectionpool import HTTPConnectionPool

try:
    from aiohttp import ClientSession, UnixConnector
except ImportError:
    async_installed = False
else:
    async_installed = True


class UnixConnection(HTTPConnection):
    def __init__(self, path):
        super().__init__('localhost')
        self.__path = path

    def connect(self):
        self.sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        self.sock.connect(self.__path)


class UnixConnectionPool(HTTPConnectionPool):
    def __init__(self, path):
        super().__init__('localhost')
        self.__path = path

    def _new_conn(self):
        return UnixConnection(self.__path)


class UnixAdapter(HTTPAdapter):
    def __init__(self, path, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__path = path

    def get_connection(self, url, proxies=None):
        return UnixConnectionPool(self.__path)


@cache
def create_requests(socket_path=None):
    requests = Session()
    if socket_path is not None:
        requests.mount('unix://', UnixAdapter(socket_path))
    return requests


if async_installed:
    @cache
    def create_aiohttp(socket_path=None):
        if socket_path is not None:
            conn = UnixConnector(path=socket_path)
            session = ClientSession(connector=conn, raise_for_status=True)
        else:
            session = ClientSession(raise_for_status=True)

        return session


__all__ = (
    'create_requests',
    'create_aiohttp',
)
