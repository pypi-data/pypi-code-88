import inspect
from typing import Callable, Type, Dict, Tuple

from .protocol import Protocol
from . import liquid_files, sftp
from ..utils.progress import ProgressInterface

protocols: Tuple[Type[Protocol], ...] = (sftp.Protocol, liquid_files.Protocol)
protocols_by_name: Dict[str, Type[Protocol]] = {
    p.__module__.replace(__name__ + ".", ""): p for p in protocols
}
__all__ = tuple(protocols_by_name)


def parse_protocol(s: str) -> Type[Protocol]:
    try:
        return protocols_by_name[s]
    except KeyError:
        raise ValueError(f"Invalid protocol: {s}") from None
