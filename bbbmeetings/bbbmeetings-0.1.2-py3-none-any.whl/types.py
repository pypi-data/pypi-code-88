#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from typing import NewType, Optional, Tuple, Iterable, List
from collections import OrderedDict

Secret = NewType('Secret', str)
Url    = NewType('Url', str)
UnparsedResponse    = NewType('UnparsedResponse', OrderedDict)
CheckedResponse    = NewType('CheckedResponse', OrderedDict)