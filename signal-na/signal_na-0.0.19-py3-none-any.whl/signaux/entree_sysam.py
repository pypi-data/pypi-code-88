#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 15:43:58 2019

@author: nicolas
"""
import time

import os, sys
import numpy as np

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))

import base.constantes_base as cst
from base.temps_base import BaseTemps
from signaux.signal_complet import SignalComplet


import matplotlib.pyplot as plt
 
__all__ = ["EntreeSysam"]



class EntreeSysam(SignalComplet):
    def __init__(self, nom_voie, calibre = 10., liste_tmin_tmax = cst.liste_tmin_tmax, Te = cst.Te, nom = ""):

        base_de_temps = BaseTemps(liste_tmin_tmax, Te)
        vecteur_signal = np.zeros(base_de_temps.N)
        SignalComplet.__init__(self, base_de_temps, vecteur_signal, nom)
        self.configurer_sysam(nom_voie, calibre)


if __name__ == "__main__":

    s1 = EntreeSysam("EA1", nom="$s_1$")
    print("fin")