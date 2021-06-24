from sqlalchemy.orm import  sessionmaker
from sqlalchemy import create_engine,MetaData, engine
from sqlalchemy import  Column, Integer, String,DateTime
from sqlalchemy.ext.declarative import declarative_base
class Column(Column):
    pass

class Integer(Integer):
    pass

class String(String):
    pass

class DateTime(DateTime):
    pass

class FiresqlBase():
    def begin(self):
        return declarative_base()


class dotdict(dict):
    """dot.notation access to dictionary attributes"""

    __getattr__ = dict.get
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__


class NewSesion(sessionmaker):

    def add(self,instance):
        super.begin_nested()
        super.add(instance)

    def commit(self):
        super.commit()

    def close(self):
        super.close()

    def delete(self,instance):
        super.delete(instance)

    def rollback(self):
        super.rollback()


class Firesql(object):
    conn:engine
    

    def connect_sql(self,host_name:str, user_name:str, user_password:str,db_name:str,port=3306):
        try:
            self.conn = create_engine(f"mysql+pymysql://{user_name}:{user_password}@{host_name}:{port}/{db_name}")
            self.metadata = MetaData(self.conn) 
            print("Connection to MySQL DB successful")
        except Exception as e:
            print(f"The error '{e}' occurred")

    def create_all(self,base):
        base.metadata.create_all(self.conn)
        
    def drop_all(self,base):
        base.metadata.drop_all(self.conn)
        
    def session(self):
        Sess = NewSesion(bind=self.conn)
        session:NewSesion = Sess()
        return session
    
    
    
