#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 15:43:58 2019

@author: nicolas
"""
import copy
import numpy as np

import os, sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))
from base.temps_base import BaseTemps
from base.frequence_base import BaseFrequence
from base.mesure_base import Mesures
from base.voie_base import Voie
from base.trigger_base import Trigger

__all__ = ["SignalBase", "convertir_liste_signaux_vers_str", "convertir_liste_paires_signaux_vers_str", "afficher_liste_paires_signaux", "afficher_liste_signaux", "lister_signaux_test", "lister_paires_signaux_test"]


class SignalBase():

    liste_n_signaux = [0]

    def __init__(self, base_de_temps, vecteur_signal = [], nom = ""):
        self.base_de_temps = base_de_temps.copier()
        self.base_de_frequence = BaseFrequence(base_de_temps)
        self.mesures = Mesures()
        self.voie = Voie()
        self.trigger = Trigger()


        self.__chercher_nom_valide(nom)
        if len(vecteur_signal) > 0:
            self.vecteur_signal = vecteur_signal
        else:
            self.vecteur_signal = np.zeros(self.base_de_temps.N)

        if base_de_temps.N != len(self.vecteur_signal):
            print("Constructeur Signal: la base de temps et le vecteur_signal sont incompatibles")


    def copier(self, nom = ""):
        sortie = copy.deepcopy(self)
        sortie.mesures = Mesures()
        sortie.voie = Voie()
        sortie.trigger = Trigger()
        if nom != "":
            sortie.nom = nom + "_copié"
        return sortie

    def calculer_vecteur_t(self, liste_imin_imax = [None, None]):
        return self.base_de_temps.calculer_vecteur_t(liste_imin_imax)

    def calculer_vecteur_f(self, liste_imin_imax = [None, None]):
        return self.base_de_frequence.calculer_vecteur_f(liste_imin_imax)


    def __chercher_nom_valide(self, nom):
        if nom != "":
            self.nom = nom
        else:
            numero = np.max(self.liste_n_signaux)+1
            self.nom = "s_" + str(numero)
            self.liste_n_signaux.append(numero)

    def configurer_voie(self, nom_voie, calibre = 10., repetition = False):
        self.voie.nom = nom_voie
        self.voie.calibre = calibre
        self.voie.repetition = repetition

    def deconfigurer_voie(self):
        self.voie = Voie()

    def configurer_trigger(self, seuil, montant=True, pretrigger=0, pretrigger_souple=False, hysteresys=False):
        self.trigger.seuil = seuil
        self.trigger.montant = montant
        self.trigger.pretrigger = pretrigger
        self.trigger.pretrigger_souple = pretrigger_souple
        self.trigger.hysteresys = hysteresys

    def deconfigurer_trigger(self):
        self.trigger = Trigger()

    def __str__(self):
        chaine = self.nom
        if self.voie.nom != None:
            chaine += "({0})".format(self.voie.nom)
        else:
            chaine += "(X)"
        if self.trigger.seuil != None:
            chaine += "T".format(self.voie.nom)
        return chaine

if __name__ == "__main__":
    N = 10
    bdt = BaseTemps([0, 1], 1e-3)
    liste_signaux = []
    for i in range(N):
        liste_signaux.append(SignalBase(bdt))

    liste_signaux.append(SignalBase(bdt, nom = "nico"))
    liste_signaux.append(SignalBase(bdt, nom = "s_1"))

    for i in range(N+2):
        print(liste_signaux[i].nom)
    # Te = 1e-1
    # T = 1

    # liste_tmin_tmax = -1, 3

    # bdt = BaseTemps(liste_tmin_tmax, Te)
    # bdt_periode = BaseTemps([0,T], Te)
    # vecteur_t = bdt.calculer_vecteur_t()
    # vecteur_t_periode = bdt_periode.calculer_vecteur_t()
    # vecteur_signal = np.cos(2*np.pi*vecteur_t)
    # vecteur_periode_signal = np.cos(2*np.pi*vecteur_t_periode)
    # s1 = SignalBase(bdt, vecteur_signal, nom = "s1")
    # s2 = SignalBase(bdt, vecteur_signal, nom = "s2")

    # liste_signaux = []
    # for i in range(10):
    #     liste_signaux.append(SignalBase(bdt, vecteur_signal))

    # print("*"*100)
    # for s in liste_signaux:
    #     print(s.nom)        

