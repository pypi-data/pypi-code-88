from pyfactcast.client.config import get_client_configuration

from pyfactcast.client.sync import FactStore, get_synchronous_grpc_client


def get_sync_eventstore(profile: str = "default") -> FactStore:
    return FactStore(
        get_synchronous_grpc_client(get_client_configuration(profile=profile))
    )
