from dataclasses import dataclass

from . import SerdeMixin


@dataclass
class CallableWrapper(SerdeMixin):
    dill_payload: str
