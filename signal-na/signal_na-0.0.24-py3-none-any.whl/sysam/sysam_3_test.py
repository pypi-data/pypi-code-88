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

from sysam.sysam_2_mode import Sysam2Mode

from signaux.signalll import Signal

import base.voie_base
import base.utiles_base as utb


class Sysam3Test(Sysam2Mode):
    def __init__(self, liste_signaux, affichage = True):
        Sysam2Mode.__init__(self, liste_signaux, affichage)
        if self.tester_liste_signaux():
            self.test_signaux = True
        else:
            self.test_signaux = False
            sys.exit()


    ##################################################################################################################
    ## tester liste signaux
    ##################################################################################################################
    def tester_liste_signaux(self):
        # Générer Xe_entrées_min
        liste_Xe = [0.]
        if "entree" in self.chaine_mode:
            liste_Xe.append(base.voie_base.Xe_direct)
        if "multiplex" in self.chaine_mode:
            liste_Xe.append(base.voie_base.Xe_multiplex)
        if "synchrone" in self.chaine_mode:
            liste_Xe.append(base.voie_base.Xe_sortie)
        self.Xe_entree_min = np.max(liste_Xe)

        # Générer Xe_sorties_min
        liste_Xe = [0.]
        if "sortie" in self.chaine_mode:
            liste_Xe.append(base.voie_base.Xe_sortie)
        if "multiplex" in self.chaine_mode and "synchrone" in self.chaine_mode:
            liste_Xe.append(base.voie_base.Xe_multiplex)
        self.Xe_sortie_min = np.max(liste_Xe)

        # Générer base de temps entrées
        if self.liste_entrees_simples:
            self.axe_x_base_entrees = self.liste_entrees_simples[0]._PlotBase__lire_axe_x_base()
        elif self.liste_entrees_diffs:
            self.axe_x_base_entrees = self.liste_entrees_diffs[0]._PlotBase__lire_axe_x_base()
        else:
            self.axe_x_base_entrees = None

        # tester validite des noms des voies
        liste_signaux_noms_voies_ko = utb.lister_test(self.liste_signaux, 
            lambda s: s._Signal6Sysam__lire_voie_base().tester_sysam() and (not s._Signal6Sysam__lire_voie_base().tester_nom()),
            lambda s: s._Signal6Sysam__lire_voie_base().calculer_numero()
            )
        if liste_signaux_noms_voies_ko:
            print("Problème avec les noms des voies voie suivants:")
            utb.print_liste(liste_signaux_noms_voies_ko, begin = " -> ")
            return False

        # tester compatibilités entre les noms des voies
        liste_paires_signaux_noms_voies_ko = utb.lister_paires_test(self.liste_signaux, 
            lambda s1, s2: s1._Signal6Sysam__lire_voie_base().tester_sysam() and s2._Signal6Sysam__lire_voie_base().tester_sysam() and not s1._Signal6Sysam__lire_voie_base().tester_compatibilite_nom(s2._Signal6Sysam__lire_voie_base()),
            lambda p: p[0]._Signal6Sysam__lire_voie_base().calculer_numero(),
            lambda s: s._Signal6Sysam__lire_voie_base().calculer_numero()
            )
        if liste_paires_signaux_noms_voies_ko:
            print("Problème de compatibilité entre les noms des paires de voies voie suivants:")
            utb.print_liste_de_listes(liste_paires_signaux_noms_voies_ko, begin1 = " -> ")
            return False

        # tester trigger
        if self.liste_sorties_triggers:
            print("Problèmes des triggers sont affectés sur des sorties:")
            utb.print_liste(self.liste_sorties_triggers, begin = " -> ")
            return False

        if len(self.liste_entrees_triggers) > 1:
            print("Problèmes plusieurs triggers sont affectés sur des entrées:")
            utb.print_liste(self.liste_entrees_triggers, begin = " -> ")
            return False

        # tester entrees echantillonnés trop vite
        liste_entrees_echantillonnees_trop_vite = utb.lister_test(self.liste_entrees, 
            lambda s: s._PlotBase__lire_axe_x_base().lire_Xe() < self.Xe_entree_min,
            lambda s: s._Signal6Sysam__lire_voie_base().calculer_numero()
            )
        if liste_entrees_echantillonnees_trop_vite:
            print("Les entrees suivantes ne respectent pas Xe > {0} s".format(self.Xe_entree_min))
            utb.print_liste(liste_entrees_echantillonnees_trop_vite, begin = " -> ")
            return False

        # tester sorties echantillonnées trop vite
        liste_sorties_echantillonnees_trop_vite = utb.lister_test(self.liste_sorties, 
            lambda s: s._PlotBase__lire_axe_x_base().lire_Xe() < self.Xe_sortie_min,
            lambda s: s._Signal6Sysam__lire_voie_base().calculer_numero()
            )
        if liste_sorties_echantillonnees_trop_vite:
            print("Les sorties suivantes ne respectent pas Xe > {0} s".format(self.Xe_sortie_min))
            utb.print_liste(liste_sorties_echantillonnees_trop_vite, begin = " -> ")
            return False

        # tester compatibilités entre les bases de temps des entrées
        liste_paires_entrees_bases_de_temps_ko = utb.lister_paires_test(self.liste_entrees, 
            lambda s1, s2: s1._PlotBase__lire_axe_x_base() != s2._PlotBase__lire_axe_x_base(),
            lambda p: p[0]._Signal6Sysam__lire_voie_base().calculer_numero(),
            lambda s: s._Signal6Sysam__lire_voie_base().calculer_numero()
            )
        if liste_paires_entrees_bases_de_temps_ko:
            print("Problème de compatibilité entre les bases de temps des paires d'entrées suivantes:")
            utb.print_liste_de_listes(liste_paires_entrees_bases_de_temps_ko, begin1 = " -> ")
            return False

        # tester validite des bases de temps de sortie
        if "synchrone" in self.chaine_mode:
            liste_sorties_echantillonnage_ko = utb.lister_test(self.liste_sorties, 
                lambda s: s._PlotBase__lire_axe_x_base().lire_Xe() != self.axe_x_base_entrees.lire_Xe(),
                lambda s: s._Signal6Sysam__lire_voie_base().calculer_numero()
                )
            if liste_sorties_echantillonnage_ko:
                print("Problème de périodes d'échantillonnage sur les sorties suivantes (ES synchrones):")
                utb.print_liste(liste_sorties_echantillonnage_ko, begin = " -> ")
                return False

        # tester si les sorties commencent à t=0
        liste_sorties_tardives = utb.lister_test(self.liste_sorties, 
            lambda s: s._PlotBase__lire_axe_x_base().iemin != 0,
            lambda s: s._Signal6Sysam__lire_voie_base().calculer_numero()
            )
        if liste_sorties_tardives:
            print("Les sorties suivantes ne débutent pas à t=0:")
            utb.print_liste(liste_sorties_tardives, begin = " -> ")
            return False


        # tester espace memoire
        liste_signaux_sysam = utb.lister_test(
            self.liste_signaux, 
            lambda s: s._Signal6Sysam__lire_voie_base().tester_sysam(),
            lambda s: s._Signal6Sysam__lire_voie_base().calculer_numero()
            )
        liste_N_ech = [s._PlotBase__lire_axe_x_base().lire_N() for s in liste_signaux_sysam]
        if np.sum(liste_N_ech) > base.voie_base.N_ech_max:
            print("Trop d'échantillons stockés en mémoire (max = {0})".format(base.voie_base.N_ech_max))
            for i in range(len(liste_signaux_sysam)):
                N1, N2, N3 = 15, 20, 8
                chaine = " -> {0:" + str(N1) + "} {1} {2:" + str(N3) + "}"
                print(chaine.format(str(liste_signaux_sysam[i]), "."*N2, liste_N_ech[i]))
            print(" "*(N1+N2+5), "-"*N3)
            chaine = " "*(N1+N2+6) + "{0:" +str(N3) + "}"
            print(chaine.format(np.sum(liste_N_ech)))
            return False

        return True

if __name__ == "__main__":
    # # # Test noms KO
    # s1 = Signal(nom_voie = "EA12")
    # s2 = Signal(nom_voie = "DIFF2")
    # s3 = Signal(nom_voie = "EA3")
    # s4 = Signal(nom_voie = "SA1")
    # s5 = Signal(nom_voie = "SA2")
    # sys = Sysam3Test([s1, s2, s3, s4, s5])

    # # # Test paires noms incompatibles 
    # s1 = Signal(nom_voie = "EA1")
    # s2 = Signal(nom_voie = "DIFF1")
    # s3 = Signal(nom_voie = "EA3")
    # s4 = Signal(nom_voie = "SA1")
    # s5 = Signal(nom_voie = "SA1")
    # sys = Sysam3Test([s1, s2, s3, s4, s5])

    # # # tester trigger sortie
    # s1 = Signal(nom_voie = "EA0")
    # s2 = Signal(nom_voie = "DIFF1")
    # s3 = Signal(nom_voie = "EA3")
    # s4 = Signal(nom_voie = "SA1", seuil = 0)
    # s5 = Signal(nom_voie = "SA2", seuil = 0)
    # sys = Sysam3Test([s1, s2, s3, s4, s5])

    # # # tester trigger entrees
    # s1 = Signal(nom_voie = "EA0", seuil = 0)
    # s2 = Signal(nom_voie = "DIFF1", seuil = 0)
    # s3 = Signal(nom_voie = "EA3", seuil = 0)
    # s4 = Signal(nom_voie = "SA1")
    # s5 = Signal(nom_voie = "SA2")
    # sys = Sysam3Test([s1, s2, s3, s4, s5])

    # # # tester entrees echantillonnées trop vite
    # Te = 1e-8
    # liste_tmin_tmax = [0, 1e-5]
    # s1 = Signal(nom_voie = "EA0", seuil = 0, Te = Te, liste_tmin_tmax = liste_tmin_tmax)
    # s2 = Signal(nom_voie = "DIFF1", Te = Te, liste_tmin_tmax = liste_tmin_tmax)
    # s3 = Signal(nom_voie = "EA3", Te = Te, liste_tmin_tmax = liste_tmin_tmax)
    # s4 = Signal(nom_voie = "SA1", liste_tmin_tmax = liste_tmin_tmax)
    # s5 = Signal(nom_voie = "SA2", liste_tmin_tmax = liste_tmin_tmax)
    # sys = Sysam3Test([s1, s2, s3, s4, s5])

    # # # tester sorties echantillonnées trop vite
    # Te = 2e-7
    # liste_tmin_tmax = [0, 1e-5]
    # s1 = Signal(nom_voie = "EA0", seuil = 0, liste_tmin_tmax = liste_tmin_tmax)
    # s2 = Signal(nom_voie = "DIFF1", liste_tmin_tmax = liste_tmin_tmax)
    # s3 = Signal(nom_voie = "EA3", liste_tmin_tmax = liste_tmin_tmax)
    # s4 = Signal(nom_voie = "SA1", Te = Te, liste_tmin_tmax = liste_tmin_tmax)
    # s5 = Signal(nom_voie = "SA2", Te = Te, liste_tmin_tmax = liste_tmin_tmax)
    # sys = Sysam3Test([s1, s2, s3, s4, s5])

    # # # tester compatibilité bases de temps des entrées
    # Te1 = 2e-7
    # Te2 = 1e-7
    # s1 = Signal(nom_voie = "EA0", seuil = 0, Te = Te1)
    # s2 = Signal(nom_voie = "DIFF1", Te = Te2)
    # s3 = Signal(nom_voie = "EA3", Te = Te1)
    # s4 = Signal(nom_voie = "SA1")
    # s5 = Signal(nom_voie = "SA2")
    # sys = Sysam3Test([s1, s2, s3, s4, s5])

    # # # tester compatibilité bases de temps des sorties Te entree = Te sortie si synchrone
    # Te1 = 1e-3
    # Te2 = 2e-3
    # s1 = Signal(nom_voie = "EA0", Te = Te1)
    # s2 = Signal(nom_voie = "DIFF1", Te = Te1)
    # s3 = Signal(nom_voie = "EA3", Te = Te1)
    # s4 = Signal(nom_voie = "SA1", Te = Te2)
    # s5 = Signal(nom_voie = "SA2", Te = Te2)
    # sys = Sysam3Test([s1, s2, s3, s4, s5])

    # # # tester compatibilité bases de temps des sorties entrees tardives
    # Te1 = 1e-3
    # Te2 = 1e-3
    # liste_tmin_tmax_1 = [0.2, 1]
    # liste_tmin_tmax_2 = [0.3, 1]
    # s1 = Signal(nom_voie = "EA0", Te = Te1, liste_tmin_tmax = liste_tmin_tmax_1)
    # s2 = Signal(nom_voie = "DIFF1", Te = Te1, liste_tmin_tmax = liste_tmin_tmax_1)
    # s3 = Signal(nom_voie = "EA3", Te = Te1, liste_tmin_tmax = liste_tmin_tmax_2)
    # s4 = Signal(nom_voie = "SA1", Te = Te2)
    # s5 = Signal(nom_voie = "SA2", Te = Te2)
    # sys = Sysam3Test([s1, s2, s3, s4, s5])

    # tester espace mémoire
    # # tester compatibilité bases de temps des sorties entrees tardives
    Te1 = 1e-6
    Te2 = 1e-6
    liste_tmin_tmax_1 = [0.2, 1]
    liste_tmin_tmax_2 = [0.2, 1]
    s1 = Signal(nom_voie = "EA0", Te = Te1, liste_tmin_tmax = liste_tmin_tmax_1)
    s2 = Signal(nom_voie = "DIFF1", Te = Te1, liste_tmin_tmax = liste_tmin_tmax_1)
    s3 = Signal(nom_voie = "EA3", Te = Te1, liste_tmin_tmax = liste_tmin_tmax_2)
    s4 = Signal(nom_voie = "SA1", Te = Te2)
    s5 = Signal(nom_voie = "SA2", Te = Te2)
    sys = Sysam3Test([s1, s2, s3, s4, s5])

