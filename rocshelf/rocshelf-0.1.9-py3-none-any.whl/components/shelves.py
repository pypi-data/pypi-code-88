""" Модуль для работы с шелфами.

Описаны все переменные и функции для работы с шелфами.

Зависимости:
    Необходима инициализация конфигурации

"""

from __future__ import annotations

import re
from rocshelf.components.files import GetFileInfo
import typing as _T
from copy import copy, deepcopy

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


class ShelfItemPaths(object):
    """ Класс для управлениями путей элемента шелфа """

    mainPath: rPath
    fileNames: dict[str, str]

    _paths: dict[str, _T.Optional[rPath]]

    def __init__(self, shelfPath: rPath, fileNames: dict[str, str]) -> None:
        self.mainPath = shelfPath
        self.fileNames = fileNames

        self.find_files()

    def __gen_root_files(self) -> dict[str, rPath]:
        filePaths = {}

        for fileType, _ in self.fileNames.items():
            fileExpansion = GetFileInfo.expansion(fileType)
            filePath = self.mainPath.parent().merge('{0}.{1}'.format(
                self.mainPath.name, fileExpansion
            ))

            filePaths[fileType] = filePath

        return filePaths

    def __gen_folder_files(self) -> dict[str, rPath]:
        filePaths = {}

        for fileType, fileName in self.fileNames.items():
            fileExpansion = GetFileInfo.expansion(fileType)
            filePath = copy(self.mainPath).merge('{0}.{1}'.format(
                fileName, fileExpansion
            ))

            filePaths[fileType] = filePath

        return filePaths

    def find_files(self) -> dict[str, _T.Optional[rPath]]:
        """ Поиск исходников шелфа

        Returns:
            dict[str, rPath]: Словарь путей до каждого типа исходников

        """

        if self.mainPath.path.is_dir():
            filePaths = self.__gen_folder_files()

        else:
            filePaths = self.__gen_root_files()

        for fileType, filePath in filePaths.items():
            if not filePath.check():
                filePaths[fileType] = None

        logger.debug('У шелфа по пути "{0}" найдены следующие файлы-исходники: {1}'.format(
            self.mainPath, filePaths
        ))

        self._paths = filePaths

    def check(self) -> bool:
        """ Проверка существования хотя бы одного файла исходников

        Returns:
            bool: Есть исходники или нет

        """

        founded = False

        for filePath in self._paths.values():
            if filePath is not None:
                founded = True

        return founded

    def folder(self) -> _T.Optional[rPath]:
        """ Получить папку в которой находится шелф

        Returns:
            _T.Optional[rPath]: Папка

        """

        if not self.mainPath.path.is_dir():
            return None

        return copy(self.mainPath)

    def types(self) -> dict[str, _T.Optional[rPath]]:
        return deepcopy(self._paths)

    def type(self, fileType: str) -> _T.Optional[rPath]:
        return copy(self._paths[fileType])

    def expected(self) -> dict[str, rPath]:
        """ Формирование словаря с ожидаемым расположением файлов исходников

        Returns:
            dict[str, rPath]: Пути до типов исходников

        """

        if self.check():
            if self.mainPath.path.is_dir():
                return self.__gen_folder_files()
            return self.__gen_root_files()

        return self.__gen_folder_files()


class ShelfSlug(object):
    """ Интерфейс для создания лейблов шелфов """

    @staticmethod
    def slug(shelfType: str, shelfName: str):
        """ Создание идентифицирующий строки шелфа """

        return '{0}/{1}'.format(
            shelfType, shelfName
        )

    @staticmethod
    def unslug(shelfLabel: str) -> tuple[str, str]:
        """ Разделение лейбла на составляющие

        Args:
            shelfLabel (str): Лейбел шелфа

        Returns:
            tuple[str, str]: Тип и имя шелфа

        """

        split = shelfLabel.split('/')

        return split[0], '/'.join(split[1:])

    @staticmethod
    def group_slug(shelfGroupName: str, shelfName: str):
        return '{0}-{1}'.format(
            shelfGroupName, shelfName
        )

    @staticmethod
    def group_unslug(shelfName: str):
        split = shelfName.split('-')

        return split[0], '-'.join(split[1:])


class ShelfItem(object):
    """ Класс представляющий некий шелф """

    type: str
    name: str
    id: str

    paths: ShelfItemPaths

    def __str__(self):
        return ShelfSlug.slug(self.type, self.name)

    def __init__(self, userShelfConfig: dict):
        shelfConfig = defaultShelfConfig.copy()
        shelfConfig.update(userShelfConfig)

        self.type = shelfConfig['type']
        self.name = shelfConfig['name']
        self.id = shelfConfig['id']

        if self.type not in SHELFTYPES:
            raise ex.ex.errors.DeveloperIsShitError('{0} - несуществующий тип шелфа'.format(
                self.type
            ))

        if shelfConfig['path'] is None:
            raise Exception('FUCK')

        self.paths = ShelfItemPaths(shelfConfig['path'], {
            'html': shelfConfig['html'],
            'style': shelfConfig['style'],
            'script': shelfConfig['script']
        })

    def check(self) -> bool:
        """ Проверка на существование шелфа

        Шелф считается существующим, если есть файл разметки html

        """

        founded = self.paths.check()

        logger.debug('Проверка существования шелфа "{0}" по пути "{1}". Шелф {2}существует, так как {2}найдет минимум один файл-исходник'.format(
            self,
            self.paths.mainPath,
            '' if founded else ' не'
        ))

        return founded


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

        shelfType, shelfName = ShelfSlug.unslug(shelfSlug)

        GetShelf.check_params(shelfType, shelfName)

        return shelves[shelfType][shelfName]

    @staticmethod
    def create(shelfType: str, shelfName: str, shelfMainPath: rPath) -> ShelfItem:
        """ Создание объекта шелфа. Бкз сохранения в общий список

        Args:
            shelfType (str): Тип шелфа
            shelfName (str): Имя шелфа
            shelfMainPath (rPath): Расположение шелфа

        Returns:
            ShelfItem: Шелф

        """

        check_shelf_name(shelfName)

        shelfConfig = {
            'type': shelfType,
            'name': shelfName,
            'path': shelfMainPath
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
                    shelfName = ShelfSlug.group_slug(groupPrefix, keyShelfName)

                else:
                    shelfName = keyShelfName

                processedShelves[ShelfSlug.slug(shelfType, shelfName)] = processedShelvesTopLevel[keyShelfName]

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
                ShelfSlug.slug(shelfType, shelfName),
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

    def check_names(self):
        """ Проверка валидности имен """

        logger.info('Проверка валидности имен инициализованных шелфов')

        for shelfSlug in self.shelvesPaths:
            _, shelfName = ShelfSlug.unslug(shelfSlug)

            check_shelf_name(shelfName)

    def check_paths(self):
        """ Проверка наличия шелфов по пути.

        Если два шелфа ссылаются на одни файлы - вывести предупреждение.

        Raises:
            ShelfNotFoundError: У некого шелфа нет ни одного файла

        """

        usedPaths = {}

        logger.info('Проверка наличия исходников инициализованных шелфов')

        for shelfType, shelfName, shelfItem in GetShelf.walk():
            if not shelfItem.check():
                raise ex.ShelfNotFoundError(shelfType, shelfName, shelfItem.paths.mainPath)

            if shelfItem.paths.mainPath in usedPaths.items():
                logger.warning('Шелф "{0}" и "{1}" имеют одинаковое расположение: {2}'.format(
                    shelfItem, usedPaths.get(shelfItem.paths.mainPath), shelfItem.paths.mainPath
                ))

            usedPaths[shelfItem.paths.mainPath] = shelfItem

    def construct(self):
        """ Создание объектов шелфов

        Raises:
            ValueError: В конфигурации двух шелфов указаны одинаковые идентификаторы или имена

        """

        usersShelvesName = {}
        for shelfType in SHELFTYPES:
            usersShelvesName[shelfType] = {}

        for shelfLabel in self.shelvesPaths:
            shelfType, shelfName = ShelfSlug.unslug(shelfLabel)

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
                shelfType, shelfName = ShelfSlug.unslug(shelfSlug)

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
            DeveloperIsShitError: Если произошло дублирование идентификаторов

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
        initObject.check_names()
        initObject.construct()
        initObject.check_paths()
        initObject.recover_id()
        initObject.add_id()
        initObject.save_cache()

        logger.info('Инициализированно {0} шелфов'.format(
            utils.len_generator(GetShelf.walk())
        ))
        logger.info('Результат:  Пути: "{0}"; Идентификаторы: "{1}"'.format(
            rPath(saveShelvesPathsFileName, fromPath='cache'),
            rPath(saveShelvesIdsFileName, fromPath='cache')
        ))
