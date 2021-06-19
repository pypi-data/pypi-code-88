import datetime
from abc import ABC
from enum import Enum
import datetime
import unicodedata
import typesystem as ts
import re


definitions = ts.SchemaDefinitions()

class StrEnum(str, Enum):
    def __str__(self):
        return self.value


class Base(ABC):

    def __init__(self, *args, **kwargs):
        super(Base, self).__init__(*args, **kwargs)
        self.request = kwargs.pop('request')
        for k,v in kwargs.items():
            setattr(self, k, v)


    def setup_metadata(self, **kwargs):
        # setting search names and normalizing birthdate
        if hasattr(self, 'fullname'):
            setattr(self, 'search_name', self.fullname.lower())
            if hasattr(self, 'birthdate'):
                if isinstance(self.birthdate, str):
                    self.birthdate = datetime.date.fromisoformat(self.birthdate)
        elif hasattr(self, 'name'):
            setattr(self, 'search_name', self.name.lower())

        if not hasattr(self, 'model'):
            setattr(self, 'model', kwargs.get('model') or self.__class__.__name__)

        if not hasattr(self, 'created'):
            setattr(self, 'created', datetime.datetime.now())

        if kwargs.get('request'):
            request = kwargs.get('request')
            setattr(self, 'owner', request.session['auth_user']['email'])
            if hasattr(request.session['auth_user'], 'provider'):
                setattr(self, 'provider_key', request.session['auth_user']['provider']['key'])
            elif hasattr(request.session[ 'auth_user' ], 'assistant'):
                setattr(self, 'assistant_key', request.session[ 'auth_user' ][ 'assistant' ][ 'key' ])
            elif hasattr(request.session[ 'auth_user' ], 'patient'):
                setattr(self, 'patient_key', request.session[ 'auth_user' ][ 'patient' ][ 'key' ])

        if not hasattr(self, 'code'):
            setattr(self, 'code', self.find_code())
        else:
            if getattr(self, 'code') == '':
                setattr(self, 'code', self.find_code())

    def find_code(self):
        if hasattr(self, 'birthdate') and hasattr(self, 'fullname') and hasattr(self, 'gender'):
            birthdate = self.birthdate if isinstance(self.birthdate, datetime.date) else datetime.date.fromisoformat(self.birthdate)
            code = f'{birthdate.isoformat().replace("-","")}{self.fullname.split()[0][0]}{self.fullname.split()[-1][0]}{"1" if self.gender.startswith("M") else "2"}'
        elif hasattr(self, 'patient_key'):
            if hasattr(self, 'provider_key'):
                if not hasattr(self, 'date'):
                    setattr(self, 'date', datetime.date.today())
                    code = f'{str(self.date).replace("-","")}.{self.patient_key}.{self.model}.{self.provider_key}'
        else:
            code = f'{self.created.isoformat().split("T")[0].replace("-","")}.{self.__class__.__name__}'
        setattr(self, 'code', code)
        return code

### ABSTRACT MODELS

class BaseModel(ts.Schema, Base, definitions=definitions):

    @property
    def url(self):
        model = getattr(self, 'model', None) or self.__class__.__name__
        return f'/{model.lower()}/k/{self.key}'

    @property
    def json(self):
        return {k: str(v) for (k, v) in self.__dict__.items() if
                v != None and not k in [ 'model', 'table', 'owner', 'created' ]}

    def full_json(self, **kwargs):
        self.setup_metadata(**kwargs)
        x = self.__dict__
        x.update(kwargs)
        return {k: str(v) for (k, v) in x.items() if v != None}


class Profile(BaseModel):
    fullname = ts.String()
    class Gender(StrEnum):
        Male = 'Masculino'
        Female = 'Feminino'
    gender = ts.Choice(choices=Gender)
    birthdate = ts.Date()
    cpf = ts.String(allow_blank=True)
    email = ts.String(allow_blank=True)

    def __eq__(self, other):
        return (self.fullname, self.birthdate, self.gender, self.cpf) == (self.fullname, self.birthdate, self.gender, self.cpf)

    def __hash__(self):
        return hash((self.search_name, self.birthdate, self.gender, self.cpf))

    @property
    def age(self):
        bdate = self.birthdate if isinstance(self.birthdate, datetime.date) else datetime.date.fromisoformat(self.birthdate)
        return ((datetime.date.today() - bdate).days / 365).__round__(1)

    @property
    def age_str(self):
        bdate = self.birthdate if isinstance(self.birthdate, datetime.date) else datetime.date.fromisoformat(self.birthdate)
        age = ((datetime.date.today() - bdate).days / 365).__round__(1)
        if age <= 1:
            return ' '.join([str(age), 'ano'])
        return ' '.join([str(age), 'anos'])

