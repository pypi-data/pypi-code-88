from sqlalchemy import text, Column, String, Integer, create_engine, Float, TIMESTAMP, MetaData
from sqlalchemy.sql.expression import func
from sqlalchemy.ext.declarative import declarative_base
import pandas as pd
import os

import logging
logger = logging.getLogger(__name__)
formatter = logging.Formatter('%(levelname)s: [%(name)s] %(message)s')
ch = logging.StreamHandler()
ch.setFormatter(formatter)
logger.addHandler(ch)
logger.setLevel(logging.WARNING)

Base = declarative_base()


class C101(Base):
    __tablename__ = 'c101'
    date = Column("date", String, primary_key=True, nullable=False)
    코드 = Column("코드", String)
    종목명 = Column("종목명", String)
    업종 = Column("업종", String)
    주가 = Column("주가", Integer)
    거래량 = Column("거래량", Integer)
    EPS = Column("EPS", Float)
    BPS = Column("BPS", Float)
    PER = Column("PER", Float)
    업종PER = Column("업종PER", Float)
    PBR = Column("PBR", Float)
    배당수익률 = Column("배당수익률", Float)
    최고52주 = Column("최고52주", Float)
    최저52주 = Column("최저52주", Float)
    거래대금 = Column("거래대금", Float)
    시가총액 = Column("시가총액", Float)
    베타52주 = Column("베타52주", Float)
    발행주식 = Column("발행주식", Float)
    유통비율 = Column("유통비율", Float)
    intro1 = Column("intro1", String)
    intro2 = Column("intro2", String)
    intro3 = Column("intro3", String)

    def __str__(self):
        return '/'.join((self.date, self.코드, str(self.종목명), str(self.업종), self.주가))


class Timestamp(Base):
    __tablename__ = 'timestamp'
    id = Column(Integer, nullable=False, primary_key=True, autoincrement=True)
    name = Column(String)
    sqltime = Column(TIMESTAMP(timezone=True), server_default=func.now(), onupdate=func.current_timestamp())


def make_engine(db_path, code, echo=False):
    # make folder - /db/corp_db
    path = os.path.join(db_path, 'corps')
    if not os.path.isdir(path):
        os.makedirs(path)
    dsn = f"sqlite:///{os.path.join(path, ''.join([code, '.db']))}"
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


def save_df_to_db(engine, df: pd.DataFrame, tablename:str):
    drop_table(engine, tablename)
    # 테이블을 저장한다.
    if tablename.startswith('c106'):
        df.to_sql(tablename, con=engine, index=True, if_exists='replace')
    else:
        df.to_sql(tablename, con=engine, index=False, if_exists='replace')
    logger.info(f"Save dataframe on {tablename} table successfully...")


def stamping(session, tablename):
    stamp = Timestamp(name=tablename)
    session.add(stamp)
    logger.info(f"Stamping.. name:'{tablename}'")
    session.commit()
