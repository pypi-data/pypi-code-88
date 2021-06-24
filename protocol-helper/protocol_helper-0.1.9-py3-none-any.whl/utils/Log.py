#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:LeisureMan
# email:LeisureMam@gmail.com
# datetime:2021-06-16 17:22
# software: PyCharm
from loguru import logger as logs
from protocol_helper.setting import RUNTIME
import sys


class Log(object):
    def __init__(self, file_name = 'default') -> None:
        """
        :param file_name: 文件名称
        """
        super(Log).__init__()
        self._logs = logs
        self._file_name = file_name

    def __overload_configuration(self):
        """
        重载配置
        :return:
        """
        self._logs.remove()
        return {
                "handlers": [
                        {
                                "sink":    sys.stdout,
                                "format":  "<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> "
                                           "| <level>{level: <8}</level> | "
                                           "<cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan>"
                                           " - <level>{message}</level>",
                                "enqueue": True,
                                'catch':   True,
                        },
                        {
                                "sink":     RUNTIME + "/{time:YYYY}{time:MM}/{time:DD}/" + self._file_name + "_{"
                                                                                                             "time:DD"
                                                                                                             "}.log",
                                "enqueue":  True,
                                'catch':    True,
                                'rotation': '200MB',
                                'mode':     'a',
                                'encoding': 'utf-8',
                        },
                ],

                "extra":    {"user": "someone"}
        }

    def success(self, _msg):
        self._logs.configure(**self.__overload_configuration())
        self._logs.success(_msg)

    def warning(self, _msg):
        self._logs.configure(**self.__overload_configuration())
        self._logs.warning(_msg)

    def info(self, _msg):
        self._logs.configure(**self.__overload_configuration())
        self._logs.info(_msg)

    def debug(self, _msg):
        self._logs.configure(**self.__overload_configuration())
        self._logs.debug(_msg)

    def error(self, _msg):
        self._logs.configure(**self.__overload_configuration())
        self._logs.error(_msg)

    def exception(self, _msg):
        self._logs.configure(**self.__overload_configuration())
        self._logs.exception(_msg)


log = Log()
