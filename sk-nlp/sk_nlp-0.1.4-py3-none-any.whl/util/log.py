# -*- coding: utf-8 -*-
"""
日志打印
"""

import os
import sys
current_dir = os.path.dirname(__file__)
sys.path.append(current_dir)

import logging.config
from logging import LogRecord
from sk_nlp.util import file_conf

LOG_LEVEL = logging.INFO
# 通常用于Linux系统下，使控制台输出的日志带颜色
class ColorFormatter(logging.Formatter):
    log_colors = {
        'CRITICAL': '\033[0;31m',
        'ERROR': '\033[0;33m',
        'WARNING': '\033[0;35m',
        'INFO': '\033[0;32m',
        'DEBUG': '\033[0;00m',
    }

    def format(self, record: LogRecord):
        s = super().format(record)
        level_name = record.levelname
        if level_name in self.log_colors:
            return self.log_colors[level_name] + s + '\033[0m'
        return s

LOGGER = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'color': {
            'class': 'log.ColorFormatter',
            'format': '%(asctime)s [%(name)s] %(levelname)s: %(message)s'
        },
        'default': {
            'class': 'logging.Formatter',
            'format': '%(message)s'
        }
    },
    'handlers': {
        'console': {
            'level': LOG_LEVEL,
            'class': 'logging.StreamHandler',
            'formatter': 'color',
        },
        'machine_learning': {
            'level': LOG_LEVEL,
            'class': 'logging.handlers.RotatingFileHandler',
            'backupCount': 5,
            'maxBytes': 10*1024*1024,
            'formatter': 'color',
            'filename': file_conf.log_file_path,
            'encoding': 'utf-8',
        },
    },
    'loggers': {
        'ml': {
            'handlers': ['machine_learning', 'console'],
            'level': LOG_LEVEL,
        },
    }
}

logging.config.dictConfig(LOGGER)
logger = logging.getLogger('ml')


