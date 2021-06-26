"""Util modules are evil."""
import importlib

from .base import IClient


__NETWORK_CLIENTS = {
    'urn:ibrb:network:bsc:main': 'ibrb.ext.clients.web3',
    'urn:ibrb:network:bsc:test': 'ibrb.ext.clients.web3',
    'urn:ibrb:network:eth:main': 'ibrb.ext.clients.web3',
    'urn:ibrb:network:eth:test': 'ibrb.ext.clients.web3',
}


async def get(network: str, *args, **kwargs) -> IClient:
    """Return a new client for the given `network`."""
    module = importlib.import_module(__NETWORK_CLIENTS[network])
    return await module.new(network, *args, **kwargs)
