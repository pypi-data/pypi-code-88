#   coding:utf-8
#   This file is part of Alkemiems.
#
#   Alkemiems is free software: you can redistribute it and/or modify
#   it under the terms of the MIT License.

__author__ = 'Guanjie Wang'
__version__ = 1.0
__maintainer__ = 'Guanjie Wang'
__email__ = "gjwang@buaa.edu.cn"
__date__ = '2021/01/14 17:49:43'

import sys
import logging
from matfleet.utilities.constant import LOG_FILE_FMT, LOG_STREA_MFMT


class MatFleetLog(object):
    fdir = '.'
    mode = 'a'
    fn_level = ["INFO", "ERROR"]
    
    def __init__(self, name, stream_level=logging.INFO, file_level=logging.INFO, add_file_log=False, prefix='matfleet'):
        self.name = name
        self.stream_level = stream_level
        self.file_level = file_level
        self.add_file_log = add_file_log
        self._logfilename = prefix + '_' + self.name.replace('.', '_') + '.log'
        
        self._logger = logging.getLogger(name=self.name)
        self._logger.setLevel(stream_level)
    
    @property
    def logger(self):
        return self()
    
    @property
    def handler(self):
        return self._logger.handlers
    
    @property
    def logfilename(self):
        return self._logfilename
    
    @logfilename.setter
    def logfilename(self, filename):
        self._logfilename = filename
    
    def __filehalder(self, mode):
        filehandler = logging.FileHandler(self.logfilename, mode=mode)
        filehandler.setFormatter(logging.Formatter(LOG_FILE_FMT))
        filehandler.setLevel(self.file_level)
        self._logger.addHandler(filehandler)
    
    def __streadmhanlder(self):
        self.streamhandler = logging.StreamHandler(sys.stdout)
        self.streamhandler.setFormatter(logging.Formatter(LOG_STREA_MFMT))
        self.streamhandler.setLevel(self.stream_level)
        self._logger.addHandler(self.streamhandler)
    
    def run_handler(self, mode='a'):
        if self.add_file_log:
            if not self._logger.handlers:
                self.__filehalder(mode)
                self.__streadmhanlder()
            else:
                if mode != 'a':
                    self._logger.removeHandler(self._logger.handlers[0])
                    self.__filehalder(mode)
        else:
            if not self._logger.handlers:
                self.__streadmhanlder()
    
    def __call__(self, *args, **kwargs):
        # self.get_handler(*args, **kwargs)
        self.run_handler(*args, **kwargs)
        return self._logger
