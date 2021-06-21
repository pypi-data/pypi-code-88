#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 15:43:58 2019

@author: nicolas
"""

import os, sys

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))

import base.constantes_base as cst

from signaux.signal_base import SignalBase
import base.utiles_base as utb
from base.temps_base import BaseTemps
from signaux.signal_complet import SignalComplet

import numpy as np


__all__ = ["SignalGBF"]

liste_types_signaux_gbf = ["cosinus", "carre", "triangle"]

class SignalSinus(SignalComplet):
    def __init__(self, F, Vpp, offset, phi, tr, liste_tmin_tmax, Te, nom):
        T = 1/F
        if T < liste_tmin_tmax[1]-liste_tmin_tmax[0]:        
            base_de_temps_periode = BaseTemps([0, 1/F], Te)
            base_de_temps = BaseTemps(liste_tmin_tmax, Te)

            Nperiode = base_de_temps_periode.convertir_n_vers_i(base_de_temps_periode.Nmax)
            Nsignal = base_de_temps.convertir_n_vers_i(base_de_temps.Nmax)

            Nretard = base_de_temps.calculer_n(tr) - base_de_temps.Nmin
            decalage_retard = Nretard % Nperiode

            vecteur_t_periode = base_de_temps_periode.calculer_vecteur_t()
            vecteur_signal_periode = np.roll(offset + Vpp*np.cos(2*np.pi*F*vecteur_t_periode + phi)/2, decalage_retard)

            SignalComplet.__init__(self, base_de_temps, utb.periodiser(Nsignal, vecteur_signal_periode), nom)
        else:
            base_de_temps = BaseTemps(liste_tmin_tmax, Te)

            tr = tr%T

            vecteur_t = base_de_temps.calculer_vecteur_t() - tr
            vecteur_signal = offset + Vpp*np.cos(2*np.pi*F*vecteur_t + phi)/2

            SignalComplet.__init__(self, base_de_temps, vecteur_signal, nom)

        self.mesures.T_th = T

class SignalCarre(SignalComplet):
    def __init__(self, F, Vpp, offset, alpha, tr, liste_tmin_tmax, Te, nom):
        T = 1/F
        tmin, tmax = liste_tmin_tmax
        alpha = max(alpha, 0)
        alpha = min(alpha, 1)
        if T < tmax - tmin:        
            base_de_temps_periode = BaseTemps([0, 1/F], Te)
            base_de_temps = BaseTemps(liste_tmin_tmax, Te)

            Nperiode = base_de_temps_periode.convertir_n_vers_i(base_de_temps_periode.Nmax)
            Nsignal = base_de_temps.convertir_n_vers_i(base_de_temps.Nmax)

            Nalpha = int(np.round(alpha*Nperiode))
            Nretard = base_de_temps.calculer_n(tr) - base_de_temps.Nmin
            decalage_retard = Nretard % Nperiode

            vecteur_signal_periode = np.roll(np.concatenate([np.ones(Nalpha)/2, -np.ones(Nperiode-Nalpha)/2])*Vpp+offset, decalage_retard)

            SignalComplet.__init__(self, base_de_temps, utb.periodiser(Nsignal, vecteur_signal_periode), nom)
        else:
            base_de_temps = BaseTemps(liste_tmin_tmax, Te)

            tmontant = np.ceil((tmin-tr)/T)*T+tr
            tdescendant = (np.ceil((tmin-tr)/T-alpha)+alpha)*T+tr

            if tmin <= tmontant <= tmax:
                n_montant = base_de_temps.calculer_n(tmontant)
                i_montant = base_de_temps.convertir_n_vers_i(n_montant)
            elif tmontant <= tmin:
                i_montant = 0
            else:
                i_montant = base_de_temps.N

            if tmin <= tdescendant <= tmax:
                n_descendant = base_de_temps.calculer_n(tdescendant)
                i_descendant = base_de_temps.convertir_n_vers_i(n_descendant)
            elif tmontant <= tmin:
                i_descendant = 0
            else:
                i_descendant = base_de_temps.N

            if i_montant <= i_descendant:
                vecteur_signal =np.zeros(base_de_temps.N)
                vecteur_signal[i_montant:i_descendant] = np.ones(i_descendant-i_montant)
            else:
                vecteur_signal =np.ones(base_de_temps.N)
                vecteur_signal[i_descendant:i_montant] = np.zeros(i_montant-i_descendant)


            base_de_temps = BaseTemps(liste_tmin_tmax, Te)

            SignalComplet.__init__(self, base_de_temps, Vpp*(vecteur_signal-0.5)+offset, nom)

        self.mesures.T_th = T

class SignalTriangle(SignalComplet):
    def __init__(self, F, Vpp, offset, alpha, tr, liste_tmin_tmax, Te, nom):
        T = 1/F
        tmin, tmax = liste_tmin_tmax
        alpha = max(alpha, 0)
        alpha = min(alpha, 1)
        if T < tmax - tmin:        

            base_de_temps_periode = BaseTemps([0, 1/F], Te)
            base_de_temps = BaseTemps(liste_tmin_tmax, Te)

            Nperiode = base_de_temps_periode.convertir_n_vers_i(base_de_temps_periode.Nmax)
            Nsignal = base_de_temps.convertir_n_vers_i(base_de_temps.Nmax)

            Nalpha = int(np.round(alpha*Nperiode))
            Nretard = base_de_temps.calculer_n(tr) - base_de_temps.Nmin
            decalage_retard = Nretard % Nperiode

            vecteur_signal_periode = np.roll(np.concatenate([np.linspace(-0.5, 0.5,Nalpha), np.linspace(0.5, -0.5, Nperiode-Nalpha)])*Vpp+offset, decalage_retard)

            SignalComplet.__init__(self, base_de_temps, utb.periodiser(Nsignal, vecteur_signal_periode), nom)
        else:
            base_de_temps = BaseTemps(liste_tmin_tmax, Te)

            tmontant = np.ceil((tmin-tr)/T)*T+tr
            tdescendant = (np.ceil((tmin-tr)/T-alpha)+alpha)*T+tr

            if tmin <= tmontant <= tmax:
                i_montant = base_de_temps.convertir_n_vers_i(base_de_temps.calculer_n(tmontant))
            elif tmontant <= tmin:
                i_montant = 0
            else:
                i_montant = base_de_temps.N

            if tmin <= tdescendant <= tmax:
                i_descendant = base_de_temps.convertir_n_vers_i(base_de_temps.calculer_n(tdescendant))
            elif tmontant <= tmin:
                i_descendant = 0
            else:
                i_descendant = base_de_temps.N

            vecteur_signal = np.zeros(base_de_temps.N)
            if tmontant <= tdescendant:
                u_tmin = (tmontant-tmin)/((1-alpha)*T)
                if tmontant >= tmax:
                    u_tmax = (tmontant-tmax)/((1-alpha)*T)
                    vecteur_signal = np.linspace(u_tmin, u_tmax, base_de_temps.N)
                else:
                    vecteur_signal[0:i_montant] = np.linspace(u_tmin, 0, i_montant)
                    if tdescendant >= tmax:
                        u_tmax = (tmax-tmontant)/(alpha*T)
                        vecteur_signal[i_montant:base_de_temps.N] = np.linspace(0, u_tmax, base_de_temps.N-i_montant)
                    else:
                        vecteur_signal[i_montant:i_descendant] = np.linspace(0, 1, i_descendant-i_montant)
                        u_tmax = (T+tmontant-tmax)/((1-alpha)*T)
                        vecteur_signal[i_descendant:base_de_temps.N] = np.linspace(1, u_tmax, base_de_temps.N-i_descendant)
            else:
                u_tmin = (tmin-tmontant+T)/(alpha*T)
                if tdescendant >= tmax:
                    u_tmax = (tmax-tmontant+T)/(alpha*T)
                    vecteur_signal = np.linspace(u_tmin, u_tmax, base_de_temps.N)
                else:
                    vecteur_signal[:i_descendant] = np.linspace(u_tmin, 1, i_descendant)
                    if tmontant >= tmax:
                        u_tmax = (tmontant-tmax)/((1-alpha)*T)
                        vecteur_signal[i_descendant:base_de_temps.N] = np.linspace(1, u_tmax, base_de_temps.N-i_descendant)
                    else:
                        vecteur_signal[i_descendant:i_montant] = np.linspace(1, 0, i_montant-i_descendant)
                        u_tmax = (tmax-tmontant)/(alpha*T)
                        vecteur_signal[i_montant:base_de_temps.N] = np.linspace(0, u_tmax, base_de_temps.N-i_montant)

            SignalComplet.__init__(self, base_de_temps, Vpp*(vecteur_signal-0.5)+offset, nom)

        self.mesures.T_th = T

class SignalGBF(SignalComplet):
    def __init__(self, type_signal = "cosinus", F=1, Vpp= 1, offset = 0, tr=0., phi = 0., alpha = 0.5, liste_tmin_tmax = cst.liste_tmin_tmax, Te = cst.Te, nom = ""):
        if type_signal not in liste_types_signaux_gbf:
            print("Ce type de signaux n'existe pas")
            sys.exit()
        if type_signal == "cosinus":
            SignalSinus.__init__(self, F, Vpp, offset, phi, tr, liste_tmin_tmax, Te, nom)
        elif type_signal == "carre":
            SignalCarre.__init__(self, F, Vpp, offset, alpha, tr, liste_tmin_tmax, Te, nom)
        elif type_signal == "triangle":
            SignalTriangle.__init__(self, F, Vpp, offset, alpha, tr, liste_tmin_tmax, Te, nom)

if __name__ == "__main__":
    bdt = BaseTemps(cst.liste_tmin_tmax, cst.Te)

    s = SignalGBF("triangle", 1, Vpp = 5, liste_tmin_tmax = [0,0.99], tr = -0.2, alpha = 0.5, phi=-np.pi/2)
    s.tracer_signal()
    # liste_tmin_tmax=[0, 1]
    # F = 2
    # phi = 0.2
    # tr = phi/(2*np.pi*F)
    # s1 = SignalGBF("carre", 3, 2, 1, tr = 0.1, phi = 3, nom="$s_1$")
    
    # s1.tracer_signal()


    print("fin")