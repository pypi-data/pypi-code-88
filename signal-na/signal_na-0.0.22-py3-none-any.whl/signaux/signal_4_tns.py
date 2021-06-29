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
from base.axe_base import AxeBase
from base.axe_x_base import AxeXBase, calculer_axe_x_base
from base.can_base import CANBase
from plot.plot_base import tracer

class Signal4TNS(Signal3Mesure):
    def sous_echantillonner(self, P, nom = ""):
        axe_x_base_entree = self._PlotBase__lire_axe_x_base()
        liste_xmin_xmax = axe_x_base_entree.calculer_liste_xmin_xmax()
        Xe_entree = axe_x_base_entree.lire_Xe()
        Xe_sortie = P * Xe_entree
        axe_x_base_sortie = AxeXBase(liste_xmin_xmax, Xe_sortie)
        vecteur_x_sortie = axe_x_base_sortie.lire_vecteur_x()
        vecteur_ia_sortie = axe_x_base_sortie.convertir_x_vers_ia(vecteur_x_sortie)
        vecteur_i_entree = axe_x_base_entree.convertir_ia_vers_ie(vecteur_ia_sortie)
        
        vecteur_y = self.lire_vecteur_y()

        sortie = self.copier()
        sortie._PlotBase__axe_x_base = axe_x_base_sortie
        sortie._Signal1Base__vecteur_y = vecteur_y[vecteur_i_entree]
        if nom == "":
            sortie._Signal1Base__nom = self.lire_nom() + "_sous_échantillonné_bloqué{0}".format(P)
        else:
            sortie._Signal1Base__nom = nom
        return sortie

    def sur_echantillonner(self, P, nom = ""):
        axe_x_base_entree = self._PlotBase__lire_axe_x_base()
        NTa = axe_x_base_entree.NXa
        assert NTa % P == 0, "Impossible de suréchantilloner. La période d'échantillonnage finale doit être multiple de {0} s".format(10**-axe_x_base_entree.Pa)
        Xe_entree = axe_x_base_entree.lire_Xe()
        Xe_sortie = Xe_entree / P

        liste_xmin_xmax = axe_x_base_entree.calculer_liste_xmin_xmax()
        axe_x_base_sortie = AxeXBase(liste_xmin_xmax, Xe_sortie)
        vecteur_x_entree = axe_x_base_entree.lire_vecteur_x()
        vecteur_ia_entree = axe_x_base_entree.convertir_x_vers_ia(vecteur_x_entree)
        vecteur_i_sortie = axe_x_base_sortie.convertir_ia_vers_ie(vecteur_ia_entree)
        
        vecteur_y = self.lire_vecteur_y()
        N_sortie = axe_x_base_sortie.lire_N()
        sortie = self.copier()
        sortie._PlotBase__axe_x_base = axe_x_base_sortie
        sortie._Signal1Base__vecteur_y = np.zeros(N_sortie)
        sortie._Signal1Base__vecteur_y[vecteur_i_sortie] = vecteur_y
        if nom == "":
            sortie._Signal1Base__nom = self.lire_nom() + "_sur_échantillonné_{0}".format(P)
        else:
            sortie._Signal1Base__nom = nom
        return sortie

    def echantillonner(self, Xe, nom = ""):
        assert self._PlotBase__lire_axe_x_base().NXa == 1, 'Le signal d\'entrée doit être "analogique"'        
        axe_x_base_sortie = AxeXBase(self._PlotBase__lire_axe_x_base().calculer_liste_xmin_xmax(), Xe)        
        P = axe_x_base_sortie.NXa
        sortie = self.sous_echantillonner(P).sur_echantillonner(P)
        if nom == "":
            sortie._Signal1Base__nom = self.lire_nom() + "_échantillonné"
        else:
            sortie._Signal1Base__nom = nom
        return sortie


    def bloquer(self, P, nom = ""):
        vecteur_y = self.lire_vecteur_y()
        N = len(vecteur_y)

        vecteur_porte = np.ones(P)
        vecteur_y = np.convolve(vecteur_y, vecteur_porte)[0:N]

        sortie = self.copier()
        sortie._Signal1Base__vecteur_y = vecteur_y
        
        if nom == "":
            sortie._Signal1Base__nom = self.lire_nom() + "_bloqué_{0}".format(P)
        else:
            sortie._Signal1Base__nom = nom
        return sortie

    def extrapoler(self, P, nom = ""):
        vecteur_y = self.lire_vecteur_y()
        N = len(vecteur_y)

        vecteur_xriangle = np.concatenate( [np.linspace(0, 1, P+1), np.linspace(1, 0, P+1)[1:]])
        vecteur_y = np.convolve(vecteur_y, vecteur_xriangle)[P:N+P]

        sortie = self.copier()
        sortie._Signal1Base__vecteur_y = vecteur_y
        
        if nom == "":
            sortie._Signal1Base__nom = self.lire_nom() + "_extrapolé_{0}".format(P)
        else:
            sortie._Signal1Base__nom = nom
        return sortie


    def quantifier(self, Pbits = 8, liste_umin_umax=[-10., 10.], nom = ""):
        sortie = self.__convertir_analogique_vers_numerique(Pbits, liste_umin_umax).__convertir_numerique_vers_analogique()
        if nom == "":
            sortie._Signal1Base__nom = self.lire_nom() + "_quantifié_{0}".format(Pbits)
        else:
            sortie._Signal1Base__nom = nom
        return sortie

    def __convertir_analogique_vers_numerique(self, Pbits = 8, liste_umin_umax=[-10., 10.], nom = ""):
        can_base = self.__lire_can_base()
        can_base.Pbits = Pbits
        can_base.liste_umin_umax = liste_umin_umax

        sortie = self.copier()
        vecteur_y = sortie.lire_vecteur_y()
        umin, umax = liste_umin_umax
        Nmin = -2**(Pbits-1)
        Nmax = -Nmin-1 
        vecteur_y = np.clip( np.floor( ( 2*vecteur_y - (umax+umin) ) / (umax - umin)* 2**(Pbits-1) ), Nmin, Nmax).astype(np.int64)
        sortie._Signal1Base__vecteur_y = vecteur_y
        if nom == "":
            sortie._Signal1Base__nom = self.lire_nom() + "_can"
        else:
            sortie._Signal1Base__nom = nom
        return sortie

    def __convertir_numerique_vers_analogique(self, nom = ""):
        can_base = self.__lire_can_base()

        Pbits = can_base.Pbits
        liste_umin_umax = can_base.liste_umin_umax 
        
        assert Pbits != None and liste_umin_umax !=None, "__convertir_numerique_vers_analogique: le signal n'est pas numérique"

        sortie = self.copier()
        vecteur_y = sortie.lire_vecteur_y()
        umin, umax = liste_umin_umax
        vecteur_y =   (vecteur_y+0.5) * (umax - umin) / 2**Pbits + (umax+umin) / 2
        sortie._Signal1Base__vecteur_y = vecteur_y
        if nom == "":
            sortie._Signal1Base__nom = self.lire_nom() + "_cna"
        else:
            sortie._Signal1Base__nom = nom
        return sortie

    # def numeriser(self, Pbits = 8, liste_umin_umax=[-10., 10.], nom = ""):
    #     sortie = self.__convertir_analogique_vers_numerique(Pbits, liste_umin_umax)
    #     if nom == "":
    #         sortie._Signal1Base__nom = self.lire_nom() + "_numerisé"
    #     else:
    #         sortie._Signal1Base__nom = nom
    #     return sortie

    def __lire_can_base(self):
        try:
            self.__can_base
        except:
            self.__can_base = CANBase()
        return self.__can_base

    def calculer_spectre(self, nom = ""):
        ux = self._PlotBase__lire_axe_x_base().unite
        assert ux == "s", "Impossible de calculer le spectre de ce signal"

        sortie = self.copier()
        if nom:
            sortie._Signal1Base__nom = nom
        else:
            sortie._Signal1Base__nom = "spectre_" + self.lire_nom()
        bdt = self._PlotBase__lire_axe_x_base()
        N = bdt.lire_N()
        Xe = bdt.lire_Xe()
        vecteur_fft = np.fft.fft( self.lire_vecteur_y() )
        vecteur_f = np.arange(0, N)/(N*Xe)
        sortie._PlotBase__axe_x_base = calculer_axe_x_base(vecteur_f, "f", "Hz")
        sortie._PlotBase__axe_y_base = AxeBase("U", "V.Hz")

        sortie._Signal1Base__vecteur_y = vecteur_fft*2/N
        sortie._Signal1Base__vecteur_y[0] /= 2
        return sortie


    def calculer_fft(self, nom = ""):
        ux = self._PlotBase__lire_axe_x_base().unite
        assert ux == "s", "Impossible de calculer la FFT de ce signal"

        sortie = self.copier()
        if nom:
            sortie._Signal1Base__nom = nom
        else:
            sortie._Signal1Base__nom = "fft_" + self.lire_nom()
        bdt = self._PlotBase__lire_axe_x_base()
        N = bdt.lire_N()
        Xe = bdt.lire_Xe()
        vecteur_fft = np.fft.fft( self.lire_vecteur_y() )
        vecteur_f = np.arange(0, N)/(N*Xe)
        sortie._PlotBase__axe_x_base = calculer_axe_x_base(vecteur_f, "f", "Hz")
        sortie._PlotBase__axe_y_base = AxeBase("U", "V.Hz")

        sortie._Signal1Base__vecteur_y = vecteur_fft/N
        return sortie

    def calculer_ifft(self, nom = ""):
        ux = self._PlotBase__lire_axe_x_base().unite
        assert ux == "Hz", "Impossible de calculer la FFT inverse de ce signal"

        sortie = self.copier()
        if nom:
            sortie._Signal1Base__nom = nom
        else:
            sortie._Signal1Base__nom = "ifft_" + self.lire_nom()

        bdt = self._PlotBase__lire_axe_x_base()
        N = bdt.lire_N()
        Xe = bdt.lire_Xe()
        vecteur_fft = np.fft.ifft( self.lire_vecteur_y() )
        vecteur_f = np.arange(0, N)/(N*Xe)
        sortie._PlotBase__axe_x_base = calculer_axe_x_base(vecteur_f)
        sortie._PlotBase__axe_y_base = AxeBase("u", "V")
        sortie._Signal1Base__vecteur_y = np.real(vecteur_fft)*N
        return sortie

if __name__ == "__main__":
    liste_xmin_xmax = [0, 10e-3]
    bdt = AxeXBase(liste_xmin_xmax)
    vecteur_x = bdt.lire_vecteur_x()
    vecteur_y = 2*np.cos(2*np.pi*1e3*vecteur_x)
    s1 = Signal4TNS(bdt, vecteur_y)
    P = 4
    s1 = s1 + 1
    
    s2 = s1.calculer_fft()
    s3 = s2.calculer_ifft()
    s4 = s1.calculer_spectre()
    s3 = s2.calculer_ifft()
    s5 = s1.echantillonner(1e-4)
    s6 = s1.quantifier(8, [-10, 10])
    # tracer(s1, s4, s2, s3, s5, s6, superposition=False)

    print(s6._Signal4TNS__lire_can_base().liste_umin_umax)
    # bdt1 =s1._PlotBase__lire_axe_x_base()
    # bdt2 =s2._PlotBase__lire_axe_x_base()
    
    # print(bdt1, bdt2)