# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from ..diacritics import ACUTE
from ..utils import translator

IN, OUT = 'Ь', ACUTE

convert = translator(IN + IN.lower(), OUT * 2)
