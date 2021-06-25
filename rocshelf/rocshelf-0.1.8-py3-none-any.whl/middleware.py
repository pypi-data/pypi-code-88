""" Прослойка между интерфейсом взаимодействия и основным функционалом.

Объекты этого модуля могут использоваться другими python приложениями.

"""

import json
import os
import typing as _T
import pathlib as pa
import rlogging
from rcore.config import CfEditNamedFile
from rcore.rpath import rPathCopy
from rcore.utils import input_yes_no

from rocshelf import exception as ex
from rocshelf import integration
from rocshelf.components import localization, media, relations, routes, shelves
from rocshelf.components.routes import GetRoute
from rocshelf.config import pcf, rcf

logger = rlogging.get_logger('mainLogger')


class UIIntegration(object):
    """ Интерфейс для интеграции rocshelf в веб приложения python """

    config: _T.Optional[dict[str, _T.Any]] = None

    @classmethod
    def init(cls, distFolderName: _T.Optional[str] = None, cacheFolderName: _T.Optional[str] = None):
        from rocshelf.integration.save import configFileName

        if cacheFolderName is None:
            cacheFolderName = 'cache'

        cacheFolderPath = pa.Path.cwd() / cacheFolderName
        cacheFolderPath = cacheFolderPath.resolve()

        configFilePath = cacheFolderPath / configFileName

        cls.config = json.loads(configFilePath.read_text())

        if 'null' in cls.config['templates']:
            cls.config['templates'][None] = cls.config['templates']['null']
            del cls.config['templates']['null']

    @classmethod
    def path(cls, exportFolderName: str) -> str:
        """ Возвращает абсолютный путь до корневых директорий: template, static и media файлов

        Args:
            exportFolderName (str): Запрашиваемая директория: template, static или media.

        Raises:
            KeyError: Искомый элемент не существует.

        Returns:
            str: Путь до директории.

        """

        if cls.config is None:
            raise RuntimeError('Конфигурация "UIIntegration" не инициализирована')

        try:
            return cls.config['export'][exportFolderName]

        except KeyError:
            raise KeyError('Корневая папка {0} не объявлена'.format(
                exportFolderName
            ))

        logger.debug('Запрос абсолютного пути до корневой директории "{0}"'.format(
            exportFolderName
        ))

        try:
            return rcf.get(['export', exportFolderName])

        except ex.ex.errors.ItemNotFound as exError:
            raise KeyError(exError.description) from None

    @classmethod
    def template(cls, localizationName: _T.Optional[str], route: str) -> str:
        """ Возвращает путь от корневой папки template к запрашиваемому шаблону.

        Args:
            route (str): Маршрут страницы.

        Raises:
            KeyError: Искомый элемент не существует.

        Returns:
            str: Путь до нужного шаблона.

        """

        if cls.config is None:
            raise RuntimeError('Конфигурация "UIIntegration" не инициализирована')

        try:
            return cls.config['templates'][localizationName][route]

        except KeyError:
            raise KeyError('Шаблон для маршрута "{0}" и локализации "{1}" не объявлен'.format(
                route, localizationName
            ))

        logger.debug('Запрос пути до шаблона маршрута: "{0}"'.format(
            route
        ))

        if localizationName is None:
            localizationName = 'null'

        try:
            return rcf.get(['templates', localizationName, route])

        except ex.ex.errors.ItemNotFound as exError:
            logger.error('При запросе пути до файла шаблона ({0}:{1}) произошло исключение: {2}'.format(
                localizationName,
                route,
                exError
            ))
            raise KeyError('Шаблон для маршрута "{0}" и локализации "{1}" не объявлен'.format(
                route, localizationName
            ))

    @classmethod
    def templates(cls) -> dict:
        """ Возвращает словарь всех доступных шаблонов.

        Raises:
            KeyError: Искомый элемент не существует.

        Returns:
            dict: Словарь маршрутов и соответствующих шаблонов.

        """

        if cls.config is None:
            raise RuntimeError('Конфигурация "UIIntegration" не инициализирована')

        try:
            return cls.config['templates']

        except KeyError:
            raise KeyError('Список шаблонов не объявлен')

        logger.debug('Запрос всех маршрутов и соответствующих путей шаблонов')

        try:
            allTemplates = rcf.get(['templates'])

        except ex.ex.errors.ItemNotFound:
            raise KeyError

        if 'null' in allTemplates:
            allTemplates[None] = allTemplates['null']
            del allTemplates['null']

        return allTemplates


class rUI(object):
    """ Базовый класс для создания интерфейсов взаимодействия с компонентами приложения """

    output: str = "dict"
    counter: dict[str, int] = {}
    permission: dict[str, _T.Union[None, bool, int]] = {}

    def __init__(self):
        self.counter = {
            "edited": 0, "created": 0, "existing": 0, "missed": 0, "deleted": 0
        }
        self.permission = {
            'shelf': None, 'route': None
        }

    def get_permission(self, to: str, message: str) -> bool:
        """ Получение разрешения на замену файлов некого Объекта.

        Args:
            to (str): Объект: shelf, route
            message (str): Сообщение для запроса. Defaults to False.

        Returns:
            bool: Полученый ответ

        """

        if self.permission[to] is None:
            self.permission[to] = input_yes_no(message, False)

        return self.permission[to]

    def merge_counts(self, counter: dict[str, int]):
        """ Обновление значений счетчика.

        Args:
            counter (dict[str, int]): Счетчик, из которого берутся значения.

        """

        for i in counter:
            self.counter[i] += counter[i]


class UICompile(rUI):
    """ Интерфейс для работы с компиляцией """

    forFramework: str

    def __init__(self, forFramework: str = 'server'):
        """ Инициализация объекта

        Args:
            forFramework (str): Фреймвор, под который будет адаптированна компиляция.

        """

        self.forFramework = forFramework
        super().__init__()

    def init(self):
        """ Инициализация системы для компиляции """

        shelves.InitComponent.all_stages()
        routes.InitComponent.all_stages()
        localization.InitComponent.all_stages()
        media.init()

        relations.Relation.set_framework(self.forFramework)

    def compile(self):
        """ Запуск компиляции всех страниц """

        self.init()

        from rocshelf import compile
        compile.run()

        integration.save.save_processing_config()


class UIShelves(rUI):
    """ Интерфейс для работы с шелфами.

    Для редактирования файла конфигурации нужно указать его с ключом "shelf" при использовании функции set_config.

    """

    initComponent: shelves.InitComponent

    shelf: shelves.ShelfItem

    restpath: str
    dictpath: list[str]

    def __init__(self, shelfType: str, shelfName: str):
        """ Инициализация Объекта

        Args:
            shelfType (str): Тип шелфа
            shelfName (str): Имя/путь директори шелфа.

        """

        super().__init__()

        self.initComponent = shelves.InitComponent()
        self.initComponent.all_stages()

        (self.shelfPath, shelfName) = os.path.split(shelfName)

        self.shelf = shelves.GetShelf.create(shelfType, shelfName)
        self.dictpath = ['path', 'import', shelfType] + shelfName.split('.')

        self.shelfPath = '/'.join([i for i in [self.shelfPath, shelfName.split('.')[-1]] if i])

    def __create_shelf(self, layout: bool):
        logger.info('Создание шелфа "{0}" по пути "{1}" {2}используя шаблон'.format(
            self.shelf,
            self.shelf.path,
            '' if layout else 'не '
        ))

        if layout:
            targetFolder = self.shelf.path
            layoutFolder = pcf.path('layout', self.shelf)
            rPathCopy.mergedir(
                str(targetFolder),
                [str(layoutFolder)]
            )

        else:
            self.shelf.get_path('html').create()

    def __create(self, layout: bool):
        """ Создание директори шелфа

        Args:
            layout (bool): Использовать шаблон

        """

        needCreate = True
        shelfFound = self.shelf.check()

        if shelfFound:
            needCreate = self.get_permission('shelf', 'По адресу "{0}" есть файлы шелфа. Пересоздать их?'.format(
                self.shelf.path
            ))

        if needCreate:
            self.__create_shelf(layout)

        if needCreate and shelfFound:
            self.counter['edited'] += 1

        elif needCreate:
            self.counter['created'] += 1

        elif shelfFound:
            self.counter['existing'] += 1

        else:
            self.counter['missed'] += 1

    def create(self, layout: bool = False):
        """ Создание шелфа

        Args:
            layout (bool): Использовать шаблон

        """

        try:
            shelves.GetShelf.name(self.shelf.type, self.shelf.name)

        except ex.ShelfNotFoundError:
            with CfEditNamedFile(pcf, 'shelf') as config:
                config.set(self.shelfPath, self.dictpath)
            self.initComponent.parse()
            self.initComponent.construct()

        self.shelf = shelves.GetShelf.name(
            self.shelf.type,
            self.shelf.name,
        )
        self.__create(layout)
        self.initComponent.all_stages()

    def __delete(self):
        paths = self.shelf.get_paths()
        self.counter['deleted'] += 1

        # Удаление основных файлов шелфа
        for shelfFile in paths.values():
            shelfFile.delete(True)

    def delete(self):
        """ Удаление шелфа """

        try:
            shelves.GetShelf.name(self.shelf.type, self.shelf.name)

        except ex.ShelfNotFoundError:
            self.counter['missed'] += 1
            return

        self.__delete()

        with CfEditNamedFile(pcf, 'shelf') as config:
            config.delete(self.dictpath)

        self.initComponent.all_stages()

    def get(self):
        """ Получение информацию о шелфе """

    def sync(self, layout: bool = False):
        """ Создание недостающих шелфов из файла конфигурации

        Args:
            layout (bool): Использовать шаблон

        """

        for shelfType, shelfName, _ in shelves.GetShelf.walk():
            ui = UIShelves(shelfType, shelfName)
            ui.permission['shelf'] = 0
            ui.create(layout)
            self.merge_counts(ui.counter)

        self.initComponent.all_stages()


class UIRoute(rUI):
    """ Интерфейс для работы с маршрутами.

    Для редактирования файла конфигурации нужно указать его с ключом "route" при использовании функции set_config.

    """

    routeKey: str

    initComponent: routes.InitComponent

    def __init__(self, routeKey: str):
        """ Инициализация Объекта.

        Args:
            routeKey (str): Идентификатор маршрута

        """

        super().__init__()
        self.routeKey = routeKey

        routes.check_name_route(routeKey)

    def init_components(self):
        shelves.InitComponent.all_stages()
        routes.InitComponent.all_stages()

    def create(self, pageShelfName: str, layout: bool = False):
        """ Создание маршрута

        Args:
            pageShelfName (str): Путь до директории шелфа-page
            layout (bool, optional): Использовать шаблон

        """

        shelves.check_shelf_name(pageShelfName)

        with CfEditNamedFile(pcf, 'route') as config:
            config.set(
                {'page': pageShelfName, 'data': {}},
                ['route'] + self.routeKey.split('.')
            )

        ui = UIShelves('page', pageShelfName)
        ui.permission['shelf'] = 0
        ui.create(layout)
        self.merge_counts(ui.counter)

        self.init_components()

    def delete(self):
        """ Удаление маршрута """

        with CfEditNamedFile(pcf, 'route') as config:
            config.delete(
                ['route'] + self.routeKey.replace('/', '.').split('.') + ['page']
            )
            config.delete(
                ['route'] + self.routeKey.replace('/', '.').split('.') + ['data']
            )

        self.init_components()

    def get(self):
        """ Получение информации о маршруте """

    def sync(self, layout: bool = False):
        """ Создание недостающих шелфов-page из файла конфигурации

        Args:
            layout (bool): Использовать шаблон

        """

        for _, route in GetRoute.walk():
            ui = UIShelves('page', route.page)
            ui.permission['shelf'] = 0
            ui.create(layout)
            self.merge_counts(ui.counter)

        self.init_components()
