from sqlalchemy import select, text

from src.sql.settings import create_conn

engine = create_conn()

"""
CRUD with postgres
"""


def select_all(table_name):
    conn = engine.connect()
    query = select(text('select * from variables'))
    #print(query)
    result = conn.execute(query)
    # row = result.fetchone()
    # print(row)
    #for res in result:
    #    print(res)


if __name__ == '__main__':
    table_name = 'variables'
    select_all(table_name)