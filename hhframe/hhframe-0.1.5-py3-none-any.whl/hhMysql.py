
# -*- codeing = utf-8 -*-
# @File：hhMysql.py
# @Ver：1.0.0
# @Author：立树
# @Time：2021/6/10 1:32
# @IDE：PyCharm

import MySQLdb

class hhMysql(object):

    conn = None
    hhOpt = {
        "host": "",
        "port": 3306,
        "username": "",
        "password": "",
        "database": ""
    }

    def __init__(self,opt={}):
        try:
            # 配置
            self.hhOpt.update(opt)
            # 连接数据库
            self.connect()
        except Exception as err:
            self.__Error(err)

    # 连接数据库
    def connect(self):
        # 参数判断
        host,port,username,password,database = self.hhOpt.values()
        if host=="" or port=="" or username=="" or password=="" or database=="":
            self.__Error("请补全数据库参数（host、port、username、password、database）")
            return

        try:
            self.conn = MySQLdb.connect(
                host = host,
                port = port,
                user = username,
                passwd = password,
                db = database,
                charset = "utf8"
            )
        except MySQLdb.Error as err:
            self.__Error(f"Error {err.args[0]}: {err.args[1]}")

    # 关闭连接
    def close(self):
        if self.conn:
            self.conn.close()

    # 查询数据
    def query(self,sql=""):
        # 参数判断
        if sql=="":
            return self.__Response({
                "msg": "fail"
            })

        # 执行 SQL
        Command = {
            "select": "查询成功",
            "insert": "插入成功",
            "update": "修改成功",
            "delete": "删除成功"
        }
        command = sql[0:6].lower()
        cursor = self.conn.cursor()
        try:
            if command=="select":
                cursor.execute(sql)
                rows = cursor.fetchall()
                cols = [key[0] for key in cursor.description]
                return self.__Response({
                    "result": [dict(zip(cols,row)) for row in rows],
                    "nums": cursor.rowcount,
                    "rows": rows,
                    "cols": cols,
                    "sql": sql,
                    "msg": Command[command]
                })
            else:
                cursor.execute(sql)
                self.conn.commit()
                return self.__Response({
                    "nums": cursor.rowcount,
                    "sql": sql,
                    "msg": Command[command] if cursor.rowcount>0 else "ok"
                })
        except Exception as err:
            self.__Error(f"Error {err.args[0]}: {err.args[1]}")
            self.conn.rollback()
            return self.__Response({
                "msg": err
            })
        finally:
            cursor.close()

    # 执行结果
    def __Response(self,opt={}):
        hhRet = {
            "result": [],
            "nums": 0,
            "rows": tuple(),
            "cols": [],
            "sql": "",
            "msg": ""
        }
        hhRet.update(opt)
        # print(hhRet)
        return hhRet

    # 错误处理
    def __Error(self,msg):
        print("hhframe.hhMysql Error - ", msg)