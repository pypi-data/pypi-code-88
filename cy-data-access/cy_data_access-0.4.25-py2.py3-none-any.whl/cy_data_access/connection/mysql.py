import pymysql
from sqlalchemy import create_engine


def mysql_connection(host='127.0.0.1', port=3306, user='root', passwd='123456', db='grafana'):

    database_connection = create_engine('mysql+pymysql://{0}:{1}@{2}/{3}'.
                                        format(user, passwd,
                                               host, db))
    return database_connection
