# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from ..diacritics import ACUTE
from ..utils import translator

IN, OUT = ACUTE, 'Ь'

convert = translator(IN, OUT.lower())
