""" Модуль работы с маршрутизацией

"""
from __future__ import annotations
import re
import typing as _T
from copy import deepcopy

from rcore import utils
import rlogging
from rcore.rpath import rPath
from rcore.utils import rDict
from rocshelf import exception as ex
from rocshelf.config import pcf

from . import shelves

logger = rlogging.get_logger('mainLogger')

saveRoutesFileName = 'rocshelf-routes.json'

routes: dict[str, RouteItem] = {}

re_route_name = re.compile(r'^(?P<route>[\w]+(\.[\w]+)*)$')


def check_name_route(route: str):
    """ Проверка валидности идентификатора маршрута """

    if re_route_name.match(route) is None:
        raise ValueError('"{}" - novalid route name'.format(
            route
        ))


class RouteItem(object):
    """ Маршрут """

    page: str
    localVars: dict[_T.Any, _T.Any]

    def __init__(self, shelfPageName: str, localVars: dict[_T.Any, _T.Any]) -> None:
        self.page = shelfPageName
        self.localVars = localVars

    @classmethod
    def from_dict(cls, routeInfo: dict[str, _T.Any]) -> RouteItem:
        """ Создание экземпляра класса из информации в виде словаря

        Args:
            routeInfo (dict[str, _T.Any]): Информация о маршруте

        Returns:
            [type]: [description]

        """

        return cls(routeInfo['page'], routeInfo['data'])


class GetRoute(object):
    """ Выборка маршрутов """

    @staticmethod
    def all() -> dict[str, RouteItem]:
        """ Выборка всех маршрутов """

        return routes

    @staticmethod
    def route(routeKey: str) -> RouteItem:
        """ Выборка маршрута """

        return routes[routeKey]

    @staticmethod
    def walk() -> _T.Generator[tuple[str, RouteItem], None, None]:
        for routeKey, route in routes.items():
            yield (routeKey, route)


def _transformation_routes_config(importRoutes: dict):
    """ Преобразование дерева маршрутов из конфигурации в одномерный массив """

    callback_keys = {
        'page': lambda cb, val, *args, **kwargs: val,
        'data': lambda cb, val, *args, **kwargs: val,
        'common': lambda cb, val, *args, **kwargs: val,
    }

    def cb_key(key: _T.Union[str, tuple]) -> str:
        if isinstance(key, tuple):
            return '{0}.{1}'.format(
                key[0], key[1]
            )

        return key

    def callback(cb_core: _T.Callable, attend: dict[str, _T.Union[str, dict]]) -> dict:
        attend = cb_core(attend)

        noRec: dict[str, _T.Union[str, dict, bool]] = {'common': False, 'page': False, 'data': {}}
        for i in noRec:
            try:
                noRec[i] = attend[i]
                del attend[i]
                if i != 'data' and not isinstance(noRec[i], str):
                    raise TypeError(f'The value for the "{i}" name must be a string')
            except KeyError:
                pass

        fr = noRec['common']
        del noRec['common']

        for k in attend:
            if fr:
                if attend[k]['page'] == '.':
                    attend[k]['page'] = fr

                else:
                    attend[k]['page'] = fr + '.' + attend[k]['page']

            if 'data' in attend[k]:
                pageVars = deepcopy(noRec['data'])
                mergedPageVars = rDict(pageVars).merge(attend[k]['data'], True)
                attend[k]['data'] = mergedPageVars.attend

        if noRec['page']:
            if fr:
                if noRec['page'] == '.':
                    noRec['page'] = fr

                else:
                    noRec['page'] = fr + '.' + noRec['page']

            attend['__value__'] = noRec

        return attend

    processedRoutes = utils.rRecursion(importRoutes).core(callback, cb_key, CB_to_keys=callback_keys)

    # Удаление пустых маршрутов
    processedRoutes = {routeKey: processedRoutes[routeKey] for routeKey in processedRoutes if processedRoutes[routeKey]}

    return processedRoutes


class InitComponentCore(object):
    """ Класс с основными функциями для инициализации компонента шелфов """

    routesDict: dict[str, dict]

    def __init__(self) -> None:
        logger.info('Инициализация класса инициализации компонента маршрутов')

        global routes
        routes = {}

        self.routesDict = {}


class InitComponent(InitComponentCore):
    """ Класс инициализации компонента шелфов """

    def parse(self):
        """ Сбор всех маршрутов.

        Перебирает и сохраняет маршруты из конфигурации

        """

        # Инициализация маршрутов из конфигурации path -> import -> (page, wrapper, tag, block)
        logger.debug('Инициализация маршрутов из конфигурации')
        processedRoutes = _transformation_routes_config(pcf.get(['route']))
        self.routesDict.update(processedRoutes)

    def construct(self):
        """ Создание объектов маршрутов из сырых словарей """

        for routeKey, routeInfo in self.routesDict.items():
            routes[routeKey] = RouteItem.from_dict(routeInfo)

    def check(self):
        """ Проверка валидности маршрутов"""

        for routeKey, route in routes.items():
            check_name_route(routeKey)

            if route.page not in shelves.GetShelf.types('page'):
                raise ValueError('Для маршурта "{0}" не инициализирован шелф-page "{1}"'.format(
                    routeKey,
                    shelves.ShelfItem.slug('page', route.page)
                ))

    def save_cache(self):
        """ Сохранение полезой информации о маршрутах в кеш """

        rPath(saveRoutesFileName, fromPath='cache').dump(self.routesDict)

    @classmethod
    def all_stages(cls):
        """ Прохождение всех этапов инициализации компонента шелфов """

        initObject = cls()

        logger.info('Инициализации компонента шелфов через функцию прохода по всем этапам')

        initObject.parse()
        initObject.construct()
        initObject.check()
        initObject.save_cache()

        logger.info('Инициализированно {0} маршрутов'.format(
            utils.len_generator(GetRoute.walk())
        ))
        logger.info('Результат: "{0}"'.format(
            rPath(saveRoutesFileName, fromPath='cache')
        ))

        return initObject
