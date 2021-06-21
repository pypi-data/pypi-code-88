from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel


class SubredditAliasBase(BaseModel):
    subreddit: str
    alias: str


class SubredditAliasOut(BaseModel):
    alias: str

    class Config:
        orm_mode = True


class SubredditBase(BaseModel):
    subreddit: str
    is_text: bool
    submitter: str


class SubredditIn(SubredditBase):
    aliases: List[str] = []


class SubredditOut(SubredditBase):
    submitted: datetime
    aliases: List[SubredditAliasOut] = []

    class Config:
        orm_mode = True


class SubredditAliasUpdate(BaseModel):
    # We receive the subreddit implicitly through the endpoint
    alias: str
    remove: bool = False


class SubredditUpdate(BaseModel):
    is_text: Optional[bool] = None
    aliases: List[SubredditAliasUpdate] = []
