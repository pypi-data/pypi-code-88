__all__ = ['Licence']

from typing import Union
from enum import Enum

class LicenceDescriptor(object):
    '''
    Licence Descriptor object.
    '''

    class Entity(object):

        def __set__(self, instance, value: str):
            instance._entity = value.upper()

        def __get__(self, instance, owner):
            return instance._entity


    class Code(object):

        def __set__(self, instance, value: Union[str, int]):
            instance._code = str(value)

        def __get__(self, instance, owner):
            return instance._code


    class Region(object):

        class BrazilianRegion(str, Enum):
            AC = 'Acre'
            AL = 'Alagoas'
            AP = 'Amapá'
            AM = 'Amazonas'
            BA = 'Bahia'
            CE = 'Ceará'
            DF = 'Distrito Federal'
            ES = 'Espírito Santo'
            GO = "Goiás"
            MA = 'Maranhão'
            MT = 'Mato Grosso'
            MS = 'Mato Grosso do Sul'
            MG = 'Minas Gerais'
            PA = 'Pará'
            PB = 'Paraíba'
            PR = 'Paraná'
            PE = 'Pernambuco'
            PI = 'Piauí'
            RJ = 'Rio de Janeiro'
            RN = 'Rio Grande do Norte'
            RS = 'Rio Grande do Sul'
            RO = 'Rondônia'
            RR = 'Roraima'
            SC = 'Santa Catarina'
            SP = 'São Paulo'
            SE = 'Sergipe'
            TO = 'Tocantins'

        def __set__(self, instance, value: str):
            members = self.BrazilianRegion.__members__.keys()
            region = value.upper()
            if region in members:
                instance._region = region
            else:
                raise ValueError(f'A região {region} não foi reconhecida. as opções são: {", ".join(members)}.')

        def __get__(self, instance, owner):
            return instance._region




class Licence(object):
    entity: str = LicenceDescriptor.Entity()
    code: str = LicenceDescriptor.Code()
    region: str = LicenceDescriptor.Region()

    def __init__(self, entity, code, region):
        self.entity = entity
        self.code = code
        self.region = region


    def __str__(self):
        return f'{self.entity}-{self.region} {self.code}'

