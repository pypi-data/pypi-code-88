from datetime import datetime

from sqlalchemy import Boolean, Column, DateTime, Float, ForeignKey, Integer, String

from ..db import Base


class Skribbl(Base):
    __tablename__ = "Skribbl"

    word = Column(String, primary_key=True, index=True)
    submitter = Column(String)
    submitted = Column(DateTime, default=datetime.utcnow)
    submittedReal = Column(Float, default=0.0)
