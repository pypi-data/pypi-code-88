# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 14:16:19 2017

@author: Piotr Zioło
"""


def are_lists_equal(list1, list2):
    list1 = list(list1)
    list2 = list(list2)
    return len(list1) == len(list2) and sorted(list1) == sorted(list2)
