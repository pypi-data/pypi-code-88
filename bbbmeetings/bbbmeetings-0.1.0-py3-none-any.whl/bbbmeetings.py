#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from typing import NewType, Optional, Tuple, Iterable, List
from collections import OrderedDict
from datetime import datetime, timedelta
import hashlib
import requests
import xmltodict

from bbbmeetings.classes import BBBServers, BBBServer

