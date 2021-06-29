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

def linspace_(umin, umax, N):
    return np.linspace(umin, umax, N+1)[:N]

def generer_portion_triangle(axe_x_base, F, alpha, tr):
    xmin, xmax = axe_x_base.calculer_liste_xmin_xmax()
    n = int(np.floor((xmin-tr)*F))

    t0 = n/F+tr
    t1 = t0 + alpha/F
    t2 = t0 + 1/F
    t3 = t0 + (1+alpha)/F
    t4 = t0 + 2/F

    if xmin < t1:
        # On commence par un état montant
        ned = axe_x_base.convertir_ia_vers_ie(axe_x_base.convertir_x_vers_ia(xmin))
        if xmax < t1:
            # Et c'est tout
            ud = (xmin-t0)/(t1-t0)
            uf = (xmax-t0)/(t1-t0)
            nef = axe_x_base.convertir_ia_vers_ie(axe_x_base.convertir_x_vers_ia(xmax))
            vecteur_y = linspace_(ud, uf, nef-ned)
        else:
            # On poursuit par un état desendant
            ud = (xmin-t0)/(t1-t0)
            uf = 1
            nef = axe_x_base.convertir_ia_vers_ie(axe_x_base.convertir_x_vers_ia(t1))
            vecteur_y = linspace_(ud, uf, nef-ned)
            ned = nef
            if xmax < t2:
                # Et c'est tout
                ud = 1
                uf = (t2-xmax)/(t2-t1)
                nef = axe_x_base.convertir_ia_vers_ie(axe_x_base.convertir_x_vers_ia(xmax))
                vecteur_y = np.concatenate([vecteur_y, linspace_(ud, uf, nef-ned)])
            else:
                # On poursuit par un état montant
                ud = 1
                uf = 0
                nef = axe_x_base.convertir_ia_vers_ie(axe_x_base.convertir_x_vers_ia(t2))
                vecteur_y = np.concatenate([vecteur_y, linspace_(ud, uf, nef-ned)])
                ud = 0
                uf = (xmax-t2)/(t3-t2) 
                ned = nef
                nef = axe_x_base.convertir_ia_vers_ie(axe_x_base.convertir_x_vers_ia(xmax))
                vecteur_y = np.concatenate([vecteur_y, linspace_(ud, uf, nef-ned)])
    else:
        # On commence par un état descendant
        ned = axe_x_base.convertir_ia_vers_ie(axe_x_base.convertir_x_vers_ia(xmin))
        if xmax < t2:
            # Et c'est tout
            ud = (t2-xmin)/(t2-t1)
            uf = (t2-xmax)/(t2-t1)
            nef = axe_x_base.convertir_ia_vers_ie(axe_x_base.convertir_x_vers_ia(xmax))
            vecteur_y = linspace_(ud, uf, nef-ned)

        else:
            # On poursuit par un état montant
            ud = (t2-xmin)/(t2-t1)
            uf = 0
            nef = axe_x_base.convertir_ia_vers_ie(axe_x_base.convertir_x_vers_ia(t2))
            vecteur_y = linspace_(ud, uf, nef-ned)
            ned = nef
            if xmax < t3:
                # Et c'est tout
                ud = 0
                uf = (xmax-t2)/(t3-t2)
                nef = axe_x_base.convertir_ia_vers_ie(axe_x_base.convertir_x_vers_ia(xmax))
                vecteur_y = np.concatenate([vecteur_y, linspace_(ud, uf, nef-ned)])
            else:
                # On poursuit par un état bas
                ud = 0
                uf = 1
                nef = axe_x_base.convertir_ia_vers_ie(axe_x_base.convertir_x_vers_ia(t3))
                vecteur_y = np.concatenate([vecteur_y, linspace_(ud, uf, nef-ned)])
                ud = 1
                uf = (t4-xmax)/(t4-t3)
                ned = nef
                nef = axe_x_base.convertir_ia_vers_ie(axe_x_base.convertir_x_vers_ia(xmax))
                vecteur_y = np.concatenate([vecteur_y, linspace_(ud, uf, nef-ned)])
    return vecteur_y


class SignalTriangle(SignalComplet):
    def __init__(self, F = cst.F, Vpp = cst.Vpp, offset = 0, alpha = 0.5, tr = 0, liste_tmin_tmax = cst.liste_xmin_xmax, Te = cst.Xe, nom = ""):
        T = 1/F
        xmin, xmax = liste_tmin_tmax
        alpha = max(alpha, 0)
        alpha = min(alpha, 1)
        if T < xmax - xmin:        
            axe_x_base_periode = AxeXBase([0, 1/F], Te)
            vecteur_y_periode = (generer_portion_triangle(axe_x_base_periode, F, alpha, tr)-0.5)*Vpp+offset
            axe_x_base = AxeXBase(liste_tmin_tmax, Te)
            Nsignal = axe_x_base.lire_N()
            SignalComplet.__init__(self, axe_x_base, utb.periodiser(Nsignal, vecteur_y_periode), nom)
        else:
            axe_x_base = AxeXBase(liste_tmin_tmax, Te)
            vecteur_y = (generer_portion_triangle(axe_x_base, F, alpha, tr)-0.5)*Vpp+offset
            SignalComplet.__init__(self, axe_x_base, vecteur_y, nom)

        base_mesures = self._Signal3Mesure__lire_mesure_base()
        base_mesures.T_th = 1/F

if __name__ == "__main__":
    s1 = SignalTriangle()
    s1.plot()
    plt.legend()
    plt.show()

    print("fin")