""" Основной модуль пакета rcore -"""

__debug_mod__ = True

import os
import pathlib as pa
import typing as _T

import rlogging

from rcore import analyze, cli, utils
from rcore import exception as ex
from rcore import rpath
from rcore.config import cf

analyze.init('rcore')

logger = rlogging.get_logger('mainLogger')


def logging_setup():
    """ Настройка логеров """

    lineFormater = rlogging.formaters.LineFormater()

    # Вывод критических ошибок
    # terminalPrinter = rlogging.printers.TerminalPrinter()
    # terminalPrinter.formater = lineFormater

    # mainProcessHandler = rlogging.handlers.MainProcessHandler()
    # mainProcessHandler.printersPool = rlogging.printers.PrintersPool([
    #     terminalPrinter
    # ])

    # Вывод всех сообщений
    filePrinter = rlogging.printers.FilePrinter(
        lineFormater,
        str(rpath.rPath('rcore.log', fromPath='logs'))
    )

    subProcessHandler = rlogging.handlers.SubProcessHandler()
    subProcessHandler.printersPool = rlogging.printers.PrintersPool([
        filePrinter
    ])

    logger.handlersPool = rlogging.handlers.HandlersPool([
        # mainProcessHandler,
        subProcessHandler
    ])
    logger.minLogLevel = 40

    rlogging.start_loggers()


def set_path(userPath: _T.Union[pa.Path, str],
             projectPath: _T.Optional[_T.Union[pa.Path, str]] = None,
             cacheFolderName: _T.Optional[str] = None,
             logsFolderName: _T.Optional[str] = None
             ):
    """ Инициализация корневых путей приложения

    Args:
        userPath (_T.Union[pa.Path, str]): Рабочая директория пользователя
        projectPath (_T.Union[pa.Path, str, None], optional): Директория надстройки над rcore. Defaults to pa.Path(__file__).parent.
        cacheFolderName (_T.Optional[str], optional): Папка используемая как кеш приложения. Defaults to 'cache'.
        logsFolderName (_T.Optional[str], optional): Папка для хранения логов приложения. Defaults to 'cache/logs'.

    """

    if isinstance(userPath, str):
        userPath = pa.Path(userPath)

    if projectPath is None:
        projectPath = pa.Path(__file__).parent

    elif isinstance(projectPath, str):
        projectPath = pa.Path(projectPath)

    if cacheFolderName is None:
        cacheFolderName = 'cache'

    if logsFolderName is None:
        logsFolderName = 'cache/logs'

    rpath.rPaths.init(
        userPath,
        projectPath,
        pa.Path(__file__).parent,
        cacheFolderName,
        logsFolderName
    )


def set_config(patterns: list = [], files: dict = {}, dictconfig: dict = {}):
    """ Определение файлов конфигурации. """

    cf.init({
        'project': patterns,
        'app': ['*.json']
    }, files, dictconfig)


""" Пример работы с rcore

Функции init и start являются примерами инициализации и запуска программы.
Функцию stop можно вызывать надстройками.

"""


def init():
    """ Инициализация приложения rcore.

    Запуск необходимых функций, процессов, etc.

    """

    logger.info('Инициализация rcore')

    # В версии rlogging удаляемый хендлер не выключается, из-за чего происходит бесконечное ожидание
    rlogging.stop_loggers()
    logging_setup()

def stop():
    """ Остановка всех служб rcore """

    logger.info('Остановка всех служб rcore')

    analyze.stop()
    rlogging.stop_loggers()


@ex.exceptions(stop)
def start():
    """ Запуск основного функционала приложения """

    logger.info('Запуск rcore')

    set_path(os.getcwd(), os.path.dirname(__file__))
    init()

    cli.start()
