"""Declares :class:`Algorithm`."""
import abc


class Algorithm(metaclass=abc.ABCMeta):
    __module__ = 'unimatrix.ext.crypto.algorithms'

    async def get_public_key(self):
        raise NotImplementedError
