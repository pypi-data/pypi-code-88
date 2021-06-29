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

from signaux.signal_7_filtre import Signal7Filtre
from base.axe_x_base import AxeXBase

import numpy as np

import matplotlib.pyplot as plt
 
__all__ = []

class SignalComplet(Signal7Filtre):
    pass


if __name__ == "__main__":
    liste_xmin_xmax=[0, 1]
    Xe = 1e-3
    F = 2
    
    bdt = AxeXBase(liste_xmin_xmax, Xe)
    vecteur_x = bdt.lire_vecteur_x()
    vecteur_y = np.cos(2*np.pi*F*vecteur_x)

    s = SignalComplet(bdt, vecteur_y)
    s.configurer_voie("EA0")
    s.tracer()

    print("fin")