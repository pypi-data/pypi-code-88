""" Модуль работы со статикой

"""

from __future__ import annotations

import typing as _T

import rlogging
import sass
from rcore import sync
from rcore.rpath import rPath
from rocshelf import template
from rocshelf.compile.params import StaticCompilationMetaData
from rocshelf.components import shelves
from rocshelf.components.relations import Relation
from rocshelf.config import pcf
from rocshelf.frontend.chunks import Chunk

logger = rlogging.get_logger('mainLogger')


def static_file_types() -> list[tuple[str, str]]:
    """ Формирует список из под типов каждого файла

    Returns:
        list[tuple[str, str]]: Список

    """

    return [(i, d) for d in ['prep', 'final'] for i in ['style', 'script']]


def cache_folder(subFolder: _T.Optional[str] = None) -> rPath:
    if subFolder is None:
        return rPath('static', fromPath='cache')

    return rPath('static', fromPath='cache').merge(subFolder)


class CompileStaticCode(object):
    """ Группировка функций для компиляции разных видов кода """

    @staticmethod
    def sass(inputFile: rPath, exportFile: rPath):
        """ Компиляция sass кода

        Args:
            inputFile (rPath): Входной файл
            exportFile (rPath): Результат сохранить в файл

        """

        if not exportFile.check():
            exportFile.create()

        try:
            compiledText = sass.compile(filename=str(inputFile), output_style=pcf.setting('compression'))

        except sass.CompileError as error:
            logger.error('При компиляции sass кода, произошла ошибка: {0}'.format(
                error
            ))
            compiledText = inputFile.read()

        exportFile.write(compiledText, 'w')


class CompileChunkType(sync.process.OnProcessMixin):
    """ Компиляция конкретного файла группы статики """

    relation: Relation
    localizationName: str

    staticType: str
    loadTime: str
    chunk: Chunk

    staticFileName: str

    def __init__(self, staticType: str, loadTime: str, chunk: Chunk, localizationName: str) -> None:
        self.relation = Relation(None, localizationName)
        self.localizationName = localizationName

        self.staticType = staticType
        self.loadTime = loadTime
        self.chunk = chunk

        self.staticFileName = self.relation.static_filename(staticType, loadTime, chunk.shelfSlugs)

    def __compile_file(self, targetFile: rPath) -> str:
        """ Обработка и компиляция файла статики

        Args:
            targetFile (rPath): Исходный файл

        Returns:
            str: Скомпилированный код

        """

        logger.debug('Обработка и компиляция файла статики "{0}"'.format(
            targetFile
        ))

        # None - localizationName
        processingParams = StaticCompilationMetaData.processing_params(
            self.localizationName, self.staticType, self.loadTime, self.chunk, self.staticFileName
        )

        shelfFileNode = template.file.FileNode(targetFile)
        processingNode = shelfFileNode.processing(processingParams)
        return processingNode.compile(processingParams)

    def add_comment(self, commentKey: str, *args):
        """ Добавление в файл статики комментария """

        cacheFolder = cache_folder('raw')
        staticFile = cacheFolder.merge(self.staticFileName)

        if commentKey == 'welcome':
            textComment = '/* Rocshelf processing static file ({0}): {1} - {2} */\n'.format(
                self.staticFileName,
                self.staticType,
                self.loadTime
            )
            textComment += '/* For routes: {0} */\n'.format(
                ', '.join(self.chunk.routeKeys)
            )
            textComment += '/* On shelves: {0} */\n'.format(
                ', '.join(self.chunk.shelfSlugs)
            )
            if self.chunk.isBase:
                textComment += '/* And default code */\n'
            staticFile.write(textComment, 'w')

        elif commentKey == 'br':
            textComment = '\n\n/* -- {0} -- */\n\n'.format(
                args[0]
            )
            staticFile.write(textComment, 'a')

    def parse_base_code(self):
        """ Чтение основных файлов статики и сохранение в промежуточной папке """

        logger.info('Чтение файлов базовой статики и добавление в файл чанка "{0}"'.format(
            self.chunk
        ))

        if not self.chunk.isBase:
            logger.debug('Чанк "{0}" не должен содержать код базовый статики. Добавление пропускается.'.format(
                self.chunk
            ))
            return

        cacheFolder = cache_folder('raw')
        cacheStaticFile = cacheFolder.merge(self.staticFileName)

        userStaticFolder = pcf.path('import', 'static')

        if self.staticType == 'style':
            userStaticFile = userStaticFolder.merge('style.scss')

        else:
            userStaticFile = userStaticFolder.merge('script.js')

        if not userStaticFile.check():
            logger.warning('Файл базовой статики "{0}" не существует. Добавление пропускается.'.format(
                userStaticFile
            ))
            return

        self.add_comment('br', 'basic code')
        cacheStaticFile.write(self.__compile_file(userStaticFile), 'a')

    def parse_shelves(self):
        """ Чтение файлов статики шелфов и сохранение в промежуточной папке """

        logger.info('Чтение файлов статики шелфов и добавление в файл чанка "{0}"'.format(
            self.chunk
        ))

        cacheStaticFile = cache_folder('raw').merge(self.staticFileName)

        for shelfSlug in self.chunk.shelfSlugs:
            shelf = shelves.GetShelf.slug(shelfSlug)

            shelfStaticFile = shelf.get_path(self.staticType)

            if not shelfStaticFile.check():
                logger.warning('Файл статики шелфа "{0}" не существует. Добавление пропускается.'.format(
                    shelfStaticFile
                ))
                return

            self.add_comment('br', str(shelf))

            cacheStaticFile.write(self.__compile_file(shelfStaticFile), 'a')

    def compile(self):
        fromStaticFile = cache_folder('raw').merge(self.staticFileName)
        targetStaticFile = cache_folder('compiled').merge(self.staticFileName)

        if self.staticType == 'style':
            CompileStaticCode.sass(fromStaticFile, targetStaticFile)

        else:
            fromStaticFile.copy_file(targetStaticFile)

    def filter(self):
        """ Фильтрация импорта

        Добавление параметра ignoreDowload для файлов статики, которые:
        * Не содержат кода

        """

        staticFile = cache_folder('compiled').merge(self.staticFileName)

        noCommentString = template.file.FileNode(staticFile).processing().compile().strip()

        if noCommentString == '':
            logger.warning('Файл статики "{0}" чанка {1} с временем загрузки "{2}" пустой'.format(
                self.staticType,
                self.chunk,
                self.loadTime
            ))
            staticFile.delete()

    def move(self):
        """ Перемещение скомпилированных группы """

        fromStaticFile = cache_folder('compiled').merge(self.staticFileName)
        targetStaticFile = self.relation.static_path(self.staticFileName)

        # Если новый файл статики не существует, то нужно удалить и тот, который должен скачиваться.
        # Далее в логике, если targetStaticFile, то ссылка на него формироваться не будет.
        if not fromStaticFile.check():
            targetStaticFile.delete()

        else:
            fromStaticFile.copy_file(targetStaticFile)

    def on_process(self):
        self.add_comment('welcome')
        self.parse_base_code()
        self.parse_shelves()
        self.compile()
        self.filter()
        self.move()


class CompileChunk(sync.process.OnProcessMixin):
    """ Компиляция группы статики """

    chunk: Chunk
    localizationName: str

    def __init__(self, chunk: Chunk, localizationName: str) -> None:
        super().__init__()
        self.chunk = chunk
        self.localizationName = localizationName

    def on_process(self):
        processesPool = sync.process.NoDeamonProcessesPoolController(CompileChunkType)

        for staticType, loadTime in static_file_types():
            processesPool.add_process(staticType, loadTime, self.chunk, self.localizationName)

        processesPool.map()


def start_compile(chunks: list[Chunk], localizationName: str):
    """ Компиляция и сохранение статики

    Args:
        chunks (list[Chunk]): Проанализированные группы статики
        localizationName (str): Компилируемая локализация

    """

    processesPool = sync.process.NoDeamonProcessesPoolController(CompileChunk)

    for chunk in chunks:
        processesPool.add_process(chunk, localizationName)

    processesPool.map()
