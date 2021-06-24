import logging
from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.orm import backref, relationship
from src.sql.settings import create_session
from src.sql.base import Base

log = logging.getLogger(__name__)


class Variable(Base):

    __tablename__ = 'variables'

    id = Column(Integer, primary_key=True)
    _key = Column(String(256), unique=True)
    value = Column(String)
    is_encrypted = Column(Boolean, unique=False, default=False)

    def __str__(self):
        return "%d, %s" % (self.id, self._key)

    def __repr__(self):
        return f'Id: {self.id}, Key: {self._key},' \
               f' Value: {self.value}, Is_encrypted: {self.is_encrypted}'

    @classmethod
    #@provide_session
    def select_all(cls, session=None):
        result = session.query(Variable).all()
        session.close()
        return result

    @classmethod
    def get_by_key(cls, key):
        session = create_session()
        item = session.query(Variable).filter(Variable._key == key).one()
        session.close()
        return item

    @classmethod
    #@provide_session
    def create(cls, key, value, is_encrypted): #, session=None):
        session = create_session()
        session.add(Variable(_key=key, value=value, is_encrypted=is_encrypted))
        #session.flush()
        session.commit()
        print("Add")

    def update(self):
        pass

    @classmethod
    #@provide_session
    def delete(cls, key): #, session=None):
        #to_delete = session.query(Variable).get(1)
        #session.delete(to_delete)
        #session.commit()
        session = create_session()
        session.query(cls).filter(cls._key == key).delete()
        session.commit()

    def serialize(self):
        return {
            'key': self._key,
            'value': self.value,
            'is_encrypted': self.is_encrypted,
        }


class Task(Base):

    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True)
    state = Column(String(20))
    _try_number = Column('Try_number', Integer, default=0)
    pool = Column(String(50), nullable=False)
    pool_slot = Column(Integer, default=1)
    job_id = Column(Integer, )

    #def __init__(self):


class Job(Base):

    __tablename__ = "jobs"
    id = Column(Integer, primary_key=True)
    state = Column(String(20))
    start_date = Column(DateTime)
    end_date = Column(DateTime)

    # Relatioship
    tasks_instances = relationship(
        Task,
        primaryjoin=id == Task.job_id,
        foreign_keys=id,
        backref=backref('queued_by_job', uselist=False),
    )



"""

if __name__ == "__main__":

    
    addresses = Union[str, Iterable[str]]
    print(type(addresses).__name__)

    test = say_hello.__code__.co_varnames
    print(test)

    # Test json
    x = {
        "name": "John",
        "age": 30,
        "city": "New York"
    }
    y = json.dumps(x, indent=2)
    print(y)


    print("Class: {}, Name: {}".format(Variable.__class__, Variable.__name__))

    db_url = config.get('database', "db_url")
    if not db_url:
        log.error("Database url not provided")
    else:
        print("DB_URL {}".format(db_url))
        # entry point
        engine = create_engine(db_url)

        # create all objects
        Base.metadata.create_all(engine)

        # create session to handle db objects
        Session = sessionmaker(bind=engine)
        session = Session()

        # add
        #session.add(variable)
        #session.commit()

        # update
        session.query(Variable).filter(Variable.id == 1).update({Variable.value: 'value2'}, synchronize_session=False)

        # select all
        result = session.query(Variable).all()
        if result is not None:
            for row in result:
                print("Id: {}, Key: {}, Value: {}".format(row.id, row._key, row.value))
        else:
            print("No record")

        # delete


        print(f"Count = {session.query(Variable).count()}")

        # get
        res = session.query(Variable).filter_by(id=1).first()

        # remove all objects from session
        session.expunge_all() 
"""