from . import configuration, connection
import typing

__version__ = '0.0.4'


def initialize():
    options = configuration.parse()
    hosts: typing.List[str] = options.host
    if hosts:
        connection.set_grpc(hosts=hosts)
