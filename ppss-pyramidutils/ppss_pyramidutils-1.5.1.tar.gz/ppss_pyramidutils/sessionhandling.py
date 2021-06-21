from contextlib import contextmanager

import logging
l = logging.getLogger(__name__)

################# create session factory from pyramid settings
from sqlalchemy import engine_from_config
from sqlalchemy.orm import sessionmaker

def engineFromSettings(config):
  engine = engine_from_config(config, "sqlalchemy.")
  return engine

def factoryFormSettings(config):
  engine = engineFromSettings(config)
  session_factory = sessionmaker(bind=engine)
  return session_factory


#### allow usage of "with" clause with session
@contextmanager
def session_scope(sessionFactory):
    session = sessionFactory()
    l.info ("new session created")
    try:
        yield session
        l.info ("committing")
        session.commit()
    except Exception as e:
        session.rollback()
        l.exception("rollback for exception {}".format(e))
        raise e
    finally:
        session.close()
        l.info ("session closed")