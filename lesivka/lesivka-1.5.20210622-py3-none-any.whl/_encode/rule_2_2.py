# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from itertools import product

from ..diacritics import ACUTE
from ..utils import applier, replacer, translator

IN, OUT = "ЄЇЮЯ", "EIUA"
AFTER = "БВГҐДЖЗКЛМНПРСТФХЦЧШЩ"

TRANSLATE = {
    'Є': 'JE',
    "Ї": "JI",  # rule_1_6
    'Ю': 'JU',
    'Я': 'JA',
}


def get_step1():
    data = {c + i: c + ACUTE + o for c, (i, o) in
            product(AFTER + AFTER.lower(),
                    zip(IN + IN.lower(), OUT + OUT.lower()))}
    return replacer(data)


def get_step2():
    data = TRANSLATE.copy()
    data.update({i.lower(): o.lower() for i, o in TRANSLATE.items()})
    return translator(data)


convert = applier(get_step1(), get_step2())
