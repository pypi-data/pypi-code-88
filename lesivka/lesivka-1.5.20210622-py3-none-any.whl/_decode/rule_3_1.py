# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from itertools import product

from ..utils import replacer

AFTER = 'BVHGDZKLMNPRSTFXC' + 'ŽČŠ'
BEFORE = 'AEIU'

convert = replacer({
    x + y + z: x + "'" + y + z for x, y, z in
    product(AFTER + AFTER.lower(), 'Jj', BEFORE + BEFORE.lower())
})
