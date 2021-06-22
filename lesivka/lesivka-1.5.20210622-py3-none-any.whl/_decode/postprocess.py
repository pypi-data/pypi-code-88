# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from ..utils import replacer

EXCLUDES = {
    "БАТЮЩИН": "БАТЮШЧИН",
    "ПЛЯЩИН": "ПЛЯШЧИН",
    "ПОДУЩАН": "ПОДУШЧАН",
    "ШАРАЩИН": "ШАРАШЧИН",
    "МЕЛАЩИН": "МЕЛАШЧИН",
}


def get_convert():
    data = EXCLUDES.copy()
    data.update({i.title(): o.title() for i, o in EXCLUDES.items()})
    data.update({i.lower(): o.lower() for i, o in EXCLUDES.items()})

    return replacer(data)


convert = get_convert()
