#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Содержит набор вспомогательных классов и функций, использующихся в PPL.
"""

import logging
import time
from datetime import date, datetime
from typing import Any, Union
from .consts import TYPES_MAP
from ..exceptions import *


class TypeConverter():
    """
    Реализация преобразования типов, определённых Полиматикой, к Python-типам.
    """
    def __init__(self, sc: 'BusinessLogic'):
        """
        Конструктор класса.
        :param sc: экземпляр класса BusinessLogic.
        """
        self.sc = sc
        self.datetime_format = self._get_current_datetime_format()

    def _get_current_datetime_format(self) -> str:
        """
        Получить из текущих настроек системы Полиматики формат хранения даты-времени.
        :return: (str) формат даты-времени в виде масок.
        """
        config_data = self.sc.execute_manager_command(command_name='user_iface', state='get_configuration')
        return self.sc.h.parse_result(config_data, 'configuration', 'datetime_format')

    def _convert_to_int(self, value: Any) -> Union[int, Any]:
        """
        Преобразование исходных данных в целочисленный тип.
        Если преобразование не удалось - вернутся данные в исходном виде.
        :param value: (Any) исходные данные.
        :return: (int) исходные данные в целочисленном типе.
        """
        try:
            result = int(value)
        except ValueError:
            result = value
        return result

    def _convert_to_float(self, value: Any) -> Union[float, Any]:
        """
        Преобразование исходных данных в тип дробных чисел.
        Если преобразование не удалось - вернутся данные в исходном виде.
        :param value: (Any) исходные данные.
        :return: (float) исходные данные в виде дробного числа.
        """
        try:
            result = float(value)
        except ValueError:
            result = value
        return result

    def _convert_to_string(self, value: Any) -> Union[str, Any]:
        """
        Преобразование исходных данных в строковый тип.
        Если преобразование не удалось - вернутся данные в исходном виде.
        :param value: (Any) исходные данные.
        :return: (float) исходные данные в строковом типе.
        """
        try:
            result = str(value)
        except ValueError:
            result = value
        return result

    def _convert_to_date(self, value: Any) -> Union[date, Any]:
        """
        Преобразование исходных данных в формат даты.
        Если преобразование не удалось - вернутся данные в исходном виде.
        :param value: (Any) исходные данные.
        :return: (int) исходные данные в формате даты.
        """
        # немного костыльный способ, но пока ничего лучше не придумал; если упадёт где-нибудь - будем разбираться
        date_format = self.datetime_format.split(' ')[0]
        try:
            result = datetime.strptime(value, date_format).date()
        except ValueError:
            result = value
        return result

    def _convert_to_time(self, value: Any) -> Union['time', Any]:
        """
        Преобразование исходных данных в формат времени.
        Если преобразование не удалось - вернутся данные в исходном виде.
        :param value: (Any) исходные данные.
        :return: (int) исходные данные в формате времени.
        """
        # немного костыльный способ, но пока ничего лучше не придумал; если упадёт где-нибудь - будем разбираться
        time_format = self.datetime_format.split(' ')[1]
        try:
            result = datetime.strptime(value, time_format).time()
        except ValueError:
            result = value
        return result

    def _convert_to_datetime(self, value: Any) -> Union[datetime, Any]:
        """
        Преобразование исходных данных в формат дата-время.
        Если преобразование не удалось - вернутся данные в исходном виде.
        :param value: (Any) исходные данные.
        :return: (int) исходные данные в формате дата-время.
        """
        try:
            result = datetime.strptime(value, self.datetime_format)
        except ValueError:
            result = value
        return result

    def convert_data_types(self, types: list, data: list) -> list:
        """
        Непосредственно функция преобразования типов, определённых Полиматикой, к Python-типам.
        :param types: (list) список используемых типов.
        :param data: (list) набор начальных данных.
        :return: (list) начальные данные, преобразованные к нужному типу.
        """
        convert_funcs_map = {
            'integer': self._convert_to_int,
            'float': self._convert_to_float,
            'string': self._convert_to_string,
            'date': self._convert_to_date,
            'time': self._convert_to_time,
            'datetime': self._convert_to_datetime
        }

        # по идее, в нормальной ситуации длина списков должна совпадать (длина списка типов равна количеству колонок, а
        # количество колонок должно совпадать с количеством данных); поэтому, если это не так - сгенерируем ошибку
        if len(types) != len(data):
            exception_func = raise_exception(sc)
            exception_func(
                PolymaticaException, 'Length of column list does not match length of data list!', with_traceback=False)

        # преобразовываем данные
        result = list()
        for item in tuple(zip(data, types)):
            c_func = convert_funcs_map.get(TYPES_MAP.get(item[1]))
            result.append(c_func(item[0]))
        return result


def timing(func):
    """
    Используется как декоратор функций класса BusinessLogic для профилирования времени работы.
    :param func: декорируемая функция.
    """
    def timing_wrap(self, *args, **kwargs):
        """
        Непосредственно функция-декоратор.
        :param self: экземпляр класса BusinessLogic.
        """
        self.func_name = func.__name__
        try:
            logging.info('Exec func "{}"'.format(self.func_name))
            start_time = time.time()
            result = func(self, *args, **kwargs)
            end_time = time.time()
            self.func_timing = 'func "{}" exec time: {:.2f} sec'.format(self.func_name, (end_time - start_time))
            logging.info(self.func_timing)
            return result
        except SystemExit:
            logging.critical('Func "{}" failure with SystemExit exception!'.format(self.func_name))
            raise
    return timing_wrap


def raise_exception(bl_instance: 'BusinessLogic'):
    """
    Обёртка над функцией-генератором исключений.
    Сделано для того, чтобы каждый раз не передавать в функцию экземпляр класса "BusinessLogic".
    :param bl_instance: экземпляр класса BusinessLogic.
    """
    def wrap(exception: Exception, message: str, extend_message: str = '', code: int = 0, with_traceback: bool = True):
        """
        Непосредственно функция, генерирующая пользовательские исключения с заданным сообщением.

        :param exception: вид исключения, которое нужно сгенерировать. Например, ValueError, PolymaticaException...
        :param message: сообщение об ошибке.
        :param extend_message: расширенное сообщение об ошибке (не обязательно).
        :param code: код ошибки (не обязательно).
        :param with_traceback: нужно ли показывать traceback ошибки (по-умолчанию True).
        :return: (str) сообщение об ошибке, если работа с API происходит через Jupyter Notebook;
            в противном случае генерируется ошибка.
        """
        bl_instance.current_exception = message

        # записываем сообщение в логи
        # logging.error(msg, exc_info=True) аналогичен вызову logging.exception() - вывод с трассировкой ошибки
        # logging.error(msg, exc_info=False) аналогичен вызову logging.error(msg) - вывод без трассировки ошибки
        logging.error(message, exc_info=with_traceback)
        logging.info("APPLICATION STOPPED")

        # если работа с API происходит через Jupyter Notebook, то выведем просто сообщение об ошибке
        if bl_instance.jupiter:
            return message

        # если текущее исключение является наследником класса PolymaticaException, то генерируем ошибку Полиматики
        if issubclass(exception, PolymaticaException):
            raise exception(message, extend_message, code)

        # прочие (стандартные) исключения, по типу ValueError, IndexError и тд
        raise exception(message)
    return wrap


def log(message: str, level: str = 'info'):
    """
    Запись сообщения в логи.
    :param message: сообщение, записываемое в логи.
    :param level: уровень логирования; возможны варианты: 'debug', 'info', 'warning', 'error', 'critical'.
        По-умолчанию 'info'.
    """
    level = level.lower()
    if level not in ['debug', 'info', 'warning', 'error', 'critical']:
        level = 'info'
    if level == 'debug':
        logging.debug(message)
    elif level == 'info':
        logging.info(message)
    elif level == 'warning':
        logging.warning(message)
    elif level == 'error':
        logging.error(message)
    elif level == 'critical':
        logging.critical(message)
