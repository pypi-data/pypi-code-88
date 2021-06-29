import numpy as np
import copy

import os, sys

from numpy.core.numeric import convolve
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))

import base.constantes_base as cst

class AxeBase():

    def __init__(self, nom = "t", unite = "s"):
        self.nom = nom
        self.unite = unite

    def cloner(self, other):
        self.nom = other.nom
        self.unite = other.unite

    def __str__(self):
        return self.nom + ", " + self.unite
if __name__ == "__main__":
    a = AxeBase()

    print(a)

