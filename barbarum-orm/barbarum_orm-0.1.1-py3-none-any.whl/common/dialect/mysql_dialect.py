from .dialect import Dialect
from enum import Enum, unique
from urllib.parse import quote_plus

@unique
class MysqlDriver(Enum): 
    PYMYSQL = 1, "pymysql"
    MYSQL_CLIENT = 2, "mysqldb"
    MYSQL_CONNECTOR = 3, "mysqlconnector"
    AIOMYSQL = 4, "aiomysql"
    CYMYSQL = 5, "cymysql"
    OUR_SQL = 6, "oursql"
    PYODBC = 7, "pyodbc"
    
    def __new__(cls, *args):
        obj = object.__new__(cls)
        obj._value_ = args[0]
        return obj

    def __init__(self, _, driver_name):
        self.driver_name = driver_name
    
    def get_driver_name(self): 
        return self.driver_name

class MysqlDialect(Dialect): 

    def __init__(self, user:str, password:str, schema:str, host:str, port:int=3306, charset:str="utf8", driver:MysqlDriver=MysqlDriver.PYMYSQL) -> None:
        super().__init__()
        self.host = host
        self.port = port 
        self.user = user
        self.password = password
        self.schema = schema
        self.charset = charset
        self.driver = driver

    def get_url(self) -> str:
        if self.driver == MysqlDriver.PYODBC: 
            connection_string = (
                'DRIVER=MySQL ODBC 8.0 ANSI Driver;'
                f'SERVER={self.host};'
                f'PORT={self.port};'
                f'DATABASE={self.schema};'
                f'UID={self.user};'
                f'PWD={self.password};'
                f'charset={self.charset};'
            )
            return f"{self.get_dialect_name()}+{self.driver.get_driver_name()}:///?odbc_connect={quote_plus(connection_string)}"
        return f"{self.get_dialect_name()}+{self.driver.get_driver_name()}://{self.user}:{self.password}@{self.host}:{self.port}/{self.schema}?charset={self.charset}"
    
    def get_dialect_name(self) -> str:
        return "mysql"