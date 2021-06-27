from sqlalchemy import Column, String, Integer, ForeignKey
from ..db import Base


class PFMMeme(Base):
    __tablename__ = "PFMMeme"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    topic = Column(String, index=True)
    title = Column(String)
    description = Column(String, nullable=True)
    content = Column(String)
    media_type = Column(String, ForeignKey("MediaType.media_type"))
