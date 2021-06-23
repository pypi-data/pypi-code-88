from __future__ import annotations

from typing import TypeVar, Generic, Callable, Generator


_T = TypeVar("_T")
_Thunk = Callable[[], _T]


class CommandError(Exception):
    pass


class Command(Generic[_T]):
    def __init__(self, cmd: _Thunk[_T], retries: int = 3):
        self.cmd = cmd
        self.retries = retries

    def run(self) -> _T:
        for ntry in range(0, self.retries):
            try:
                return self.cmd()
            except Exception as ex:
                if ntry == self.retries - 1:
                    raise CommandError(ex)

                continue

        raise RuntimeError()

    def __await__(self) -> Generator[_T, None, None]:
        yield self.run()
