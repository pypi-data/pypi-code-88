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
from base.axe_x_base import AxeXBase, convertir_vecteur_x_vers_axe_x_base
from signaux.signal_complet import SignalComplet
from base.voie_base import Voie
from base.trigger_base import Trigger

import base.voie_base

import matplotlib.pyplot as plt
 
__all__ = ["SignalSysam"]



class SignalPerso(SignalComplet):
    def __init__(self, vecteur_x, vecteur_y = [], nom = ""):

        axe_x_base = convertir_vecteur_x_vers_axe_x_base(vecteur_x)
        print(axe_x_base, axe_x_base.N)
        SignalComplet.__init__(self, axe_x_base, vecteur_y, nom)

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

    vecteur_x = np.linspace(0,10,1000)
    s1 = SignalPerso(vecteur_x)
    vecteur_x_bis = s1.axe_x_base.lire_vecteur_x()
    # print(vecteur_x)
    # print(vecteur_x_bis)
    s1.tracer_signal()
    print("fin")

