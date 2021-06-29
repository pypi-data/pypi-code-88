#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 15:43:58 2019

@author: nicolas
"""

import os, sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))
from signaux.signal_base import SignalBase
from base.temps_base import BaseTemps
from base.frequence_base import BaseFrequence
from base.mesure_base import Mesures

import numpy as np
import matplotlib.pyplot as plt

__all__ = ["SignalMesure"]

def dephasage_ok(phi):
    phi = phi % (2*np.pi)
    if phi > np.pi:
        phi = phi - 2*np.pi
    return phi

class SignalMesure(SignalBase):
    def forcer_T_th(self, T_th):
        self.mesures.T_th = T_th
    def calculer_Vmax(self):
        if self.mesures.Vmax == None:
            self.mesures.Vmax = np.max(self.vecteur_signal)
    def calculer_Vmin(self):
        if self.mesures.Vmin == None:
            self.mesures.Vmin = np.min(self.vecteur_signal)

    def __calculer_liste_i_trigger_conf(self, trigger_bas = 0, trigger_haut = 0):
        assert trigger_bas <= trigger_haut
        trigger = True
        liste_i_trigger = []
        for i in range(len(self.vecteur_signal)):
            if trigger == False and self.vecteur_signal[i] > trigger_haut:
                trigger = True
                liste_i_trigger.append(i)
            elif trigger == True and self.vecteur_signal[i] < trigger_bas:
                trigger = False
        return liste_i_trigger

    def __calculer_liste_i_trigger(self):
        if self.mesures.liste_i_trigger == None:
            self.calculer_Vmin()
            self.calculer_Vmax()
            trigger_haut = (self.mesures.Vmin+self.mesures.Vmax)/2
            trigger_bas = (3*self.mesures.Vmin+self.mesures.Vmax)/4
            self.mesures.liste_i_trigger = self.__calculer_liste_i_trigger_conf(trigger_bas, trigger_haut)

    def mesurer_T(self):
        if self.mesures.T == None:
            self.__calculer_liste_i_trigger()
            liste_Delta_i = []
            i = 1
            for i in range(1, len(self.mesures.liste_i_trigger)):
                liste_Delta_i.append(self.mesures.liste_i_trigger[i] - self.mesures.liste_i_trigger[i-1])


            if len(liste_Delta_i) > 0:
                self.mesures.T = np.mean(liste_Delta_i)*self.base_de_temps.Te
                return self.mesures.T
        return self.mesures.T

    def mesurer_sur_chaque_periodes_disponibles(self, fonction):
        T = self.__choisir_T()

        iTe = int(np.round(T/self.base_de_temps.Te))

        N = len(self.vecteur_signal)
        P = int(np.floor(N/iTe))
        assert P > 0, "pas assez d'échantillons pour faire des mesures. Augmenter la durée du signal."
        return np.mean([fonction(self.vecteur_signal[i*iTe: (i+1)*iTe]) for i in range(P)])

    def mesurer_Vdc(self):
        if self.mesures.Vdc == None:
            self.mesures.Vdc = self.mesurer_sur_chaque_periodes_disponibles(np.mean)
            return self.mesures.Vdc

    def mesurer_Vpp(self):
        if self.mesures.Vpp == None:
            self.mesures.Vpp = self.mesurer_sur_chaque_periodes_disponibles(lambda x: np.max(x) - np.min(x))
            return self.mesures.Vpp

    def mesurer_Veff(self):
        if self.mesures.Veff == None:
            self.mesures.Veff = self.mesurer_sur_chaque_periodes_disponibles(lambda x: np.sqrt(np.mean(x*x)))
            return self.mesures.Veff

    def mesurer_phi(self):
        if self.mesures.phi == None:
            signal_cos = self.copier()
            vecteur_t = signal_cos.base_de_temps.calculer_vecteur_t()
            T = self.__choisir_T()
            signal_cos.vecteur_signal = np.cos(2*np.pi/T*vecteur_t)

            signal_cos.__calculer_liste_i_trigger()
            self.__calculer_liste_i_trigger()

            N = min(len(self.mesures.liste_i_trigger), len(signal_cos.mesures.liste_i_trigger))
            
            liste_Delta_i = [signal_cos.mesures.liste_i_trigger[i]-self.mesures.liste_i_trigger[i] for i in range(N)]
            Delta_i = np.mean(liste_Delta_i)
            Delta_t = Delta_i*self.base_de_temps.Te
            phi = Delta_t * 2*np.pi / T
            self.mesures.phi = dephasage_ok(phi)
            return self.mesures.phi

    def __choisir_T(self):
        T = self.mesurer_T()
        if T == None:
            T = self.mesures.T_th
        if T == None:
            print("pas assez d'échantillons pour faire des mesures. Forcer T_th ou augmenter la durée du signal.")
            sys.exit()
        return T

    def mesurer_dephasage_par_rapport_a(self, other):
        self.mesurer_phi()
        other.mesurer_phi()
        Delta_phi = self.mesures.phi - other.mesures.phi 
        return dephasage_ok(Delta_phi)
    
    def signal_trigger(self):
        self.__calculer_liste_i_trigger()
        sortie = self.copier()
        sortie.vecteur_signal = np.zeros(self.base_de_temps.N)
        for i in self.mesures.liste_i_trigger:
            sortie.vecteur_signal[i] = 1
        return sortie

if __name__ == "__main__":
    F = 3
    liste_tmin_tmax = [0.1, 1.4]
    Te = 1e-6
    bdt = BaseTemps(liste_tmin_tmax, Te)
    vecteur_t = bdt.calculer_vecteur_t()
    vecteur_signal = 4+3*np.sqrt(2)*np.cos(2*np.pi*F*vecteur_t  +2.2*np.pi)


    s = SignalMesure(bdt, vecteur_signal)
    print(s.mesures.T_th)
    print(s.mesurer_T())
    print(s.mesures.liste_i_trigger)

    s_trig = s.signal_trigger()
    print(type(s), type(s_trig))
    plt.plot(s.vecteur_signal)
    plt.plot(s_trig.vecteur_signal)
    plt.show()
    
