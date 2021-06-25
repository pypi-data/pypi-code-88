import os
from sqlalchemy import text, Column, String, create_engine, Float, MetaData
from sqlalchemy.ext.declarative import declarative_base

import logging
logger = logging.getLogger(__name__)
formatter = logging.Formatter('%(levelname)s: [%(name)s] %(message)s')
ch = logging.StreamHandler()
ch.setFormatter(formatter)
logger.addHandler(ch)
logger.setLevel(logging.WARNING)

Base = declarative_base()

"""
파이프라인에서 sqlite3로 저장하는데 사용되는 함수들 모음
"""


class Kospi(Base):
    __tablename__ = 'kospi'
    date = Column("date", String, primary_key=True, nullable=False)
    value = Column("value", Float)

    def __str__(self):
        return '/'.join((self.date, str(self.value)))


class Kosdaq(Base):
    __tablename__ = 'kosdaq'
    date = Column("date", String, primary_key=True, nullable=False)
    value = Column("value", Float)

    def __str__(self):
        return '/'.join((self.date, str(self.value)))


class Gbond3y(Base):
    __tablename__ = 'gbond3y'
    date = Column("date", String, primary_key=True, nullable=False)
    value = Column("value", Float)

    def __str__(self):
        return '/'.join((self.date, str(self.value)))


class Sp500(Base):
    __tablename__ = 'sp500'
    date = Column("date", String, primary_key=True, nullable=False)
    value = Column("value", Float)

    def __str__(self):
        return '/'.join((self.date, str(self.value)))


class Usdkrw(Base):
    __tablename__ = 'usdkrw'
    date = Column("date", String, primary_key=True, nullable=False)
    value = Column("value", Float)

    def __str__(self):
        return '/'.join((self.date, str(self.value)))


class Wti(Base):
    __tablename__ = 'wti'
    date = Column("date", String, primary_key=True, nullable=False)
    value = Column("value", Float)

    def __str__(self):
        return '/'.join((self.date, str(self.value)))


class Aud(Base):
    __tablename__ = 'aud'
    date = Column("date", String, primary_key=True, nullable=False)
    value = Column("value", Float)

    def __str__(self):
        return '/'.join((self.date, str(self.value)))


class Chf(Base):
    __tablename__ = 'chf'
    date = Column("date", String, primary_key=True, nullable=False)
    value = Column("value", Float)

    def __str__(self):
        return '/'.join((self.date, str(self.value)))


class Gold(Base):
    __tablename__ = 'gold'
    date = Column("date", String, primary_key=True, nullable=False)
    value = Column("value", Float)

    def __str__(self):
        return '/'.join((self.date, str(self.value)))


class Silver(Base):
    __tablename__ = 'silver'
    date = Column("date", String, primary_key=True, nullable=False)
    value = Column("value", Float)

    def __str__(self):
        return '/'.join((self.date, str(self.value)))


class YieldGap(Base):
    __tablename__ = 'yieldgap'
    date = Column("date", String, primary_key=True, nullable=False)
    value = Column("value", Float)

    def __str__(self):
        return '/'.join((self.date, str(self.value)))


class AvgPer(Base):
    __tablename__ = 'avgper'
    date = Column("date", String, primary_key=True, nullable=False)
    value = Column("value", Float)

    def __str__(self):
        return '/'.join((self.date, str(self.value)))


def make_engine(db_path, echo=False):
    # make folder - /db/mi
    path = os.path.join(db_path, 'mi')
    if not os.path.isdir(path):
        os.makedirs(path)
    dsn = f"sqlite:///{os.path.join(path, 'mi.db')}"
    return create_engine(dsn, echo=echo)


def get_tables(engine):
    meta = MetaData()
    meta.reflect(bind=engine)
    return tuple(meta.tables.keys())


def drop_table(engine, tablename):
    with engine.connect() as conn:
        logger.info(f"Drop '{tablename}' table ...")
        conn.execute(text(f'DROP TABLE IF EXISTS {tablename}'))
        conn.execute(text('VACUUM'))

