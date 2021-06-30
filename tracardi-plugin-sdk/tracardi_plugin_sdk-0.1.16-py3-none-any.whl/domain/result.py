from typing import Any
from pydantic import BaseModel


class Result(BaseModel):
    port: str
    value: Any

    class Config:
        allow_mutation = False
