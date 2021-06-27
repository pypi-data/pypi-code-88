from sqlalchemy import Column, String
from ..db import Base


class MediaType(Base):
    __tablename__ = "MediaType"

    media_type = Column(String, primary_key=True, index=True)
    description = Column(String)
