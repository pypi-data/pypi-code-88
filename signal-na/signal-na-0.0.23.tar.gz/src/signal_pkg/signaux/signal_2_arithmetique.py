#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 15:43:58 2019

@author: nicolas
"""

import numpy as np
import matplotlib.pyplot as plt

import os, sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))
from signaux.signal_1_base import Signal1Base
from base.axe_x_base import AxeXBase
from plot.plot_base import tracer
class Signal2Arithmetique(Signal1Base):
    def __addnum(self, num):
        sortie = self.copier("({0}_+_{1})".format(self.lire_nom(), num))
        sortie._Signal1Base__vecteur_y = self._Signal1Base__vecteur_y + num
        return sortie
         
    def __raddnum(self, num):
        sortie = self.copier("({0}_+_{1})".format(num, self.lire_nom()))
        sortie._Signal1Base__vecteur_y = num + self._Signal1Base__vecteur_y
        return sortie
         
    def __subnum(self, num):
        sortie = self.copier("({0}_-_{1})".format(self.lire_nom(), num))
        sortie._Signal1Base__vecteur_y = self._Signal1Base__vecteur_y - num
        return sortie
         
    def __rsubnum(self, num):
        sortie = self.copier("({0}_-_{1})".format(num, self.lire_nom()))
        sortie._Signal1Base__vecteur_y = num - self._Signal1Base__vecteur_y
        return sortie
         
    def __mulnum(self, num):
        sortie = self.copier("({0}_*_{1})".format(self.lire_nom(), num))
        sortie._Signal1Base__vecteur_y = self._Signal1Base__vecteur_y * num
        return sortie
         
    def __rmulnum(self, num):
        sortie = self.copier("({0}_*_{1})".format(num, self.lire_nom()))
        sortie._Signal1Base__vecteur_y = num * self._Signal1Base__vecteur_y
        return sortie
         
    def __addsig(self, sig):
        assert self._PlotBase__lire_axe_x_base() == sig._PlotBase__lire_axe_x_base(), "Abscisses incompatibles"
        assert self._PlotBase__lire_axe_y_base() == sig._PlotBase__lire_axe_y_base(), "Ordonnées incompatibles"
        sortie = self.copier("({0}_+_{1})".format(self.lire_nom(), sig.lire_nom()))
        sortie._Signal1Base__vecteur_y = self._Signal1Base__vecteur_y + sig._Signal1Base__vecteur_y
        return sortie
         
    def __raddsig(self, sig):
        assert self._PlotBase__lire_axe_x_base() == sig._PlotBase__lire_axe_x_base(), "Abscisses incompatibles"
        assert self._PlotBase__lire_axe_y_base() == sig._PlotBase__lire_axe_y_base(), "Ordonnées incompatibles"
        sortie = self.copier("({0}_+_{1})".format(sig.lire_nom(), self.lire_nom()))
        sortie._Signal1Base__vecteur_y = sig._Signal1Base__vecteur_y + self._Signal1Base__vecteur_y
        return sortie
         
    def __subsig(self, sig):
        assert self._PlotBase__lire_axe_x_base() == sig._PlotBase__lire_axe_x_base(), "Abscisses incompatibles"
        assert self._PlotBase__lire_axe_y_base() == sig._PlotBase__lire_axe_y_base(), "Ordonnées incompatibles"
        sortie = self.copier("({0}_-_{1})".format(self.lire_nom(), sig.lire_nom()))
        sortie._Signal1Base__vecteur_y = self._Signal1Base__vecteur_y - sig._Signal1Base__vecteur_y
        return sortie
         
    def __rsubsig(self, sig):
        assert self._PlotBase__lire_axe_x_base() == sig._PlotBase__lire_axe_x_base(), "Abscisses incompatibles"
        assert self._PlotBase__lire_axe_y_base() == sig._PlotBase__lire_axe_y_base(), "Ordonnées incompatibles"
        sortie = self.copier("({0}_-_{1})".format(sig.lire_nom(), self.lire_nom()))
        sortie._Signal1Base__vecteur_y = sig._Signal1Base__vecteur_y - self._Signal1Base__vecteur_y
        return sortie
         
    def __mulsig(self, sig):
        assert self._PlotBase__lire_axe_x_base() == sig._PlotBase__lire_axe_x_base(), "Abscisses incompatibles"
        assert self._PlotBase__lire_axe_y_base() == sig._PlotBase__lire_axe_y_base(), "Ordonnées incompatibles"
        sortie = self.copier("({0}_*_{1})".format(self.lire_nom(), sig.lire_nom()))
        sortie._Signal1Base__vecteur_y = self._Signal1Base__vecteur_y * sig._Signal1Base__vecteur_y
        return sortie
         
    def __rmulsig(self, sig):
        assert self._PlotBase__lire_axe_x_base() == sig._PlotBase__lire_axe_x_base(), "Abscisses incompatibles"
        assert self._PlotBase__lire_axe_y_base() == sig._PlotBase__lire_axe_y_base(), "Ordonnées incompatibles"
        sortie = self.copier("({0}_*_{1})".format(sig.lire_nom(), self.lire_nom()))
        sortie._Signal1Base__vecteur_y = sig._Signal1Base__vecteur_y * self._Signal1Base__vecteur_y
        return sortie

    def __add__(self, other):
        if isinstance(other, (int, float)):
            return self.__addnum(other)
        elif isinstance(other, Signal2Arithmetique):
            return self.__addsig(other)
        print("Opération arithmétique impossible")
        sys.exit()

    
    def __radd__(self, other):
        if isinstance(other, (int, float)):
            return self.__raddnum(other)
        elif isinstance(other, Signal2Arithmetique):
            return self.__raddsig(other)
        print("Opération arithmétique impossible")
        sys.exit()

    def __sub__(self, other):
        if isinstance(other, (int, float)):
            return self.__subnum(other)
        elif isinstance(other, Signal2Arithmetique):
            return self.__subsig(other)
        print("Opération arithmétique impossible")
        sys.exit()

    def __rsub__(self, other):
        if isinstance(other, (int, float)):
            return self.__rsubnum(other)
        elif isinstance(other, Signal2Arithmetique):
            return self.__rsubsig(other)
        print("Opération arithmétique impossible")
        sys.exit()
    
    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return self.__mulnum(other)
        elif isinstance(other, Signal2Arithmetique):
            return self.__mulsig(other)
        print("Opération arithmétique impossible")
        sys.exit()

    def __rmul__(self, other):
        if isinstance(other, (int, float)):
            return self.__rmulnum(other)
        elif isinstance(other, Signal2Arithmetique):
            return self.__rmulsig(other)
        print("Opération arithmétique impossible")
        sys.exit()
        
if __name__ == "__main__":
    bdt = AxeXBase([0, 1], 1e-3)
    vecteur_x = bdt.lire_vecteur_x()
    vecteur_y1 = np.sin(2*np.pi*3*vecteur_x)
    vecteur_y2 = np.cos(2*np.pi*3*vecteur_x)

    signal1 = Signal2Arithmetique(bdt, vecteur_y1)
    signal2 = Signal2Arithmetique(bdt, vecteur_y2)

    signal3 = 3 + signal1 * signal2
    

    tracer(signal1, signal2, signal3)
    print("fin")