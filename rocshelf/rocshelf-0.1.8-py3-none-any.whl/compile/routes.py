""" Модуль компиляции страниц.

Компиляция зависит от следующих параметров:
    Маршруты (настройка route): каждый маршрут - это отдельная страница
    Файлы локализации (настройка path -> import -> localization):
        На каждый файл с расширением .lang будет производиться итерация компиляция страниц из пункта выше.
        Результат компиляции каждого файла локализации будет храниться в папке с именем файла локализации.

"""

from __future__ import annotations

import typing as _T

import rlogging
from bs4 import BeautifulSoup
from rcore import sync
from rocshelf import template
from rocshelf.compile import params, static, tracebacks
from rocshelf.components import localization
from rocshelf.components.relations import Relation
from rocshelf.components.routes import GetRoute
from rocshelf.frontend.chunks import Chunk, StaticAnalyze

logger = rlogging.get_logger('mainLogger')


@tracebacks.stage_pre_analyze
def pre_analyze():
    """ Запуск анализатора шаблонов.

    Нужен для прочтения всех файлов, разбитие их на литералы и предварительную обработку.

    """

    logger.info('Анализ всех используемых shelf-страниц')

    for routeKey, route in GetRoute.walk():
        logger.debug('Анализ shelf-страницы "{0}" на которую ссылается маршрут "{1}"'.format(
            route.page,
            routeKey
        ))

        template.shelves.ShelfPageNode(route.page)


class CompileRoute(object):
    """ Класс в рамках которого происходит компиляция одного маршрута для одной локации """

    routeKey: str
    localizationName: str

    procParams: ProcessingParams
    shelfNode: template.shelves.ShelfNode

    processingNode: template.nodes.ProcessingOutputNode

    def __init__(self, routeKey: str, localizationName: str) -> None:
        self.routeKey = routeKey
        self.localizationName = localizationName

        route = GetRoute.route(routeKey)

        self.procParams = params.TemplateCompilationMetaData.processing_params(routeKey, localizationName)
        self.shelfNode = template.shelves.ShelfPageNode(route.page)

        self.processingNode = None

    @tracebacks.stage_route_processing
    def processing(self):
        """ Обработка маршрута """

        logger.info('Обработка маршрута "{0}" с локализацией "{1}"'.format(
            self.routeKey, self.localizationName
        ))

        self.processingNode = self.shelfNode.processing(self.procParams)

    @tracebacks.stage_route_compile
    def compile(self) -> str:
        """ Компиляция маршрута

        Raises:
            ValueError: Маршрут не прошел обработку

        Returns:
            str: Скомпилированный текст

        """

        logger.info('Компиляция маршрута "{0}" в локализации "{1}"'.format(
            self.routeKey, self.localizationName
        ))

        if self.processingNode is None:
            raise ValueError('Сначала нужно обработать узлы с помощью "CompileRoute.processing"')

        return self.processingNode.compile(self.procParams)


class CompileLocalization(sync.process.OnProcessMixin):
    """ Класс в рамках которого происходит компиляция всех маршрутов для одной локации """

    relation: Relation
    localizationName: _T.Optional[str]

    processingRoutes: dict[str, CompileRoute]
    chunks: Chunk

    def __init__(self, localizationName: _T.Optional[str] = None) -> None:
        self.processingRoutes = {}

        self.relation = Relation(None, localizationName)
        self.localizationName = localizationName

    def processing(self):
        """ Обработка """

        logger.info('Обработка инициализированных маршутов в локализации "{0}"'.format(
            self.localizationName
        ))

        for routeKey, _ in GetRoute.walk():

            filePath = self.relation.template_path(routeKey)

            if not filePath.check():
                filePath.create()

            self.processingRoutes[routeKey] = CompileRoute(routeKey, self.localizationName)
            self.processingRoutes[routeKey].processing()

    def analyze_static(self):
        """ Передача собраных данных в анализатор статики """

        logger.info('Передача собраных, во время компиляции маршутов в локализации "{0}", данных в анализатор статики'.format(
            self.localizationName
        ))

        staticProcessingData = {
            'shelves': {}
        }

        for routeKey, compileRoute in self.processingRoutes.items():
            staticProcessingData['shelves'][routeKey] = set(compileRoute.processingNode.collectedData['shelves'])

        staticAnalyze = StaticAnalyze.all_stages(
            staticProcessingData
        )

        self.chunks = staticAnalyze.chunks

    def compile_static(self):
        """ Компиляция и сохранение групп статики """

        static.start_compile(
            self.chunks,
            self.localizationName
        )

    def update_proc_params(self):
        """ Обнуление параметров компиляции после анализа статики """

        for routeKey, compileRoute in self.processingRoutes.items():
            targetChunks = [chunk for chunk in self.chunks if routeKey in chunk.routeKeys]

            # localbars -> __meta__ -> chunks
            compileRoute.procParams.meta().add_chucks(targetChunks)

    def compile_templates(self):
        """ Компиляция и сохранение.

        Raises:
            append_traceback: Во время компиляции что-то пошло не так

        """

        logger.info('Компиляция всех инициализированных маршутов в локализации "{0}"'.format(
            self.localizationName
        ))

        for _, compileRoute in self.processingRoutes.items():
            compileRoute.compile()

        logger.info('Сохранение  всех инициализированных маршутов в локализации "{0}"'.format(
            self.localizationName
        ))

        for routeKey, compileRoute in self.processingRoutes.items():

            filePath = self.relation.template_path(routeKey)
            compiledText = compileRoute.compile()

            filePath.write(compiledText, 'w')

    def normalize_html(self):
        """ Нормализация html страницы """

        logger.info('Нормализация Html страниц всех маршрутов')

        for routeKey in GetRoute.all():
            pageFile = self.relation.template_path(routeKey)

            logger.debug('Нормализация Html страницы "{0}" маршрута "{1}"'.format(
                pageFile, routeKey
            ))

            pageText = pageFile.read()

            soup = BeautifulSoup(pageText, 'html.parser')

            pageFile.write(
                soup.prettify(), 'w'
            )

    @tracebacks.stage_localization
    def on_process(self):
        self.processing()

        self.analyze_static()
        self.compile_static()

        self.update_proc_params()
        self.compile_templates()

        self.normalize_html()


def run():
    """ Запуск компиляции маршрутов """

    logger.info('Компиляция маршрутов')
    
    logger.info('Запущена параллельная компиляция всех локализаций в {0} процессов'.format(
        len(localization.localsData)
    ))

    processesPool = sync.process.NoDeamonProcessesPoolController(CompileLocalization)

    for localizationName in localization.GetLocal.all():
        processesPool.add_process(localizationName)

    processesPool.map()
