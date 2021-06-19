from dataclasses import dataclass
from abc import ABC, abstractmethod
from typing import List, Optional, Union
from datetime import date, datetime
import json

n2 = lambda x: f'0{x}' if x >= 9 else str(x)

class Created(object):
    def __set__(self, instance, value):
        if not value:
            instance._created = datetime.now()

    def __get__(self, instance, owner):
        date = instance._created
        return f'{date.year}-{n2(date.monthy)}-{n2(date.day)} '

class DatabaseObject(ABC):
    key: Optional[str] = None
    created: Optional[str] = None


@dataclass
class BasePerson(DatabaseObject):
    '''
    Base person with "fullname", "gender", "birthdate"
    '''
    fullname: str
    gender: str
    birthdate: str

    @property
    def age(self):
        today = date.today()
        birth = date(*[int(x) for x in self.birthdate.split('-')])
        return ((today - birth).days / 365).__round__(1)

    @property
    def code(self):
        names = self.fullname.split()
        initials = names[0][0] + names[-1][0]
        code = (self.birthdate.replace('-', '') + initials).upper()
        return code


@dataclass
class BaseProfessional(BasePerson):
    '''
    Base professional with "profession", "licence", "specialties"
    '''
    profession: str
    licence: str
    specialties: Union[List[str], str, None] = None


@dataclass
class Patient(BasePerson):
    pass

@dataclass
class Professional(BaseProfessional):
    pass

if __name__ == '__main__':
    new = Professional(fullname='Daniel Arantes', gender='Masculino', birthdate='1978-09-07', licence='9553GO', profession='Medicina')
    print(new)
    print(issubclass(new.__class__, BasePerson))
    print(new.__class__.mro())
    print(new.age)
    print(new.code)