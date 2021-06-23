from typing import Optional, Sequence

from .wrappers import Database as _Database, HyperscanError as error
from .constants import *

class Database:
    def __init__(self, mode: HsMode = HsMode.BLOCK) -> None:
        self._db: Optional[_Database] = None
        self._mode = mode

    def compile(
            self,
            expressions: Sequence[ByteString],
            ids: Optional[Sequence[int]] = None,
            flags: Optional[Sequence[HsFlag]] = None,
            ext: Optional[Sequence[HsExprExt]] = None,
            elements: int = -1,
    ) -> None:
        if elements not in (-1, len(expressions)):
            raise ValueError
        self._db = _Database(expressions, ids, flags, ext, mode)

    def scan(
            self,
            data: ByteString,
            match_event_handler: Optional[Callable[[int, int, int, int, T], Optional[bool]]],
            context: T = None,
    ) -> None:
        if match_event_handler is not None:
            def wrapped_event_handler(id_, from_, to_, flags):
                return match_event_handler(id_, from_, to_, flags, context)
        else:
            wrapped_event_handler = None
        return self._db.scan(data, match_event_handler)


def loadb(data: typing.ByteString) -> Database:
    db = _Database.load(data)
    wrapper = object.__new__(Database)
    wrapper._db = db

def dumpb(db: Database) -> typing.ByteString:
    return db._db.dump()
