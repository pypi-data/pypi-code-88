#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 15:43:58 2019

@author: nicolas
"""

import os, sys
import matplotlib.pyplot as plt

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))

from base.temps_base import TempsBase
from signaux.signal_complet import SignalComplet

__all__ = ["SignalWav"]

class SignalWav(SignalComplet):
    def __init__(self, nom_fichier_wav, Pbits = 16, liste_umin_umax = [-10, 10], nom = ""):
        base_de_temps = TempsBase()
        NBase = max(base_de_temps.liste_bases_de_temps_sysam)+1
        base_de_temps._TempsBase__Nbase = NBase
        SignalComplet.__init__(self, base_de_temps, nom)
        self.lire_wav(nom_fichier_wav, Pbits, liste_umin_umax)

if __name__ == "__main__":
    s1 = SignalWav('/Users/nicolas/tmp/A3.wav')
    s1.plot()
    plt.legend()
    plt.show()
    print("fin")