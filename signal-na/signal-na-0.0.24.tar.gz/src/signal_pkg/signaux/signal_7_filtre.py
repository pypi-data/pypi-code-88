#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 15:43:58 2019

@author: nicolas
"""
import time

import os, sys
import numpy as np
import matplotlib.pyplot as plt


sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))

from base.axe_x_base import AxeXBase
from signaux.signal_6_sysam import Signal6Sysam
from base.filtrage_base import calculer_sortie_filtre
from plot.plot_base import tracer
 
__all__ = ["SignalSysam"]



class Signal7Filtre(Signal6Sysam):
    def filtrer(self, filtre):
        return calculer_sortie_filtre(filtre, self)

if __name__ == "__main__":
    class Test():
        def __init__(self):
            self._FiltreBase__fonction_H = lambda f: 1/(1+1j*f/1e2)
        def __calculer_H(self, f):
            return self._FiltreBase__fonction_H(f)

        def lire_nom(self):
            return "filtre"

    fil = Test()
    bdt = AxeXBase([0, 1], 1e-6)
    vt = bdt.lire_vecteur_x()
    ve = np.sin(2*np.pi*1e2*vt)
    e = Signal7Filtre(bdt, ve)
    s = e.filtrer(fil)
    tracer(e, s)
    pass