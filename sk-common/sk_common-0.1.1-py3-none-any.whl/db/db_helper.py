# -*- coding:utf-8 -*-
"""
连接sql server 或者mysql数据库，进行sql语句操作，可读取数据到pandas dataframe
"""
import pyodbc
import pandas as pd
import numpy as np


class DBHelper(object):

    def __init__(self, db_kind, driver, server, user, pwd, database, port='0'
                 ):
        """
        初始化数据库连接

        :param db_kind:  str，数据库类型, 目前只支持两种类型，mysql 和 sql server
        :param driver: str，odbc驱动，pyodbc.drivers()可查询系统所含驱动。例如：'SQL Server、'MySQL ODBC 8.0 Unicode Driver'
        :param server: str, 服务器ip
        :param user: str, 账号
        :param pwd: str, 密码
        :param database: str，数据库名
        :param port: str，特定端口，默认'0'
        """
        if db_kind == 'sql server':
            if port == '0':
                conn_info = 'DRIVER=' + driver + ';SERVER=' + server + \
                    ';DATABASE=' + database + ';UID=' + user + ';PWD=' + pwd
            else:
                conn_info = 'DRIVER=' + driver + ';SERVER=' + server + ',' + port + \
                    ';DATABASE=' + database + ';UID=' + user + ';PWD=' + pwd + ';'
            self.connection = pyodbc.connect(conn_info)
            self.cursor = self.connection.cursor()

        elif db_kind == 'mysql':
            conn_info = 'Driver=' + driver + ';Server=' + server + ';Port=' + port + \
                ';Database=' + database + ';User=' + user + ';Password=' + pwd + ';'

            self.connection = pyodbc.connect(conn_info)
            self.cursor = self.connection.cursor()
        else:
            print("数据库类型db_kind参数只支持sql server和 mysql")

    def __del__(self):
        if self.cursor:
            self.cursor.close()
            self.cursor = None
        if self.connection:
            self.connection.close()
            self.connection = None

    def destroy(self):
        """
        关闭cursor和connection
        """
        if self.cursor:
            print(self.cursor, 'cursor closed')
            self.cursor.close()
            self.cursor = None
        if self.connection:
            print(self.connection, 'connection closed')
            self.connection.close()
            self.connection = None

    def read_table_to_df(self, sql):
        """
        读取数据库表并存为pandas dataframe

        :param sql: sql查询语句
        :return: pandas dataframe
        """
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        result = np.array(result)
        if result.shape[0] != 0:
            result = pd.DataFrame(result, columns=list(
                zip(*self.cursor.description))[0])
        else:
            result = None
        return result

    def get_cursor(self, sql):
        """
        执行sql语句，返回对应cursor

        :param sql: 要执行的sql语句
        :return:  对应cursor
        """
        self.cursor.execute(sql)
        return self.cursor

    def conn_commit(self):
        """
        执行建表或删表等操作后，做connection commit
        """
        self.connection.commit()
