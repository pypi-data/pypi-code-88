'''Module to define the class of MB-60 Dassym's electronic board representation.

:author: F. Voillat
:date: 2021-02-24 Creation
'''
from .base import DBoard
from dboard.base import DBoardPreferedDapiMode

class Board60(DBoard):
    '''Class for MB-60 Dassym's board.'''
    
    number = '60'
    '''Board type number (str)'''

    def __init__(self, dapi, dmode=DBoardPreferedDapiMode.REGISTER):
        '''Constructor'''
        super().__init__(dapi, dmode)
        self.speed_range.set(0,40000)         