import numpy as np
import copy

import os, sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))

import base.constantes_base as cst

liste_calibres_entrees = [10., 5., 1., 0.2]
liste_calibres_sorties = [10.]

liste_noms_entrees_simples = ["EA0", "EA1", "EA2", "EA3", "EA4", "EA5", "EA6", "EA7"]
liste_noms_entrees_diffs = ["DIFF0", "DIFF1", "DIFF2", "DIFF3"]
liste_noms_sorties = ["SA1", "SA2"]

Xe_direct = 100e-9
Xe_multiplex = 2e-6
Xe_sortie = 200e-9

N_ech_max = 262142

T_sysam = 1e-6

class VoieBase():

    def __init__(self):
        self.nom = None
        self.calibre = None
        self.repetition = None

    def tester(self):
        return not self.nom == None

    def tester_compatibilite_nom(self, other):
        numero = other.calculer_numero()
        liste_noms_incompatibles = []
        if other.tester_entree_simple():
            liste_noms_incompatibles = ["EA"+str(numero), "DIFF"+str(numero%4)]
        if other.tester_entree_diff():
            liste_noms_incompatibles = ["EA"+str(numero), "EA"+str(numero+4), "DIFF"+str(numero)]
        if other.tester_sortie():
            liste_noms_incompatibles = ["SA"+str(numero)]
        return self.nom not in liste_noms_incompatibles

    def tester_necessite_multiplexage(self, other):
        if self.tester_entree_simple() and other.tester_entree_simple():
            return self.calculer_numero()%4 == other.calculer_numero()%4
        return False    

    def tester_entree_simple(self):
        return self.nom in liste_noms_entrees_simples
    
    def tester_entree_diff(self):
        return self.nom in liste_noms_entrees_diffs

    def tester_entree(self):
        return self.tester_entree_simple() or self.tester_entree_diff()

    def tester_sortie(self):
        return self.nom in liste_noms_sorties

    def tester_sysam(self):
        return self.nom != None

    def tester_nom(self):
        return self.tester_entree() or self.tester_sortie()
    
    def calculer_numero(self):
        if self.nom != None:
            return int(self.nom[-1])
        return None

    def tester_calibre(self):
        if self.tester_entree():
            return self.calibre in liste_calibres_entrees
        if self.tester_sortie():
            return self.calibre in liste_calibres_sorties

if __name__ == "__main__":
    v1 = VoieBase()
    v2 = VoieBase()
    v3 = VoieBase()
    v4 = VoieBase()

    v1.nom = "EA0"
    v2.nom = "EA5"

    v3.nom = "DIFF1"

    print(v1.tester_necessite_multiplexage(v2))
    print(v1.tester_compatibilite_nom(v2))
    print(v1.tester_compatibilite_nom(v3))

    print(v4.tester())
