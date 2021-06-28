# !/usr/bin/env python
# coding: utf-8
# version: 1.0
# author: Fennel
# contact: gongkangjia@gmail.com
# date: 2021/5/29

import re
from collections import defaultdict

with open("namelist.wps") as f:
    nl = f.readlines()

data = defaultdict(dict)
i = 0
while True:
    print(i)
    line = nl[i]
    li = re.sub(r"\s+", "", line)
    if not li or li.startswith("!"):
        i += 1
        continue
    if li.startswith("&"):
        section = li[1:]
        i+=1
        continue

    if "=" in li:
        data[section][k]=v
        k, v = li.split("=")
    else:
        v+=v
    i+=1