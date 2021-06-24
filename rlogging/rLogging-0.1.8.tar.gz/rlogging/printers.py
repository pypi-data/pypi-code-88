""" Модуль описания различных принтеров

"""

from __future__ import annotations

import os
import pathlib as pa
from queue import Queue
import re
import sys
import typing as _T

from rlogging import formaters
from rlogging.records import Record, StopSystemRecord


class BasePrinter(object):
    """ Основной класс Принтер.

    Принтер - функционал, который обрабатывает, выводит или сохраняет Log.

    """

    _started: bool = False

    def start(self):
        """ Запуск Принтера """

        self._started = True

    def stop(self):
        """ Остановка Принтера """

        self._started = False

    def print(self, record: Record):
        """ Принт лога

        Args:
            record (Record): Некий лог

        Raises:
            AttributeError: Дочерний класс не переназначил данный метод

        """

        raise AttributeError('Принтер "{0}" не переназначил функцию принта'.format(
            self.__class__.__name__
        ))


class TerminalPrinter(BasePrinter):
    """ Принтер, выводящий сообщения в консоль

    Args:
        colors (dict[str, str]): Цвет сообщения соответствующий уровня лога.

    """

    formater: formaters.BaseFormater

    colors: dict = {
        'rubbish': '0m',
        'debug': '37m',
        'info': '32m',
        'warning': '33m',
        'error': '31m',
        'critical': '31m',
    }

    def __init__(self, formater: formaters.BaseFormater) -> None:
        self.formater = formater

    def print(self, record: Record):
        text = self.formater.formate(record)

        # Добавление цвета
        text = '\033[' + self.colors[record.loggingLevelLabel] + text + '\033[0m'

        print(text)


class MonitoringFileMixin(object):
    """ Миксин с функциями для мониторинга записи размера файла """

    filePath: pa.Path
    maxFileSize: int
    checkSizeEveryThisRepeat: int

    _writeInFileScore: int

    def __check_file(self):
        if not self.filePath.parent.is_dir():
            self.filePath.parent.mkdir(parents=True)

        if not self.filePath.is_file():
            with open(self.filePath, 'w') as f:
                pass

    def __init_file_name(self):
        """ Инициализация файла, в который будет писаться логи """

        self.filePath = pa.Path(self.filePath).resolve()
        self.__check_file()

    def __new_file_name(self, init: bool = False):
        """ Генерация нового имени файла логирования """

        fileNameNoExtension, fileExtension = os.path.splitext(self.filePath)
        path, fileName = os.path.split(fileNameNoExtension)

        fileNameMath = re.search(r'([\s\S]*)\.(\d*)$', fileName)
        if fileNameMath is not None:
            fileName = fileNameMath.group(1)
            count = int(fileNameMath.group(2)) + 1
            fileName = '{0}.{1}'.format(
                fileName, count
            )

        else:
            fileName = '{0}.1'.format(
                fileName
            )

        fileName = '{0}/{1}{2}'.format(
            path, fileName, fileExtension
        )

        self.filePath = pa.Path(fileName)
        self.__check_file()

    def file_size_check(self):
        """ Проверка файла на соответствие заданому максимальному значению """

        if not self._writeInFileScore:
            self.__init_file_name()

        try:
            size = os.path.getsize(self.filePath)

        except FileNotFoundError:
            size = 0

        if size > self.maxFileSize:
            self.__new_file_name()

    def file_size_count(self):
        if self._writeInFileScore % self.checkSizeEveryThisRepeat == 0:
            self.file_size_check()


class PrintInFileMixin(object):
    """ Класс, запускаемый в отдельном процессе, для записи чего-либо в файл """

    filePath: pa.Path
    messageQueue: Queue

    writeChunk: int

    _writeInFileScore: int

    def clear_queue(self):
        with open(self.filePath, 'a') as fileIO:
            while not self.messageQueue.empty():
                fileIO.write(self.messageQueue.get())

    def file_print(self, string: str):
        """ Запись строки в файл с шагом в 50 записей

        Args:
            string (str): Строка для записи

        """

        if self._writeInFileScore % self.writeChunk == 0:
            self.clear_queue()

        self.messageQueue.put(string)


class FilePrinter(BasePrinter, PrintInFileMixin, MonitoringFileMixin):
    """ Принтер, выводящий сообщения в консоль """

    formater: formaters.BaseFormater

    def __init__(self,
                 formater: formaters.BaseFormater,
                 filePath: os.PathLike,
                 writeChunk: int = 50,
                 maxFileSize: int = 83886080,
                 checkSizeEveryThisRepeat: int = 500
                 ) -> None:
        """ Инициализация объекта

        Args:
            formater (formaters.BaseFormater): Форматер выходных данных.
            filePath (os.PathLike): Путь до файла.
            writeChunk (int): По сколько сообщений за раз писать в файл.
            maxFileSize (int): Максимальное вес файла в битах. Default 10MB.
            checkSizeEveryThisRepeat (int): После скольких записей проверять файла на соответствие допустимому весу. Defaults to 500.

        """

        self.formater = formater
        self.filePath = pa.Path(filePath)
        self.writeChunk = writeChunk
        self.maxFileSize = maxFileSize
        self.checkSizeEveryThisRepeat = checkSizeEveryThisRepeat

        self._writeInFileScore = -1

        self.messageQueue = Queue(self.writeChunk)

    def print(self, record: Record):

        if isinstance(record, StopSystemRecord):
            self.stop()

        self._writeInFileScore += 1

        self.file_size_count()

        text = '{0}\n'.format(
            self.formater.formate(record)
        )

        self.file_print(text)

    def stop(self):
        self.clear_queue()


class PrintersPool(object):
    """ Класс для создания пула Принтеров """

    printers: list[BasePrinter]

    def __init__(self, printers: list[BasePrinter]) -> None:
        self.printers = printers

    def print(self, record: Record):
        """ Передача лога в Принтеры пула

        Args:
            record (Record): Некий лог

        """

        for printer in self.printers:
            printer.print(record)
