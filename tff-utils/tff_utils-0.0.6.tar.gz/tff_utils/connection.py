import logging
import typing

import grpc
import tensorflow_federated as tff


def initialize_grpc(hosts, ca_cert_path: str) -> None:
    if ca_cert_path:
        logging.debug(f'using CA cert located at {ca_cert_path}')
        with open(ca_cert_path, 'rb') as f:
            creds = grpc.ssl_channel_credentials(f.read())
        channels = [grpc.secure_channel(host, creds) for host in hosts]
    else:
        logging.debug('not using CA cert')
        channels = [grpc.insecure_channel(host) for host in hosts]

    tff.backends.native.set_remote_execution_context(channels)


if __name__ == '__main__':
    initialize_grpc(hosts=[], ca_cert_path='')
