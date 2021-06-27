from __future__ import annotations

import functools
import typing as _T
from copy import copy

from rocshelf import compile
from rocshelf import exception as ex
from rocshelf.components.routes import GetRoute


def main(targetFunc: _T.Callable,
         addTraceBackFun: _T.Callable[[ex.rExError, list[_T.Any], dict[str, _T.Any]], _T.Optional[ex.rExError]]
         ) -> _T.Any:
    """ Основной метод для добавления уровня трейсбека.

    Args:
        targetFunc (_T.Callable): Оборачиваямая функция
        addTraceBackFun (_T.Callable[[ex.rExError, list[_T.Any], dict[str, _T.Any]], _T.Optional[ex.rExError]]):
        Функция в которую передается ошибка и параметры вызова функции.

    Returns:
        _T.Any: Результат функции targetFunc

    """

    @functools.wraps(targetFunc)
    def wrapper(*args, **kwargs):
        try:
            return targetFunc(*args, **kwargs)

        except ex.rExError as exError:
            newError = addTraceBackFun(copy(exError), *args, **kwargs)
            if newError is None:
                raise exError
            raise newError

    return wrapper


def stage_run(func: _T.Callable) -> _T.Callable:
    def __add(exError: ex.rExError):
        exError.append_traceback(
            ex.ex.traceback.TextTracebackStage(
                'Стадия компиляции',
                'Запуск компиляции'
            )
        )
        raise exError
    return main(func, __add)


def stage_localization(func: _T.Callable) -> _T.Callable:
    def __add(exError: ex.rExError, someSelf: compile.routes.CompileLocalization, *args, **kwargs):
        exError.append_traceback(
            ex.ex.traceback.TextTracebackStage(
                'Параметры компиляции.',
                'Используемая локализация: "{0}"'.format(
                    someSelf.localizationName
                )
            )
        )
        raise exError
    return main(func, __add)


def stage_pre_analyze(func: _T.Callable):
    def __add(exError: ex.rExError, *args, **kwargs):
        exError.append_traceback(
            ex.ex.traceback.TextTracebackStage(
                'Стадия компиляции',
                'Преанализ шаблонов, которые будут задействованы в компиляции'
            )
        )
        raise exError
    return main(func, __add)


def stage_route_processing(func: _T.Callable):
    def __add(exError: ex.rExError, someSelf: compile.routes.CompileRoute, *args, **kwargs):
        route = GetRoute.route(someSelf.routeKey)
        raise exError.append_traceback(
            ex.ex.traceback.ConfigTracebackStage(['route'] + someSelf.routeKey.split('.'), route.page)
        )
    return main(func, __add)


def stage_route_compile(func: _T.Callable):
    return stage_route_processing(func)
