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

__all__ = ["SignalCarre"]

def generer_portion_carre(axe_x_base, F, alpha, tr):
    xmin, xmax = axe_x_base.calculer_liste_xmin_xmax()
    n = int(np.floor((xmin-tr)*F))

    t0 = n/F+tr
    t1 = t0 + alpha/F
    t2 = t0 + 1/F
    t3 = t0 + (1+alpha)/F

    if xmin < t1:
        # On commence par un état haut
        ned = axe_x_base.convertir_ia_vers_ie(axe_x_base.convertir_x_vers_ia(xmin))
        if xmax < t1:
            # Et c'est tout
            nef = axe_x_base.convertir_ia_vers_ie(axe_x_base.convertir_x_vers_ia(xmax))
            vecteur_y = np.ones(nef-ned)
        else:
            # On poursuit par un état bas
            nef = axe_x_base.convertir_ia_vers_ie(axe_x_base.convertir_x_vers_ia(t1))
            vecteur_y = np.ones(nef-ned)
            ned = nef
            if xmax < t2:
                # Et c'est tout
                nef = axe_x_base.convertir_ia_vers_ie(axe_x_base.convertir_x_vers_ia(xmax))
                vecteur_y = np.concatenate([vecteur_y, np.zeros(nef-ned)])
            else:
                # On poursuit par un état haut
                nef = axe_x_base.convertir_ia_vers_ie(axe_x_base.convertir_x_vers_ia(t2))
                vecteur_y = np.concatenate([vecteur_y, np.zeros(nef-ned)])
                ned = nef
                nef = axe_x_base.convertir_ia_vers_ie(axe_x_base.convertir_x_vers_ia(xmax))
                vecteur_y = np.concatenate([vecteur_y, np.ones(nef-ned)])
    else:
        # On commence par un état bas
        ned = axe_x_base.convertir_ia_vers_ie(axe_x_base.convertir_x_vers_ia(xmin))
        if xmax < t2:
            # Et c'est tout
            nef = axe_x_base.convertir_ia_vers_ie(axe_x_base.convertir_x_vers_ia(xmax))
            vecteur_y = np.zeros(nef-ned)
        else:
            # On poursuit par un état haut
            nef = axe_x_base.convertir_ia_vers_ie(axe_x_base.convertir_x_vers_ia(t2))
            vecteur_y = np.zeros(nef-ned)
            ned = nef
            if xmax < t3:
                # Et c'est tout
                nef = axe_x_base.convertir_ia_vers_ie(axe_x_base.convertir_x_vers_ia(xmax))
                vecteur_y = np.concatenate([vecteur_y, np.ones(nef-ned)])
            else:
                # On poursuit par un état bas
                nef = axe_x_base.convertir_ia_vers_ie(axe_x_base.convertir_x_vers_ia(t3))
                vecteur_y = np.concatenate([vecteur_y, np.ones(nef-ned)])
                ned = nef
                nef = axe_x_base.convertir_ia_vers_ie(axe_x_base.convertir_x_vers_ia(xmax))
                vecteur_y = np.concatenate([vecteur_y, np.zeros(nef-ned)])
    return vecteur_y

class SignalCarre(SignalComplet):
    def __init__(self, F = cst.F, Vpp = cst.Vpp, offset = 0, alpha = 0.5, tr = 0, liste_tmin_tmax = cst.liste_xmin_xmax, Te = cst.Xe, nom = ""):
        T = 1/F
        xmin, xmax = liste_tmin_tmax
        alpha = max(alpha, 0)
        alpha = min(alpha, 1)
        if T < xmax - xmin:        
            axe_x_base_periode = AxeXBase([0, 1/F], Te)
            vecteur_y_periode = (generer_portion_carre(axe_x_base_periode, F, alpha, tr)-0.5)*Vpp+offset
            axe_x_base = AxeXBase(liste_tmin_tmax, Te)
            Nsignal = axe_x_base.lire_N()
            SignalComplet.__init__(self, axe_x_base, utb.periodiser(Nsignal, vecteur_y_periode), nom)
        else:
            axe_x_base = AxeXBase(liste_tmin_tmax, Te)
            vecteur_y = (generer_portion_carre(axe_x_base, F, alpha, tr)-0.5)*Vpp+offset
            SignalComplet.__init__(self, axe_x_base, vecteur_y, nom)

        base_mesures = self._Signal3Mesure__lire_mesure_base()
        base_mesures.T_th = 1/F


if __name__ == "__main__":
    s1 = SignalCarre()
    s1.tracer()
    print("fin")