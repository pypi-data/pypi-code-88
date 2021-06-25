""" Основной модуль пакета

Raises:
    ex.RocshelfNotInitError: [description]
"""

import pathlib as pa
import typing as _T

import rlogging
from rcore import main as coreMain
from rcore.rpath import rPath

from rocshelf import cli
from rocshelf import exception as ex
from rocshelf.config import pcf, rcf

VERSION = '0.3'

coreMain.analyze.init('rocshelf')

logger = rlogging.get_logger('mainLogger')


def set_path(userPath: _T.Union[pa.Path, str, None] = None, cacheFolderName: _T.Optional[str] = None, logsFolderName: _T.Optional[str] = None):
    """ Инициализация путей рабочей области.

    Args:
        userPath (pa.Path, str, optional): Рабочая директория пользователя. Defaults to cwd().
        cacheFolderName (_T.Optional[str], optional): Папка используемая как кеш приложения. Defaults to 'cache'.
        logsFolderName (_T.Optional[str], optional): Папка для хранения логов приложения. Defaults to 'cache/logs'.

    """

    if userPath is None:
        userPath = pa.Path.cwd()

    elif isinstance(userPath, str):
        userPath = pa.Path(userPath)

    coreMain.set_path(userPath, pa.Path(__file__).parent, cacheFolderName, logsFolderName)


def set_config(patterns: _T.Optional[list] = None, files: _T.Optional[dict] = None, dictconfig: _T.Optional[dict] = None):
    """ Определение файлов конфигурации.

    Args:
        patterns (list): Паттерн по которому будут искаться файлы конфигурации.
        files (dict): Файлы для отзывчивой работы с CLI.
        dictconfig (dict): Настройки инициализированные напряму.

    """

    if patterns is None:
        patterns = []

    if files is None:
        files = []

    if dictconfig is None:
        dictconfig = []

    appPatterns = {
        'project': patterns,
        'app': ['source/*.json'],
    }

    pcf.init(appPatterns, files, dictconfig)


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
        str(rPath('rocshelf.log', fromPath='logs'))
    )

    subProcessHandler = rlogging.handlers.SubProcessHandler()
    subProcessHandler.printersPool = rlogging.printers.PrintersPool([
        filePrinter
    ])

    logger.handlersPool = rlogging.handlers.HandlersPool([
        # mainProcessHandler,
        subProcessHandler
    ])
    logger.minLogLevel = 20

    rlogging.start_loggers()


def init_for_compiling():
    """ Инициализация системы для компиляции """

    logger.info('Подготовка системы для компиляции')

    pcf.preparation()
    logging_setup()


def init_for_reading():
    """ Инициализация системы для работы с результатом компиляции

    Raises:
        RocshelfNotInitError: Приложение не инициализировано

    """

    logger.info('Подготовка системы для чтения результата')

    rcf.preparation()
    logging_setup()


def stop():
    """ Остановка всех служб приложения """

    coreMain.stop()


@ex.ex.exceptions(stop)
def start_cli():
    """ Запуск CLI.

    Help arguments:
        Option: [--help -h] - Опции и подкоманды у активной команды
        Command: [..tree .trs] - Дерево всех команд и их опций у активной команды

    """

    init_for_compiling()

    cli.init_cli()
    cliOut = cli.entrypoint_command.handler()
    cliOut.start()


def print_rocshelf_info(version: bool = False, clear: bool = False):
    """ Основные функции приложнения

    Args:
        version (bool, optional): Вывести версию. Defaults to False.
        clear (bool, optional): Очистить кеш. Defaults to False.

    """

    if version:
        print(1, 1)

    elif clear:
        rPath(fromPath='cache').delete()

    else:
        raise Exception('так стоп')


def print_rocshelf_help_info(configuration: bool = False):
    """ Вывод вспомогательной информации о приложени

    Args:
        configuration (bool, optional): Показать описание конфигурации. Defaults to False.

    """

    if configuration:
        raise ex.ex.CliHelpPrint(pcf.core.docs_rules())
