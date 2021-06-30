from abc import ABC, abstractmethod
from sqlalchemy import select
from sqlalchemy.sql.expression import delete
from sqlalchemy.orm.attributes import InstrumentedAttribute
from sqlalchemy.sql.functions import func

from .database import Database, Base

class Repository(ABC): 
    """
    Generic repository interface.
    """

    def __init__(self, database:Database) -> None:
        if type(database) != Database: 
            raise ValueError(f"Invalid database type, expected {Database} but {type(database)}")
        self._database = database

    @abstractmethod
    def get_domain(self) -> Base:
        raise NotImplementedError(f"Domain is not specified for {self.__class__}")

    def get_database(self): 
        return self._database

    def find_all(self): 
        with self.get_database().open() as session: 
            statement = select(self.get_domain())
            result = session.execute(statement)
            return result.all()

    def find_by_id(self, id): 
        if(type(id) != int):
            raise ValueError("Invalid type, expected int, but %s" % (type(id)))
        with self.get_database().open() as session: 
            return session.get(self.get_domain(), id)

    def count(self): 
        with self.get_database().open() as session:
            return session.execute(func.count(self.get_domain().id)).fetchone()[0]

    def insert(self, instance): 
        if type(instance) != self.get_domain():
            message = "Invalid class type, expected %s, but %s" % (self.get_domain(), type(instance))
            raise ValueError(message)
        with self.get_database().open() as session: 
            session.add(instance)
        return instance
    
    def update(self, instance): 
        if type(instance) != self.get_domain():
            message = "Invalid class type, expected %s, but %s" % (self.get_domain(), type(instance))
            raise ValueError(message)
        fields = Repository._get_domain_dict(self.get_domain(), instance)
        with self.get_database().open() as session: 
            toUpdate = session.execute(select(self.get_domain()).filter_by(id=fields["id"])).scalar_one()
            for key, value in fields.items(): 
                if key == "id": 
                    continue
                toUpdate.__setattr__(key, value)
            return toUpdate

    def delete_all(self): 
        with self.get_database().open() as session: 
            count = self.count()
            session.execute(delete(self.get_domain()))
            return count
    
    def delete_by_id(self, id):
        with self.get_database().open() as session: 
            instance = session.get(self.get_domain(), id)
            if not instance: 
                return 0
            session.delete(instance)
            return 1
    
    def _find_by_field(self, name:str, value): 
        with self.get_database().open() as session: 
            return session.execute(select(self.get_domain()).filter_by(**{name: value})).all()
    
    def _count_by_field(self, name:str, value): 
        with self.get_database().open() as session: 
            result = session.execute(select(func.count(self.get_domain().id)).filter_by(**{name: value})).fetchone()
            return result[0] if result is not None else 0 

    @staticmethod
    def _get_domain_dict(clazz, object):
        fields = set()
        for key, value in clazz.__dict__.items(): 
            if(type(value) != InstrumentedAttribute): 
                continue
            fields.add(key)
        result = dict()
        for key, value in object.__dict__.items(): 
            if key not in fields:
                continue
            result[key] = value
        return result