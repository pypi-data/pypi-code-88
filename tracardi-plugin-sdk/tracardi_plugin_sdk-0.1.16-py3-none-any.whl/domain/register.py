from typing import List, Optional
from pydantic import BaseModel


class Spec(BaseModel):
    className: str
    module: str
    inputs: Optional[List[str]] = []
    outputs: Optional[List[str]] = []
    init: Optional[dict] = None
    manual: Optional[str] = None


class MetaData(BaseModel):
    name: str
    desc: Optional[str] = ""
    type: str
    width: int
    height: int
    icon: str
    group: Optional[List[str]] = ["General"]


class Plugin(BaseModel):
    start: bool = False
    debug: bool = False
    spec: Spec
    metadata: MetaData
