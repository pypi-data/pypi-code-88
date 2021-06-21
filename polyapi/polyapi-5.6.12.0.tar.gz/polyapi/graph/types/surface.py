#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Реализация графика типа "Поверхность".
"""

from ..base_graph import BaseGraph

class Surface(BaseGraph):
    """
    Реализация графика типа "Поверхность".
    """
    def __init__(self, base_bl: 'BusinessLogic', settings: str, grid: str, labels: dict,
                other: dict, common_params: dict, plot_type: str):
        super().__init__(base_bl, settings, grid, labels, other, common_params, plot_type, -1)

    def _get_settings(self) -> dict:
        return dict()

    def _get_labels_settings(self) -> dict:
        return dict()

    def _get_other_settings(self) -> dict:
        return dict()

    def draw(self):
        """
        Отрисовка графика. Состоит из нескольких этапов:
        1. Проверка данных для текущего типа графика;
        2. Формирование конфигурации графика;
        3. Вызов команды, отрисовывающей график.
        """
        pass

