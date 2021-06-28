# !/usr/bin/env python
# coding: utf-8
# version: 1.0
# author: Fennel
# contact: gongkangjia@gmail.com
# date: 2021/5/13


class Mydict(dict):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __getitem__(self, item):
        print(item)
        return super().__getitem__(item)


d = Mydict(name="kjgong")
print(d)
print(d["name"])