__all__ = ['Day', 'Month', 'Date']

from enum import Enum
from pydantic import BaseModel, validator, Field
from typing import Union

class Day(int, Enum):
    '''
    values: 1 to 31 (int)
    '''
    Dia01 = 1
    Dia02 = 2
    Dia03 = 3
    Dia04 = 4
    Dia05 = 5
    Dia06 = 6
    Dia07 = 7
    Dia08 = 8
    Dia09 = 9
    Dia10 = 10
    Dia11 = 11
    Dia12 = 12
    Dia13 = 13
    Dia14 = 14
    Dia15 = 15
    Dia16 = 16
    Dia17 = 17
    Dia18 = 18
    Dia19 = 19
    Dia20 = 20
    Dia21 = 21
    Dia22 = 22
    Dia23 = 23
    Dia24 = 24
    Dia25 = 25
    Dia26 = 26
    Dia27 = 27
    Dia28 = 28
    Dia29 = 29
    Dia30 = 30
    Dia31 = 31


class Month(object):

    class Integer(int, Enum):
        '''
        values: 1 to 12 (int)
        '''
        JAN = 1
        FEB = 2
        MAR = 3
        APR = 4
        MAY = 5
        JUN = 6
        JUL = 7
        AUG = 8
        SEP = 9
        OCT = 10
        NOV = 11
        DEZ = 12

    class String(str, Enum):
        JAN = 'Janeiro'
        FEV = 'Fevereiro'
        MAR = 'Março'
        APR = 'Abril'
        MAY = 'Maio'
        JUN = 'Junho'
        JUL = 'Julho'
        AUG = 'Agosto'
        SEP = 'Setembro'
        OCT = 'Outubro'
        NOV = 'Novembro'
        DEC = 'Dezembro'

    @classmethod
    def flip(cls, v) -> str:
        if isinstance(v, int):
            if v == 1: return cls.String.JAN.value
            elif v == 2: return cls.String.FEV.value
            elif v == 3: return cls.String.MAR.value
            elif v == 4: return cls.String.APR.value
            elif v == 5: return cls.String.MAY.value
            elif v == 6: return cls.String.JUN.value
            elif v == 7: return cls.String.JUL.value
            elif v == 8: return cls.String.AUG.value
            elif v == 9: return cls.String.SEP.value
            elif v == 10: return cls.String.OCT.value
            elif v == 11: return cls.String.NOV.value
            elif v == 12: return cls.String.DEC.value




class Date(BaseModel):
    day: int = Field(...)
    month: str = Field(...)


if __name__ == '__main__':
    date = Date(day=1, month='Janeiro')
    print(date)