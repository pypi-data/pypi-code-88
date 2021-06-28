"""Declares :class:`KeyLoader`."""
import abc

from unimatrix.lib.datastructures import ImmutableDTO

from .keychain import chain as default_chain
from .truststore import trust as default_trust


class KeyLoader(metaclass=abc.ABCMeta):
    """Declares the interface for all Key Loader implementations. A
    key loader knows how to retrieve keys from various backends. For
    the reference example, see the :mod:`unimatrix.ext.crypto.google`
    module.
    """

    def __init__(self, opts, public_only=False):
        self.__opts = opts
        self.__public_only = public_only
        self.setup(ImmutableDTO.fromdict(opts))

    def setup(self, opts):
        """Hook called during instance initialization."""
        pass

    async def load(self, chain=None, trust=None):
        """Load all keys and add them to the :term:`Key Store` and
        :term:`Trust Store`.
        """
        chain = chain or default_chain
        trust = trust or default_trust
        async for key in self.list():
            if key.is_private():
                if not self.__public_only:
                    chain.register(key.id, key)
                if key.has_public_key():
                    trust.register(key.id, await key.get_public_key())
                continue
            if key.is_public():
                trust.register(key.id, key)
                continue
