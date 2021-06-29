#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 15:43:58 2019

@author: nicolas
"""
import os, sys

import scipy.io.wavfile as wave
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
import matplotlib.pyplot as plt

# import time
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))

import numpy as np
from signaux.signal_4_tns import Signal4TNS
from base.axe_x_base import AxeXBase
from plot.plot_base import tracer

class Signal5Wav(Signal4TNS):
    def lire_wav(self, nom_fichier, Pbits = 16, liste_umin_max = [-10, 10]):
        Fe, data = wave.read(nom_fichier)
        Xe = 1/Fe
        N = len(data)
        xmax = 10*Xe
        axe_x_base = AxeXBase([0, xmax], Xe)
        Xe_eff = axe_x_base.lire_Xe()

        xmax_eff = N*Xe_eff
        
        axe_x_base = self._PlotBase__lire_axe_x_base()

        axe_x_base.cloner(AxeXBase([0, xmax_eff], Xe_eff))
        Nx = len(axe_x_base.lire_vecteur_x())
        self._Signal1Base__vecteur_y = data
        
        can_base = self._Signal4TNS__lire_can_base()
        can_base.Pbits = Pbits
        can_base.liste_umin_umax = liste_umin_max
        
        
    def ecouter_wav(self):
        self.enregistrer_wav(".tmp-123456789.wav")
        pygame.init()
        pygame.mixer.init()
        sounda = pygame.mixer.Sound(".tmp-123456789.wav")
        sounda.play()

        while pygame.mixer.get_busy():
            pass
        os.remove(".tmp-123456789.wav")

    def enregistrer_wav(self, nom_fichier):
        sortie = self.__mettre_en_forme_wav()
        Fe = int(1/sortie._PlotBase__lire_axe_x_base().lire_Xe())
        vecteur_y = sortie.lire_vecteur_y()
        wave.write(nom_fichier, Fe, vecteur_y)

    def __mettre_en_forme_wav(self):
        can_base = self._Signal4TNS__lire_can_base()
        assert can_base.Pbits != None, "__mettre_en_forme_wav: le signal n'est pas quantifié"
        assert can_base.Pbits <= 16, "__mettre_en_forme_wav: le signal est quantifié sur plus de 16 bits"
        Fe = 1/self._PlotBase__lire_axe_x_base().lire_Xe()

        assert Fe <= 50000, "__mettre_en_forme_wav: le signal est échantillonné à plus de 50kHz"
        can_base = self._Signal4TNS__lire_can_base()
        # sortie = self._Signal4TNS__convertir_numerique_vers_analogique()._Signal4TNS__convertir_analogique_vers_numerique(16, can_base.liste_umin_umax)
        sortie = self._Signal4TNS__convertir_analogique_vers_numerique(16, can_base.liste_umin_umax)
        vecteur_y = sortie._Signal1Base__vecteur_y
        sortie._Signal1Base__vecteur_y = vecteur_y.astype(np.int16)
        return sortie
                
        


if __name__ == "__main__":
    # s1 = Signal5Wav(AxeXBase())
    # s1.lire_wav("/Users/nicolas/tmp/A3.wav")
    # # s1.ecouter_wav()

    # bdt = s1._PlotBase__lire_axe_x_base()
    # Xe = bdt.lire_Xe()

    # s2 = s1.sous_echantillonner(100)
    # s2.enregistrer_wav("/Users/nicolas/tmp/test.wav")

    # axe_x_base2 = s2._PlotBase__lire_axe_x_base()
    # Xe = axe_x_base2.lire_Xe()
    # F = 1/(2*Xe)
    # print(F)
    # vecteur_x = axe_x_base2.lire_vecteur_x()
    # vecteur_y = 10*np.cos(2*np.pi*F*vecteur_x)
    # s3 = Signal5Wav(axe_x_base2, vecteur_y)._Signal4TNS__convertir_analogique_vers_numerique(16, [-10, 10])
    # s3.ecouter_wav()

    # s2.plot()
    # plt.show()
    Fe =20e3
    F1 = 1000
    F2 = Fe-F1

    Xe = 1/Fe
    bdt = AxeXBase([0, 1], Xe)
    vt = bdt.lire_vecteur_x()
    vs1 = np.sin(2*np.pi*F1*vt)
    vs2 = np.sin(2*np.pi*F2*vt)
    s1 = Signal5Wav(bdt, vs1)#.numeriser(Xe, 16, [-10, 10])
    s2 = Signal5Wav(bdt, vs2)#.numeriser(Xe, 16, [-10, 10])
    # s1.enregistrer_wav("/Users/nicolas/tmp/test.wav")
    # s1.ecouter_wav()#"/Users/nicolas/tmp/test.wav")

    tracer(s1, s2)
