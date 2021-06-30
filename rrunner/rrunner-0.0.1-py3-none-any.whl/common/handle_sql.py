import pymysql
from rrunner.common.handle_config import config


# 封装一个获取数据库的类
class DB:
    def __init__(self, host, port, user, password):
        # 创建一个连接对象
        self.con = pymysql.connect(host=host,
                                   port=port,
                                   user=user,
                                   password=password,
                                   charset="utf8",
                                   cursorclass=pymysql.cursors.DictCursor)
        self.cur = self.con.cursor()

    def find_data(self, sql):
        """定义一个查询数据库的方法，sql为查询语句"""
        # 提交事务
        self.con.commit()
        # 执行sql语句
        self.cur.execute(sql)
        self.con.commit()
        # 以元组的形式返回所有的记录
        res = self.cur.fetchall()
        return res

    def find_count(self, sql):
        """返回查询数据的条数"""
        self.con.commit()
        return self.cur.execute(sql)

    def find_count1(self, sql):
        """返回查询数据的条数"""
        # 提交事务
        self.con.commit()
        # 执行sql语句
        self.cur.execute(sql)
        self.con.commit()
        # 以元组的形式返回所有的记录
        res = self.cur.fetchall()
        return str(res[0]['count(*)'])


# 创建db对象，连接数据库
db = DB(host=config.get("mysql", "host"),
        port=int(config.get("mysql", "port")),
        user=config.get("mysql", "user"),
        password=config.get("mysql", "password"))
