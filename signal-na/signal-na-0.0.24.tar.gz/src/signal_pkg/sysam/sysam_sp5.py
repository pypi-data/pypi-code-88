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

from signaux.signal_1_base import Signal1Base
from signaux.signalll import Signal

import base.axe_x_base
import base.voie_base
import base.utiles_base as utb

from sysam.sysam_4_methodes import Sysam4Methodes
from plot.plot_base import tracer
__all__ = ["demarrer_sysam", "acquerir_signaux"]

def acquerir_signaux(*args, **kwargs):
    demarrer_sysam(*args, **kwargs)
    
def demarrer_sysam(*args, **kwargs):
    args = list(args)
    liste_signaux = []
    test_signal = len(args) > 0 and isinstance(args[0], Signal1Base)
    if not test_signal:
        print("Quels sont les signaux gérés par sysam?")
        return
    s = args[0]
    while test_signal:
        liste_signaux.append(utb.analyser_args(args, " ", lambda x: isinstance(x, Signal1Base), s)[0])
        test_signal = len(args) > 0 and isinstance(args[0], Signal1Base)
    affichage = utb.analyser_args_kwargs(args, kwargs, "affichage", lambda x: isinstance(x, bool), True)

    with SysamSP5(liste_signaux, affichage) as sysam:
        pass

# def demarrer_sysam(liste_signaux=None):
#     if __name__ == '__main__':
#         try:
#             sysam = SysamSP5(liste_signaux)
#         except KeyboardInterrupt:
#             print('Interrupted')
#             try:
#                 sys.sys.exit(0)
#             except Systemsys.exit:
#                 os._sys.exit(0)

class SysamSP5(Sysam4Methodes):
    def __init__(self, liste_signaux, affichage = True):
        Sysam4Methodes.__init__(self, liste_signaux, affichage)

        if "entree" in self.chaine_mode:
            self.sysam.config_entrees(*self.calculer_arguments_config_entrees())
            self.sysam.config_echantillon(*self.calculer_arguments_config_echantillon())

        if "trigger" in self.chaine_mode:
            self.sysam.config_trigger(*self.calculer_arguments_config_trigger())
 
        if "sortie1" in self.chaine_mode and "synchrone" not in self.chaine_mode:
            self.sysam.config_sortie(*self.calculer_arguments_config_sortie(1))

        if "sortie2" in self.chaine_mode and "synchrone" not in self.chaine_mode:
            self.sysam.config_sortie(*self.calculer_arguments_config_sortie(2))


        if "synchrone" in self.chaine_mode:
            self.sysam.acquerir_avec_sorties(*self.calculer_arguments_acquerir_avec_sorties())
            self.mettre_a_jour_entrees()
        elif "entree" in self.chaine_mode and "sortie" in self.chaine_mode:
            xmin, xmax = self.axe_x_base_entrees.calculer_liste_xmin_xmax()
            self.sysam.declencher_sorties(*self.calculer_arguments_declencher_sorties())
            if xmin != 0:
                time.sleep(xmin)
            self.sysam.acquerir()
            self.mettre_a_jour_entrees()
        elif "entree" in self.chaine_mode and "sortie" not in self.chaine_mode:
            xmin, xmax = self.axe_x_base_entrees.calculer_liste_xmin_xmax()
            self.sysam.acquerir()
            self.mettre_a_jour_entrees()            
        elif "sortie" in self.chaine_mode and "entree" not in self.chaine_mode:
            self.sysam.declencher_sorties(*self.calculer_arguments_declencher_sorties())
            test_fin = False
            while not test_fin:
                chaine = input("On arrête les signaux o/N?")
                if chaine == "o" or chaine == "O":
                    test_fin = True

    def mettre_a_jour_entrees(self):
        # print("On met les entrées à jour")
        temps = self.sysam.temps()
        entrees = self.sysam.entrees()
        voies = self.calculer_arguments_config_entrees()[0]
        # print("mettre a jour entrees ", self.chaine_mode)
        if "synchrone" not in self.chaine_mode:
            Nsysam = np.max(base.axe_x_base.AxeXBase.liste_NBase) + 1
            base.axe_x_base.AxeXBase.liste_NBase.append(Nsysam)
        else:
            Nsysam = 0

        for s in self.liste_entrees:
            voie = s._Signal6Sysam__lire_voie_base().calculer_numero()
            indice = voies.index(voie)
            s._Signal1Base__vecteur_y = np.array(entrees[indice])
            s._PlotBase__axe_x_base = base.axe_x_base.calculer_axe_x_base(np.array(temps[indice]))
            s._PlotBase__axe_x_base.Nsysam = Nsysam

if __name__ == "__main__":
    liste_tmin_tmax = [0, 1e-4]
    Te = 1e-6
    s1 = Signal(liste_tmin_tmax =liste_tmin_tmax, nom_voie = "EA0", Te = Te, seuil = 0, pretrigger = 3)
    # s2 = Signal(liste_tmin_tmax =liste_tmin_tmax, nom_voie = "DIFF2", Te = Te)
    # s3 = Signal(liste_tmin_tmax =liste_tmin_tmax, nom_voie = "EA3", Te = Te)
    # s4 = Signal(liste_tmin_tmax =liste_tmin_tmax, nom_voie = "SA2", Te = Te)
    s5 = Signal(F = 1e4, liste_tmin_tmax =liste_tmin_tmax, nom_voie = "SA1", Te = Te)
    
    demarrer_sysam(s1, s5, True)
    tracer(s1, s5, superposition = False)