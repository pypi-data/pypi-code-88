"""DTO of user"""
from pydantic import BaseModel


class User(BaseModel):
    """
    Represents a user connected to the server.
    """
    user_id: int
    username: str
