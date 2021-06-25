from __future__ import annotations

from dataclasses import dataclass
from typing import List, TypeVar, Optional, Tuple

from .tag import Tag


@dataclass
class WithTags:
    tags: Optional[List[Tag]] = None
    """
     list of tags associated with the artifact
    """

    T = TypeVar("T", bound="WithTags")

    def with_tag(self: T, key: str, value: str) -> T:
        if self.tags is None:
            self.tags = []
        self.tags.append(Tag(key, value))
        return self

    def with_tags(self: T, tags: List[Tuple[str, str]]) -> T:
        if self.tags is None:
            self.tags = []
        for (key, value) in tags:
            self.tags.append(Tag(key, value))
        return self
