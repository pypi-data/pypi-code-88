import sys
from contextlib import contextmanager
from os.path import abspath, dirname

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session, declarative_base

from .dialect.dialect import Dialect

sys.path.append(abspath(dirname(__file__) + "/.."))
from utils.app_logger import get_logger

Base = declarative_base()

class Database(): 

    def __init__(self, dialect:Dialect) -> None:
        self.dialect = dialect
        self.logger = get_logger("common.database")
        self._setup_connection()
    
    def _setup_connection(self): 
        if self.dialect is None:
            raise ValueError("Database dialect can not be None while setting up connection.")
        self.session_factory = sessionmaker(bind=self.create_engine(), expire_on_commit=False)

    def create_engine(self): 
        return create_engine(self.get_dialect().get_url(), echo=True, pool_size=100, max_overflow=0, pool_recycle=3600)

    def get_dialect(self) -> Dialect: 
        return self.dialect

    @contextmanager
    def open(self):
        try: 
            session = scoped_session(self.session_factory)()
            yield session
            session.commit()
        except Exception as e: 
            self.logger.exception(e)
            session.rollback()
            raise e
        finally: 
            session.expunge_all()
            session.close()