from typing import Optional

from pydantic import BaseModel


class DockerReference(BaseModel):
    image: str
    port: Optional[int]


class BlobReference(BaseModel):
    url: str


class ModelReference(BaseModel):
    docker: Optional[DockerReference]
    blob: Optional[BlobReference]


class ModelReferenceJson(BaseModel):
    reference: ModelReference
