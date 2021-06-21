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
import base.utiles_base as utb
from base.temps_base import BaseTemps
from signaux.signal_complet import SignalComplet
from base.voie_base import Voie
from base.trigger_base import Trigger

import base.voie_base

import matplotlib.pyplot as plt
 
__all__ = ["SignalSysam"]



class SignalSysam(SignalComplet):
    def __init__(self, nom_voie, calibre = 10., liste_tmin_tmax = cst.liste_tmin_tmax, Te = cst.Te, nom = ""):

        base_de_temps = BaseTemps(liste_tmin_tmax, Te)
        SignalComplet.__init__(self, base_de_temps = base_de_temps, nom = nom)
        self.configurer_voie(nom_voie, calibre)
    
    def calculer_calibre_optimal(self):
        liste = base.voie_base.liste_calibres_entrees
        liste.sort()

        signal_max = np.max(self.vecteur_signal)
        signal_min = np.min(self.vecteur_signal)
        calibre_min = max(np.abs(signal_max), np.abs(signal_min))
        for calibre in liste:
            if calibre > calibre_min:
                return calibre
        return np.max(liste)
        
    # def configurer_sysam(self, nom_voie, calibre = 10., repetition = False):
    #     self.voie.nom = nom_voie
    #     self.voie.calibre = calibre
    #     self.voie.repetition = repetition

    # def deconfigurer_sysam(self):
    #     self.voie = Voie()

    # def configurer_trigger(self, seuil, montant=True, pretrigger=0, pretrigger_souple=False, hysteresys=False):
    #     self.trigger.seuil = seuil
    #     self.trigger.montant = montant
    #     self.trigger.pretrigger = pretrigger
    #     self.trigger.pretrigger_souple = pretrigger_souple
    #     self.trigger.hysteresys = hysteresys

    # def deconfigurer_trigger(self):
    #     self.trigger = Trigger()


if __name__ == "__main__":

    liste_tmin_tmax=[0, 1e-8]
    Te = 2e-7

    bdt = BaseTemps(liste_tmin_tmax, Te)

    liste_signaux = []

    liste_signaux.append(SignalSysam("EA0"))
    liste_signaux.append(SignalSysam("EA1"))
    liste_signaux.append(SignalSysam("EA2"))
    liste_signaux.append(SignalSysam("SA0"))
    liste_signaux.append(SignalSysam("SA1"))

    utb.print_liste(liste_signaux)
    print("fin")

