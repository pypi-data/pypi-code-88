import numpy as np
import matplotlib.pyplot as plt

import os, sys, time
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))

try:
    import pycanum.main as pycan
    print("import pycanum OK")
except:
    # print("Attention: la bibliothèque pycanum n'est pas installée")
    # print(" -> Fonctionnement en mode émulation")
    import acquisition.emulateur_sysam_sp5 as pycan

from signaux.signalll import Signal

import base.utiles_base as utb

class Sysam1Base():
    def __init__(self, liste_signaux, affichage = True):
        self.sysam = pycan.Sysam("SP5")
        self.affichage = affichage

        if isinstance(liste_signaux, list) and len(liste_signaux)> 0:
            self.liste_signaux = liste_signaux
        else:
            print("Pas de signaux")
            sys.exit()
        if affichage:  
            utb.print_liste(self.liste_signaux)

        self.liste_entrees_simples = utb.lister_test(self.liste_signaux, 
            lambda s: s._Signal6Sysam__lire_voie_base().tester_entree_simple(),
            lambda s: s._Signal6Sysam__lire_voie_base().calculer_numero()
            )
        self.liste_entrees_diffs = utb.lister_test(self.liste_signaux, 
            lambda s: s._Signal6Sysam__lire_voie_base().tester_entree_diff(),
            lambda s: s._Signal6Sysam__lire_voie_base().calculer_numero()
            )
        self.liste_entrees = utb.lister_test(self.liste_signaux, 
            lambda s: s._Signal6Sysam__lire_voie_base().tester_entree(),
            lambda s: s._Signal6Sysam__lire_voie_base().calculer_numero()
            )
        self.liste_sorties = utb.lister_test(self.liste_signaux, 
            lambda s: s._Signal6Sysam__lire_voie_base().tester_sortie(),
            lambda s: s._Signal6Sysam__lire_voie_base().calculer_numero()
            )
        self.liste_sortie1 = utb.lister_test(self.liste_sorties, 
            lambda s: s._Signal6Sysam__lire_voie_base().nom == "SA1",
            lambda s: s._Signal6Sysam__lire_voie_base().calculer_numero()
            )
        self.liste_sortie2 = utb.lister_test(self.liste_sorties, 
            lambda s: s._Signal6Sysam__lire_voie_base().nom == "SA2",
            lambda s: s._Signal6Sysam__lire_voie_base().calculer_numero()
            )
        self.liste_triggers = utb.lister_test(self.liste_signaux, 
            lambda s: s._Signal6Sysam__lire_trigger_base().tester(),
            lambda s: s._Signal6Sysam__lire_voie_base().calculer_numero()
            )
        self.liste_entrees_triggers = utb.lister_test(self.liste_entrees, 
            lambda s: s._Signal6Sysam__lire_trigger_base().tester(),
            lambda s: s._Signal6Sysam__lire_voie_base().calculer_numero()
            )
        self.liste_sorties_triggers = utb.lister_test(self.liste_sorties, 
            lambda s: s._Signal6Sysam__lire_trigger_base().tester(),
            lambda s: s._Signal6Sysam__lire_voie_base().calculer_numero()
            )
        self.liste_paires_signaux_multiplex = utb.lister_paires_test(self.liste_signaux, 
            lambda s1, s2: s1._Signal6Sysam__lire_voie_base().tester_necessite_multiplexage(s2._Signal6Sysam__lire_voie_base()),
            lambda p: p[0]._Signal6Sysam__lire_voie_base().calculer_numero(),
            lambda s: s._Signal6Sysam__lire_voie_base().calculer_numero()
            )
        
    def __enter__(self):
        return self

    def __exit__(self, *args, **kwargs):
        # self._Signal6Sysam__lire_voie_base().close()
        pass

    def __del__(self):
        self.sysam.stopper_sorties(1, 1)
        self.sysam.fermer()
    
if __name__ == "__main__":
    s1 = Signal(nom_voie = "EA1", seuil = 0)
    s2 = Signal(nom_voie = "DIFF2")
    s3 = Signal(nom_voie = "EA3")
    s4 = Signal(nom_voie = "SA1")
    s5 = Signal(nom_voie = "SA2")
    
    sys = Sysam1Base([s1, s2, s3, s4, s5])

    utb.print_liste(sys.liste_entrees)
