""" Модуль разделения фронтенда на чанки

"""


from __future__ import annotations

import typing as _T

import rlogging

logger = rlogging.get_logger('mainLogger')


class Chunk(object):
    """ Группа статики для группы страниц """

    __slots__ = ('routeKeys', 'shelfSlugs', 'isBase')

    routeKeys: set[str]
    shelfSlugs: set[str]
    isBase: bool

    def __str__(self) -> str:
        return self.__repr__()

    def __repr__(self) -> str:
        return '<Chunk isBase:{0} {1}:{2}>'.format(
            self.isBase,
            self.routeKeys,
            self.shelfSlugs
        )

    def __init__(self,
                 routeKeys: _T.Optional[_T.Iterable[str]] = None,
                 shelfSlugs: _T.Optional[_T.Iterable[str]] = None,
                 isBase: bool = False
                 ) -> None:

        self.routeKeys = set()
        if routeKeys is not None:
            self.routeKeys = set(routeKeys)

        self.shelfSlugs = set()
        if shelfSlugs is not None:
            self.shelfSlugs = set(shelfSlugs)

        self.isBase = isBase


class StaticAnalyze(object):
    """ Анализ статики. Разбиение на чанки """

    routesKeys: _T.KeysView[str]
    staticData: dict[str, _T.Any]

    chunks: list[Chunk]

    def __init__(self, staticData: dict[str, _T.Any]) -> None:
        super().__init__()

        self.routesKeys = staticData['shelves'].keys()
        self.staticData = staticData
        self.chunks = []

    def add_base_static(self):
        """ Добавление групп с базывыми статик файлами """

        for routeKey in self.routesKeys:
            self.chunks.append(
                Chunk([routeKey], None, True)
            )

    def add_shelves(self):
        """ Добавление шелфов в группы """

        for routeKey in self.routesKeys:
            for shelfName in self.staticData['shelves'][routeKey]:
                self.chunks.append(
                    Chunk([routeKey], [shelfName], False)
                )

    def __merge_chunks_iterable(self, targetChunk: Chunk, callback: _T.Callable[[Chunk], None]) -> bool:
        if targetChunk.shelfSlugs is None or targetChunk.routeKeys is None:
            return False

        for subChunk in self.chunks:
            if id(targetChunk) == id(subChunk):
                continue

            callback(targetChunk, subChunk)

        return targetChunk

    def __merge_chunks_by_static(self, targetChunk: Chunk, subChunk: Chunk):
        if targetChunk.shelfSlugs == subChunk.shelfSlugs and targetChunk.isBase == subChunk.isBase:
            targetChunk.routeKeys.update(subChunk.routeKeys)
            subChunk.shelfSlugs = None

    def __merge_chunks_by_routes(self, targetChunk: Chunk, subChunk: Chunk):
        if targetChunk.routeKeys == subChunk.routeKeys:
            targetChunk.shelfSlugs.update(subChunk.shelfSlugs)
            if targetChunk.isBase or subChunk.isBase:
                targetChunk.isBase = True
            subChunk.routeKeys = None

    def merge_chunks(self):
        """ Слияние групп

        В приоритете уменьшение до 0 скачивания ненужных файлов

        """

        while True:
            lastLen = len(self.chunks)

            self.chunks = list(filter(
                lambda x: x,

                map(
                    lambda x: self.__merge_chunks_iterable(x, self.__merge_chunks_by_static),
                    self.chunks
                )
            ))

            self.chunks = list(filter(
                lambda x: x,

                map(
                    lambda x: self.__merge_chunks_iterable(x, self.__merge_chunks_by_routes),
                    self.chunks
                )
            ))

            if len(self.chunks) == lastLen:
                break

    def sort(self):
        """ Сортировка шелфов

        Статика в файлах сортируется по причастности к шелфу:
        `Tag` -> `Block` -> `Page` -> `Wrapper` - где Tag будет в начале файла, а Wrapper в конце

        """

        # !!!
        # shelfSlugs должен быть списком

        countTable = {
            'tag': 4,
            'block': 3,
            'page': 2,
            'wrapper': 1
        }

        def __sort(value: str):
            shelfType = value.split('/')[0]
            return countTable[shelfType]

        for chunk in self.chunks:
            shelfSlugsList = list(chunk.shelfSlugs)
            shelfSlugsList.sort(key=__sort)
            chunk.shelfSlugs = set(shelfSlugsList)

    @classmethod
    def all_stages(cls, staticData: dict[str, _T.Any]) -> StaticAnalyze:
        analyzeObject = cls(staticData)
        analyzeObject.add_base_static()
        analyzeObject.add_shelves()
        analyzeObject.merge_chunks()
        analyzeObject.sort()
        return analyzeObject
