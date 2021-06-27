
from __future__ import annotations

import functools
import typing as _T

import rlogging
from rocshelf.components import localization, relations, routes, shelves
from rocshelf.components.routes import GetRoute
from rocshelf.frontend.chunks import Chunk

logger = rlogging.get_logger('mainLogger')


class SharedCompilationMetaData(object):
    """ Общая информация обо всей компиляции.

    Парметры:
      frameworks (list[str]):
        Список фреймворков для которых будет происходить компиляция

      locals (list[str]):
        Список локализаций компиляции

      locals (list[str]):
        Список компилируемых маршрутов

    Использование:
      В шаблон компиляции передается словарь данных, один из которых __meta__, у которого атрибут __shared__, в виде объекта данного класса

    """

    __slots__ = (
        'localizations', 'shelves', 'routes',
    )

    localizations: str
    shelves: str
    routes: str

    def __init__(self):
        self.localizations = tuple(localization.localsData.keys())
        self.routes = tuple(routes.routes.keys())

        self.shelves = {}
        for shelfType in shelves.SHELFTYPES:
            self.shelves[shelfType] = tuple(shelves.shelves[shelfType].keys())

    @classmethod
    @functools.cache
    def cached(cls):
        """ Кеширование создания класса

        Returns:
            [type]: Экземпляр класса SharedCompilationMetaData

        """

        return cls()


class TemplateCompilationMetaData(object):
    """ Информация о процессе компиляции.

    Использование:
      В шаблон компиляции передается словарь данных, один из которых __meta__ в виде объекта данного класса

    """

    __slots__ = (
        '__shared__',
        'framework', 'localization', 'relation',
        'route', 'page', 'shelf', 'chunks',
    )

    __shared__: SharedCompilationMetaData

    framework: str
    localization: _T.Union[str, None]
    relation: relations.Relation

    route: str
    page: str
    shelf: str

    chunks: _T.Optional[list[Chunk]]

    def __init__(self, localizationName: _T.Union[str, None], route: str, page: str, shelf: str):
        self.__shared__ = SharedCompilationMetaData.cached()

        self.relation = relations.Relation(None, localizationName)
        self.framework = self.relation.framework
        self.localization = self.relation.localizationName

        self.route = route
        self.page = page
        self.shelf = shelf

        self.chunks = None

    def add_chucks(self, chunks: list[Chunk]):
        """ Добавление в метаданные компиляции атрибута с чанками статики

        Args:
            chunks (list[Chunk]): Чанки статики

        """

        self.chunks = chunks

    @classmethod
    def processing_params(cls, routeKey: str, localizationName: _T.Union[str, None]) -> ProcessingParams:
        """ Создание объекта параметров компиляции

        Args:
            routeKey (str): Идентификатор маршрута
            localizationName (_T.Union[str, None]): Компилируемая локализация

        Returns:
            ProcessingParams: Параметры компиляции

        """

        route = GetRoute.route(routeKey)

        page = route.page
        localVars = route.localVars

        shelf = shelves.GetShelf.name('page', page)

        localVars['__meta__'] = cls(localizationName, routeKey, page, str(shelf))

        return ProcessingParams(localVars)


class StaticCompilationMetaData(object):
    """ Информация о процессе компиляции.

    Использование:
      В шаблон компиляции передается словарь данных, один из которых __meta__ в виде объекта данного класса

    """

    __slots__ = (
        '__shared__',
        'framework', 'localization', 'relation',
        'staticType', 'loadTime', 'routeKeys', 'shelfSlugs', 'staticFileName'
    )

    __shared__: SharedCompilationMetaData

    framework: str
    localization: _T.Optional[str]
    relation: relations.Relation

    staticType: str
    loadTime: str
    routeKeys: set[str]
    shelfSlugs: set[str]
    staticFileName: str

    def __init__(self,
                 localizationName: _T.Optional[str],
                 staticType: str,
                 loadTime: str,
                 routeKeys: set[str],
                 shelfSlugs: set[str],
                 staticFileName: str
                 ):

        self.__shared__ = SharedCompilationMetaData.cached()

        self.relation = relations.Relation(None, localizationName)
        self.framework = self.relation.framework
        self.localization = self.relation.localizationName

        self.staticType = staticType
        self.loadTime = loadTime
        self.routeKeys = routeKeys
        self.shelfSlugs = shelfSlugs
        self.staticFileName = staticFileName

    @classmethod
    def processing_params(cls,
                          localizationName: _T.Optional[str],
                          staticType: str,
                          loadTime: str,
                          chunk: Chunk,
                          staticFileName: str) -> ProcessingParams:
        """ Создание объекта параметров компиляции

        Args:
            localizationName (_T.Optional[str]): [description]
            staticType (str): [description]
            loadTime (str): [description]
            Chunk (Chunk): [description]
            staticFileName (str): [description]

        Returns:
            ProcessingParams: Параметры компиляции

        """

        localVars = {}

        localVars['__meta__'] = cls(
            localizationName,
            staticType,
            loadTime,
            chunk.routeKeys,
            chunk.shelfSlugs,
            staticFileName
        )

        return ProcessingParams(localVars)


class ProcessingParams(object):
    """ Параметры компиляции """

    localVars: dict[_T.Any, _T.Any]

    def __init__(self, localVars: _T.Optional[dict] = None) -> None:

        if localVars is None:
            localVars = {}

        self.localVars = localVars

    def add(self, proccParams: ProcessingParams):
        """ Слияние двух объектов параметризации компиляции """

        logger.debug('Слияние двух объектов {0}: {1} & {2}'.format(
            self.__class__.__name__,
            id(self),
            id(proccParams)
        ))

        self.localVars.update(
            proccParams.localVars
        )

    def meta(self) -> TemplateCompilationMetaData:
        return self.localVars.get('__meta__', None)
