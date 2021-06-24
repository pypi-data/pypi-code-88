from typing import NamedTuple, Optional


class Song(NamedTuple):
    track: str
    artist: str
    source: Optional[str]
    url: Optional[str]
