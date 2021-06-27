""" Модуль для работы с файлами, которые попадают в шаблонизатор """

from __future__ import annotations

import os
import typing as _T
from copy import copy, deepcopy

import rlogging
from rcore.rpath import rPath
from rocshelf import exception as ex
from rocshelf.template import areas, deconstruct, literals
from rocshelf.template.main import (NodesList, ProcessingParams,
                                    context_generator, registration)
from rocshelf.template.nodes import Node, ProcessingOutputNode

logger = rlogging.get_logger('mainLogger')

# Словарь пути до файла и объекта файла
deconstructedFiles: dict[str, DeconstructedFile] = {}

# Словарь идентификатора файла и объекта файла
deconstructedFilesId: dict[int, DeconstructedFile] = {}

# Количество разрешимых обработок для файла
MAX_RECURSION_COUNT = 10

def get_file(fileId: int) -> rPath:
    """ Получение файла по идентификатору

    Args:
        fileId (int): Идентификатор файла

    Raises:
        TypeError: [description]
        FileNotFoundError: [description]

    Returns:
        rPath: Путь до файла

    """

    return deconstructedFilesId[fileId].pathFile


class DeconstructedFile(object):
    """ Файл прошедший разборку """

    __slots__ = ('pathFile', 'hash', 'id', 'subNodes', 'recursionCount')

    # Счетчик объектов, используемый при установке идентификаторов
    quantityFiles: int = 0

    pathFile: rPath
    hash: str
    id: int

    subNodes: NodesList

    recursionCount: int

    def __str__(self) -> str:
        return '<{0}.{1} id: {2} ({3})>'.format(
            __name__,
            self.__class__.__name__,
            self.id,
            self.pathFile,
        )

    def __init__(self, pathFile: rPath) -> None:
        """ Инициализация объекта

        Args:
            pathFile (rPath): Путь до файла

        """

        logger.debug('Инициализация объекта файла проходящего разбор')

        self.recursionCount = 0

        self.pathFile = pathFile
        self.hash = self.file_hash(pathFile)

        self.id = DeconstructedFile.quantityFiles
        DeconstructedFile.quantityFiles += 1

        deconstructedFiles[self.pathFile] = self
        deconstructedFilesId[self.id] = self

        context = context_generator(pathFile)

        self.subNodes = deconstruct.deconstruct(
            pathFile.read(), self.id, context
        )

        logger.debug('Инициализация объекта файла проходящего разбор с идентификатором {0} и {1} под нод'.format(
            self.id,
            len(self.subNodes)
        ))

    def check_actual(self):
        """ Проверка актуальности объекта

        Raises:
            TypeError: Объект, из которого вызван метод устарел

        """

        actualObject = deconstructedFiles[self.pathFile]

        if actualObject.hash != self.hash:
            raise TypeError('Объект, из которого вызван метод, устарел')

    def get_nodes(self) -> NodesList:
        """ Получение копии нод файла

        Returns:
            NodesList: Ноды

        """

        self.check_actual()

        return deepcopy(self.subNodes)

    def recursion(self):
        """ Учет рекурсии """

        self.recursionCount += 1

        if self.recursionCount >= MAX_RECURSION_COUNT:
            raise ex.RecursionTemplateError('Обрабатываемый файл "{0}" превысил рекурсионный лимит.'.format(
                self.pathFile
            ))

    @staticmethod
    def file_hash(pathFile: rPath) -> str:
        """ Генерация хеша файла, проходящего обработку

        Хеш формируется из пути файла и содержимого.

        Args:
            pathFile (rPath): Путь до файла

        Returns:
            str: Хеш файла

        """

        pathHash = hash(pathFile)
        contentHash = hash(
            pathFile.read()
        )

        resultHash = str(pathHash) + str(contentHash)

        logger.debug('Формирование хеша для файла "{0}". Результат: "{1}"'.format(
            pathFile,
            resultHash
        ))

        return resultHash

    @classmethod
    def get(cls: _T.Type[DeconstructedFile], pathFile: rPath) -> DeconstructedFile:
        """ Получение экземпляра объекта разобранного файла

        Args:
            pathFile (rPath): Путь до файла

        Returns:
            DeconstructedFile: Разобранный файл

        """

        if pathFile not in deconstructedFiles:
            logger.debug('Файл "{0}" не проходил разбор'.format(
                pathFile
            ))
            return cls(pathFile)

        decFile = deconstructedFiles[pathFile]
        hashFile = cls.file_hash(pathFile)

        if decFile.hash == hashFile:
            logger.debug('Файл "{0}" ({1}) проходил разбор и хеши с имеющимся объектом совпадают'.format(
                pathFile, decFile.id
            ))
            return decFile

        logger.debug('Файл "{0}" ({1}) проходил разбор и хеши с имеющимся объектом не совпадают'.format(
            pathFile, decFile.id
        ))

        return cls(pathFile)


class _FileNode(Node):
    """ Нода определяющая файл

    Нода обработки нового файла

    При инициализации принимает ссылку на файл

    """

    __slots__ = ('decFile', )

    decFile: _T.Optional[DeconstructedFile]

    def _exception(self, stage: str, exError: ex.rExError) -> ex.rExError:
        exError.append_traceback(
            self.fileSpan.generate_traceback()
        )
        return exError

    def _deconstruct(self, filePath: rPath):
        if not filePath.check():
            raise ex.rException(FileNotFoundError(str(filePath)))

        self.decFile = DeconstructedFile.get(filePath)

    def get_file_nodes(self) -> _T.Optional[NodesList]:
        """ Получение нод файла

        Returns:
            _T.Optional[NodesList]: Ноды

        """

        logger.debug('Получения нод файла {0}'.format(
            self.decFile
        ))

        self.decFile.recursion()

        if self.decFile is not None:
            return self.decFile.get_nodes()

        return None


    def _processing(self, proccParams: ProcessingParams) -> ProcessingOutputNode:
        logger.debug('Обработка ноды "{0}" разобранного файла "{1}"'.format(
            self.__class__.__name__,
            self.decFile
        ))

        self.subNodes = self.get_file_nodes()

        return ProcessingOutputNode.from_node(self, proccParams)


class FileNode(_FileNode):
    """ Нода файла для инициализации напрямую """

    def _exception(self, stage: str, exError: ex.rExError) -> ex.rExError:
        exError.append_traceback(
            ex.ex.traceback.TextTracebackStage('Прямая инициализация файла через "{0}"'.format(
                self.__class__.__name__
            ))
        )
        return exError

    def __init__(self, filePath: rPath):
        super().__init__(None, None, None)
        self.deconstruct(filePath)


class FileStructureNode(_FileNode):
    """ Нода файла для инициализации через литералы """

    area = areas.ThisNodeArea

    def _exception(self, stage: str, exError: ex.rExError) -> ex.rExError:
        exError.append_traceback(
            self.fileSpan.generate_traceback()
        )
        return exError

    @classmethod
    def literal_rule(cls):
        return literals.InLineStructureLiteral(
            'file', cls,
            ('import', None)
        )

    @classmethod
    def create(cls, literal: literals.LiteralValue):
        fileNode = cls(literal.content, literal.fileSpan)

        thisDecFile = deconstructedFilesId[literal.fileSpan.fileId]
        thisPathFile = copy(thisDecFile.pathFile)

        _, parentFileExtension = os.path.splitext(str(thisPathFile))

        fileName = literal.content
        fileName += parentFileExtension
        targetFile = thisPathFile.merge(fileName)

        fileNode.deconstruct(targetFile)

        return fileNode


# Регистрация описанных узлов
for node in [FileStructureNode]:
    registration(node)
