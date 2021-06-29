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

import base.constantes_base as cst
import base.utiles_base as utb
from base.axe_x_base import AxeXBase
from signaux.signal_complet import SignalComplet

__all__ = ["SignalSinus"]

def generer_portion_sinus(axe_x_base, F, phi, tr):
    vecteur_x = axe_x_base.lire_vecteur_x()
    return np.cos(2*np.pi*F*(vecteur_x-tr)+phi)


class SignalSinus(SignalComplet):
    def __init__(self, F = cst.F, Vpp = cst.Vpp, offset = 0, phi = 0, tr = 0, liste_tmin_tmax = cst.liste_xmin_xmax, Te = cst.Xe, nom = ""):
        T = 1/F
        axe_x_base = AxeXBase(liste_tmin_tmax, Te)
        vecteur_y = generer_portion_sinus(axe_x_base, F, phi, tr)*0.5*Vpp+offset
        SignalComplet.__init__(self, axe_x_base, vecteur_y, nom)
        base_mesures = self._Signal3Mesure__lire_mesure_base()
        base_mesures.T_th = 1/F

if __name__ == "__main__":
    s1 = SignalSinus()
    s1.tracer()

    print("fin")