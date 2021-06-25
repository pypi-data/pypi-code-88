
import typing as _T

import rocshelf

from django.conf import settings
from django.template.backends.django import DjangoTemplates


class RocshelfTemplates(DjangoTemplates):
    """ Надстройка над модулем django.template.backends.django.DjangoTemplates

    Для корректной работы формирования путей шаблонов

    """

    def __init__(self, params: dict[str, _T.Any]) -> None:
        super().__init__(params)

        self.engine.dirs = [
            rocshelf.UIIntegration.path('template')
        ]
