# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from ..diacritics import ACUTE

convert = lambda text: text.lstrip(ACUTE)
