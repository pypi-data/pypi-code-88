from flask_appbuilder.models.sqla import Base

from src.sql import settings

db_url = ""


def init_db():
    connection = settings.engine.create() # create_engine(db_url)
    Base.metadata.create_all(settings.engine)
