from sqlalchemy import Column, Integer, String
from ..db import Base


class GamingMoment(Base):
    __tablename__ = "Gamingmoment"

    user_id = Column(String, primary_key=True, index=True)
    count = Column(Integer, index=True)
