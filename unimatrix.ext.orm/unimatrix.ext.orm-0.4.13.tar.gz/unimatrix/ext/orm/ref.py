"""Declares a reference datamodel for examples and tests."""
from sqlalchemy import Column
from sqlalchemy import Date
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class Book(Base):
    __tablename__ = 'books'

    id = Column(
        Integer,
        primary_key=True,
        name='id'
    )

    title = Column(String,
        unique=True,
        nullable=False,
        name='title'
    )

    published = Column(
        Date,
        nullable=False,
        name='published'
    )


def create(engine):
    """Creates the reference datamodel using the given `engine`."""
    return Base.metadata.create_all(engine)
