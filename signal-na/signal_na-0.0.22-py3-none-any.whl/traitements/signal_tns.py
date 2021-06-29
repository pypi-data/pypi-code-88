#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 15:43:58 2019

@author: nicolas
"""

import matplotlib.pyplot as plt
import os, sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))

import numpy as np
from signaux.signal_base import SignalBase
from base.temps_base import BaseTemps

class SignalTNS(SignalBase):

    def __bloquer_1_ech(self, Te):
        sortie = self.copier()
        sortie.vecteur_signal = np.zeros(self.base_de_temps.N)
        base_de_temps_ech = BaseTemps(self.base_de_temps.calculer_liste_tmin_tmax(), Te)
        vecteur_n = base_de_temps_ech.calculer_vecteur_n()
        liste_i = [self.base_de_temps.convertir_n_vers_i(n) for n in vecteur_n]
        sortie.vecteur_signal[liste_i] = self.vecteur_signal[liste_i]
        return sortie

    def __bloquer_N_ech(self, Te, N):
        sortie = self.__bloquer_1_ech(Te)
        print(min(1, N))
        vecteur_porte = np.ones(min(1, N))
        sortie.vecteur_signal = np.convolve(sortie.vecteur_signal, vecteur_porte)[0:self.base_de_temps.N]
        return sortie
        
    def bloquer(self, Te, alpha=0):
        assert 0<= alpha <= 1
        Nbloque = self.base_de_temps.calculer_n(alpha*Te) // self.base_de_temps.NTa
        sortie = self.__bloquer_N_ech(Te, Nbloque)
        if self.nom != "":
            sortie.nom = self.nom + "_bloqué"
        return sortie

    def quantifier(self, Pbits = 8, liste_umin_umax=[-10., 10.]):
        sortie = self.copier()
        umin, umax = liste_umin_umax
        assert umax > umin, 'SignalTNS -> quantifier'
        N = 2**Pbits
        sortie.vecteur_signal = (sortie.vecteur_signal-umin)/(umax-umin)
        sortie.vecteur_signal = np.floor(sortie.vecteur_signal*N)
        sortie.vecteur_signal = np.clip(sortie.vecteur_signal, 0, N-1)+0.5
        
        sortie.vecteur_signal = (umax-umin)*sortie.vecteur_signal/N + umin
        if self.nom != "":
            sortie.nom = sortie.nom + "_quantifié"

        return sortie

    def __sous_echantillonner_N_ech(self, N):
        sortie = self.copier()
        sortie.NTa = N*self.NTa
        Te = sortie.NTa*self.Ta
        sortie.Nmin, sortie.Nmax = SignalBase.calculer_liste_Nmin_Nmax(self.generer_liste_tmin_tmax(), Te)
        imin, imax = self.calculer_index(sortie.Nmin*self.Ta), self.calculer_index(sortie.Nmax*self.Ta)
        sortie.vecteur_signal = np.array(self.vecteur_signal[imin: imax+N: N])
        return sortie

    def __sur_echantillonner_N_ech(self, N):
        sortie = self.copier()
        sortie.NTa = SignalBase.calculer_et_tester_rapport_entier(self.NTa, N)
        Te = sortie.NTa*self.Ta

        sortie.Nmin, sortie.Nmax = SignalBase.calculer_liste_Nmin_Nmax(self.generer_liste_tmin_tmax(), Te)
        imin, imax = sortie.calculer_index(sortie.Nmin*self.Ta), sortie.calculer_index(sortie.Nmax*self.Ta)
        sortie.vecteur_signal = np.zeros(imax-imin+1)
        sortie.vecteur_signal[imin: imax+N: N] = self.vecteur_signal
        return sortie.__bloquer_N_ech(Te, N)

    def changer_Te(self, Te):
        Te_depart = self.NTa*self.Ta
        if Te_depart > Te:
            N = SignalBase.calculer_et_tester_rapport_entier(Te_depart, Te)
            return self.__sous_echantillonner_N_ech(N)
        if Te_depart < Te:
            N = SignalBase.calculer_et_tester_rapport_entier(Te, Te_depart)
            return self.__sur_echantillonner_N_ech(N)
        else:
            return self.copier()

if __name__ == "__main__":
    generer_liste_tmin_tmax = [0, 1]
    Te = 1e-6
    bdt = BaseTemps(generer_liste_tmin_tmax, Te)
    vecteur_t = bdt.calculer_vecteur_t()
    vecteur_signal = 10*np.sin(2*np.pi*3*vecteur_t)
    s1 = SignalTNS(bdt, vecteur_signal)
    print("debut blocage")
    s2 = s1.bloquer(1e-2, 0.5)
    s3 = s2.quantifier(3)
    print("fin blocage")

    plt.plot(vecteur_t, s3.vecteur_signal)
    plt.plot(vecteur_t, s1.vecteur_signal)
    plt.show()
    print("fin")
