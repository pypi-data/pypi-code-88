from sqlalchemy.orm import sessionmaker, scoped_session
from sro_db.config.config import engine
from contextlib import contextmanager

class BaseService():
    
    def __init__(self, object):
        self.object = object
        self.type = self.object.__tablename__
        # print(dir(self))
        self.create_session_connection()

    def close_session_connection(self):
        self.session.close()
    
    #Gerewnciando a são dos objetos
    @contextmanager
    def create_session_connection(self):
        
        Session = scoped_session(sessionmaker(bind=engine, autocommit=False, autoflush=False, expire_on_commit=False))
        self.session = Session()
        self.session.begin(subtransactions=True)
        try:
            yield self.session
            self.session.commit()
        except:
            self.session.rollback()
            raise
        finally:
            self.session.expunge_all()
            self.session.close()

    def find_all(self):
        with self.create_session_connection() as session:   
            results = session.query(self.object).order_by(self.object.id).all()
            return results

    def get_all(self):
        with self.create_session_connection() as session:   
            return session.query(self.object).order_by(self.object.id).all()
    
    def get_by_uuid(self, uuid):
        with self.create_session_connection() as session:   
            return session.query(self.object).filter(self.object.uuid == uuid).first()


    def create_bulk(self, list_object):
        try:   
            with self.create_session_connection() as session:        
                session.add_all(list_object)
                session.commit()
            return list_object
        except:
            #self.session.rollback() 
            raise
      
		
    def create(self, object):        
        try:            
            with self.create_session_connection() as session:     
            
                local_object = self.session.merge(object)
                session.add(local_object)
                session.commit()            
            
            return local_object
        except:
            #self.session.rollback() 
            raise
        

    def update(self, object):
        
        try:
            print("--- update test ---")
            with self.create_session_connection() as session:
                session.query(self.object).filter(self.object.id == object.id).update({column: getattr(object, column) for column in self.object.__table__.columns.keys()})
                session.commit()
            return object
        except:
            print("--- except ---")
            self.session.rollback() 
            raise

    def delete(self, object):
        
        try:
            local_object = self.session.merge(object)            
            self.session.delete(local_object)
            self.session.commit()
        except:
            self.session.rollback() 
            raise
