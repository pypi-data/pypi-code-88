#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 15:43:58 2019

@author: nicolas
"""

import os, sys
import numpy as np
import matplotlib.pyplot as plt

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))
from signaux.signal_2_arithmetique import Signal2Arithmetique
from base.temps_base import TempsBase
from base.mesure_base import MesureBase


__all__ = ["Signal3Mesure"]

def mettre_en_forme_dephasage(phi, offset = 2):
    phi = phi % (2*np.pi)
    if phi > np.pi*(2-offset/2):
        phi -= 2*np.pi
    return phi

class Signal3Mesure(Signal2Arithmetique):
    def lire_base_mesures(self):
        try:
            mesures = self.__mesures_base
        except:
            mesures = MesureBase()
        self.__mesures_base = mesures
        return self.__mesures_base


    def forcer_T_th(self, T_th):
        mesures = self.lire_base_mesures()
        mesures.T_th = T_th

    def __calculer_Vmax(self):
        mesures = self.lire_base_mesures()
        if mesures.Vmax == None:
            mesures.Vmax = np.max(self.lire_vecteur_signal())

    def __calculer_Vmin(self):
        mesures = self.lire_base_mesures()
        if mesures.Vmin == None:
            mesures.Vmin = np.min(self.lire_vecteur_signal())

    def __calculer_liste_i_trigger_conf(self, trigger_bas, trigger_haut):
        mesures = self.lire_base_mesures()
        trigger = True
        mesures.liste_i_trigger = []
        vecteur_signal = self.lire_vecteur_signal()
        N = len(vecteur_signal)
        for i in range(N):
            if trigger == False and vecteur_signal[i] > trigger_haut:
                trigger = True
                mesures.liste_i_trigger.append(i)
            elif trigger == True and vecteur_signal[i] < trigger_bas:
                trigger = False

    def __calculer_liste_i_trigger(self, trigger_bas = None, trigger_haut = None):
        mesures = self.lire_base_mesures()
        test_init = False
        if mesures.liste_i_trigger == None:
            test_init = True
        elif (mesures.trigger_bas != None and mesures.trigger_bas != trigger_bas):
            test_init = True
        elif (mesures.trigger_haut != None and mesures.trigger_haut != trigger_haut):
            test_init = True

        if test_init:
            self.__calculer_Vmin()
            self.__calculer_Vmax()
            _trigger_haut = ( mesures.Vmin + mesures.Vmax ) / 2
            _trigger_bas = ( 3*mesures.Vmin + mesures.Vmax ) / 4
            
            if trigger_bas == None:
                trigger_bas = _trigger_bas
            if trigger_haut == None:
                trigger_haut = _trigger_haut

            mesures.trigger_bas, mesures.trigger_haut = trigger_bas, trigger_haut
            self.__calculer_liste_i_trigger_conf(trigger_bas, trigger_haut)

    def __mesurer_T(self):
        mesures = self.lire_base_mesures()
        if mesures.T == None:
            self.__calculer_liste_i_trigger()
            liste_Delta_i = []
            i = 1
            for i in range(1, len(mesures.liste_i_trigger)):
                liste_Delta_i.append(mesures.liste_i_trigger[i] - mesures.liste_i_trigger[i-1])

            if len(liste_Delta_i) > 0:
                base_de_temps = self.lire_base_de_temps()
                mesures.T = np.mean(liste_Delta_i) * base_de_temps.lire_NTa() / 10**base_de_temps.lire_Pa()

    def __choisir_T(self):
        self.__mesurer_T()
        T = self.__mesures_base.T
        if T == None:
            T = self.__mesures_base.T_th
        assert T != None, "Mesures pas assez d'échantillons pour faire des mesures. Forcer T_th ou augmenter la durée du signal."
        return T
                
    def __mesurer_sur_chaque_periodes_disponibles(self, fonction):
        T = self.__choisir_T()
        base_de_temps = self.lire_base_de_temps()
        vecteur_signal = self.lire_vecteur_signal()

        iTe = int( np.round( T * 10**base_de_temps.lire_Pa() / base_de_temps.lire_NTa() ) )


        N = len(vecteur_signal)
        P = int( np.floor( N/iTe ) )
        assert P > 0, "pas assez d'échantillons pour faire des mesures. Augmenter la durée du signal."
        return np.mean( [ fonction(vecteur_signal[i*iTe: (i+1)*iTe]) for i in range(P) ] )


    def __mesurer_Vdc(self):
        mesures = self.lire_base_mesures()
        if mesures.Vdc == None:
            mesures.Vdc = self.__mesurer_sur_chaque_periodes_disponibles(np.mean)

    def __mesurer_Vpp(self):
        mesures = self.lire_base_mesures()
        if mesures.Vpp == None:
            mesures.Vpp = self.__mesurer_sur_chaque_periodes_disponibles( lambda x: np.max(x) - np.min(x) )

    def __mesurer_Veff(self):
        mesures = self.lire_base_mesures()
        if mesures.Veff == None:
            mesures.Veff = self.__mesurer_sur_chaque_periodes_disponibles( lambda x: np.sqrt(np.mean(x*x)) )

    def __mesurer_phi(self):
        mesures = self.lire_base_mesures()
        if mesures.phi == None:
            base_de_temps = self.lire_base_de_temps()
            vecteur_t = base_de_temps.calculer_vecteur_t()
            T = self.__choisir_T()

            vecteur_cos = np.cos(2*np.pi*vecteur_t/T)
            signal_cos = Signal3Mesure(base_de_temps, vecteur_cos, "cos")

            signal_cos.__calculer_liste_i_trigger()
            self.__calculer_liste_i_trigger()

            N = min(len(self.__mesures_base.liste_i_trigger), len(signal_cos.__mesures_base.liste_i_trigger))
            
            liste_Delta_i = [signal_cos.__mesures_base.liste_i_trigger[i]-self.__mesures_base.liste_i_trigger[i] for i in range(N)]

            Delta_i = np.mean(liste_Delta_i)
            Delta_t = Delta_i * base_de_temps.lire_NTa() / 10**base_de_temps.lire_Pa()
            mesures.phi = Delta_t * 2*np.pi / T

    def mesurer_dephasage_par_rapport_a(self, other):
        assert isinstance(other, Signal3Mesure), "On peut mesurer le déphasage entre deux signaux"
        self.__mesurer_phi()
        other.__mesurer_phi()
        return self.__mesures_base.phi - other.__mesures_base.phi 
    
    def calculer_signal_trigger(self, trigger_bas = None, trigger_haut = None):
        self.__calculer_liste_i_trigger(trigger_bas, trigger_haut)
        base_de_temps = self.lire_base_de_temps()
        N = base_de_temps.calculer_N()
        vecteur_signal = np.zeros(N)

        for i in self.__mesures_base.liste_i_trigger:
            vecteur_signal[i] = 1

        sortie = self.copier( "trigger_" + self.lire_nom() )
        sortie._Signal1Base__vecteur_signal = vecteur_signal
        return sortie

    def lire_T(self):
        self.__mesurer_T()
        return self.__mesures_base.T

    def lire_Veff(self):
        self.__mesurer_Veff()
        return self.__mesures_base.Veff
    
    def lire_Vdc(self):
        self.__mesurer_Vdc()
        return self.__mesures_base.Vdc
    
    def lire_Vpp(self):
        self.__mesurer_Vpp()
        return self.__mesures_base.Vpp
    
    def lire_Vmax(self):
        self.__calculer_Vmax()
        return self.__mesures_base.Vmax
    
    def lire_Vmin(self):
        self.__calculer_Vmin()
        return self.__mesures_base.Vmin

    def lire_phi(self, unite = "deg", offset = 0):
        self.__mesurer_phi()
        k = 1
        if unite == "deg":
            k = 180/np.pi
        return mettre_en_forme_dephasage(self.__mesures_base.phi, offset)*k    

if __name__ == "__main__":
    F = 1
    liste_tmin_tmax = [0.1, 3.4]
    Te = 1e-6
    bdt = TempsBase(liste_tmin_tmax, Te)
    vecteur_t = bdt.calculer_vecteur_t()
    phi_deg = -340
    phi = phi_deg*np.pi/180
    vecteur_signal = np.cos(2*np.pi*F*vecteur_t  + phi)


    s = Signal3Mesure(bdt, vecteur_signal)

    s_trig = s.calculer_signal_trigger(-0.5, 0.5)
    
    s.plot()
    s_trig.plot()
    plt.show()

    print(s.lire_phi("deg", 4))
