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

__all__ = ["SignalCarre"]

def generer_portion_carre(base_de_temps, F, alpha, tr):
    tmin, tmax = base_de_temps.calculer_liste_tmin_tmax()
    n = int(np.floor((tmin-tr)*F))

    t0 = n/F+tr
    t1 = t0 + alpha/F
    t2 = t0 + 1/F
    t3 = t0 + (1+alpha)/F

    if tmin < t1:
        # On commence par un état haut
        ned = base_de_temps._TempsBase__convertir_ia_vers_ie(base_de_temps._TempsBase__convertir_t_vers_ia(tmin))
        if tmax < t1:
            # Et c'est tout
            nef = base_de_temps._TempsBase__convertir_ia_vers_ie(base_de_temps._TempsBase__convertir_t_vers_ia(tmax))
            vecteur_signal = np.ones(nef-ned)
        else:
            # On poursuit par un état bas
            nef = base_de_temps._TempsBase__convertir_ia_vers_ie(base_de_temps._TempsBase__convertir_t_vers_ia(t1))
            vecteur_signal = np.ones(nef-ned)
            ned = nef
            if tmax < t2:
                # Et c'est tout
                nef = base_de_temps._TempsBase__convertir_ia_vers_ie(base_de_temps._TempsBase__convertir_t_vers_ia(tmax))
                vecteur_signal = np.concatenate([vecteur_signal, np.zeros(nef-ned)])
            else:
                # On poursuit par un état haut
                nef = base_de_temps._TempsBase__convertir_ia_vers_ie(base_de_temps._TempsBase__convertir_t_vers_ia(t2))
                vecteur_signal = np.concatenate([vecteur_signal, np.zeros(nef-ned)])
                ned = nef
                nef = base_de_temps._TempsBase__convertir_ia_vers_ie(base_de_temps._TempsBase__convertir_t_vers_ia(tmax))
                vecteur_signal = np.concatenate([vecteur_signal, np.ones(nef-ned)])
    else:
        # On commence par un état bas
        ned = base_de_temps._TempsBase__convertir_ia_vers_ie(base_de_temps._TempsBase__convertir_t_vers_ia(tmin))
        if tmax < t2:
            # Et c'est tout
            nef = base_de_temps._TempsBase__convertir_ia_vers_ie(base_de_temps._TempsBase__convertir_t_vers_ia(tmax))
            vecteur_signal = np.zeros(nef-ned)
        else:
            # On poursuit par un état haut
            nef = base_de_temps._TempsBase__convertir_ia_vers_ie(base_de_temps._TempsBase__convertir_t_vers_ia(t2))
            vecteur_signal = np.zeros(nef-ned)
            ned = nef
            if tmax < t3:
                # Et c'est tout
                nef = base_de_temps._TempsBase__convertir_ia_vers_ie(base_de_temps._TempsBase__convertir_t_vers_ia(tmax))
                vecteur_signal = np.concatenate([vecteur_signal, np.ones(nef-ned)])
            else:
                # On poursuit par un état bas
                nef = base_de_temps._TempsBase__convertir_ia_vers_ie(base_de_temps._TempsBase__convertir_t_vers_ia(t3))
                vecteur_signal = np.concatenate([vecteur_signal, np.ones(nef-ned)])
                ned = nef
                nef = base_de_temps._TempsBase__convertir_ia_vers_ie(base_de_temps._TempsBase__convertir_t_vers_ia(tmax))
                vecteur_signal = np.concatenate([vecteur_signal, np.zeros(nef-ned)])
    return vecteur_signal

class SignalCarre(SignalComplet):
    def __init__(self, F = cst.F, Vpp = cst.Vpp, offset = 0, alpha = 0.5, tr = 0, liste_tmin_tmax = cst.liste_tmin_tmax, Te = cst.Te, nom = ""):
        T = 1/F
        tmin, tmax = liste_tmin_tmax
        alpha = max(alpha, 0)
        alpha = min(alpha, 1)
        if T < tmax - tmin:        
            base_de_temps_periode = TempsBase([0, 1/F], Te)
            vecteur_signal_periode = (generer_portion_carre(base_de_temps_periode, F, alpha, tr)-0.5)*Vpp+offset
            base_de_temps = TempsBase(liste_tmin_tmax, Te)
            Nsignal = base_de_temps.calculer_N()
            SignalComplet.__init__(self, base_de_temps, utb.periodiser(Nsignal, vecteur_signal_periode), nom)
        else:
            base_de_temps = TempsBase(liste_tmin_tmax, Te)
            vecteur_signal = (generer_portion_carre(base_de_temps, F, alpha, tr)-0.5)*Vpp+offset
            SignalComplet.__init__(self, base_de_temps, vecteur_signal, nom)

        base_mesures = self.lire_base_mesures()
        base_mesures.T_th = 1/F


if __name__ == "__main__":
    s1 = SignalCarre()
    s1.plot()
    plt.legend()
    plt.show()

    print("fin")