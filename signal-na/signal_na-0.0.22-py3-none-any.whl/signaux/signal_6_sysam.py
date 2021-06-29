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

from base.axe_x_base import AxeXBase
from signaux.signal_5_wav import Signal5Wav
from base.voie_base import VoieBase
from base.trigger_base import TriggerBase

import base.voie_base
 
__all__ = ["SignalSysam"]



class Signal6Sysam(Signal5Wav):
    # def __init__(self, nom_voie, calibre = 10., liste_xmin_xmax = cst.liste_xmin_xmax, Xe = cst.Xe, nom = ""):

    #     axe_x_base = AxeXBase(liste_xmin_xmax, Xe)
    #     SignalComplet.__init__(self, axe_x_base = axe_x_base, nom = nom)
    #     self.configurer_voie(nom_voie, calibre)

    def __lire_voie_base(self):
        try:
            a = self.__voie_base
        except:
            self.__voie_base = VoieBase()
        return self.__voie_base
        
    def __lire_trigger_base(self):
        try:
            a = self.__trigger_base
        except:
            self.__trigger_base = TriggerBase()
        return self.__trigger_base
    
    def __str__(self):
        trigger_base = self.__lire_trigger_base()
        voie_base = self.__lire_voie_base()
        chaine = self.lire_nom()
        if voie_base.tester():
            chaine += "({0})".format(voie_base.nom)
        if trigger_base.tester():
            chaine += "T"
        return chaine

    def configurer_voie(self, nom="", calibre = 10., repetition = True):
        voie_base = self.__lire_voie_base()
        voie_base.nom = nom
        voie_base.calibre = calibre
        voie_base.repetition = repetition

    def configurer_trigger(self, seuil, montant = True, pretrigger = 0, pretrigger_souple = False, hysteresys = False):
        trigger_base = self.__lire_trigger_base()
        trigger_base.seuil = seuil
        trigger_base.montant = montant
        trigger_base.pretrigger = pretrigger
        trigger_base.pretrigger_souple = pretrigger_souple
        trigger_base.hysteresys = hysteresys

    def __calculer_calibre_optimal(self):
        liste = base.voie_base.liste_calibres_entrees
        liste.sort()

        signal_max = np.max(self.lire_vecteur_y())
        signal_min = np.min(self.lire_vecteur_y())
        calibre_min = max(np.abs(signal_max), np.abs(signal_min))
        for calibre in liste:
            if calibre > calibre_min:
                return calibre
        return np.max(liste)
    
    def deconfigurer_voie(self):
        self.__voie_base = VoieBase()
        
    def deconfigurer_trigger(self):
        self.__trigger_base = TriggerBase()
        
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

    liste_xmin_xmax=[0, 1e-8]
    Xe = 2e-7

    bdt = AxeXBase(liste_xmin_xmax, Xe)

    liste_signaux = []

    liste_signaux.append(Signal6Sysam(bdt))
    liste_signaux.append(Signal6Sysam(bdt))
    liste_signaux.append(Signal6Sysam(bdt))
    liste_signaux.append(Signal6Sysam(bdt))
    liste_signaux.append(Signal6Sysam(bdt))
    liste_signaux.append(Signal6Sysam(bdt))

    liste_signaux[0].configurer_voie("EA0")
    liste_signaux[1].configurer_voie("EA1")
    liste_signaux[1].configurer_trigger(0)
    for s in liste_signaux:
        print(s)

    print("fin")

    print(type(s))
