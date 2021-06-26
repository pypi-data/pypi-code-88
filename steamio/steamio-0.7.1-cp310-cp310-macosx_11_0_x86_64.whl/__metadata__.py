from typing import NamedTuple

from typing_extensions import Literal

__all__ = (
    "__title__",
    "__author__",
    "__license__",
    "__version__",
    "version_info",
)


class VersionInfo(NamedTuple):
    major: int
    minor: int
    micro: int
    releaselevel: Literal["alpha", "beta", "candidate", "final"]


__title__ = "steam"
__author__ = "Gobot1234"
__license__ = "MIT"
__version__ = "0.7.1"
version_info = VersionInfo(major=0, minor=7, micro=1, releaselevel="final")
