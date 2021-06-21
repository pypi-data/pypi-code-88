from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel


class SkribblIn(BaseModel):
    submitter: str
    words: List[str]


class SkribblOut(BaseModel):
    word: str
    submitter: str
    submitted: datetime

    class Config:
        orm_mode = True


class SkribblAddOut(BaseModel):
    added: List[str]
    failed: List[str]


class SkribblAggregateStats(BaseModel):
    words: int
    authors: int


class SkribblAuthorStats(BaseModel):
    user_id: str
    words: int


class SkribblStats(BaseModel):
    stats: List[SkribblAuthorStats]
