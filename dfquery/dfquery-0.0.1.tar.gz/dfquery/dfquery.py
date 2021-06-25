"""
dfquery process.
It supports READ/UPDATE/DELETE to pandas.DataFrame

@author hctaw-srp
"""
import sqlite3
import pandas as pd
import os
import uuid
import sqlparse

# --- Exception ---

class DFQueryError(Exception):
    pass

# --- private functions ---

def __get_sql_conn():
    dbname = str(uuid.uuid4())
    return sqlite3.connect(dbname), dbname


def __close_sql_conn(conn, dbname):
    conn.close()
    os.remove(dbname)


def __judge_query_type(query, crud_type):
    tokens = list(sqlparse.parse(query)[0].flatten())
    for t in tokens:
        if t.ttype == sqlparse.tokens.Keyword.DML:
            if t.value.upper() == crud_type.upper():
                return True
    return False

# --- public functions ---

def read(dataframe, query, resources=[]):
    if not __judge_query_type(query, "select"):
        raise DFQueryError("Not SELECT query is not supported by this function.")
    
    conn, dbname = __get_sql_conn()
    try:
        dataframe.to_sql("df", con=conn, index=False)
        if len(resources) != 0:
            for inx, r in enumerate(resources):
                r.to_sql(f"it{inx}", con=conn, index=False)
        return pd.read_sql_query(query, conn)
    finally:
        __close_sql_conn(conn, dbname)


def update(dataframe, query, resources=[]):
    if not __judge_query_type(query, "update"):
        raise DFQueryError("Not UPDATE query is not supported by this function.")

    conn, dbname = __get_sql_conn()
    try:
        dataframe.to_sql("df", con=conn, index=False)
        if len(resources) != 0:
            for inx, r in enumerate(resources):
                r.to_sql(f"it{inx}", con=conn, index=False)
        cur = conn.cursor()
        cur.execute(query)
        conn.commit()
        return pd.read_sql_query(f"select * from df", con=conn)
    finally:
        __close_sql_conn(conn, dbname)