from __future__ import annotations

import functools
import sys
import typing as _T
from copy import copy

import rcore
import rlogging
from rcore import exception as ex

logger = rlogging.get_logger('mainLogger')


def print_python_traceback():
    """ Вывести в консоль python исключение """

    if rcore.main.__debug_mod__:
        ex.traceback.print_traceback()
        print()


def exceptions(stopCallback: _T.Union[_T.Callable, None] = None):
    """ Декоратор для обработки исключений.

    В конце выполнения декоратор вызовет функцию остановки приложения.

    Args:
        stopCallback (_T.Callable, optional): Функция для корректной остановки приложения.

    """

    def wrapper(func):

        @functools.wraps(func)
        def inner(*args, **kwargs):
            try:
                return func(*args, **kwargs)

            except rEx as ex:
                print_python_traceback()
                ex.print()

            except BaseException as ex:
                logger.exception(ex)
                print_python_traceback()

            else:
                logger.info('Программа завершилась')
                stopCallback()
                sys.exit(0)

            finally:
                logger.warning('Программа завершилась из-за исключения')
                stopCallback()
                sys.exit(1)

        return inner
    return wrapper


class rEx(BaseException):
    """ Extended Exception Class

    Values:
        description (str): exception description

    """

    description: _T.Union[str, None] = None

    traceback: _T.Union[ex.traceback.BaseTracebackStage, None] = None

    def __str__(self):
        if self.description is None:
            return 'Extended Exception Class'
        return self.description

    def __init__(self, description: _T.Union[str, None] = None):
        if description is not None:
            self.description = description

    def append_traceback(self, tb: ex.traceback.BaseTracebackStage):
        logger.info('Добавление к исключению "{0}" стадию пользовательского трейсбека "{1}"'.format(
            self.__class__.__name__,
            tb.__class__.__name__
        ))

        child = copy(self.traceback)
        self.traceback = tb
        if child:
            self.traceback.add_child(child)
        return self

    def print(self):
        """ Вывод исключения в консоль """

        logger.exception(self)

        print(type(self).__name__ + ': ', sep='', end='')
        if self.description:
            print(self.description, end='')

        print()
