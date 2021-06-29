#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 15:43:58 2019

@author: nicolas
"""

import numpy as np

import os, sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))
from signaux.signal_base import SignalBase
from base.temps_base import BaseTemps

class SignalArithmetique(SignalBase):

    def __add__(self, other):
        sortie = self.copier()
        test = False
        if isinstance(other, (int, float)):
            test = True
            sortie.vecteur_signal = self.vecteur_signal + other
            sortie.nom = "({0}  + {1})".format(self.nom, other)
        elif isinstance(other, SignalArithmetique):
            test = self.base_de_temps == other.base_de_temps
            if not test:
                print("Opération arithmétique: Les deux signaux doivent avoir la même base de temps")
                sys.exit()
            sortie.vecteur_signal = self.vecteur_signal + other.vecteur_signal
            sortie.nom = "({0}  + {1})".format(self.nom, other.nom)
        assert test == True, "Opération arithmétique impossible entre {0} et {1}".format(type(self), type(other))
        return sortie
    
    def __radd__(self, other):
        sortie = self.copier()
        test = False
        if isinstance(other, (int, float)):
            test = True
            sortie.vecteur_signal = other + self.vecteur_signal
            sortie.nom = "({0}  + {1})".format(other, self.nom)
        elif isinstance(other, SignalArithmetique):
            test = self.base_de_temps == other.base_de_temps
            if not test:
                print("Opération arithmétique: Les deux signaux doivent avoir la même base de temps")
                sys.exit()
            sortie.vecteur_signal = other.vecteur_signal + self.vecteur_signal
            sortie.nom = "({0}  + {1})".format(other.nom, self.nom)
        assert test == True, "Opération arithmétique impossible entre {0} et {1}".format(type(self), type(other))
        return sortie
    
    def __sub__(self, other):
        sortie = self.copier()
        test = False
        if isinstance(other, (int, float)):
            test = True
            sortie.vecteur_signal = self.vecteur_signal - other
            sortie.nom = "({0} - {1})".format(self.nom, other)
        elif isinstance(other, SignalArithmetique):
            test = self.base_de_temps == other.base_de_temps
            if not test:
                print("Opération arithmétique: Les deux signaux doivent avoir la même base de temps")
                sys.exit()
            sortie.vecteur_signal = self.vecteur_signal - other.vecteur_signal
            sortie.nom = "({0} - {1})".format(self.nom, other.nom)
        assert test == True, "Opération arithmétique impossible entre {0} et {1}".format(type(self), type(other))
        return sortie

    def __rsub__(self, other):
        sortie = self.copier()
        test = False
        if isinstance(other, (int, float)):
            test = True
            sortie.vecteur_signal = other - self.vecteur_signal
            sortie.nom = "({0} - {1})".format(other, self.nom)
        elif isinstance(other, SignalArithmetique):
            test = self.base_de_temps == other.base_de_temps
            if not test:
                print("Opération arithmétique: Les deux signaux doivent avoir la même base de temps")
                sys.exit()
            sortie.vecteur_signal = other.vecteur_signal - self.vecteur_signal
            sortie.nom = "({0}  - {1})".format(other.nom, self.nom)
        assert test == True, "Opération arithmétique impossible entre {0} et {1}".format(type(self), type(other))
        return sortie
    
    def __mul__(self, other):
        sortie = self.copier()
        test = False
        if isinstance(other, (int, float)):
            test = True
            sortie.vecteur_signal = self.vecteur_signal * other
            sortie.nom = "({0} $\\times$ {1})".format(self.nom, other)
        elif isinstance(other, SignalArithmetique):
            test = self.base_de_temps == other.base_de_temps
            if not test:
                print("Opération arithmétique: Les deux signaux doivent avoir la même base de temps")
                sys.exit()
            sortie.vecteur_signal = self.vecteur_signal * other.vecteur_signal
            sortie.nom = "({0} $\\times$ {1})".format(self.nom, other.nom)
        assert test == True, "Opération arithmétique impossible entre {0} et {1}".format(type(self), type(other))
        return sortie

    def __rmul__(self, other):
        sortie = self.copier()
        test = False
        if isinstance(other, (int, float)):
            test = True
            sortie.vecteur_signal = other * self.vecteur_signal
            sortie.nom = "({0} $\\times$ {1})".format(other, self.nom)
        elif isinstance(other, SignalArithmetique):
            test = self.base_de_temps == other.base_de_temps
            if not test:
                print("Opération arithmétique: Les deux signaux doivent avoir la même base de temps")
                sys.exit()
            sortie.vecteur_signal = other.vecteur_signal * self.vecteur_signal
            sortie.nom = "({0} $\\times$ {1})".format(other.nom, self.nom)
        assert test == True, "Opération arithmétique impossible entre {0} et {1}".format(type(self), type(other))
        return sortie
        
if __name__ == "__main__":
    Te1 = 1e-4
    liste_tmin_tmax1 = -1.05, 0.35

    Te2 = 1e-3
    liste_tmin_tmax2 = 0.05, 1.05

    bdt1 = BaseTemps(liste_tmin_tmax1, Te1)
    bdt2 = BaseTemps(liste_tmin_tmax2, Te2)

    vecteur_t1 = bdt1.calculer_vecteur_t()
    vecteur_t2 = bdt2.calculer_vecteur_t()
    vecteur_signal1 = np.cos(2*np.pi*vecteur_t1)
    vecteur_signal1_2 = np.sin(2*np.pi*vecteur_t1)
    vecteur_signal2 = np.sin(2*np.pi*vecteur_t2)

    s1 = SignalArithmetique(bdt1, vecteur_signal1)
    s1_2 = SignalArithmetique(bdt1, vecteur_signal1)
    s2 = SignalArithmetique(bdt2, vecteur_signal2)

    s3 = s1+2


    print("fin")