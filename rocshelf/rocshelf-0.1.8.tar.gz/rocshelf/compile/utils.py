""" Модуль с некими доп функциями, которые могут запускаться при компиляции.

В основном это функции, запуск которых определяется конфигурацией приложения.

"""

import rlogging
from rcore.rpath import rPath
from rocshelf.config import pcf

logger = rlogging.get_logger('mainLogger')


def backuping_last_compilation():
    """ Создание backup`а прошлой компиляции.

    Архивирует прошлую версию скомпилированного приложения.
    Сохраняются все исходники и некоторые кеши.

    Делать бекап или нет решает настройка `setting->backup`

    """

    logger.info('Создание backup`а прошлой компиляции')

    if not pcf.setting('backup'):
        logger.debug('Создание backup`а пропущено, так как настройка setting->backup имеет значение False')
        return

    latsCompilationDataFile = rPath('rocshelf-compilation.json', fromPath='cache')

    if not latsCompilationDataFile.check():
        logger.info('Создание backup`а пропущено, так как нет файла с информацией о прошлой компиляции')
        return

    latsCompilationData = latsCompilationDataFile.parse()


def delete_dist():
    """ Очистка папок, куда будет сохранен результат компиляции

    Очищать папки или нет решает настройка `setting->deldist`

    """

    logger.info('Очистка папок экспорта')

    if not pcf.setting('deldist'):
        logger.debug('Очистка папок экспорта пропущено, так как настройка setting->deldist имеет значение False')
        return

    for exportFolderName in ['template', 'static', 'media', 'meta']:
        exportFolderPath = pcf.path('export', exportFolderName)

        logger.warning('Удаление папки экспорта "{0}" по пути "{1}"'.format(
            exportFolderName,
            exportFolderPath
        ))
        exportFolderPath.delete()
