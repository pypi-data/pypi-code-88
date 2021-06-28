"""Declares :class:`TrustStore`."""
from .abstractkeystore import AbstractKeystore


class TrustStore(AbstractKeystore):
    """Like :class:`~unimatrix.ext.crypto.AbstractKeystore`, but only
    works with public keys.
    """
    __module__ = 'unimatrix.ext.crypto'


trust = TrustStore()
