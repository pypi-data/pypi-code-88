""" Модуль адаптации процесса компиляции под настройки

Поддерживаемые фреймворки
    folder - сайт расположен в некой папке.
      Связь между файлами относительные
    server - сайт на неком сервере
      Связь между файлами абсолютная
    django - результат компиляции - это шаблон для django
      Связь между файлами абсолютная
      Все возможные структуры адаптированы под шабдлнизатор django

"""
from __future__ import annotations

import functools
import os
import typing as _T
from copy import copy

import rlogging
from rcore.rpath import arcmerge, rPath
from rocshelf.components import localization, shelves
from rocshelf.config import pcf

logger = rlogging.get_logger('mainLogger')

supported_framework = ('folder', 'server', 'django')


def logging_result_relations(title: str) -> _T.Callable:
    """ Логирование входных данных и результата генерации связей

    Args:
        title (str): Заголовок генерируемого процесса

    Returns:
        _T.Any: результат callback функции

    """

    def wrapper(func: _T.Callable):
        @functools.wraps(func)
        def inner(self, *args, **kwargs):

            if self.framework is None:
                raise AttributeError('"Relation" object has no attribute "framework"')

            try:
                genResult = func(self, *args, **kwargs)

            except Exception as exError:
                logger.error('Произошла ошибка при генерации "{0}" для связи ({1}:{2}) с параметрами: [{3}, {4}]"'.format(
                    title,
                    self.framework, self.localizationName,
                    args, kwargs
                ))
                raise exError

            logger.debug('Генерация "{0}" для связи ({1}:{2}) с параметрами: [{3}, {4}] -> "{5}"'.format(
                title,
                self.framework, self.localizationName,
                args, kwargs,
                genResult
            ))

            return genResult

        return inner
    return wrapper


class InitRelations(object):
    """ Варианты инициализации интерфейса взаимодействия """

    framework: _T.Optional[str] = None

    localizationName: _T.Optional[str]

    def __init__(self, framework: _T.Optional[str] = None, localizationName: _T.Optional[str] = None) -> None:
        if self.framework is None:
            self.__class__.framework = framework

        self.localizationName = localizationName

    def init(self, framework: _T.Optional[str] = None, localizationName: _T.Optional[str] = None):
        """ Инициализация интерфеса адаптации компиляции под фреймворк """

        logger.info('Инициализация объекта связей ({0}:{1})'.format(
            framework,
            localizationName
        ))

        if framework:
            if framework not in supported_framework:
                raise ValueError('"{0}" - неподдерживаемый фреймворк'.format(
                    framework
                ))

            self.framework = framework

        if localizationName:
            if localizationName not in localization.localsData:
                raise ValueError('"{0}" - неизвестный идентификатор локализации'.format(
                    localizationName
                ))

            self.localizationName = localizationName

    @classmethod
    def set_framework(cls, framework: str):
        """ Установка фреймворка, с учетом которого будут формироваться связи

        Args:
            framework (str): фреймворк

        Returns:
            InitRelations: Экземпляр класса

        """

        cls.framework = framework
        return cls()

    @classmethod
    def set_local(cls, localizationName: str):
        """ Установка фреймворка, с учетом которого будут формироваться связи

        Args:
            localizationName (str): Идентификатор локализации

        Returns:
            InitRelations: Экземпляр класса

        """

        relation = cls()
        relation.localizationName = localizationName
        return relation


class FileNameRelations(InitRelations):
    """ Формирование имен компонентов приложения """

    @logging_result_relations('Имя файла шаблона')
    def template_filename(self, route: str) -> str:
        """ Генерация пути относительно папки расположения шаблонов

        Args:
            route (str): Маршрут, для страницы которого генерируется имя

        Returns:
            str: Имя файла страницы

        """

        if self.framework in ['folder', 'server']:
            fileName = os.path.join(*route.split('.'))

        elif self.framework == 'django':
            fileName = route.replace('.', '-')

        fileName = '{0}.html'.format(
            fileName
        )

        if self.localizationName is not None:
            return '{0}/{1}'.format(
                self.localizationName,
                fileName
            )

        return fileName

    @logging_result_relations('Имя файла статики из имени файла статики')
    def static_filename_safe(self, staticFileName: str):
        if self.localizationName is not None:
            return '{0}-{1}'.format(
                self.localizationName,
                staticFileName
            )

        return staticFileName

    @logging_result_relations('Имя файла статики')
    def static_filename(self, staticType: str, loadTime: str, usedShelves_slugs: _T.Iterable[str]) -> str:
        """ Генерация имени файла статики

        Args:
            staticType (str): Тип файла статики (style, script)
            loadTime (str): Время загрузки (prep, final)
            usedShelves_slugs (_T.Iterable[str]): Используемые шелфы

        Returns:
            str: [description]

        """

        # ХУ Е ТА
        staticTypeExtensions = {
            'style': 'css',
            'script': 'js',
            'html': 'html',
        }

        usedShelvesIds = []
        for shelfSlug in usedShelves_slugs:
            usedShelvesIds.append(
                shelves.GetShelf.slug(shelfSlug).id
            )

        staticTypeExtension = staticTypeExtensions[staticType]

        return '{0}-{1}-{2}-{3}.{4}'.format(
            'nolang' if self.localizationName is None else self.localizationName,
            staticType,
            loadTime,
            '-'.join(usedShelvesIds),
            staticTypeExtension
        )

    @logging_result_relations('Имя медиа файла')
    def media_filename(self, mediaFile: str) -> str:
        """ Генерация имени файла статики """

        if self.localizationName is not None:
            return '{0}-{1}'.format(
                self.localizationName,
                mediaFile
            )

        return mediaFile


class PathRelations(FileNameRelations):
    """ Формирование путей компонентов приложения """

    @logging_result_relations('Путь до файла шаблона')
    def template_path(self, route: str) -> rPath:
        """ Генерация пути, по которому должен располагаться файл страницы

        Args:
            route (str): Маршрут страницы

        Returns:
            rPath: Путь, по которому должен располагаться файл

        """

        return pcf.path('export', 'template').merge(self.template_filename(route))

    @logging_result_relations('Путь до файла статики')
    def static_path(self, staticFileName: str) -> rPath:
        """ Генерация пути до файла статики

        Args:
            staticFileName (str): Сгенерированное имя файла статики (.static_filename())

        Returns:
            rPath: Путь, по которому должен располагаться файл

        """

        return pcf.path('export', 'static').merge(staticFileName)

    @logging_result_relations('Путь до медиа файла')
    def media_path(self, mediaFileName: str) -> rPath:
        """ Генерация пути до медиа файла

        Args:
            mediaFileName (str): Сгенерированное имя медиа файла (.media_filename())

        Returns:
            rPath: Путь, по которому должен располагаться файл

        """

        return pcf.path('export', 'media').merge(mediaFileName)


class UrlRelations(PathRelations):
    """ Формирование ссылок между компонентами приложения """

    @logging_result_relations('Ссылка до страницы')
    def url_to_page(self, activeRoute: str, targetRoute: str) -> str:
        """ Генерация ссылки до страницы

        Args:
            activeRoute (str): Маршрут активной страницы, с которой происходит переход
            targetRoute (str): Маршрут целевой страницы, на которую нужно перейти

        Returns:
            str: Ссылка для перехода

        """

        if self.framework == 'folder':
            activePagePath = self.template_path(activeRoute)
            targetPagePath = self.template_path(targetRoute)

            url = arcmerge(str(activePagePath), str(targetPagePath))

        elif self.framework == 'server':
            url = '/' + self.template_filename(targetRoute)

        elif self.framework == 'django':
            url = "{% url '" + targetRoute + "' %}"

        return str(url)

    @logging_result_relations('Ссылка до файла статики')
    def url_to_static(self, activeRoute: str, staticFileName: str) -> str:
        """ Генерация ссылки на файл статики

        Args:
            activeRoute (str): Маршрут активной страницы, с которой происходит обращение
            staticFileName (str): Имя целевого файла, на который нужно сослаться

        Returns:
            str: Ссылка для обращения

        """

        if self.framework == 'folder':
            activePagePath = self.template_path(activeRoute)
            targetFile = self.static_path(staticFileName)

            url = arcmerge(str(activePagePath), str(targetFile))

        elif self.framework in ('server', 'django'):

            # Возможно это нужно будет заменить на префикс, который будет задаваться в конфигурации
            baseUrl = arcmerge(str(pcf.path('export', 'template')), str(pcf.path('export', 'static')))

            baseUrl = baseUrl.replace('../', '')

            if baseUrl[0] != '/':
                baseUrl = '/{0}'.format(baseUrl)

            url = '{0}/{1}'.format(
                baseUrl, staticFileName
            )

        return url

    @logging_result_relations('Ссылка до медиа файла')
    def url_to_media(self, activeRoute: str, mediaFileName: str) -> str:
        """ Генерация ссылки на медиа файл

        Args:
            activeRoute (str): Маршрут активной страницы, с которой происходит обращение
            mediaFileName (str): Имя целевого файла, на который нужно сослаться

        Returns:
            str: Ссылка для обращения

        """

        if self.framework == 'folder':
            activePagePath = self.template_path(activeRoute)
            targetFile = self.media_path(mediaFileName)

            url = arcmerge(str(activePagePath), str(targetFile))

        elif self.framework in ('server', 'django'):

            # Возможно это нужно будет заменить на префикс, который будет задаваться в конфигурации
            baseUrl = arcmerge(str(pcf.path('export', 'template')), str(pcf.path('export', 'media')))

            baseUrl = baseUrl.replace('../', '')

            if baseUrl[0] != '/':
                baseUrl = '/{0}'.format(baseUrl)

            url = '{0}/{1}'.format(
                baseUrl, mediaFileName
            )

        return url


class Relation(UrlRelations):
    """ Функции для установления связей между компонентами/файлами """
