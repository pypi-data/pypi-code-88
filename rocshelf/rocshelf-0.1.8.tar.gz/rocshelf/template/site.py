""" Модуль описания структур для создания полноценной html страницы """

import typing as _T

import rlogging
from rocshelf.components import localization
from rocshelf.components.media import MediaFile
from rocshelf.components.relations import Relation
from rocshelf.components.static import StaticFile
from rocshelf.config import pcf
from rocshelf.frontend.chunks import Chunk
from rocshelf.template import areas
from rocshelf.template.literals import (InLineOptionalStructureLiteral,
                                        InLineStructureLiteral, LiteralValue)
from rocshelf.template.main import ProcessingParams, registration
from rocshelf.template.nodes import DevNode, Node, ProcessingOutputNode

logger = rlogging.get_logger('mainLogger')

contextTypes = {
    'route': 'page-route'
}


class DownloadStaticPlaceProcessing(object):
    """ Основные функции обработки ноды, растравляющей ссылки на скачивание статики """

    relation: Relation

    def _compile_links(self, loadTime: str, route: str, chunks: _T.Optional[list[Chunk]]) -> str:
        """ Формирование тегов для подключения файлов статики.

        Args:
            loadTime (str): Время загрузки.
            route (str): Активная страница.
            chunks (_T.Optional[list[Chunk]]): Задействованные чанки.

        Raises:
            ValueError: Нет информации о чанков статики.

        Returns:
            str: Теги для подключения файлов статики.

        """

        if chunks is None:
            raise ValueError('При компиляции нод "{0}" в параметрах компиляции должна быть информация о чанках статики'.format(
                self.__class__.__name__
            ))

        # Код импорта стилей в начале и конце страницы различаются
        linkTagList = \
            self._compile_style_prep(route, loadTime, chunks) if loadTime == 'prep' else self._compile_style_final(route, loadTime, chunks)

        linkTagList += self._compile_script(route, loadTime, chunks)

        return ''.join(linkTagList)

    def __url_to_static(self, staticType: str, loadTime: str, shelfSlugs: str, route: str) -> _T.Optional[str]:
        """ Формирование ссылки на скачивание файла статики.

        При создании ссылки проверяется целесообразность подключения файла.
        Если файл пустой, возвращается None.

        Args:
            staticType (str): Тип статики.
            loadTime (str): Время загрузки.
            shelfSlugs (str): Список лейблов шелфов
            route (str): Обрабатываемый маршрут.

        Returns:
            _T.Optional[str]: Ссылка для подключения скачивания файла статики

        """

        staticFileName = self.relation.static_filename(staticType, loadTime, shelfSlugs)

        staticFilePath = self.relation.static_path(staticFileName)
        if not staticFilePath.check():
            return None

        return self.relation.url_to_static(route, staticFileName)

    def _compile_style_prep(self, route: str, loadTime: str, chunks: list[Chunk]) -> list[str]:
        """ Формирование тегов для подключения стилей в начале страницы

        Args:
            route (str): Обрабатываемый маршрут
            loadTime (str): Время загрузки
            chunks (list[Chunk]): Чанки статики

        Returns:
            [type]: Теги для подключения стилей

        """

        linksList = []

        for chunk in chunks:
            linkToStatic = self.__url_to_static('style', loadTime, chunk.shelfSlugs, route)

            if linkToStatic is None:
                continue

            linksList.append('<link href="{0}" rel="stylesheet" type="text/css">'.format(
                linkToStatic
            ))

        return linksList

    def _compile_style_final(self, route: str, loadTime: str, chunks: list[Chunk]) -> list[str]:
        """ Формирование тегов для подключения стилей в конце страницы

        Args:
            route (str): Обрабатываемый маршрут
            loadTime (str): Время загрузки
            chunks (list[Chunk]): Чанки статики

        Returns:
            [type]: Теги для подключения стилей

        """

        linksList = []

        for chunk in chunks:
            linkToStatic = self.__url_to_static('style', loadTime, chunk.shelfSlugs, route)

            if linkToStatic is None:
                continue

            linksList.append(
                linkToStatic
            )

        if not linksList:
            return []

        downloadScript = pcf.path('layout', 'html_links_final_css').read()
        conpileVars = {
            'urls': ','.join(['"{0}"'.format(i) for i in linksList])
        }
        downloadScript = DevNode(downloadScript, ['operators']).processing(conpileVars).compile()

        return [downloadScript]

    def _compile_script(self, route: str, loadTime: str, chunks: list[Chunk]) -> list[str]:
        """ Формирование тегов для подключения скриптов

        Args:
            route (str): Обрабатываемый маршрут
            loadTime (str): Время загрузки
            chunks (list[Chunk]): Чанки статики

        Returns:
            [type]: Теги для подключения скриптов

        """

        linkTagList = []
        for chunk in chunks:
            linkToStatic = self.__url_to_static('script', loadTime, chunk.shelfSlugs, route)

            if linkToStatic is None:
                continue

            linkTagList.append('<script src="{0}"></script>'.format(
                linkToStatic
            ))

        return linkTagList


class DownloadStaticPlaceNode(Node, DownloadStaticPlaceProcessing):
    """ Указатель на точку подключения статики """

    area = areas.ThisNodeArea

    @classmethod
    def literal_rule(cls):
        return InLineStructureLiteral(
            contextTypes['route'], cls,
            ('static', 'place')
        )

    @classmethod
    def create(cls, litValue: LiteralValue):
        return cls(litValue.content, litValue.fileSpan)

    def _deconstruct(self) -> None:
        if self.callParameter not in ('prep', 'final'):
            raise ValueError('При инициализации ноды "{0}" нужно передать время загрузки: ("prep", "final")'.format(
                self.__class__.__name__
            ))

    def _processing(self, proccParams: ProcessingParams) -> ProcessingOutputNode:
        return ProcessingOutputNode.node(self, proccParams)

    def _compile(self, proccParams: ProcessingParams) -> str:
        loadTime = self.callParameter
        route = proccParams.meta().route
        chunks = proccParams.meta().chunks
        self.relation = proccParams.meta().relation
        return self._compile_links(loadTime, route, chunks)


class BaseLinkNode(Node):
    """ Базовая нода для указания ссылок на компоненты сайта """

    area = areas.ThisNodeArea

    @classmethod
    def create(cls, litValue: LiteralValue):
        return cls(litValue.content, litValue.fileSpan)

    def _processing(self, proccParams: ProcessingParams) -> ProcessingOutputNode:
        return ProcessingOutputNode.node(self, proccParams)


class LinkPageNode(BaseLinkNode):
    """ Нода ссылки на другую страницу. """

    @classmethod
    def literal_rule(cls):
        for structurePoint in ['h', 'u', 'url', 'url-p']:
            yield InLineStructureLiteral(
                contextTypes['route'], cls,
                (structurePoint, None)
            )

    def _compile(self, proccParams: ProcessingParams) -> str:
        activeRoute = proccParams.meta().route
        targetRoute = self.callParameter

        return proccParams.meta().relation.url_to_page(activeRoute, targetRoute)


class LinkMediaNode(BaseLinkNode):
    """ Нода ссылки на медиа файл.

    Если вызывается эта нода, то указный файл, относительно папки (input->media), переместится в папку экспорта

    """

    @classmethod
    def literal_rule(cls):
        for structurePoint in ['m', 'url-m']:
            yield InLineStructureLiteral(
                contextTypes['route'], cls,
                (structurePoint, None)
            )

    def _compile(self, proccParams: ProcessingParams) -> str:
        activeRoute = proccParams.meta().route

        targetMediaFile = proccParams.meta().relation.media_filename(self.callParameter)

        MediaFile(self.callParameter).move_to_dist(
            targetMediaFile
        )

        return proccParams.meta().relation.url_to_media(activeRoute, targetMediaFile)


class LinkStaticNode(BaseLinkNode):
    """ Нода ссылки на медиа файл.

    Если вызывается эта нода, то указный файл, относительно папки (input->static), переместится в папку экспорта

    """

    @classmethod
    def literal_rule(cls):
        for structurePoint in ['s', 'url-s']:
            yield InLineStructureLiteral(
                contextTypes['route'], cls,
                (structurePoint, None)
            )

    def _compile(self, proccParams: ProcessingParams) -> str:
        activeRoute = proccParams.meta().route

        targetStaticFile = proccParams.meta().relation.static_filename_safe(self.callParameter)

        StaticFile(self.callParameter).move_to_dist(
            targetStaticFile
        )

        return proccParams.meta().relation.url_to_static(activeRoute, targetStaticFile)


class LocalizationNode(BaseLinkNode):
    """ Нода локализации """

    @classmethod
    def literal_rule(cls):
        for structurePoint in ['l', 'local']:
            yield InLineOptionalStructureLiteral(
                contextTypes['route'], cls,
                (structurePoint, None)
            )

    __slots__ = ('localizationName', )

    localizationName: _T.Optional[str]

    def _deconstruct(self, localizationName: _T.Optional[str]) -> None:
        self.localizationName = localizationName

    @classmethod
    def create(cls, literal: LiteralValue):

        try:
            option = literal.contentMath.group('option')

        except IndexError:
            option = None

        node = cls(literal.content, literal.fileSpan)
        node.deconstruct(option)

        return node

    def _compile(self, proccParams: ProcessingParams) -> str:
        if self.localizationName is None:
            self.localizationName = proccParams.meta().localization

        if self.localizationName is None:
            logger.error('Попытка запросить локализированное значение при компиляций без использования локализации')
            return 'None'

        try:
            return localization.GetLocal.value(self.localizationName, self.callParameter)

        except KeyError as ex:
            logger.error(ex.args[0])
            return 'None'


# Регистрация узлов, которые могут быть вызваны в шаблонах
for node in [DownloadStaticPlaceNode, LinkPageNode, LinkStaticNode, LinkMediaNode, LocalizationNode]:
    registration(node)
