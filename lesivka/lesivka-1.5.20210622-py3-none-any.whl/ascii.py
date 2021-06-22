# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from .diacritics import ACUTE
from .utils import replacer, translator

TRANSLATE = {
    ACUTE: "'",
    "Č": "CW",
    "Š": "SW",
    "Ž": "ZW",
    "Đ": "DQ",
    "Ƶ": "ZQ",
}


def get_asciilator():
    data = TRANSLATE.copy()
    data.update({i.lower(): o.lower() for i, o in TRANSLATE.items()})

    return translator(data)


def get_deasciilator():
    replace = {v: k for k, v in TRANSLATE.items()}

    data = replace.copy()
    data.update({i.title(): o for i, o in replace.items()})
    data.update({i.lower(): o.lower() for i, o in replace.items()})

    return replacer(data)


asciilator = get_asciilator()
deasciilator = get_deasciilator()

del get_asciilator
del get_deasciilator
