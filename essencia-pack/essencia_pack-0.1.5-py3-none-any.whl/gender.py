__all__ = ['Gender']

from enum import Enum
from typing import Union


class Gender(str):
    '''
    Normaliza o gênero para string, sendo o input do tipo int ou string.
    '''

    class GenderStr(str, Enum):
        MALE = 'Masculino'
        FEMALE = 'Feminino'
        UNDEFINED = 'Indefinido'

    def __new__(cls, value: Union[ int, str ], trans: bool = False):
        _value = cls.GenderStr.UNDEFINED
        if isinstance(value, int):
            if value == 1:
                _value = cls.GenderStr.MALE
            elif value == 2:
                _value = cls.GenderStr.FEMALE
        elif isinstance(value, str):
            if value in [ 'M', 'm', 'Masc', 'masc', 'Masculino', 'masculino' ]:
                _value = cls.GenderStr.MALE
            elif value in [ 'F', 'f', 'Fem', 'fem', 'Feminino', 'feminino' ]:
                _value = cls.GenderStr.FEMALE
        return str.__new__(cls, _value.value)
