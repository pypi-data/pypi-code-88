import grpc
import tensorflow_federated as tff


def set_grpc(hosts, ca_cert_path: str) -> None:
    if ca_cert_path:
        with open('/data/ca-cert/ca.crt', 'rb') as f:
            creds = grpc.ssl_channel_credentials(f.read())
        channels = [grpc.secure_channel(host, creds) for host in hosts]
    else:
        channels = [grpc.insecure_channel(host) for host in hosts]

    tff.backends.native.set_remote_execution_context(channels)
