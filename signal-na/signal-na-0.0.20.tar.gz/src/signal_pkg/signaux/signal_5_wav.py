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
from base.temps_base import TempsBase

class Signal5Wav(Signal4TNS):
    def lire_wav(self, nom_fichier, Pbits = 16, liste_umin_max = [-10, 10]):
        Fe, data = wave.read(nom_fichier)
        Te = 1/Fe
        N = len(data)
        tmax = N*Te
        self.lire_base_de_temps()

        self._Signal1Base__base_de_temps = TempsBase([0, tmax], Te)
        self._Signal1Base__vecteur_signal = data
        
        base_can = self.lire_base_can()
        base_can.Pbits = Pbits
        base_can.liste_umin_umax = liste_umin_max
        
        
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
        sortie = self.mettre_en_forme_wav()
        base_de_temps = sortie.lire_base_de_temps()
        Te = base_de_temps.calculer_Te()
        Fe = int(1/Te)
        vecteur_signal = sortie.lire_vecteur_signal()
        wave.write(nom_fichier, Fe, vecteur_signal)

    def mettre_en_forme_wav(self):
        base_can = self.lire_base_can()
        assert base_can.Pbits != None, "mettre_en_forme_wav: le signal n'est pas numérisé"
        assert base_can.Pbits <= 16, "mettre_en_forme_wav: le signal est numérisé sur plus de 16 bits"
        base_de_temps = self.lire_base_de_temps()
        Te = base_de_temps.calculer_Te()
        Fe = 1/Te
        assert Fe <= 50000, "mettre_en_forme_wav: le signal est échantillonné à plus de 50kHz"
        can_base = self.lire_base_can()
        sortie = self.convertir_numerique_vers_analogique().convertir_analogique_vers_numerique(16, can_base.liste_umin_umax)
        vecteur_signal = sortie._Signal1Base__vecteur_signal
        sortie._Signal1Base__vecteur_signal = vecteur_signal.astype(np.int16)
        return sortie
                
        


if __name__ == "__main__":
    # s1 = Signal5Wav(TempsBase())
    # s1.lire_wav("/Users/nicolas/tmp/A3.wav")
    # # s1.ecouter_wav()

    # bdt = s1.lire_base_de_temps()
    # Te = bdt.calculer_Te()

    # s2 = s1.sous_echantillonner(100)
    # s2.enregistrer_wav("/Users/nicolas/tmp/test.wav")

    # base_de_temps2 = s2.lire_base_de_temps()
    # Te = base_de_temps2.calculer_Te()
    # F = 1/(2*Te)
    # print(F)
    # vecteur_t = base_de_temps2.calculer_vecteur_t()
    # vecteur_signal = 10*np.cos(2*np.pi*F*vecteur_t)
    # s3 = Signal5Wav(base_de_temps2, vecteur_signal).convertir_analogique_vers_numerique(16, [-10, 10])
    # s3.ecouter_wav()

    # s2.plot()
    # plt.show()
    Fe =20e3
    F1 = 1000
    F2 = Fe-F1

    Te = 1/Fe
    bdt = TempsBase([0, 1], Te)
    vt = bdt.calculer_vecteur_t()
    vs1 = np.sin(2*np.pi*F1*vt)
    vs2 = np.sin(2*np.pi*F2*vt)
    s1 = Signal5Wav(bdt, vs1)#.numeriser(Te, 16, [-10, 10])
    s2 = Signal5Wav(bdt, vs2)#.numeriser(Te, 16, [-10, 10])
    # s1.enregistrer_wav("/Users/nicolas/tmp/test.wav")
    # s1.ecouter_wav()#"/Users/nicolas/tmp/test.wav")

    s1.plot()
    s2.plot()
    plt.show()