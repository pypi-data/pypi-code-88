from . import configuration, connection
import typing


def initialize():
    options = configuration.parse()
    hosts: typing.Optional[str] = options.host
    if hosts:
        connection.set_grpc(hosts=hosts)
