""" Модуль работы с исключениями

Является проводником для исключений из rcore

"""

import typing as _T
from dataclasses import dataclass

from rcore import exception as ex
from rcore.exception import rEx, rException, rExError, rExInfo
from rcore.exception.traceback import BaseTracebackStage


class RocshelfNotInitError(ex.rExError):
    description = 'Rocshelf not init'


class ShelfNotFoundError(ex.rExError):
    """ Вызываемый shelf элемент не найден

    Args:
        type (str): Type shelf
        name (str): Name shelf
        path (str, optional): Path to root shelf

    """

    def __init__(self, shelfType: str, shelfName: _T.Optional[str], path: _T.Optional[str] = None):
        
        if path:
            self.description = 'An shelf "{0}" named "{1}" was not found at address "{2}". "html.html" file needed.'.format(
                shelfType, shelfName, path
            )

        elif shelfName:
            self.description = 'An shelf "{0}" named "{1}" was not init in config files.'.format(
                shelfType, shelfName
            )

        else:
            self.description = 'Несуществующий тип шелфа - "{0}"'.format(
                shelfType
            )


@dataclass
class SyntaxTemplateError(ex.rExError):
    """ При компиляции была найдена синтаксическая ошибка функциональных структур.

    Args:
        description (str): description

    """

    description: str


@dataclass
class RecursionTemplateError(ex.rExError):
    """ Максимальное количество рекурсионного вызова структур шаблона при компиляции.

    Args:
        description (str): description

    """

    description: str


@dataclass
class StructureValueError(ex.rExError):
    """ При инициализации структуры не были указаны необходимые данные.

    Args:
        description (str): description

    """

    description: str
