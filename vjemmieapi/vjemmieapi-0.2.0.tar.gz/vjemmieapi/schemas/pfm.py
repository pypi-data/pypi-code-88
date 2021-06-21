from typing import List, Optional
from pydantic import BaseModel


class PFMMemeBase(BaseModel):
    topic: str
    title: str
    content: str
    media_type: str
    description: Optional[str] = None


class PFMMemeIn(PFMMemeBase):
    pass


class PFMMemeOut(PFMMemeBase):
    class Config:
        orm_mode = True


class MemeList:  # NOTE: unuseds
    topic: str
    memes: List[PFMMemeOut] = []
