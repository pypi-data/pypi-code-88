import grpc
import tensorflow_federated as tff


def set_grpc(hosts) -> None:
    channels = [grpc.insecure_channel(host) for host in hosts]
    tff.backends.native.set_remote_execution_context(channels)
