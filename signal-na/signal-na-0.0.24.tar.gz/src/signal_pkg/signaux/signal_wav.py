#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 15:43:58 2019

@author: nicolas
"""

import os, sys
import matplotlib.pyplot as plt

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))

from base.axe_x_base import AxeXBase
from signaux.signal_complet import SignalComplet

__all__ = ["SignalWav"]

class SignalWav(SignalComplet):
    def __init__(self, nom_fichier_wav, Pbits = 16, liste_umin_umax = [-10, 10], nom = ""):
        SignalComplet.__init__(self, AxeXBase(), nom)
        self.lire_wav(nom_fichier_wav, Pbits, liste_umin_umax)

if __name__ == "__main__":
    s1 = SignalWav('/Users/nicolas/tmp/A3.wav')
    
    can_base = s1._Signal4TNS__lire_can_base()
    print(can_base.Pbits)
    # s1.enregistrer_wav('/Users/nicolas/tmp/A3bis.wav')

    # s1.tracer()
