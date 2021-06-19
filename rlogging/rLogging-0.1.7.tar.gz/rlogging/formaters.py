""" Модуль описания различных Форматеров

"""

from __future__ import annotations

import json
import re
import types
import typing as _T
from datetime import datetime

from rlogging.records import Record
import rlogging

class BaseFormater(object):
    """ Основной класс Хендлер

    Форматер - обработчик, через который проходит лог, и получается текст для сохранения.

    """

    def formate(self) -> str:
        """ Создание строки из данных лога

        Raises:
            AttributeError: Дочерний класс не переназначил данный метод

        """

        raise AttributeError('Форматер "{0}" не переназначил функцию форматирования'.format(
            self.__class__.__name__
        ))

    def start_clean_functions(self, record: Record):
        """ Вызов функций начинающихся с `add_` и `clean_`

        Args:
            record (Record): Некий лог

        """

        methodsNames = dir(self)

        addingMethods = []
        cleaningMethods = []

        for methodName in methodsNames:
            method = getattr(self, methodName)

            if isinstance(method, types.MethodType):
                if method.__name__.startswith('add_'):
                    addingMethods.append(method)

                elif method.__name__.startswith('clean_'):
                    cleaningMethods.append(method)

        for method in addingMethods:
            method(record)

        for method in cleaningMethods:
            method(record)


class ProcessingFormaterMixin(BaseFormater):
    """ Миксин для обработки некоторых данных в логе """

    timeFormat: str = '%H:%M:%S.%f'

    def add_time(self, record: Record):
        """ Перевод timestamp в привычное время

        Args:
            record (Record): Некий лог

        """

        time_on_datetime = datetime.fromtimestamp(record.timestamp)
        record.time = time_on_datetime.strftime(self.timeFormat)

    def add_logging_level_label(self, record: Record):
        """ Добавление лейбла уровня лога

        Args:
            record (Record): Некий лог

        """

        for maxSroreForLevel, loggingLevelLabel in rlogging.LOGGING_LEVELS.items():
            if maxSroreForLevel >= record.loggingLevel:
                record.loggingLevelLabel = loggingLevelLabel
                record.loggingLevelLabelCenter = loggingLevelLabel.center(8)
                break


class LineFormater(ProcessingFormaterMixin):
    """ Форматер для формирования строки по шаблону с использованием данных лога """

    layout: str = '%(time)s - %(pidId)s:%(threadId)s - %(loggingLevelLabelCenter)s - %(loggerName)s - %(fromModule)s:%(fromFileLine)s %(fromObject)s - %(message)s'

    def formate(self, record: Record) -> str:
        self.start_clean_functions(record)

        record.message = re.sub(r'[\s]+', ' ', record.message)

        return self.layout % record.__dict__


class StructureFormater(ProcessingFormaterMixin):
    """ Форматер для формирования строки вида json дампа с перечнем ключей из данных лога """

    allowKeys: list[str]

    def formate(self, record: Record) -> str:
        self.start_clean_functions(record)

        dataDict = {}

        for key in self.allowKeys:
            value = getattr(record, key)
            dataDict[key] = value

        return json.dumps(dataDict)
