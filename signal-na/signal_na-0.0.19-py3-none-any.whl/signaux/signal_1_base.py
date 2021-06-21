#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 15:43:58 2019

@author: nicolas
"""
import copy
import numpy as np
import matplotlib.pyplot as plt

import os, sys

from numpy.lib import vectorize

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))
from base.temps_base import TempsBase

__all__ = ["Signal1Base"]

class Signal1Base():
    liste_n_signaux = [0]
    def __init__(self, base_de_temps, vecteur_signal = [], nom = ""):
        self.__base_de_temps = base_de_temps.copier()
        self.__ecrire_nom(nom)
        N_base_de_temps = base_de_temps.calculer_N()
        N_vecteur_signal = len(vecteur_signal)

        if N_vecteur_signal == 0:
            self.__vecteur_signal = np.zeros(self.__base_de_temps.calculer_N())
        else:
            assert N_base_de_temps == N_vecteur_signal, "SignalBase: base_de_temps et vecteur_signal incompatibles"
            self.__vecteur_signal = vecteur_signal

    def lire_base_de_temps(self):
        return self.__base_de_temps

    def copier(self, nom = ""):
        sortie = copy.deepcopy(self)
        if nom == "":
            sortie.nom = "copie_de_" + self.lire_nom()
        return sortie

    def lire_vecteur_signal(self, liste_imin_imax = [None, None]):
        imin, imax = liste_imin_imax
        if imin == None:
            imin = 0
        if imax == None:
            imax = self.__base_de_temps.calculer_N()
        imin = max(imin, 0)
        imax = min(imax, len(self.__vecteur_signal))
        return self.__vecteur_signal[imin: imax]

    def calculer_vecteur_t(self, liste_imin_imax = [None, None]):
        imin, imax = liste_imin_imax
        if imin == None:
            imin = 0
        if imax == None:
            imax = self.__base_de_temps.calculer_N()
        imin = max(imin, 0)
        imax = min(imax, len(self.__vecteur_signal))
        return self.__base_de_temps.calculer_vecteur_t( [imin, imax] )

    def lire_nom(self):
        return self.__nom

    def __ecrire_nom(self, nom):
        if nom != "":
            self.__nom = nom
        else:
            numero = np.max(self.liste_n_signaux)+1
            self.__nom = "s_" + str(numero)
            self.liste_n_signaux.append(numero)

    def __str__(self):
        return self.__nom

    def plot(self, *args, **kwargs):
        vt = self.calculer_vecteur_t()
        # plt.plot(vt, self.__vecteur_signal, label=self.lire_nom())
        args = [vt, self.__vecteur_signal] + list(args)
        if "label" not in kwargs:
            kwargs["label"] = str(self)
        plt.plot(*args, **kwargs)
        plt.xlabel("$t$ (s)")
        plt.ylabel("$u$ (V)")

if __name__ == "__main__":
    bdt = TempsBase([0, 1], 1e-3)
    vecteur_t = bdt.calculer_vecteur_t()
    vecteur_signal = np.sin(2*np.pi*3*vecteur_t)

    signal = Signal1Base(bdt, vecteur_signal)

    signal.plot("r*")
    plt.legend()
    plt.show()