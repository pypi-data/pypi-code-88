#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Описание констант, использующихся в PPL.
"""

# коды различных типов модулей
MULTISPHERE_ID = 500
GRAPH_ID = 600
MAP_ID = 700
ASSOCIATION_RULES_ID = 800
CLUSTERING_ID = 900
FORECAST_ID = 1000

# маппинг "код модуля - наименование модуля"
CODE_NAME_MAP = {
    MULTISPHERE_ID: 'Мультисфера',
    GRAPH_ID: 'Графика',
    MAP_ID: 'Карты',
    ASSOCIATION_RULES_ID: 'Ассоциативные правила',
    CLUSTERING_ID: 'Кластеризация',
    FORECAST_ID: 'Прогнозирование'
}

# соответствие типов, используемых Полиматикой, с типами данных Python Core
TYPES_MAP = {
    'uint8': 'integer',
    'uint16': 'integer',
    'uint32': 'integer',
    'uint64': 'integer',
    'double': 'float',
    'string': 'string',
    'date': 'date',
    'time': 'time',
    'datetime': 'datetime',
    'date_year': 'integer',
    'date_quarter': 'integer',
    'date_month': 'string',
    'date_day': 'integer',
    'date_week': 'integer',
    'date_wday': 'string',
    'time_hour': 'integer',
    'time_minute': 'integer',
    'time_second': 'integer'
}

