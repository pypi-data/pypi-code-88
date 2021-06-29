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
from base.axe_x_base import AxeXBase
from base.mesure_base import MesureBase
from base.angle_base import AngleBase

from plot.plot_base import tracer

__all__ = ["Signal3Mesure"]

def mettre_en_forme_dephasage(phi, offset = 2):
    phi = phi % (2*np.pi)
    if phi > np.pi*(2-offset/2):
        phi -= 2*np.pi
    return phi

class Signal3Mesure(Signal2Arithmetique):
    def __lire_mesure_base(self):
        try:
            mesure_base = self.__mesure_base
        except:
            self.__mesure_base = mesure_base = MesureBase()
        return mesure_base

    def forcer_T_th(self, T_th):
        mesures = self.__lire_mesure_base()
        mesures.T_th = T_th

    def __mesurer_Vmax(self):
        mesures = self.__lire_mesure_base()
        if mesures.Vmax == None:
            mesures.Vmax = np.max(self.lire_vecteur_y())

    def __mesurer_Vmin(self):
        mesures = self.__lire_mesure_base()
        if mesures.Vmin == None:
            mesures.Vmin = np.min(self.lire_vecteur_y())

    def __calculer_liste_i_trigger_conf(self, trigger_bas, trigger_haut):
        mesures = self.__lire_mesure_base()
        trigger = True
        mesures.liste_i_trigger = []
        vecteur_y = self.lire_vecteur_y()
        N = len(vecteur_y)
        for i in range(N):
            if trigger == False and vecteur_y[i] > trigger_haut:
                trigger = True
                mesures.liste_i_trigger.append(i)
            elif trigger == True and vecteur_y[i] < trigger_bas:
                trigger = False

    def __calculer_liste_i_trigger(self, trigger_bas = None, trigger_haut = None):
        mesures = self.__lire_mesure_base()
        test_init = False
        if mesures.liste_i_trigger == None:
            test_init = True
        elif (mesures.trigger_bas != None and mesures.trigger_bas != trigger_bas):
            test_init = True
        elif (mesures.trigger_haut != None and mesures.trigger_haut != trigger_haut):
            test_init = True

        if test_init:
            self.__mesurer_Vmin()
            self.__mesurer_Vmax()
            _trigger_haut = ( mesures.Vmin + mesures.Vmax ) / 2
            _trigger_bas = ( 3*mesures.Vmin + mesures.Vmax ) / 4
            
            if trigger_bas == None:
                trigger_bas = _trigger_bas
            if trigger_haut == None:
                trigger_haut = _trigger_haut

            mesures.trigger_bas, mesures.trigger_haut = trigger_bas, trigger_haut
            self.__calculer_liste_i_trigger_conf(trigger_bas, trigger_haut)

    def __mesurer_T(self):
        mesures = self.__lire_mesure_base()
        if mesures.T == None:
            self.__calculer_liste_i_trigger()
            liste_Delta_i = []
            i = 1
            for i in range(1, len(mesures.liste_i_trigger)):
                liste_Delta_i.append(mesures.liste_i_trigger[i] - mesures.liste_i_trigger[i-1])

            if len(liste_Delta_i) > 0:
                axe_x_base = self._PlotBase__lire_axe_x_base()
                mesures.T = np.mean(liste_Delta_i) * axe_x_base.NXa / 10**axe_x_base.Pa

    def __choisir_T(self):
        self.__mesurer_T()
        T = self.__mesure_base.T
        if T == None:
            T = self.__mesure_base.T_th
        assert T != None, "Mesures pas assez d'échantillons pour faire des mesures. Forcer T_th ou augmenter la durée du signal."
        return T
                
    def __mesurer_sur_chaque_periodes_disponibles(self, fonction):
        T = self.__choisir_T()
        axe_x_base = self._PlotBase__lire_axe_x_base()
        vecteur_y = self.lire_vecteur_y()

        iXe = int( np.round( T * 10**axe_x_base.Pa / axe_x_base.NXa ) )


        N = len(vecteur_y)
        P = int( np.floor( N/iXe ) )
        assert P > 0, "pas assez d'échantillons pour faire des mesures. Augmenter la durée du signal."
        return np.mean( [ fonction(vecteur_y[i*iXe: (i+1)*iXe]) for i in range(P) ] )


    def __mesurer_Vdc(self):
        mesures = self.__lire_mesure_base()
        if mesures.Vdc == None:
            mesures.Vdc = self.__mesurer_sur_chaque_periodes_disponibles(np.mean)

    def __mesurer_Vpp(self):
        mesures = self.__lire_mesure_base()
        if mesures.Vpp == None:
            mesures.Vpp = self.__mesurer_sur_chaque_periodes_disponibles( lambda x: np.max(x) - np.min(x) )

    def __mesurer_Veff(self):
        mesures = self.__lire_mesure_base()
        if mesures.Veff == None:
            mesures.Veff = self.__mesurer_sur_chaque_periodes_disponibles( lambda x: np.sqrt(np.mean(x*x)) )

    def __mesurer_phi(self):
        mesures = self.__lire_mesure_base()
        if mesures.phi == None:
            axe_x_base = self._PlotBase__lire_axe_x_base()
            vecteur_x = axe_x_base.lire_vecteur_x()
            T = self.__choisir_T()

            vecteur_cos = np.cos(2*np.pi*vecteur_x/T)
            signal_cos = Signal3Mesure(axe_x_base, vecteur_cos, "cos")

            signal_cos.__calculer_liste_i_trigger()
            self.__calculer_liste_i_trigger()

            N = min(len(self.__mesure_base.liste_i_trigger), len(signal_cos.__mesure_base.liste_i_trigger))
            
            liste_Delta_i = [signal_cos.__mesure_base.liste_i_trigger[i]-self.__mesure_base.liste_i_trigger[i] for i in range(N)]

            Delta_i = np.mean(liste_Delta_i)
            Delta_t = Delta_i * axe_x_base.NXa / 10**axe_x_base.Pa
            phi = AngleBase(Delta_t * 2*np.pi / T)
            mesures.phi = phi.lire_angle()

    def lire_dephasage_par_rapport_a(self, other):
        assert isinstance(other, Signal3Mesure), "On peut mesurer le déphasage entre deux signaux"
        self.__mesurer_phi()
        other.__mesurer_phi()
        phi = AngleBase(self.__mesure_base.phi - other.__mesure_base.phi)
        return phi.lire_angle() 
    
    def calculer_signal_trigger(self, trigger_bas = None, trigger_haut = None, nom = ""):
        self.__calculer_liste_i_trigger(trigger_bas, trigger_haut)
        axe_x_base = self._PlotBase__lire_axe_x_base()
        N = axe_x_base.lire_N()
        vecteur_y = np.zeros(N)

        for i in self.__mesure_base.liste_i_trigger:
            vecteur_y[i] = 1
        sortie = self.copier()
        sortie._Signal1Base__nom = nom = "trigger_" + self.lire_nom() if nom == "" else nom
        sortie._Signal1Base__vecteur_y = vecteur_y
        return sortie

    def lire_T(self):
        self.__mesurer_T()
        return self.__mesure_base.T

    def lire_Veff(self):
        self.__mesurer_Veff()
        return self.__mesure_base.Veff
    
    def lire_Vdc(self):
        self.__mesurer_Vdc()
        return self.__mesure_base.Vdc
    
    def lire_Vpp(self):
        self.__mesurer_Vpp()
        return self.__mesure_base.Vpp
    
    def lire_Vmax(self):
        self.__mesurer_Vmax()
        return self.__mesure_base.Vmax
    
    def lire_Vmin(self):
        self.__mesurer_Vmin()
        return self.__mesure_base.Vmin

    def lire_phi(self, deg = False):
        self.__mesurer_phi()
        return AngleBase(self.__mesure_base.phi).lire_angle(deg)    

if __name__ == "__main__":
    F = 1
    liste_xmin_xmax = [0.1, 3.4]
    Xe = 1e-3
    bdt = AxeXBase(liste_xmin_xmax, Xe)
    vecteur_x = bdt.lire_vecteur_x()
    phi_deg = -340
    phi = phi_deg*np.pi/180
    vecteur_y = np.cos(2*np.pi*F*vecteur_x  + phi)


    s = Signal3Mesure(bdt, vecteur_y)

    s_trig = s.calculer_signal_trigger(-0.5, 0.5)
    
    tracer(s, s_trig)

    print(s.lire_phi())
