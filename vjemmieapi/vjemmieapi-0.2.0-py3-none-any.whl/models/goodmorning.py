from sqlalchemy import Column, Integer, String, DateTime, Float
from sqlalchemy.sql.functions import func
from ..db import Base


class Goodmorning(Base):
    __tablename__ = "Goodmorning"

    id = Column(Integer, primary_key=True)
    target = Column(String(2048), index=True)
    submitter = Column(String(80))
    submitted = Column(DateTime, server_default=func.now())
    submittedDouble = Column(Float, default=0.0)
