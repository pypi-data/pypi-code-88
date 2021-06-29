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

from sysam.sysam_3_test import Sysam3Test

from signaux.signalll import Signal

import base.voie_base

class Sysam4Methodes(Sysam3Test):

    def calculer_arguments_config_entrees(self):
        if "entree" in self.chaine_mode:
            voies = [s._Signal6Sysam__lire_voie_base().calculer_numero() for s in self.liste_entrees]
            calibres = [s._Signal6Sysam__lire_voie_base().calibre for s in self.liste_entrees]
            diff = [s._Signal6Sysam__lire_voie_base().calculer_numero() for s in self.liste_entrees_diffs]
            return voies, calibres, diff
        return None

    def calculer_arguments_config_echantillon(self):
        if "entree" in self.chaine_mode:
            if self.axe_x_base_entrees:
                techant = self.axe_x_base_entrees.lire_Xe() / base.voie_base.T_sysam
                nbpoints = self.axe_x_base_entrees.lire_N()
                return techant, nbpoints
        return None

    def calculer_arguments_config_trigger(self):
        if "trigger" in self.chaine_mode:
            st = self.liste_triggers[0]
            voie = st._Signal6Sysam__lire_voie_base().calculer_numero()
            seuil = st._Signal6Sysam__lire_trigger_base().seuil
            montant = 1 if st._Signal6Sysam__lire_trigger_base().montant == True else 0
            pretrigger = st._Signal6Sysam__lire_trigger_base().pretrigger
            pretrigger_souple = 1 if st._Signal6Sysam__lire_trigger_base().pretrigger_souple == True else 0
            hysteresys = 1 if st._Signal6Sysam__lire_trigger_base().hysteresys == True else 0
            return voie, seuil, montant, pretrigger, pretrigger_souple, hysteresys
        return None

    def calculer_arguments_config_sortie(self, n):
        if "sortie"+str(n) in self.chaine_mode and "synchrone" not in self.chaine_mode:
            nsortie = n
            s = self.liste_sortie1[0] if n == 1 else self.liste_sortie2[0]
            techant = s._PlotBase__lire_axe_x_base().lire_Xe() / base.voie_base.T_sysam
            tensions = s.lire_vecteur_y()
            repetition = -1 if s._Signal6Sysam__lire_voie_base().repetition else 0

            return nsortie, techant, tensions, repetition

        return None

    def calculer_arguments_declencher_sorties(self):
        if "sortie" in self.chaine_mode and "synchrone" not in self.chaine_mode:
            s1 = 1 if self.liste_sortie1 else 0
            s2 = 1 if self.liste_sortie2 else 0
            return s1, s2
        return None

    def calculer_arguments_acquerir_avec_sorties(self):
        if "synchrone" in self.chaine_mode:
            tensions1 = self.liste_sortie1[0].lire_vecteur_y() if "sortie1" in self.chaine_mode else np.zeros(1)
            tensions2 = self.liste_sortie2[0].lire_vecteur_y() if "sortie2" in self.chaine_mode else np.zeros(1)
            return tensions1, tensions2
        return None


if __name__ == "__main__":
    liste_xmin_xmax = [0, 1e-4]
    Te = 1e-5
    s1 = Signal(liste_xmin_xmax =liste_xmin_xmax, nom_voie = "EA0", Te = Te, seuil = 0, pretrigger = 3)
    s2 = Signal(liste_xmin_xmax =liste_xmin_xmax, nom_voie = "DIFF2", Te = Te)
    s3 = Signal(liste_xmin_xmax =liste_xmin_xmax, nom_voie = "EA3", Te = Te)
    s4 = Signal(liste_xmin_xmax =liste_xmin_xmax, nom_voie = "SA1", Te = Te)
    s5 = Signal(liste_xmin_xmax =liste_xmin_xmax, nom_voie = "SA2", Te = Te)
    
    sysam = Sysam4Methodes([s1, s2, s3, s4, s5])


    # N = 10
    # liste_signaux = []
    # for i in range(N):
    #     liste_signaux.append(SignalGBF(liste_xmin_xmax = liste_xmin_xmax, Te = Te))

    # liste_signaux[0].configurer_voie("EA1")
    # liste_signaux[1].configurer_voie("SA1")
    # liste_signaux[2].configurer_voie("DIFF2")

    # liste_signaux[2].configurer_trigger(0)
    # sysam = Sysam4Methodes(liste_signaux)

    print("arguments config_entrees: ", sysam.calculer_arguments_config_entrees())
    print("arguments config_echantillons: ", sysam.calculer_arguments_config_echantillon())
    print("arguments config_trigger: ", sysam.calculer_arguments_config_trigger())
    print("arguments config_sortie (1): ", sysam.calculer_arguments_config_sortie(1))
    print("arguments config_sortie (2): ", sysam.calculer_arguments_config_sortie(2))

    # del(sysam)


    # liste_signaux[2].deconfigurer_trigger()
    # sysam = Sysam4Methodes(liste_signaux)

    # print("arguments acquerir_avec_sorties: ", sysam.calculer_arguments_acquerir_avec_sorties())
    # # lancer_acquisition()