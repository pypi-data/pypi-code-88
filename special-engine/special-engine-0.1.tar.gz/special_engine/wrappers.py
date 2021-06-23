from .capi import HS, HsExprExt, HsMode, HsFlag, HsPlatformInfo, ManagedPtr, hs_database, hs_scratch, HyperscanError
from typing import Optional, Sequence, ByteString, TypeVar, Callable, List, Generator
import contextlib


class ScratchPool:
    def __init__(self):
        self._pool: List[ManagedPtr[hs_scratch]] = []

    def _take_or_create_scratch(self, db: ManagedPtr[hs_database]) -> ManagedPtr[hs_scratch]:
        try:
            s = self._pool.pop()
        except IndexError:
            s = None
        s = HS.alloc_scratch(db, s)
        return s

    def _return_scratch(self, scratch: ManagedPtr[hs_scratch]) -> None:
        self._pool.append(scratch)

    @contextlib.contextmanager
    def scratch(self, db: ManagedPtr[hs_database]) -> Generator[ManagedPtr[hs_scratch], None, None]:
        s = self._take_or_create_scratch(db)
        try:
            yield s
        finally:
            self._return_scratch(s)


T = TypeVar('T')
class Database:
    def __init__(
            self,
            expressions: Sequence[ByteString],
            ids: Optional[Sequence[int]] = None,
            flags: Optional[Sequence[HsFlag]] = None,
            ext: Optional[Sequence[HsExprExt]] = None,
            mode: HsMode = HsMode.BLOCK,
    ) -> None:
        self._sp = ScratchPool()

        if ids is None:
            ids = [0] * len(expressions)
        if flags is None:
            flags = [HsFlag(0)] * len(expressions)
        if ext is None:
            ext = [None] * len(expressions)
        self._db = HS.compile_ext_multi(
            expressions=expressions,
            ids=ids,
            flags=flags,
            exts=ext,
            mode=mode,
            platform=HsPlatformInfo(),
        )

    @classmethod
    def load(cls: T, data: ByteString) -> T:
        self = cls()
        self._db = HS.deserialize_database(data)

    def dump(self) -> ByteString:
        return HS.serialize_database(self._db)

    def scan(
            self,
            data: ByteString,
            match_event_handler: Optional[Callable[[int, int, int, int], Optional[bool]]],
    ) -> None:
        if match_event_handler is not None:
            def wrap_event_handler(id_, from_, to_, flags_, ignore_context, v=None):
                try:
                    v = match_event_handler(id_, from_, to_, flags_)
                finally:
                    return 1 if v else 0
        else:
            wrap_event_handler = None
        with self._sp.scratch(self._db) as scratch:
            HS.scan(self._db, scratch, data, wrap_event_handler)

