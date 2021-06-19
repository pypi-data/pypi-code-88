from enum import Enum
from typing import Union

class Parse(object):
    '''
    Parse instance for strings managing conversion to other types.
    '''

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


    class Date(str):
        '''
        Normaliza ojetos de data em formato brasileiro (dia - mês - ano) para o internacional utilizado para registro
        em bancos de dados.
        '''

        def __new__(cls, value):
            gen = (x for x in [ "/", ".", "-", "_" ])
            try:
                while True:
                    d = None
                    item = next(gen)
                    w = value.split(item)
                    if len(w) == 3:
                        if len(w[ 0 ]) == 4:
                            d = ddate(*[ int(x) for x in w ])
                        elif len(w[ 2 ]) == 4:
                            d = ddate(*[ int(x) for x in reversed(w) ])
                    if d != None:
                        value = jsonable_encoder(d)
                        new = str.__new__(cls, value)
                        return new
            except:
                raise ValueError('uma data válida não foi encontrada')

    class WordsListToPhrase(str):
        '''
        Output a phrase taking a list of strings as input.
        '''

        def __new__(cls, wl: List[str], **kwargs):
            value = ''
            initial = kwargs.get('initial', '')
            final = kwargs.get('final', '')
            size = len(wl)
            if size == 1:
                value = wl[0]
            elif size == 2:
                value = f'{wl[0]} e {wl[1]}'
            elif size >= 3:
                items, last = wl[:-1], wl[-1]
                value = f'{", ".join(items)} e {last}'
            value = (initial + value + final).strip().capitalize()
            if not value.endswith('.'):
                value += '. '
            return str.__new__(cls, value)

    class PhrasesListToParagraph(str):

        def __new__(cls, pl: List[str]):
            value = ''
            size = len(pl)
            while size > 0:
                try:
                    phase = pl.pop(0).capitalize().strip()
                    if not phase.endswith('.'):
                        phase += '. '
                    value += phase
                except:
                    return str.__new__(cls, value)

