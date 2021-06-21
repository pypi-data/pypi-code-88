from datetime import datetime
from typing import List

from pydantic import BaseModel


class GoodmorningBase(BaseModel):
    target: str
    submitter: str


class GoodmorningIn(GoodmorningBase):
    pass


class GoodmorningOut(GoodmorningBase):
    submitted: datetime

    class Config:
        orm_mode = True


class GoodmorningOutAll(BaseModel):
    targets: List[str]
