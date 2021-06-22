# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from ..ascii import deasciilator
from ..diacritics import ACUTE, APOSTROPHES, CARON
from ..utils import Converter, applier
from . import (
    postprocess,
    preprocess,
    rule_1_1,
    rule_1_2,
    rule_1_3,
    rule_1_4,
    rule_1_5,
    rule_1_6,
    rule_1_7,
    rule_2_2,
    rule_3_1,
    rule_3_2,
)

ORDER = (
    preprocess,
    rule_3_1,
    rule_2_2,
    rule_1_6,
    rule_1_7,
    rule_1_1,
    rule_1_2,
    rule_1_3,
    rule_1_4,
    rule_1_5,
    rule_3_2,
    postprocess,
)

LAT = "ABCČDĐEFGHIJKLMNOPRSŠTUVXYZŽƵ" + ACUTE + CARON + "ĆĹŃŔŚŹǴḰḾṔ"


def get_decode():
    def _(text, no_diacritics=False):
        converters = [rule.convert for rule in ORDER]
        converters_ascii = [deasciilator] + converters

        convert = applier(*converters)
        convert_acsii = applier(*converters_ascii)

        split = r"([^\w%s]+)" % (ACUTE + CARON)
        split_ascii = r"([^\w%s]+)" % (ACUTE + CARON + APOSTROPHES)

        converter = Converter(split, LAT, convert)
        converter_ascii = Converter(split_ascii, LAT + "QW'", convert_acsii)

        return (converter_ascii if no_diacritics else converter)(text)

    return _


decode = get_decode()

del get_decode
