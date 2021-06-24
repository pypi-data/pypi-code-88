""" Модуль описания Логов.

"""

from __future__ import annotations

import inspect
import os
import threading
import time
import typing as _T


class Record(object):
    """ Объект сообщения. Поля этого класса будут доступны ... """

    loggerName: str
    loggingLevel: int
    message: str

    loggingLevelLabel: str
    loggingLevelLabelCenter: str

    time: str
    timestamp: float
    pidId: int
    threadId: int

    fromModule: str
    fromFile: str
    fromFileLine: str
    fromObject: str
    callArgs: dict[str, _T.Any]

    def __init__(self, loggerName: str, loggingLevel: int, message: str, **kwargs):
        """ Получение данных о состянии приложения на момент вызова лога """

        self.loggerName = loggerName
        self.loggingLevel = loggingLevel
        self.message = message

        self.timestamp = time.time()
        self.pidId = os.getpid()
        self.threadId = threading.get_ident()

        self.__get_info_call_function()

        for attrName, attrValue in kwargs.items():
            setattr(self, attrName, attrValue)

    def __get_info_call_function(self):
        """ Получение информации о функции вызвавшей лог """

        stack = inspect.stack()[4]
        module = inspect.getmodule(stack.frame)

        self.fromModule = module.__name__
        self.fromFile = stack.filename
        self.fromFileLine = stack.lineno

        self.fromObject = stack.function

        # Если у функции есть атрибут self / cls значит она метод класса.
        if 'self' in stack.frame.f_locals:
            self.fromObject = '{0}.{1}'.format(
                stack.frame.f_locals.get('self').__class__.__name__,
                stack.function
            )

        elif 'cls' in stack.frame.f_locals:
            self.fromObject = '{0}.{1}'.format(
                stack.frame.f_locals.get('cls').__name__,
                stack.function
            )


class StopSystemRecord(Record):
    """ Объект, сигнализирующий о необходимости остановить систему логирования """

    def __init__(self):
        super().__init__('system', 100, 'stop system record')
