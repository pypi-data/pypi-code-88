import numpy as np
import matplotlib.pyplot as plt

import os, sys, time
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))

try:
    import pycanum.main as pycan
except:
    # print("Attention: la bibliothèque pycanum n'est pas installée")
    # print(" -> Fonctionnement en mode émulation")
    import acquisition.emulateur_sysam_sp5 as pycan


from sysam.sysam_1_base import Sysam1Base
from signaux.signalll import Signal


import base.utiles_base as utb

class Sysam2Mode(Sysam1Base):
    def __init__(self, liste_signaux, affichage = True):
        Sysam1Base.__init__(self, liste_signaux, affichage)
        self.generer_chaine_mode()
        if self.affichage:
            print(self.chaine_mode)

    def generer_chaine_mode(self):

        test_multiplex = True if self.liste_paires_signaux_multiplex else False
        test_entree = True if self.liste_entrees else False
        test_sortie = True if self.liste_sorties else False
        test_sortie1 = True if self.liste_sortie1 else False
        test_sortie2 = True if self.liste_sortie2 else False
        test_trigger = True if self.liste_triggers else False

        test_synchrone = False
        if not test_trigger and test_entree and test_sortie:
            if self.liste_entrees_simples: 
                if self.liste_entrees_simples[0]._PlotBase__lire_axe_x_base().iemin == 0:
                    test_synchrone = True
            if self.liste_entrees_diffs: 
                if self.liste_entrees_diffs[0]._PlotBase__lire_axe_x_base().iemin == 0:
                    test_synchrone = True

        chaine_mode = ""
        chaine_mode = chaine_mode + "-entree-" if test_entree else chaine_mode
        chaine_mode = chaine_mode + "-sortie1-" if test_sortie1 else chaine_mode
        chaine_mode = chaine_mode + "-sortie2-" if test_sortie2 else chaine_mode
        chaine_mode = chaine_mode + "-multiplex-" if test_multiplex else chaine_mode
        chaine_mode = chaine_mode + "-synchrone-" if test_synchrone else chaine_mode
        chaine_mode = chaine_mode + "-trigger-" if test_trigger else chaine_mode
        
        self.chaine_mode = chaine_mode


if __name__ == "__main__":
    liste_tmin_tmax_1 = [0, 1]
    liste_tmin_tmax_2 = [0.1, 1]
    s1 = Signal(liste_tmin_tmax =liste_tmin_tmax_2, nom_voie = "EA1")
    s2 = Signal(liste_tmin_tmax =liste_tmin_tmax_2, nom_voie = "DIFF2")
    s3 = Signal(liste_tmin_tmax =liste_tmin_tmax_2, nom_voie = "EA3")
    s4 = Signal(liste_tmin_tmax =liste_tmin_tmax_1, nom_voie = "SA1")
    s5 = Signal(liste_tmin_tmax =liste_tmin_tmax_1, nom_voie = "SA2")
    
    sys = Sysam2Mode([s1, s2, s3, s4, s5])

    utb.print_liste(sys.liste_entrees)
