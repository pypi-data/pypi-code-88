#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 15:43:58 2019

@author: nicolas
"""
import time

import os, sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))

import base.constantes_base as cst

from signaux.signal_6_sysam import Signal6Sysam
from base.temps_base import TempsBase

import numpy as np

import matplotlib.pyplot as plt
 
__all__ = []

class SignalComplet(Signal6Sysam):
    pass


if __name__ == "__main__":
    liste_tmin_tmax=[0, 1]
    Te = 1e-3
    F = 2
    
    bdt = TempsBase(liste_tmin_tmax, Te)
    vecteur_t = bdt.calculer_vecteur_t()
    vecteur_signal = np.cos(2*np.pi*F*vecteur_t)

    s = SignalComplet(bdt, vecteur_signal)
    s.configurer_voie("EA0")
    s.plot("r", label = "zorro")
    plt.legend()
    plt.show()

    print("fin")