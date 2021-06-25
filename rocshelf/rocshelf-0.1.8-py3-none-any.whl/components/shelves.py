""" Модуль для работы с шелфами.

Описаны все переменные и функции для работы с шелфами.

Зависимости:
    Необходима инициализация конфигурации

"""

from __future__ import annotations

import re
import typing as _T
from copy import copy

import rlogging
from rcore import utils
from rcore.rpath import rPath
from rocshelf import exception as ex
from rocshelf.config import pcf

logger = rlogging.get_logger('mainLogger')

SHELFTYPES = ['wrapper', 'page', 'block', 'tag']

saveShelvesPathsFileName = 'rocshelf-shelves-paths.json'
saveShelvesIdsFileName = 'rocshelf-shelves-ids.json'
groupsConfigFileName = 'rocshelf-groups.json'
groupConfigFileName = 'rocshelf-group.json'
shelfConfigFileName = 'shelf.yaml'

SHELF_ID_SYSTEM = 32

defaultShelfConfig = {
    'type': None,
    'name': None,
    'id': None,
    'html': 'html',
    'style': 'style',
    'script': 'script',
    'path': None
}

shelves: dict[str, dict[str, ShelfItem]] = {}


re_shelf_name = re.compile(r'^((?P<lib>[\w]+)-)?(?P<name>[\w]+(\.[\w]+)*)$')


def check_shelf_name(name: str):
    """ Проверка имени шелфа на валидность """

    if re_shelf_name.match(name) is None:
        raise ValueError(f'"{name}" - novalid shelf name')


class ShelfItem(object):

    type: str
    name: str
    id: str
    path: rPath
    files: dict[str, str]

    def __str__(self):
        return ShelfItem.slug(self.type, self.name)

    @staticmethod
    def slug(shelfType: str, shelfName: str):
        """ Создание идентифицирующий строки шелфа """

        return f'{shelfType}/{shelfName}'

    @staticmethod
    def unSlug(shelfLabel: str) -> tuple[str, str]:
        """ Разделение лейбла на составляющие """

        split = shelfLabel.split('/')

        return split[0], '/'.join(split[1:])

    def __init__(self, userShelfConfig: dict):

        shelfConfig = defaultShelfConfig.copy()
        shelfConfig.update(userShelfConfig)

        self.type = shelfConfig['type']
        self.name = shelfConfig['name']
        self.id = shelfConfig['id']

        if self.type not in SHELFTYPES:
            raise ex.ex.errors.DeveloperIsShitError(self.type + ' - несуществующий тип шелфа')

        self.path = shelfConfig['path']
        self.files = {
            'html': shelfConfig['html'],
            'style': shelfConfig['style'],
            'script': shelfConfig['script']
        }

    def check(self) -> bool:
        """ Проверка на существование шелфа

        Шелф считается существующим, если есть файл разметки html

        """

        logger.debug('Проверка на существование файлов шелфа "{0}" по пути "{1}"'.format(
            self, self.path
        ))

        folderPath = copy(self.path)

        if not folderPath.check():
            logger.debug('Шелф "{0}" не существует, так как не найдена основная папка "{1}"'.format(
                self, self.path
            ))
            return False

        if folderPath.merge(shelfConfigFileName).check():
            logger.debug('Шелф "{0}" существует, так как найден файл конфигурации "{1}"'.format(
                self, folderPath.merge(shelfConfigFileName)
            ))
            return True

        for shelfFileType, shelfFilePath in self.get_paths().items():
            if shelfFilePath.check():
                logger.debug('Шелф "{0}" существует, так как найден файл "{2}" "{1}"'.format(
                    self, shelfFilePath, shelfFileType
                ))
                return True

        logger.debug('Шелф "{0}" не существует, так как не найден ни один из основных файлов'.format(
            self, self.path
        ))

        return False

    def get_shelfName(self):
        return (self.type, self.name)

    def get_paths(self) -> dict[str, rPath]:
        return {
            'html': copy(self.path).merge('{0}.html'.format(
                self.files['html']
            )),
            'style': copy(self.path).merge('{0}.scss'.format(
                self.files['style']
            )),
            'script': copy(self.path).merge('{0}.js'.format(
                self.files['script']
            ))
        }

    def get_path(self, fileType: str) -> rPath:
        return self.get_paths()[fileType]

    def get_folder_path(self):
        """ Основная папка шелфа, где расположен файл shelf.yaml и соответствующие элементу файлы """

        return copy(self.path)


class GetShelf(object):
    """ Выборка шелфов """

    @staticmethod
    def check_params(shelfType: str, shelfName: _T.Optional[str] = None):

        if shelfType not in SHELFTYPES:
            raise ex.ShelfNotFoundError(shelfType)

        if shelfName is not None and shelfName not in shelves[shelfType]:
            raise ex.ShelfNotFoundError(shelfType, shelfName)

    @staticmethod
    def all() -> dict[str, dict[str, ShelfItem]]:
        """ Выборка всех шелфов """

        return shelves

    @staticmethod
    def types(shelfType: str) -> dict[str, ShelfItem]:
        """ Выборка однотипных шелфов """

        GetShelf.check_params(shelfType)

        return shelves[shelfType]

    @staticmethod
    def name(shelfType: str, shelfName: str) -> ShelfItem:
        """ Получение шелфа по типу и имени.

        Args:
            shelfType (str): Тип шелфа
            shelfName (str): Имя шелфа

        Returns:
            ShelfItem: Шелф

        """

        GetShelf.check_params(shelfType, shelfName)

        return shelves[shelfType][shelfName]

    @staticmethod
    def slug(shelfSlug: str) -> ShelfItem:
        """ Получение шелфа по slug`у

        Args:
            shelfSlug (str): slug шелфа

        Returns:
            ShelfItem: Шелф

        """

        shelfType, shelfName = ShelfItem.unSlug(shelfSlug)

        GetShelf.check_params(shelfType, shelfName)

        return shelves[shelfType][shelfName]

    @staticmethod
    def create(shelfType: str, shelfName: str, shelfFolderPath: _T.Optional[rPath] = None) -> ShelfItem:
        """ Создание объекта шелфа. Бкз сохранения в общий список

        Args:
            shelfType (str): Тип шелфа
            shelfName (str): Имя шелфа

        Returns:
            ShelfItem: Шелф

        """

        check_shelf_name(shelfName)

        shelfConfig = {
            'type': shelfType,
            'name': shelfName,
            'path': shelfFolderPath
        }

        return ShelfItem(shelfConfig)

    @staticmethod
    def walk() -> _T.Iterable[tuple[str, str, ShelfItem]]:
        """ Создание итерируемого объекта всех шелфов

        Yields:
            _T.Iterable[tuple[str, str, ShelfItem]: Тип шелфа, Имя шелфа, Элемента шелфа

        """

        for shelfType, shelvesType in shelves.items():
            for shelfName, shelf in shelvesType.items():
                yield (shelfType, shelfName, shelf)


class InitComponentCore(object):
    """ Класс с основными функциями для инициализации компонента шелфов """

    shelvesPaths: dict[str, rPath]
    shelvesIds: dict[str, str]
    usersShelvesIds: dict[str, str]

    shelfTypeIds: utils.IdentifierAssignment
    shelfNameIds: utils.IdentifierAssignment

    def __init__(self):
        logger.info('Инициализация класса инициализации компонента шелфов')

        self.shelvesPaths = {}
        self.shelvesIds = {}
        self.usersShelvesIds = {}

        global shelves
        shelves = {}

        for shelfType in SHELFTYPES:
            shelves[shelfType] = {}

        self.shelfTypeIds = utils.IdentifierAssignment()
        self.shelfNameIds = utils.IdentifierAssignment()

    # # # # # # # # # # # # # #
    # Вспомогательные функции #
    # # # # # # # # # # # # # #

    def transformation_shelves_config(self, importShelves: dict, groupPrefix: _T.Union[str, None] = None) -> dict:
        """ Преобразование объявленных шелфов (имя, пути) в одномерный массив

        Args:
            importShelves (dict): Словарь необработанных шелфов

        Returns:
            dict: Словарь обработанных шелфов

        """

        def cb_key(key: _T.Union[str, tuple]) -> str:
            if isinstance(key, tuple):
                if key[1] == '_':
                    return key[0]

                return '{0}.{1}'.format(
                    key[0], key[1]
                )

            return key

        MissKeys = {
            '.': lambda *args: None,
            'common': lambda *args: None,
        }

        processedShelves = {}

        for shelfType in SHELFTYPES:
            if shelfType not in importShelves:
                continue

            processedShelvesTopLevel = utils.rRecursion(importShelves[shelfType]).core(CB_key=cb_key, CB_to_keys=MissKeys)

            for keyShelfName in processedShelvesTopLevel:

                # Если у некого ключа (словаря) нет шелф значений, а, например, только common
                # То словарь останется
                if isinstance(processedShelvesTopLevel[keyShelfName], dict):
                    continue

                if groupPrefix is not None:
                    # ЦЕНТРАЛИЗИРОВАТЬ ПОСТРОЕНИЕ ТАКИХ ИМЕН
                    # shelfName = f'{groupPrefix}-{keyShelfName}'
                    shelfName = f'{groupPrefix}-{keyShelfName}'
                else:
                    shelfName = keyShelfName

                processedShelves[ShelfItem.slug(shelfType, shelfName)] = processedShelvesTopLevel[keyShelfName]

        return processedShelves

    # # # # # # # # # # #
    # Функции парсинга  #
    # # # # # # # # # # #

    def parse_shelves_group(self, groupPath: rPath) -> dict:
        """ Инициализация шелфов группы.

        Args:
            groupsPath (rPath): Директория группы

        Raises:
            FileNotFoundError: Ненайден файл конфигурации импорта шелфов группы

        """

        logger.debug('Инициализация группы шелфов из директории: "{0}"'.format(
            groupPath
        ))

        groupConfigPath = copy(groupPath).merge(groupConfigFileName)

        if not groupConfigPath.check():
            raise FileNotFoundError('Не найден файл конфигурации группы шелфов: "{0}"'.format(
                groupConfigPath
            ))

        groupConfig = groupConfigPath.parse()

        if 'shelves' not in groupConfig:
            raise KeyError('Не найден ключ "shelves" в конфигурации группы шелфов')

        groupConfigShelves = groupConfig['shelves']
        groupConfigShelves['common'] = str(groupPath)
        groupConfigShelves = utils.rRecursion(groupConfigShelves).path_common(True)

        return self.transformation_shelves_config(groupConfigShelves, groupPath.name)

    def parse_shelves_groups(self, groupsPath: rPath):
        """ Инициализация шелфов из групп.

        Args:
            groupsPath (rPath): Папка, где хранятся группы шелфов

        Raises:
            FileNotFoundError: Ненайден файл конфигурации импорта групп

        """

        logger.debug(f'Инициализация групп шелфов из директории: "{groupsPath}"')

        groupsConfigPath = copy(groupsPath).merge(groupsConfigFileName)

        if not groupsConfigPath.check():
            raise FileNotFoundError(f'Не найден файл конфигурации групп импорта по пути: "{groupsConfigPath}"')

        groupsConfig = groupsConfigPath.parse()

        if 'groups' not in groupsConfig:
            raise FileNotFoundError('Не найден ключ "groups" в конфигурации групп шелфов')

        processedShelves = {}

        for group in groupsConfig['groups']:
            processedShelvesTopLevel = self.parse_shelves_group(copy(groupsPath).merge(group))
            processedShelves.update(processedShelvesTopLevel)

        logger.debug(f'Инициализованно {len(groupsConfig["groups"])} групп в которых {len(processedShelves)} шелфов')

        return processedShelves

    def recover_id_conditions(self, shelfId: str, shelfType: str, shelfName: str) -> bool:
        """ Условия присвоения нового идентификатора шелфу

        Args:
            shelfId (str): Идентификатор
            shelfType (str): Тип шелфа
            shelfName (str): Имя шелфа

        Returns:
            bool: Нужно ли присваивать идентификатор

        """

        try:
            shelf = GetShelf.name(shelfType, shelfName)

        except ex.ShelfNotFoundError as exError:
            logger.warning('Пропущен шелф "{0}" по причине: {1}'.format(
                ShelfItem.slug(shelfType, shelfName),
                exError.description
            ))
            return False

        if shelfId == shelf.id:
            logger.warning('Идентификатор "{0}" у шелфа "{1}" повторяется c казанным пользователем'.format(
                shelfId, shelf
            ))
            return False

        if shelfId in self.usersShelvesIds:
            logger.warning('Идентификатор "{0}" у шелфа "{1}" пропущен, так как уже используется'.format(
                shelfId, shelf
            ))
            return False

        if shelf.id:
            logger.warning('Идентификатор "{0}" у шелфа "{1}" пропущен, так как у шелфа уже есть идентификатор'.format(
                shelfId, shelf
            ))
            return False

        logger.debug('Шелфу "{0}" присвоен кешированный идентификатор "{1}"'.format(
            shelf, shelfId
        ))

        return True


class InitComponent(InitComponentCore):
    """ Класс инициализации компонента шелфов """

    def parse(self):
        """ Парсинг файлов конфигурации и сбор информации обо всех шелфах """

        # Инициализация групп шелфов встроенных в rocshelf
        logger.debug('Инициализация групп шелфов встроенных в rocshelf')
        groupsPath = rPath('groups', fromPath='app.source')
        processedImport = self.parse_shelves_groups(groupsPath)
        self.shelvesPaths.update(processedImport)

        # Инициализация шелфов из конфигурации path -> import -> (page, wrapper, tag, block)
        logger.debug('Инициализация шелфов из конфигурации')
        processedImport = self.transformation_shelves_config(pcf.get(['path', 'import']))
        self.shelvesPaths.update(processedImport)

        # Инициализация добавленных пользователем групп шелфов
        groupsPath = pcf.path('import', 'groups')
        if groupsPath.check():
            logger.debug('Инициализация добавленных пользователем групп шелфов')
            processedImport = self.parse_shelves_groups(groupsPath)
            self.shelvesPaths.update(processedImport)

    def check(self):
        """ Проверка валидности инициализованных шелфов """

        logger.info('Проверка валидности инициализованных шелфов')

        for shelfSlug in self.shelvesPaths:
            shelfPath = copy(self.shelvesPaths[shelfSlug])
            _, shelfName = ShelfItem.unSlug(shelfSlug)

            logger.debug('Проверка шелфа "{0}" по пути "{1}"'.format(
                shelfSlug, shelfPath
            ))

            check_shelf_name(shelfName)

            if not shelfPath.check():
                raise FileNotFoundError(f'Шелфа по пути "{shelfPath}" не существует')

            else:
                logger.debug(f'Шелф "{shelfSlug}" валиден.')

    def construct(self):
        """ Создание объектов шелфов

        Raises:
            ValueError: В конфигурации двух шелфов указаны одинаковые идентификаторы или имена

        """

        usersShelvesName = {}
        for shelfType in SHELFTYPES:
            usersShelvesName[shelfType] = {}

        for shelfLabel in self.shelvesPaths:
            shelfType, shelfName = ShelfItem.unSlug(shelfLabel)

            path = self.shelvesPaths[shelfLabel]

            # СЛИЯНИЕ КОНФИГУРАЦИЙ ПЕРЕНЕСТИ В ИНИЦИАЛИЗАЦИЮ ЭЛЕМЕНТА ШЕЛФА
            shelfConfig = defaultShelfConfig.copy()

            # Если в папке шелфа есть конфигурация, то применяется она
            shelfConfigFile = copy(path).merge(shelfConfigFileName)
            if shelfConfigFile.check():
                shelfConfig.update(
                    shelfConfigFile.parse()
                )

            shelfConfig['path'] = path

            # Проверка валидности типа
            if shelfConfig['type'] is None:
                shelfConfig['type'] = shelfType

            elif shelfConfig['type'] not in SHELFTYPES:
                raise ValueError(f'"{shelfConfig["tp"]}" - несуществующий тип шелфа')

            # Проверка уникальности имени
            if shelfConfig['name'] is None:
                shelfConfig['name'] = shelfName

            else:
                if shelfConfig['name'] in usersShelvesName[shelfConfig['type']]:
                    raise ValueError(f'Имя {shelfConfig["name"]} повторяется у шелфов \
                        "{usersShelvesName[shelfConfig["tp"]][shelfConfig["name"]]}" и "{shelfConfig["path"]}"')

                usersShelvesName[shelfConfig['type']][shelfConfig['name']] = shelfConfig['path']

            # Проверка уникальности идентификатора
            if shelfConfig['id'] is not None:
                if shelfConfig['id'] in self.usersShelvesIds:
                    raise ValueError(f'У шелфов "{shelfConfig["name"]}" и "{self.usersShelvesIds[shelfConfig["id"]]}" указаны одинаковые идентификаторы')
                self.usersShelvesIds[shelfConfig['id']] = shelfConfig['name']

            shelves[shelfConfig['type']][shelfConfig['name']] = ShelfItem(shelfConfig)

    def recover_id(self):
        """ Восстановление идентификаторов из кеша """

        logger.info('Восстановление идентификаторов из кеша')

        # Чтение прошлых настроек идентификации
        self.shelvesIds = {}

        pastShelvesIdsFile = rPath(saveShelvesIdsFileName, fromPath='cache')
        if pastShelvesIdsFile.check():
            shelvesIds = pastShelvesIdsFile.parse()

            for shelfId, shelfSlug in shelvesIds.items():
                shelfType, shelfName = ShelfItem.unSlug(shelfSlug)

                if self.recover_id_conditions(shelfId, shelfType, shelfName):
                    GetShelf.name(shelfType, shelfName).id = shelfId
                    self.shelvesIds[shelfId] = shelfSlug

    def generate_id(self, shelfType: str, shelfName: str, shelf: ShelfItem) -> str:
        """ Генерация идентификатора для шелфа

        Args:
            shelfType (str): Тип шелфа
            shelfName (str): Имя шелфа
            shelf (ShelfItem): Шелф

        Raises:
            ex.ex.errors.DeveloperIsShitError: Если произошло дублирование идентификаторов

        Returns:
            str: Идентификатор

        """

        logger.debug('Генерация идентификатора для шелфа "{0}"'.format(
            shelf
        ))

        newId = utils.convert_base(str(self.shelfTypeIds.id(shelfType)) + str(self.shelfNameIds.id(shelfName)), 10, SHELF_ID_SYSTEM)

        if newId in self.shelvesIds and self.shelvesIds.get(newId) != str(shelf):
            raise ex.ex.errors.DeveloperIsShitError('Ну и коринджовая ситуация получилась: {0} {1} {2}'.format(
                newId, shelf, self.shelvesIds.get(newId)
            ))

        logger.debug('Идентификатор шелфа "{0}" -> {1}'.format(
            shelf,
            newId
        ))

        return newId

    def add_id(self):
        """ Присвоение идентификаторов шелфам """

        logger.info('Формирование новых идентификаторов')

        for shelfType, shelfName, shelf in GetShelf.walk():
            if shelf.id:
                logger.warning('Пропущен шелф "{0}" так как ему уже присвоен идентификатор'.format(
                    shelf
                ))

            shelf.id = self.generate_id(shelfType, shelfName, shelf)
            self.shelvesIds[shelf.id] = str(shelf)

    def save_cache(self):
        """ Сохранение полезой информации о шелфах в кеш """

        rPath(saveShelvesPathsFileName, fromPath='cache').dump(self.shelvesPaths)
        rPath(saveShelvesIdsFileName, fromPath='cache').dump(self.shelvesIds)

    @classmethod
    def all_stages(cls):
        """ Прохождение всех этапов инициализации компонента шелфов """

        initObject = cls()

        logger.info('Инициализации компонента шелфов через функцию прохода по всем этапам')

        initObject.parse()
        initObject.check()
        initObject.construct()
        initObject.recover_id()
        initObject.add_id()
        initObject.save_cache()

        logger.info('Инициализированно {0} шелфов'.format(
            utils.len_generator(GetShelf.walk())
        ))
        logger.info('Результат:  Пути: "{0}"; Идентификаторы: "{1}"'.format(
            rPath(saveShelvesPathsFileName, fromPath="cache"),
            rPath(saveShelvesIdsFileName, fromPath="cache")
        ))
