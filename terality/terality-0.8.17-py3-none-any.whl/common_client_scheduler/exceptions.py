from abc import ABC
from dataclasses import dataclass

from terality_serde import SerdeMixin


@dataclass
class TeralityError(Exception, SerdeMixin, ABC):
    """Base class for all Terality errors (propagated to the client)'."""

    message: str

    def __init__(self, message: str) -> None:
        self.message = message
        super().__init__(message)


class TeralityAuthError(TeralityError):
    pass


class TeralityInternalError(TeralityError):
    pass


class TeralityInvalidRequest(TeralityError):
    pass


class TeralityQuotaExceeded(TeralityError):
    pass


class TeralityNotSupportedError(TeralityError):
    pass
