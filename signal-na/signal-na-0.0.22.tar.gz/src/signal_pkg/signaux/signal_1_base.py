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


sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))
from base.axe_base import AxeBase
from base.axe_x_base import AxeXBase

import base.constantes_base as cst
from plot.plot_base import PlotBase
from plot.plot_base import  tracer

__all__ = ["Signal1Base"]

class Signal1Base(PlotBase):
    __liste_n_signaux = [0]

    def __init__(self, axe_x_base, vecteur_y = [], nom = ""):
        PlotBase.__init__(self)
        _axe_x_base = self._PlotBase__lire_axe_x_base()
        _axe_y_base = self._PlotBase__lire_axe_y_base()
        _axe_x_base.cloner(axe_x_base)
        _axe_y_base.cloner(AxeBase("u", "V"))

        self.__ecrire_nom(nom)
        N_axe = _axe_x_base.lire_N()
        N_signal = len(vecteur_y)
        
        assert N_signal <= cst.Nmax, "Trop d'échantillons dans le signal"
        if N_signal == 0:
            self.__vecteur_y = np.zeros(N_axe)
        else:
            assert N_axe == N_signal, "SignalBase: axe_x_base et vecteur_y incompatibles"
            self.__vecteur_y = vecteur_y
        
    def copier(self, nom = ""):
        sortie = copy.deepcopy(self)
        if nom == "":
            sortie.__nom = "copie_de_" + self.lire_nom()
        return sortie
        
    def lire_vecteur_x(self):
        return self._PlotBase__axe_x_base.lire_vecteur_x()

    def lire_vecteur_y(self):
        return self.__vecteur_y

    def lire_nom(self):
        return self.__nom

    def __ecrire_nom(self, nom):
        if nom != "":
            self.__nom = nom
        else:
            numero = np.max(self.__liste_n_signaux)+1
            self.__nom = "s_" + str(numero)
            self.__liste_n_signaux.append(numero)

    def __str__(self):
        return self.__nom

if __name__ == "__main__":
    bdt = AxeXBase()
    vecteur_x = bdt.lire_vecteur_x()
    vecteur_y = np.sin(2*np.pi*1e5*vecteur_x)

    print(bdt.NBase)
    signal = Signal1Base(bdt, vecteur_y)
    print("Fin")

    # signal.tracer(color = "blue", liste_xmin_xmax = [-1, 0.5], affichage = False, legende = False)
    # signal.tracer(color = "red", liste_xmin_xmax = [-1, 2], affichage = False, nouvelle_figure = False, legende = True)

    # tracer(signal, signal.calculer_fft(), signal.calculer_spectre(), superposition = False)
    signal.tracer(liste_nombre_axes = [4,2], indice_axe = 2)