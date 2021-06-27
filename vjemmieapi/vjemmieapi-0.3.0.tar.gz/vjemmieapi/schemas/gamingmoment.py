from pydantic import BaseModel, Field


class GamingMomentsBase(BaseModel):
    user: str
    count: int


class GamingMomentsIn(GamingMomentsBase):
    pass


class GamingMomentsOut(GamingMomentsBase):
    class Config:
        orm_mode = True
