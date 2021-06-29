# -*- coding: utf-8 -*-
"""
Created on Mon Jul 31 14:16:33 2017

@author: Piotr Zioło
"""


def dict_apply(d, f):
    return {key: f(value) for key, value in d.items()}


if __name__ == "__main__":
    import random

    dim1 = 3
    dim2 = 2
    dim3 = 2

    d = {}
    for i in range(dim1):
        for j in range(dim2):
            for k in range(dim3):
                d[(i, j, k)] = random.randint(1, 10)


    def f(x):
        return x**2


    print(d)
    print(dict_apply(d, f))
