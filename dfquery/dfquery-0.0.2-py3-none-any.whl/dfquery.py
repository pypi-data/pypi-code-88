import sqlite3
import pandas as pd
import os
import uuid
import sqlparse

# --- exception ---


class DFQueryError(Exception):
    pass


# --- query client ---


class DFQuery:
    def __init__(self, gvars):
        self.vars = gvars
        self.dbid = str(uuid.uuid4())

    # --- private functions ---

    def __get_sql_conn(self):
        return sqlite3.connect(self.dbid)

    def __close_sql_conn(self, conn):
        conn.close()

    def __judge_query_type(self, query, crud_type):
        tokens = list(sqlparse.parse(query)[0].flatten())
        for t in tokens:
            if t.ttype == sqlparse.tokens.Keyword.DML:
                if t.value.upper() == crud_type.upper():
                    return True
        return False

    def __get_var_name(self, var):
        for k, v in self.vars.items():
            if id(v) == id(var):
                return k

    # --- public functions ---

    def read(self, dataframe, query, resources=[]):
        if not self.__judge_query_type(query, "select"):
            raise DFQueryError("Not SELECT query is not supported by this function.")

        conn = self.__get_sql_conn()
        try:
            dataframe.to_sql(
                self.__get_var_name(dataframe),
                con=conn,
                index=False,
                if_exists="replace",
            )
            if len(resources) != 0:
                for r in resources:
                    r.to_sql(
                        self.__get_var_name(r),
                        con=conn,
                        index=False,
                        if_exists="replace",
                    )
            return pd.read_sql_query(query, conn)
        finally:
            self.__close_sql_conn(conn)

    def update(self, dataframe, query, resources=[]):
        if not self.__judge_query_type(query, "update"):
            raise DFQueryError("Not UPDATE query is not supported by this function.")

        conn = self.__get_sql_conn()
        target = self.__get_var_name(dataframe)
        try:
            dataframe.to_sql(target, con=conn, index=False, if_exists="replace")
            if len(resources) != 0:
                for r in resources:
                    r.to_sql(
                        self.__get_var_name(r),
                        con=conn,
                        index=False,
                        if_exists="replace",
                    )
            cur = conn.cursor()
            cur.execute(query)
            conn.commit()
            return pd.read_sql_query(f"select * from {target}", con=conn)
        finally:
            self.__close_sql_conn(conn)

    def execute(self, query):
        conn = self.__get_sql_conn()
        try:
            cur = conn.cursor()
            cur.execute(query)
            conn.commit()
        finally:
            self.__close_sql_conn(conn)

    def close(self):
        os.remove(self.dbid)
