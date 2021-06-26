"""Declare :class:`IClient`."""
import abc


class IClient(metaclass=abc.ABCMeta):
    """Specifies the interface for blockchain network clients."""
    __module__ = 'ibrb.ext.clients'

    @abc.abstractclassmethod
    async def new(cls, network, address=None):
        """Create a new client instance configured for the given
        `network`.
        """
        raise NotImplementedError

    @abc.abstractmethod
    async def get_balance(self, address: str):
        """Return a :class:`decimal.Decimal` or :class:`int` object representing
        the balance of given `address` in a networks' native token.
        """
        raise NotImplementedError

    async def get_latest_block(self):
        """Return a datastructure describing the latest block
        in a network.
        """
        raise NotImplementedError
