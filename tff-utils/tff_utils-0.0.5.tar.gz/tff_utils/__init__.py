from . import configuration, connection
import typing

__version__ = '0.0.5'


def initialize():
    options = configuration.parse()
    hosts: typing.List[str] = options.host
    ca_cert_path: str = options.ca_cert
    if hosts:
        connection.set_grpc(hosts=hosts, ca_cert_path=ca_cert_path)
