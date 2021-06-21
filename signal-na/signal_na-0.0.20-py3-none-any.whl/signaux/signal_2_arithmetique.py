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
from base.temps_base import TempsBase

class Signal2Arithmetique(Signal1Base):

    def __add__(self, other):
        base_de_temps = self.lire_base_de_temps()
        test = False
        if isinstance(other, (int, float)):
            test = True
            vecteur_signal = self.lire_vecteur_signal() + other
            nom = "({0}_+_{1})".format(self.lire_nom(), other)
        elif isinstance(other, Signal2Arithmetique):
            test = True
            assert base_de_temps == other.lire_base_de_temps(), "Opération arithmétique impossible: Les deux signaux doivent avoir la même base de temps"
            vecteur_signal = self.lire_vecteur_signal() + other.lire_vecteur_signal()
            nom = "({0}_+_{1})".format(self.lire_nom(), other.lire_nom())
        assert test == True, "Opération arithmétique impossible: les types sont {0} et {1} sont incompatibles".format(type(self), type(other))
        return Signal2Arithmetique(base_de_temps, vecteur_signal, nom)
    
    def __radd__(self, other):
        base_de_temps = self.lire_base_de_temps()
        test = False
        if isinstance(other, (int, float)):
            test = True
            vecteur_signal = other + self.lire_vecteur_signal()
            nom = "({0}_+_{1})".format(other, self.lire_nom())
        elif isinstance(other, Signal2Arithmetique):
            test = True
            assert base_de_temps == other.lire_base_de_temps(), "Opération arithmétique impossible: Les deux signaux doivent avoir la même base de temps"
            vecteur_signal =  other.lire_vecteur_signal() + self.lire_vecteur_signal()
            nom = "({0}_+_{1})".format(other.lire_nom(), self.lire_nom())
        assert test == True, "Opération arithmétique impossible: les types sont {0} et {1} sont incompatibles".format(type(other), type(self))
        return Signal2Arithmetique(base_de_temps, vecteur_signal, nom)

    def __sub__(self, other):
        base_de_temps = self.lire_base_de_temps()
        test = False
        if isinstance(other, (int, float)):
            test = True
            vecteur_signal = self.lire_vecteur_signal() - other
            nom = "({0}_-_{1})".format(self.lire_nom(), other)
        elif isinstance(other, Signal2Arithmetique):
            test = True
            assert base_de_temps == other.lire_base_de_temps(), "Opération arithmétique impossible: Les deux signaux doivent avoir la même base de temps"
            vecteur_signal = self.lire_vecteur_signal() - other.lire_vecteur_signal()
            nom = "({0}_-_{1})".format(self.lire_nom(), other.lire_nom())
        assert test == True, "Opération arithmétique impossible: les types sont {0} et {1} sont incompatibles".format(type(self), type(other))
        return Signal2Arithmetique(base_de_temps, vecteur_signal, nom)

    def __rsub__(self, other):
        base_de_temps = self.lire_base_de_temps()
        test = False
        if isinstance(other, (int, float)):
            test = True
            vecteur_signal = other - self.lire_vecteur_signal()
            nom = "({0}_-_{1})".format(other, self.lire_nom())
        elif isinstance(other, Signal2Arithmetique):
            test = True
            assert base_de_temps == other.lire_base_de_temps(), "Opération arithmétique impossible: Les deux signaux doivent avoir la même base de temps"
            vecteur_signal =  other.lire_vecteur_signal() - self.lire_vecteur_signal()
            nom = "({0}_-_{1})".format(other.lire_nom(), self.lire_nom())
        assert test == True, "Opération arithmétique impossible: les types sont {0} et {1} sont incompatibles".format(type(other), type(self))
        return Signal2Arithmetique(base_de_temps, vecteur_signal, nom)
    
    def __mul__(self, other):
        base_de_temps = self.lire_base_de_temps()
        test = False
        if isinstance(other, (int, float)):
            test = True
            vecteur_signal = self.lire_vecteur_signal() * other
            nom = "({0}_*_{1})".format(self.lire_nom(), other)
        elif isinstance(other, Signal2Arithmetique):
            test = True
            assert base_de_temps == other.lire_base_de_temps(), "Opération arithmétique impossible: Les deux signaux doivent avoir la même base de temps"
            vecteur_signal = self.lire_vecteur_signal() * other.lire_vecteur_signal()
            nom = "({0}_*_{1})".format(self.lire_nom(), other.lire_nom())
        assert test == True, "Opération arithmétique impossible: les types sont {0} et {1} sont incompatibles".format(type(self), type(other))
        return Signal2Arithmetique(base_de_temps, vecteur_signal, nom)

    def __rmul__(self, other):
        base_de_temps = self.lire_base_de_temps()
        test = False
        if isinstance(other, (int, float)):
            test = True
            vecteur_signal = other * self.lire_vecteur_signal()
            nom = "({0}_*_{1})".format(other, self.lire_nom())
        elif isinstance(other, Signal2Arithmetique):
            test = True
            assert base_de_temps == other.lire_base_de_temps(), "Opération arithmétique impossible: Les deux signaux doivent avoir la même base de temps"
            vecteur_signal =  other.lire_vecteur_signal() * self.lire_vecteur_signal()
            nom = "({0}_*_{1})".format(other.lire_nom(), self.lire_nom())
        assert test == True, "Opération arithmétique impossible: les types sont {0} et {1} sont incompatibles".format(type(other), type(self))
        return Signal2Arithmetique(base_de_temps, vecteur_signal, nom)
        
if __name__ == "__main__":
    bdt = TempsBase([0, 1], 1e-3)
    vecteur_t = bdt.calculer_vecteur_t()
    vecteur_signal1 = np.sin(2*np.pi*3*vecteur_t)
    vecteur_signal2 = np.cos(2*np.pi*3*vecteur_t)

    signal1 = Signal2Arithmetique(bdt, vecteur_signal1)
    signal2 = Signal2Arithmetique(bdt, vecteur_signal2)

    signal3 = 3 + signal1 * signal2
    

    signal1.plot()
    signal2.plot()
    signal3.plot()
    plt.legend()
    plt.show()
    print("fin")