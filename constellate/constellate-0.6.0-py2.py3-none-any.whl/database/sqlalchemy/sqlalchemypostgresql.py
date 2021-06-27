from typing import Dict, Tuple, Optional

from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.pool import QueuePool
from sqlalchemy_utils import database_exists

from constellate.database.migration.databasetype import DatabaseType
from constellate.database.migration.migrate import migrate
from constellate.database.migration.migrationaction import MigrationAction
from constellate.database.sqlalchemy.sqlalchemy import SQLAlchemy
from constellate.database.sqlalchemy.sqlalchemydbconfig import SQLAlchemyDBConfig

_POOL_CONNECTION_PERMANENT_SIZE = 10
_POOL_CONNECTION_OVERFLOW_SIZE = 5


class SQLAlchemyPostgresql(SQLAlchemy):
    def __init__(self):
        super().__init__()

    def _get_database_driver_name(self) -> Optional[str]:
        return "asyncpg"

    async def _create_engine(self, options: Dict = {}) -> Tuple[str, object]:
        """
        :options:
        - host:str               . DB host
        - port:str               . DB port
        - username:str           . DB user name
        - password:str           . DB password
        - db_name:str            . DB name
        - db_name_fallback:str    . DB name to connect to if the database "db_name" does not exist (yet)
        - pool_connection_size:int            . Max permanent connection held in the pool. Default: 10
        - pool_connection_overflow_size:int            . Max connection returned in addition to the ones in the pool. Default: 5
        - pool_connection_timeout:float . Max timeout to return a connection, in seconds. Default: 30.0 (sec)
        - pool_pre_ping: bool. Default: False
        - custom: Dict[any,any]. Dictionary of custom attribute, never used by constellate
        - asynchronous:bool . Use asyncio enabled sqlalchemy engine. Default: False
        """
        # Create engine
        # - https://docs.sqlalchemy.org/en/14/dialects/postgresql.html
        username_port = ":".join(
            filter(None, [options.get("username", None), options.get("password", None)])
        )
        host_port = ":".join(filter(None, [options.get("host", None), options.get("port", None)]))
        credential_host = f"{username_port}@{host_port}"

        db_name = options.get("db_name", None)
        db_name_default = options.get("db_name_fallback", "postgres")

        scheme_driver = f"postgresql+{self._get_database_driver_name()}"
        connection_uri = f"{scheme_driver}://{credential_host}/{db_name}"
        connection_uri_plain = f"postgresql://{credential_host}/{db_name}"
        if not database_exists(connection_uri_plain):
            await self._create_database(
                connection_uri=f"{scheme_driver}://{credential_host}/{db_name_default}",
                db_name=db_name,
            )

        pool_size = options.get("pool_connection_size", 10)
        pool_overflow_size = options.get("pool_connection_overflow_size", 5)
        pool_timeout = options.get("pool_connection_timeout", 30.0)
        pool_pre_ping = options.get("pool_pre_ping", False)

        engine = create_async_engine(
            connection_uri,
            poolclass=QueuePool,
            pool_size=pool_size,
            max_overflow=pool_overflow_size,
            pool_timeout=pool_timeout,
            pool_pre_ping=pool_pre_ping,
            future=True,
        )
        return connection_uri, connection_uri_plain, engine

    async def _create_database(
        self, connection_uri: str = None, db_name: str = None, encoding="UTF8"
    ):
        async with create_async_engine(
            connection_uri, isolation_level="AUTOCOMMIT"
        ).connect() as connection:
            await connection.execute(f"CREATE DATABASE {db_name} ENCODING {encoding};")

    async def _migrate(self, instance: SQLAlchemyDBConfig = None, options: Dict = {}):
        migrate(
            database_type=DatabaseType.POSTGRESQL,
            connection_url=instance.connection_uri_plain,
            migration_dirs=options.get("migration_dirs", []),
            action=MigrationAction.UP,
            logger=instance.logger,
        )

    async def _vacuum(self, instance: SQLAlchemyDBConfig = None, options: Dict = {}):
        """
        :options:
        - profiles: A vacumm profile. Values:
        -- analyze: Updates statistics used by the planner (to speed up queries)
        -- default: Sensible defaults
        """
        # Vacuum requires a connection/session without transaction enabled.
        async with instance.engine.connect().execution_options(
            isolation_level="AUTOCOMMIT"
        ) as connection:
            commands = {
                "analyze": ["VACUUM ANALYZE;"],
                "default": ["VACUUM (ANALYZE, VERBOSE);"],
            }
            for profile in options.get("profiles", ["default"]):
                for statement in commands[profile]:
                    try:
                        await connection.execute(statement)
                    except BaseException as e:
                        raise Exception(f"Vacuum statement failed: {statement}") from e
