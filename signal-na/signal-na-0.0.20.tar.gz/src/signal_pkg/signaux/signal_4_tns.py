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
from signaux.signal_3_mesure import Signal3Mesure
from base.temps_base import TempsBase
from base.can_base import CANBase

class Signal4TNS(Signal3Mesure):
    def echantillonner(self, Te, nom = ""):
        base_de_temps_entree = self.lire_base_de_temps()
        liste_tmin_tmax = base_de_temps_entree.calculer_liste_tmin_tmax()
        base_de_temps_sortie = TempsBase(liste_tmin_tmax, Te)
        P = base_de_temps_sortie.lire_NTa() / base_de_temps_entree.lire_NTa()
        test_Te = np.abs(P - np.round(P))/P < 1e-6
        assert test_Te, "echantillonner: La péride d'échantillonnage ne convient pas"
        P = int(P)

        sortie = self.sous_echantillonner(P).sur_echantillonner(P)
        
        if nom == "":
            sortie._Signal1Base__nom = self.lire_nom() + "_échantillonné"
        else:
            sortie._Signal1Base__nom = nom
        return sortie

    def echantillonner_bloquer(self, Te, nom = ""):
        base_de_temps_entree = self.lire_base_de_temps()
        liste_tmin_tmax = base_de_temps_entree.calculer_liste_tmin_tmax()
        base_de_temps_sortie = TempsBase(liste_tmin_tmax, Te)
        P = base_de_temps_sortie.lire_NTa() / base_de_temps_entree.lire_NTa()
        test_Te = np.abs(P - np.round(P))/P < 1e-6
        assert test_Te, "echantillonner: La péride d'échantillonnage doit être un multiple de la période d'échantillonnage originale"
        P = int(P)
        sortie = (self.sous_echantillonner(P).sur_echantillonner(P)).bloquer(P)
        
        if nom == "":
            sortie._Signal1Base__nom = self.lire_nom() + "_échantillonné_bloqué"
        else:
            sortie._Signal1Base__nom = nom
        return sortie

        pass

    def sous_echantillonner(self, P):
        base_de_temps_entree = self.lire_base_de_temps()
        liste_tmin_tmax = base_de_temps_entree.calculer_liste_tmin_tmax()
        Te_entree = base_de_temps_entree.calculer_Te()
        Te_sortie = P * Te_entree
        base_de_temps_sortie = TempsBase(liste_tmin_tmax, Te_sortie)
        vecteur_t_sortie = base_de_temps_sortie.calculer_vecteur_t()
        vecteur_ia_sortie = base_de_temps_sortie._TempsBase__convertir_t_vers_ia(vecteur_t_sortie)
        vecteur_i_entree = base_de_temps_entree._TempsBase__convertir_ia_vers_i(vecteur_ia_sortie)
        
        vecteur_signal = self.lire_vecteur_signal()

        sortie = self.copier()
        sortie._Signal1Base__base_de_temps = base_de_temps_sortie
        sortie._Signal1Base__vecteur_signal = vecteur_signal[vecteur_i_entree]
        sortie._Signal1Base__nom = self.lire_nom() + "_sous_échantillonné_{0}".format(P)
        return sortie

    def sur_echantillonner(self, P):
        base_de_temps_entree = self.lire_base_de_temps()
        Te_entree = base_de_temps_entree.calculer_Te()
        Te_sortie = Te_entree / P
        NTa = Te_sortie * 10**base_de_temps_entree.lire_Pa()
        test_Te = np.abs(np.round(NTa) - NTa) < 1e-6
        chaine_erreur = "sur_echantillonner: la nouvelle période d'échantillonnage n'est pas un multiple de {0}".format(10**-base_de_temps_entree.lire_Pa())
        assert test_Te, chaine_erreur

        liste_tmin_tmax = base_de_temps_entree.calculer_liste_tmin_tmax()
        base_de_temps_sortie = TempsBase(liste_tmin_tmax, Te_sortie)
        vecteur_t_entree = base_de_temps_entree.calculer_vecteur_t()
        vecteur_ia_entree = base_de_temps_entree._TempsBase__convertir_t_vers_ia(vecteur_t_entree)
        vecteur_i_sortie = base_de_temps_sortie._TempsBase__convertir_ia_vers_i(vecteur_ia_entree)
        
        vecteur_signal = self.lire_vecteur_signal()
        N_sortie = base_de_temps_sortie.calculer_N()
        sortie = self.copier()
        sortie._Signal1Base__base_de_temps = base_de_temps_sortie
        sortie._Signal1Base__vecteur_signal = np.zeros(N_sortie)
        sortie._Signal1Base__vecteur_signal[vecteur_i_sortie] = vecteur_signal
        sortie._Signal1Base__nom = self.lire_nom() + "_sur_échantillonné_{0}".format(P)
        return sortie

    def bloquer(self, P, nom = ""):
        vecteur_signal = self.lire_vecteur_signal()
        N = len(vecteur_signal)

        vecteur_porte = np.ones(P)
        vecteur_signal = np.convolve(vecteur_signal, vecteur_porte)[0:N]

        sortie = self.copier()
        sortie._Signal1Base__vecteur_signal = vecteur_signal
        
        if nom == "":
            sortie._Signal1Base__nom = self.lire_nom() + "_bloqué_{0}".format(P)
        else:
            sortie._Signal1Base__nom = nom
        return sortie

    def extrapoler(self, P, nom = ""):
        vecteur_signal = self.lire_vecteur_signal()
        N = len(vecteur_signal)

        vecteur_triangle = np.concatenate( [np.linspace(0, 1, P+1), np.linspace(1, 0, P+1)[1:]])
        vecteur_signal = np.convolve(vecteur_signal, vecteur_triangle)[P:N+P]

        sortie = self.copier()
        sortie._Signal1Base__vecteur_signal = vecteur_signal
        
        if nom == "":
            sortie._Signal1Base__nom = self.lire_nom() + "_extrapolé_{0}".format(P)
        else:
            sortie._Signal1Base__nom = nom
        return sortie


    def quantifier(self, Pbits = 8, liste_umin_umax=[-10., 10.], nom = ""):
        sortie = self.convertir_analogique_vers_numerique(Pbits, liste_umin_umax).convertir_numerique_vers_analogique()
        if nom == "":
            sortie._Signal1Base__nom = self.lire_nom() + "_quantifié_{0}".format(Pbits)
        else:
            sortie._Signal1Base__nom = nom
        return sortie

    def changer_Te(self, Te, nom = ""):
        def pgcd(a, b):
            while b != 0:
                a, b = b, a%b
            return a

        print("zorro")
        base_de_temps_entree = self.lire_base_de_temps()
        liste_tmin_tmax = base_de_temps_entree.calculer_liste_tmin_tmax()
        base_de_temps_sortie = TempsBase(liste_tmin_tmax, Te)

        NTa_entree, NTa_sortie = base_de_temps_entree.lire_NTa(), base_de_temps_sortie.lire_NTa()
        k = pgcd(NTa_entree, NTa_sortie)

        P1, P2 = int(NTa_entree/k), int(NTa_sortie/k)
        print(P1, P2)
        sortie = self.sur_echantillonner(P1).extrapoler(P1).sous_echantillonner(P2)
        if nom == "":
            sortie._Signal1Base__nom = self.lire_nom() + "_Te_changé"
        else:
            sortie._Signal1Base__nom = nom

        return sortie

    def convertir_analogique_vers_numerique(self, Pbits = 8, liste_umin_umax=[-10., 10.], nom = ""):
        base_can = self.lire_base_can()
        base_can.Pbits = Pbits
        base_can.liste_umin_umax = liste_umin_umax

        sortie = self.copier()
        vecteur_signal = sortie.lire_vecteur_signal()
        umin, umax = liste_umin_umax
        Nmin = -2**(Pbits-1)
        Nmax = -Nmin-1 
        vecteur_signal = np.clip( np.floor( ( 2*vecteur_signal - (umax+umin) ) / (umax - umin)* 2**(Pbits-1) ), Nmin, Nmax).astype(np.int64)
        sortie._Signal1Base__vecteur_signal = vecteur_signal
        if nom == "":
            sortie._Signal1Base__nom = self.lire_nom() + "_can"
        else:
            sortie._Signal1Base__nom = nom
        return sortie

    def convertir_numerique_vers_analogique(self, nom = ""):
        base_can = self.lire_base_can()

        Pbits = base_can.Pbits
        liste_umin_umax = base_can.liste_umin_umax 
        
        assert Pbits != None and liste_umin_umax !=None, "convertir_numerique_vers_analogique: le signal n'est pas numérique"

        sortie = self.copier()
        vecteur_signal = sortie.lire_vecteur_signal()
        umin, umax = liste_umin_umax
        vecteur_signal =   (vecteur_signal+0.5) * (umax - umin) / 2**Pbits + (umax+umin) / 2
        sortie._Signal1Base__vecteur_signal = vecteur_signal
        if nom == "":
            sortie._Signal1Base__nom = self.lire_nom() + "_cna"
        else:
            sortie._Signal1Base__nom = nom
        return sortie

    def numeriser(self, Te, Pbits = 8, liste_umin_umax=[-10., 10.], nom = ""):
        sortie = self.changer_Te(Te).convertir_analogique_vers_numerique(Pbits, liste_umin_umax)
        if nom == "":
            sortie._Signal1Base__nom = self.lire_nom() + "_numerisé"
        else:
            sortie._Signal1Base__nom = nom
        return sortie

    def lire_base_can(self):
        try:
            self.__base_can
        except:
            self.__base_can = CANBase()
        return self.__base_can
        
if __name__ == "__main__":
    Te = 1e-5
    liste_tmin_tmax = [0, 1]
    bdt = TempsBase(liste_tmin_tmax, Te)
    vecteur_t = bdt.calculer_vecteur_t()
    vecteur_signal = 0.9*np.cos(2*np.pi*3*vecteur_t)
    s1 = Signal4TNS(bdt, vecteur_signal)
    P = 4
    s2 = s1.numeriser(1e-3, P, [-1, 1])


    s1.plot()
    s2.plot()
    plt.legend()
    plt.show()
    print("fin")
    
    
    bdt1 =s1.lire_base_de_temps()
    bdt2 =s2.lire_base_de_temps()
    
    print(bdt1, bdt2)