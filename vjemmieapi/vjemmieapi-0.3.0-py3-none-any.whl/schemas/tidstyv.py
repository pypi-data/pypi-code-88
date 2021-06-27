from pydantic import BaseModel


class TidstyvBase(BaseModel):
    user: str
    stolen: float


class TidstyvIn(TidstyvBase):
    pass


class TidstyvOut(TidstyvBase):
    class Config:
        orm_mode = True
