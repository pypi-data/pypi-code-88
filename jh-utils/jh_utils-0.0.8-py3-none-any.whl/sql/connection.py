from sqlalchemy import create_engine
import psycopg2

def create_connection(database: str, user: str, password: str, host: str, port: str, sgbd = 'postgresql'):
    """
    Declare a db connection

    Args:
        database (str): database name
        user (str): user
        password (str): password
        host (str): host
        port (str): port
        sgbd (str, optional): Defaults to 'postgresql'. Change the sgbd string in the db connection-string

    Returns:
        sql alchemy db engine: 
    """    

    ## Creating db string connection
    if sgbd == 'postgresql':
        con_string = 'postgresql://'+user+':'+password+'@'+host+':'+port+'/'+database
    if sgbd == 'mysql':
        con_string = 'mysql+pymysql://'+user+':'+password+'@'+host+':'+port+'/'+database
    return create_engine(con_string)