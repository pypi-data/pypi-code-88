""" Модуль описания различных хендлеров


"""

from __future__ import annotations

import typing as _T
from copy import deepcopy

from rlogging import printers, utils
from rlogging.records import Record, StopSystemRecord


class BaseHandler(object):
    """ Основной класс Хендлер

    Хендлер - функционал, который ловит лог, вызванный программой, и передает его в принтер.

    """

    _started: bool

    printersPool: _T.Optional[printers.PrintersPool]

    def __init__(self):
        self._started = False
        self.printersPool = None

    def start(self):
        """ Запуск Хендлера """

        self._started = True

    def stop(self):
        """ Остановка Хендлера """

        self._started = False

    def send(self, record: Record):
        """ Отправка сообщения в хендлер

        Args:
            record (Record): Некий лог

        Raises:
            AttributeError: Дочерний класс не переназначил данный метод

        """

        raise AttributeError('Хендлер "{0}" не переназначил функцию отправки сообщения'.format(
            self.__class__.__name__
        ))


class MainProcessHandler(BaseHandler):
    """ Хендлер, работающий в основном потоке.

    При создании лога, он в синхронном порядке пройдет все стадии (logger->handler->printer) и программа продолжит выполнение

    """

    def send(self, record: Record):
        self.printersPool.print(record)


class SubProcessHandler(utils.SubProcessMixing, BaseHandler):
    """ Хендлер, работающий в отдельном потоке.

    При инициализации хендлера, создается отдельный процесс.
    При создании лога, он в отправляется в хендлер (в дочерни процесс) и программа продолжит выполнение.
    После остановки логера новый процесс завершится.

    """

    def on_process(self):
        """ Функция вызываемая в другом процессе.

        Проверяет очередь на наличие логов и передает в Пул Принтеров

        """

        while True:
            record = self._queue.get()

            if record is None:
                break

            self.printersPool.print(deepcopy(record))

    def send(self, record: Record):
        self._queue.put(record)

        if isinstance(record, StopSystemRecord):
            self.stop()


class HandlersPool(object):
    """ Класс для создания пула хендлера """

    handlers: list[BaseHandler]

    def __init__(self, handlers: list[BaseHandler]) -> None:
        self.handlers = handlers

    def send(self, record: Record):
        """ Отправка сообщения в Хендлеры пула

        Args:
            record (Record): Некий лог

        """

        for handler in self.handlers:

            if not handler._started:
                print('WARNING | Лог X не может быть обработан, так как логгер остановлен')
                print('WARNING | Лог X: loggingLevel: "{0}"; message: "{1}"'.format(
                    record.loggingLevel,
                    record.message
                ))

            handler.send(record)
