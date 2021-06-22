from pydantic import BaseModel


class CollectSpec(BaseModel):
    ns: str
    type: str
    version: int = 0
