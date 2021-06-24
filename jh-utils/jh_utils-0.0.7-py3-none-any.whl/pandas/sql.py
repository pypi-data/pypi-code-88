## importing libs
import pandas as pd
import json
from sqlalchemy import create_engine
import psycopg2

def get_data(query, engine):
    """
    make a query in a database
    """
    ## open connection
    engine.connect()
    
    ## make select query
    table = pd.read_sql(query, engine)

    ## close connection    
    engine.close()
    return table

def write_table(table, table_name, schema, engine, if_exists = 'append', chunksize = 10_000, index= False):
    """
    if_exists => ["append","replace"]
    
    """

    ## open connection
    engine.connect()

    ## write or replace table
    table.to_sql(name = table_name,
                 if_exists = if_exists,
                 con = engine,
                 schema=schema,
                 method='multi',
                 chunksize = chunksize,
                 index = index)

    ## close connection
    engine.close()

