# pylint: disable=line-length
"""Declares a :class:`~ibrb.ext.clients.IClient` implementation
for Ethereum-compatible networks, using the :mod:`web3`
package.
"""
import asyncio
import decimal
import threading
import urllib.parse

from web3 import Web3
from web3.middleware import geth_poa_middleware

from ibrb.ext import clients


POA_NETWORKS = [
    'urn:ibrb:network:bsc:main',
    'urn:ibrb:network:bsc:test',
    'urn:ibrb:network:eth:test',
]


async def new(network, *args, **kwargs):
    return await EthereumClient.new(network, *args, **kwargs)


class EthereumClient(clients.IClient):
    __urls = {
        'urn:ibrb:network:bsc:main': "https://bsc-dataseed1.binance.org:443",
        'urn:ibrb:network:bsc:test': "https://data-seed-prebsc-1-s1.binance.org:8545/",
        'urn:ibrb:network:eth:main': "https://mainnet.infura.io/v3/9aa3d95b3bc440fa88ea12eaa4456161",
        'urn:ibrb:network:eth:test': "https://ropsten.infura.io/v3/9aa3d95b3bc440fa88ea12eaa4456161",
    }
    __providers = {
        'http'  : Web3.HTTPProvider,
        'https' : Web3.HTTPProvider,
        'ws'    : Web3.WebsocketProvider,
        'wss'   : Web3.WebsocketProvider,
        ''      : Web3.IPCProvider, # filepath has no scheme with urllib.parse
    }

    @property
    def data_url(self) -> str:
        """Return the data URL for the provider."""
        return self.__urls[self.__network]

    @property
    def provider_class(self):
        """Return the proper provider class for the configured data URL."""
        scheme, *_ = urllib.parse.urlparse(self.data_url)
        return self.__providers[scheme]

    @property
    def provider(self):
        """Return the proper provider instance for the configured data URL."""
        return self.provider_class(self.data_url)

    @property
    def loop(self):
        return asyncio.get_running_loop()

    @property
    def web3(self):
        if not hasattr(self.__local, 'web3'):
            self.__local.web3 = w3 = Web3(self.provider)
            if self._is_poa():
                w3.middleware_onion.\
                    inject(geth_poa_middleware, layer=0)
        return self.__local.web3

    @classmethod
    async def new(cls, network, address=None):
        """Create a new client instance configured for the given
        `network`.
        """
        return cls(network)

    def __init__(self, network):
        self.__network = network
        self.__local = threading.local()

    async def get_balance(self, address: str):
        """Return a :class:`decimal.Decimal` or :class:`int` object representing
        the balance of given `address` in a networks' native token.
        """
        return decimal.Decimal(
            await self.loop.run_in_executor(
                None, self.web3.eth.get_balance,
                self._normalize_address(address))
        )

    async def get_latest_block(self):
        """Return a datastructure describing the latest block
        in a network.
        """
        return await self.loop.run_in_executor(
            None, self.web3.eth.get_block, 'latest')

    def _is_poa(self):
        return self.__network in POA_NETWORKS

    def _normalize_address(self, address):
        return Web3.toChecksumAddress(str.lower(address))
