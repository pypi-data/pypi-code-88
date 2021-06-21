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

__all__ = ["SignalSinus"]

def generer_portion_sinus(base_de_temps, F, phi, tr):
    vecteur_t = base_de_temps.calculer_vecteur_t()
    return np.cos(2*np.pi*F*(vecteur_t-tr)+phi)


class SignalSinus(SignalComplet):
    def __init__(self, F = cst.F, Vpp = cst.Vpp, offset = 0, phi = 0, tr = 0, liste_tmin_tmax = cst.liste_tmin_tmax, Te = cst.Te, nom = ""):
        T = 1/F
        tmin, tmax = liste_tmin_tmax
        if T < tmax - tmin:        
            base_de_temps_periode = TempsBase([0, 1/F], Te)
            vecteur_signal_periode = (generer_portion_sinus(base_de_temps_periode, F, phi, tr)-0.5)*Vpp+offset
            base_de_temps = TempsBase(liste_tmin_tmax, Te)
            Nsignal = base_de_temps.calculer_N()
            SignalComplet.__init__(self, base_de_temps, utb.periodiser(Nsignal, vecteur_signal_periode), nom)
        else:
            base_de_temps = TempsBase(liste_tmin_tmax, Te)
            vecteur_signal = (generer_portion_sinus(base_de_temps, F, phi, tr)-0.5)*Vpp+offset
            SignalComplet.__init__(self, base_de_temps, vecteur_signal, nom)

        base_mesures = self.lire_base_mesures()
        base_mesures.T_th = 1/F

if __name__ == "__main__":
    s1 = SignalSinus()
    s1.plot()
    plt.legend()
    plt.show()

    print("fin")