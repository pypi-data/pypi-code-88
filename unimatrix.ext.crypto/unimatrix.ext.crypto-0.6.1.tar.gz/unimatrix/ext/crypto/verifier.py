"""Declares :class:`Verifier`."""
import abc


class Verifier(metaclass=abc.ABCMeta):
    """Declares an interface to verify signatures."""

    @abc.abstractmethod
    def verify(self, signature):
        """Return a boolean indicating if `signature` is valid."""
        raise NotImplementedError
