from sqlalchemy import Column, String, Float
from ..db import Base


class Tidstyv(Base):
    __tablename__ = "Tidstyv"

    user_id = Column(String, primary_key=True, index=True)
    stolen = Column(Float)
