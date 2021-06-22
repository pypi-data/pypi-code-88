# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from ..ascii import asciilator
from ..diacritics import ACUTE, APOSTROPHES
from ..utils import Converter, applier
from . import (
    postprocess,
    rule_1_1,
    rule_1_2,
    rule_1_3,
    rule_1_4,
    rule_1_5,
    rule_1_7,
    rule_2_2,
    rule_3_1,
    rule_3_2,
)

ORDER = (
    rule_2_2,
    rule_3_2,
    rule_1_1,
    rule_1_2,
    rule_1_3,
    rule_1_4,
    rule_1_5,
    rule_1_7,
    rule_3_1,
    postprocess,
)

CYR = 'АБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯ' + ACUTE + APOSTROPHES


def get_encode():
    def _(text, no_diacritics=False):
        converters = [rule.convert for rule in ORDER]
        converters_ascii = converters + [asciilator]

        convert = applier(*converters)
        convert_acsii = applier(*converters_ascii)

        split = r"([^\w%s]+)" % (ACUTE + APOSTROPHES)

        converter = Converter(split, CYR, convert)
        converter_ascii = Converter(split, CYR, convert_acsii)

        return (converter_ascii if no_diacritics else converter)(text)

    return _


encode = get_encode()

del get_encode
