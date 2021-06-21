from typing import Sequence, Optional
from abc import ABC, abstractmethod
from ..utils.progress import ProgressInterface


class Protocol(ABC):
    @abstractmethod
    def upload(
        self,
        files: Sequence[str],
        progress: Optional[ProgressInterface] = None,
    ):
        ...

    def required_password_args(self) -> Sequence[str]:  # pylint: disable=no-self-use
        return ()
