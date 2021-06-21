from typing import Dict

from sqlalchemy.orm.query import Query
from sqlalchemy.engine import Engine
from sqlalchemy.engine.default import DefaultDialect


def stringify(
    query: Query = None,
    engine: Engine = None,
    dialect: DefaultDialect = None,
    compile_kwargs: Dict = {},
) -> str:
    """
    @query: Query object to get plain SQL query from
    @engine: Database type to know the SQL dialect to convert into

    src: https://stackoverflow.com/a/23835766/219728
    """
    return (
        query.statement.compile(engine)
        if engine is not None
        else query.statement.compile(
            dialect=dialect, compile_kwargs={"literal_binds": True, **compile_kwargs}
        )
    )


def resolve_engine_from_query(query: Query = None):
    """
    Resovle the engine used by the query. Useful when the db session uses shards
    """
    # PERF: This will execute the query!!!! As of 2021 Mai, I did not find a way to get this info without executing the
    # query against the db
    engine = query._iter()._real_result.raw.connection.engine
    return engine
