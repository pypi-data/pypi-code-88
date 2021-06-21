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
from base.temps_base import TempsBase
from signaux.signal_complet import SignalComplet

__all__ = ["SignalTriangle"]


def generer_portion_fourier(base_de_temps, F, liste_an, liste_bn):

    vecteur_t = base_de_temps.calculer_vecteur_t()
    N = base_de_temps.calculer_N()

    a0 = 0
    if len(liste_an)>0:
        a0 = liste_an[0]

    vecteur_signal = a0*np.ones(N)

    for i in range(1, len(liste_an)):
        vecteur_signal += liste_an[i]*np.cos(2*np.pi*i*F*vecteur_t)
    for i in range(1, len(liste_bn)):
        vecteur_signal += liste_bn[i]*np.sin(2*np.pi*i*F*vecteur_t)

    return vecteur_signal


class SignalFourier(SignalComplet):
    def __init__(self, F = cst.F, liste_an = cst.liste_an, liste_bn = cst.liste_bn, liste_tmin_tmax = cst.liste_tmin_tmax, Te = cst.Te, nom = ""):
        T = 1/F
        tmin, tmax = liste_tmin_tmax
        if T < tmax - tmin:        
            base_de_temps_periode = TempsBase([0, 1/F], Te)
            vecteur_signal_periode = generer_portion_fourier(base_de_temps_periode, F, liste_an, liste_bn)
            base_de_temps = TempsBase(liste_tmin_tmax, Te)
            Nsignal = base_de_temps.calculer_N()
            SignalComplet.__init__(self, base_de_temps, utb.periodiser(Nsignal, vecteur_signal_periode), nom)
        else:
            base_de_temps = TempsBase(liste_tmin_tmax, Te)
            vecteur_signal = generer_portion_fourier(base_de_temps, F, liste_an, liste_bn)
            SignalComplet.__init__(self, base_de_temps, vecteur_signal, nom)

        base_mesures = self.lire_base_mesures()
        base_mesures.T_th = 1/F

if __name__ == "__main__":
    s1 = SignalFourier(2e2, [1, 2, 3], [0, 1])
    s1.plot()
    plt.legend()
    plt.show()

    print("fin")
