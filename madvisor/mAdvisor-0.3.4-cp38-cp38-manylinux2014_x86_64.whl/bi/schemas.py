# pydantic
from pydantic import BaseModel

# Built-in
from datetime import datetime

"""
Data validation and settings management using python type annotations.

pydantic enforces type hints at runtime, and provides user friendly errors
when data is invalid.

Define how data should be in pure, canonical python; validate it with pydantic.
"""


class LogCreate(BaseModel):
    request_type: str
    units: int
    request_datetime: datetime
    response_datetime: datetime
    file_name: str
    file_size: str
    token_id: int
    user_id: int
    platform: str
    run_status: str
