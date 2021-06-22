from datetime import datetime
from enum import Enum
from typing import Dict, List, Optional
from uuid import UUID

from pydantic import BaseModel, Field


class MediaType(str, Enum):
    CSV = 'text/csv'
    GEOJSON = 'application/geo+json'
    JSON = 'application/json'


class Dataset(BaseModel):
    """A model representing an Unfolded Studio Dataset
    """
    id: UUID
    name: str
    created_at: datetime = Field(..., alias='createdAt')
    updated_at: datetime = Field(..., alias='updatedAt')
    description: Optional[str]
    is_valid: bool = Field(..., alias='isValid')

    class Config:
        allow_population_by_field_name = True


class MapState(BaseModel):
    """A model representing an Unfolded Studio Map Starte
    """
    id: UUID
    # data contains the actual map configuration, and should be modeled more concretely than a
    # generic Dictionary.
    # Todo (wesam@unfolded.ai): revisit this once we have a style building strategy
    data: Dict

    class Config:
        allow_population_by_field_name = True


class MapUpdateParams(BaseModel):
    """A model respresenting creation and update parameters for Unfolded Maps
    """
    name: Optional[str]
    description: Optional[str]
    latest_state: Optional[MapState] = Field(None, alias="latestState")
    datasets: Optional[List[UUID]]

    class Config:
        allow_population_by_field_name = True


class Map(BaseModel):
    """A model representing an Unfolded Studio Map
    """
    id: UUID
    name: str
    description: Optional[str]
    created_at: datetime = Field(..., alias='createdAt')
    updated_at: datetime = Field(..., alias='updatedAt')
    latest_state: Optional[MapState] = Field(None, alias="latestState")
    datasets: Optional[List[Dataset]]

    class Config:
        allow_population_by_field_name = True
