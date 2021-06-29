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

__all__ = ["SignalTriangle"]


def generer_portion_fourier(axe_x_base, F, liste_an, liste_bn):

    vecteur_x = axe_x_base.lire_vecteur_x()
    N = axe_x_base.lire_N()

    a0 = 0
    if len(liste_an)>0:
        a0 = liste_an[0]

    vecteur_y = a0*np.ones(N)

    for i in range(1, len(liste_an)):
        vecteur_y += liste_an[i]*np.cos(2*np.pi*i*F*vecteur_x)
    for i in range(1, len(liste_bn)):
        vecteur_y += liste_bn[i]*np.sin(2*np.pi*i*F*vecteur_x)

    return vecteur_y


class SignalFourier(SignalComplet):
    def __init__(self, F = cst.F, liste_an = cst.liste_an, liste_bn = cst.liste_bn, liste_tmin_tmax = cst.liste_xmin_xmax, Te = cst.Xe, nom = ""):
        T = 1/F
        xmin, xmax = liste_tmin_tmax
        if T < xmax - xmin:        
            axe_x_base_periode = AxeXBase([0, 1/F], Te)
            vecteur_y_periode = generer_portion_fourier(axe_x_base_periode, F, liste_an, liste_bn)
            axe_x_base = AxeXBase(liste_tmin_tmax, Te)
            Nsignal = axe_x_base.lire_N()
            SignalComplet.__init__(self, axe_x_base, utb.periodiser(Nsignal, vecteur_y_periode), nom)
        else:
            axe_x_base = AxeXBase(liste_tmin_tmax, Te)
            vecteur_y = generer_portion_fourier(axe_x_base, F, liste_an, liste_bn)
            SignalComplet.__init__(self, axe_x_base, vecteur_y, nom)

        base_mesures = self._Signal3Mesure__lire_mesure_base()
        base_mesures.T_th = 1/F

if __name__ == "__main__":
    s1 = SignalFourier(2e2, [1, 2, 3], [0, 1])
    s1.tracer()
    print("fin")
