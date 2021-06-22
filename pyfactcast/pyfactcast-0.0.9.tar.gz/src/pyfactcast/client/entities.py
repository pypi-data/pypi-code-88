from __future__ import annotations
import re

from typing import Type, TypeVar, Dict, List, Optional
from uuid import uuid4

from pyfactcast.grpc.generated.FactStore_pb2 import MSG_Notification
from pydantic import BaseModel, Extra, constr, validator

import json

F = TypeVar("F", bound="Fact")


class CatchUp:
    pass


UUID4_REGEX = re.compile(
    r"^[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}$"
)
# Sadly pydantic and mypy do not play nice here.
AggsId: constr = constr(  # type: ignore
    regex=r"^[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}$"
)


class FactHeader(BaseModel):
    class Config:
        extra = Extra.allow
        validate_assignment = True

    ns: str
    type: str
    id: str = ""  # type: ignore
    aggIds: Optional[List[AggsId]] = None  # type: ignore
    meta: Dict[str, str] = {}

    @validator("id", always=True)
    def set_id(cls, id: str) -> str:
        if id and not UUID4_REGEX.match(id):
            raise ValueError("id is not a valid UUID4")

        return id or str(uuid4())


class Fact(BaseModel):
    header: FactHeader
    payload: Dict

    @classmethod
    def from_msg(cls: Type[F], msg: MSG_Notification) -> F:
        return cls(
            header=json.loads(msg.fact.header), payload=json.loads(msg.fact.payload)
        )


class VersionedType(BaseModel):
    name: str
    version: int = 0


class SubscriptionSpec(BaseModel):
    ns: str
    type: Optional[VersionedType] = None
