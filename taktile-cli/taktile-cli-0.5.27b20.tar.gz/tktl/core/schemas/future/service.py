from pydantic import BaseModel

from tktl.core.future.t import EndpointKinds


class EndpointInfoSchema(BaseModel):
    name: str
    kind: EndpointKinds
