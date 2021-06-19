""" Модуль описания различных Логеров.

"""

from __future__ import annotations

import queue as _Q
import typing as _T

from rlogging import handlers
from rlogging.records import Record, StopSystemRecord


class BaseLogger(object):
    """ Основной класс Логер.

    Логер - Интерфейс для приема логов и передачи их в хендлер

    """

    name: str
    minLogLevel: int

    _started: bool

    handlersPool: _T.Optional[handlers.HandlersPool]

    queue: _Q.Queue
    _maxQueueLen: int = 500

    def __init__(self, loggerName: str) -> None:
        self.name = loggerName

        self.minLogLevel = 1
        self._started = False
        self.handlersPool = None

        self.queue = _Q.Queue(self._maxQueueLen)

    def clear_queue(self):
        """ Очитка очереди логгера """

        while not self.queue.empty():
            record = self.queue.get_nowait()

            if self.minLogLevel > record.loggingLevel:
                continue

            self.send_record(record)
            self.queue.task_done()

    def __save_record(self, record: Record):
        """ Сохранение лога в локальной очереди

        Args:
            record (Record): Некий лог

        """

        try:
            self.queue.put_nowait(record)

        except _Q.Full:
            firstItemInQueue = self.queue.get_nowait()

            print('Очередь логгера {0} переполнена. Лог "{1}" удален чтобы вставить лог "{2}".'.format(
                self.name,
                firstItemInQueue,
                record
            ))

    def send_record(self, record: Record):
        """ Отправка лога в пул Хендлеров

        Args:
            record (Record): Некий лог

        """

        if not self._started:
            self.__save_record(record)
            return

        elif isinstance(record, StopSystemRecord):
            self.stop()

        self.handlersPool.send(record)

    def send(self, loggingLevel: int, message: str, **kwargs):
        """ Логирование сообщения message c важность лога loggingLevel и доп параметрами args, kwargs """

        if self.minLogLevel > loggingLevel:
            return

        record = Record(self.name, loggingLevel, message, **kwargs)
        self.send_record(record)

    def start(self):
        """ Запуск Логера """

        self._started = True
        self.clear_queue()

    def stop(self):
        """ Остановка логгера """

        self._started = False
        self.queue.join()

    def __del__(self):
        self.send_record(StopSystemRecord())


class Logger(BaseLogger):
    """ Обычный логер с 5 общепринятыми уровнями логов и 2 дополнительными """

    def debug(self, message: str, **kwargs):
        """ Создать лог уровня debug """

        self.send(1, message, **kwargs)

    def info(self, message: str, **kwargs):
        """ Создать лог уровня info """

        self.send(21, message, **kwargs)

    def warning(self, message: str, **kwargs):
        """ Создать лог уровня warning """

        self.send(41, message, **kwargs)

    def error(self, message: str, **kwargs):
        """ Создать лог уровня error """

        self.send(61, message, **kwargs)

    def critical(self, message: str, **kwargs):
        """ Создать лог уровня critical """

        self.send(81, message, **kwargs)

    def log(self, loggingLevel, message: str, **kwargs):
        """ Создать лог уровня loggingLevel """

        self.send(loggingLevel, message, **kwargs)

    def exception(self, exception: Exception):
        message = '{0} : {1}'.format(
            exception.__class__.__name__,
            exception
        )
        self.critical(message)
