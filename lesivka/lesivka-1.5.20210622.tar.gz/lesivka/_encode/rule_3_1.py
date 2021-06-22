# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import re

from ..diacritics import APOSTROPHES


def get_convert():
    pattern = re.compile(r'(\w)[%s](\w)' % APOSTROPHES, re.UNICODE)

    def _(text):
        return ''.join(t for t in pattern.split(text))

    return _


convert = get_convert()
