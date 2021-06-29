import json
from mysql.connector import Error, PoolError
from .connector import MySQLConnector


class Query:
    SELECT_ONE = 'SELECT_ONE'
    SELECT_MANY = 'SELECT_MANY'
    UPDATE = 'UPDATE'
    CREATE = 'CREATE'
    DELETE = 'DELETE'

    def __init__(self, query: str, args: dict or tuple or None, type: str = SELECT_ONE):
        self.query = query
        self.args = args
        self.type = type

    def __str__(self):
        return json.dumps({'query': self.query, 'args': self.args, 'type': self.type})


class QueryResponse:
    SUCCESS = 0
    FAIL = 1

    def __init__(self, response, response_message=None, response_code=None, conn=None):
        self.result = response
        self.message = response_message
        self.code = response_code
        self.conn = conn


def execute_old(*queries) -> QueryResponse:
    if not queries:
        return QueryResponse(response=None,
                             response_message='no query provided!',
                             response_code=QueryResponse.FAIL)

    results = []
    response_code = QueryResponse.SUCCESS
    response_message = None

    try:
        conn = MySQLConnector.get_connection()
        cursor = conn.cursor(dictionary=True)
    except PoolError as e:
        response_message, response_code = e.msg, e.errno
        return QueryResponse(response=None, response_message=response_message, response_code=response_code)

    try:
        for q in queries:
            cursor.execute(q.query, q.args)
            type = q.type
            if type == Query.SELECT_ONE:
                data = cursor.fetchone()
            elif type == Query.SELECT_MANY:
                data = cursor.fetchall()
            elif type == Query.UPDATE or type == Query.DELETE:
                data = {'row_count': cursor.rowcount}
            else:  # CREATE
                data = {'last_row_id': cursor.lastrowid}
            results.append(data)
        conn.commit()

    except Error as e:
        conn.rollback()
        results = None
        response_message, response_code = e.msg, e.errno
    finally:
        if cursor is not None:
            cursor.close()
            conn.close()

    return QueryResponse(response=None if results is None else results[0] if len(queries) == 1 else results,
                         response_message=response_message,
                         response_code=response_code)


def execute(*queries, conn=None, do_commit=True) -> QueryResponse:
    if not queries:
        return QueryResponse(response=None,
                             response_message='no query provided!',
                             response_code=QueryResponse.FAIL)

    results = []
    response_code = QueryResponse.SUCCESS
    response_message = None

    try:
        if conn is None:
            conn = MySQLConnector.get_connection()
    except PoolError as e:
        response_message, response_code = e.msg, e.errno
        return QueryResponse(response=None, response_message=response_message, response_code=response_code)

    try:
        for q in queries:
            cursor = conn.cursor(dictionary=True)
            cursor.execute(q.query, q.args)
            if q.type == Query.SELECT_ONE:
                data = cursor.fetchone()
            elif q.type == Query.SELECT_MANY:
                data = cursor.fetchall()
            elif q.type == Query.UPDATE or q.type == Query.DELETE:
                data = {'row_count': cursor.rowcount}
            else:  # CREATE
                data = {'last_row_id': cursor.lastrowid}
            results.append(data)
            cursor.close()

        if do_commit: conn.commit()

    except Error as e:
        conn.rollback()
        results = None
        response_message, response_code = e.msg, e.errno
    finally:
        query_response = QueryResponse(
            response=None if results is None else results[0] if len(queries) == 1 else results,
            response_message=response_message,
            response_code=response_code)

        if do_commit or response_code != QueryResponse.SUCCESS:
            conn.close()
        else:
            query_response.conn = conn

        return query_response
