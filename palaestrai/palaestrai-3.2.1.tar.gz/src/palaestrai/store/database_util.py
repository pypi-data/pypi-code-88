import time

from sqlalchemy import create_engine
from sqlalchemy.exc import ProgrammingError, OperationalError
from sqlalchemy.sql.expression import text
from sqlalchemy_utils import database_exists, create_database

from . import LOG
from .database_model import Model


def _create_timescaledb_extension(engine):
    with engine.begin() as conn:
        conn.execute("CREATE EXTENSION IF NOT EXISTS timescaledb CASCADE;")
    timescale_tables = {
        "world_states",
        "muscle_actions",
        "muscle_sensor_readings",
        "muscle_states",
    }
    with engine.begin() as conn:
        for tbl in timescale_tables:
            cmd = (
                "SELECT * FROM create_hypertable("
                "'%s', 'id', chunk_time_interval => 40960);" % tbl
            )
            res = conn.execute(text(cmd))
            LOG.debug(
                'Result of executing "%s" during setup: %s',
                cmd,
                res.fetchall(),
            )
            res.close()


def setup_database(uri):
    """Creates the database from the current model in one go.

    :param uri: The complete database connection URI.
    """
    engine = create_engine(uri)
    while not database_exists(uri):
        i = 1
        if i > 3:  # Hardcoded max tries. No real reason to configure this.
            LOG.critical(
                "Could not create the database. See errors above for more "
                "details. Giving up now."
            )
            raise RuntimeError("Could not create database")
        try:
            create_database(uri)
        except OperationalError as e:
            try:
                import psycopg2.errors

                if isinstance(e.orig, psycopg2.errors.ObjectInUse):
                    LOG.warning(
                        "Could not create database because the template was "
                        "in use. Retrying in %d seconds.",
                        i,
                    )
                    time.sleep(i)
                else:
                    break
            except ImportError:
                pass
        except ProgrammingError as e:
            LOG.error(
                "There was an error creating the database. I will continue "
                "and hope for the best. The error was: %s",
                e,
            )
        i += 1

    with engine.begin() as conn:
        try:
            Model.metadata.create_all(engine)
        except ProgrammingError as e:
            LOG.error("Could not create database: %s" % e)
            raise e
    try:
        _create_timescaledb_extension(engine)
    except OperationalError as e:
        LOG.warning(
            "Could not create extension timescaledb and create hypertables: "
            "%s. "
            "Your database setup might lead to noticeable slowdowns with "
            "larger experiment runs. Please upgrade to PostgreSQL with "
            "TimescaleDB for the best performance." % e
        )


def get_connection(uri):
    """This function creates a database if necessary and returns an engine
    object from SQLAlchemy. The database is automatically created, if not
    existent.

    Args:
        uri (String): <driver>://<user>:<password>@<uri>/<database name>
                e.g.: postgres://otto:vBismarck@8.8.8.8/rent

    Returns:
        engine: A SQLAlchemy object that provides a connection to the database,
        given in the url.
    """
    setup_database(uri)
    return create_engine(uri)
