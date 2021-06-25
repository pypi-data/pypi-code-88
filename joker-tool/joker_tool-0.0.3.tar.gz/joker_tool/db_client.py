# -*- coding: utf-8 -*-
"""
File Name:  encrypt.py
Author:     Zsy
Place:      BeiJin
Time:       2021-03-03
"""
import pymongo
import pymysql
import redis


class DbClient(object):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def conn_redis(self, pwd=None, ip=None, port=None, db=None):
        """
        :param pwd: redis 密码
        :param ip: ip
        :param port: 端口
        :param db: 库
        :return:
        """
        if pwd:
            redis_url = f"redis://{ip}:{port}/{db}"
        else:
            redis_url = f"redis://:{pwd}@{ip}:{port}/{db}"
        return redis.StrictRedis(connection_pool=redis.ConnectionPool.from_url(redis_url))

    def conn_mongodb(self, username, pwd, ip, port, db, table):
        """
        :param username: 数据库用户名
        :param pwd: 数据库密码
        :param ip: host
        :param port: port
        :param db: 数据库名
        :param table: 表名
        :return:
        """
        mongodb_url = f"mongodb://{username}:{pwd}@{ip}:{port}/{db}"
        client = pymongo.MongoClient(mongodb_url)
        dbs = eval(f'client.{db}')
        tables = eval(f"dbs.{table}")
        return tables

    def conn_mysql(self, username, pwd, ip, port, db, sql, method=None, ty=None):
        conn = pymysql.connect(host=ip, port=int(port), user=username, password=pwd,
                               db=db, cursorclass=pymysql.cursors.DictCursor, charset='utf8')
        cursor = conn.cursor()
        if method == "find":
            cursor.execute(sql)
            if ty == 0:
                result = cursor.fetchone()
                return result
            elif ty == 1:
                result = cursor.fetchall()
                return result
        elif method == "update":
            try:
                cursor.execute(sql)
                conn.commit()
                return "Data update successful!"
            except Exception as e:
                info = f"Data update failed!\n{e}"
                raise info
        else:
            return cursor.execute(sql)
