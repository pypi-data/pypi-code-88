from pydantic import BaseModel


class TidstyvBase(BaseModel):
    user_id: str
    stolen: float


class TidstyvIn(TidstyvBase):
    pass


class TidstyvOut(TidstyvBase):
    class Config:
        orm_mode = True
