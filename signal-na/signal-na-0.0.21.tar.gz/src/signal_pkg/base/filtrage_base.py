import numpy as np
import copy
import matplotlib.pyplot as plt

import os, sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))

import base.constantes_base as cst
# from signaux.signalll import Signal
# from filtres.filtre import Filtre
# from plot.plot_base import tracer

def calculer_sortie_filtre(filtre, entree, nom = ""):
    assert filtre._FiltreBase__fonction_H != None, "Impossible de filtrer le signal avec ce iltre"
    fft_entree = entree.calculer_fft()
    vecteur_f = fft_entree.lire_vecteur_x()
    N = len(vecteur_f)
    Fe = 1 / entree._PlotBase__lire_axe_x_base().lire_Xe()
    vecteur_f[N//2:] -= Fe

    vecteur_H = np.array([filtre.calculer_H(f) for f in vecteur_f])

    fft_sortie = fft_entree.copier()
    fft_sortie._Signal1Base__vecteur_y = fft_entree._Signal1Base__vecteur_y * vecteur_H        
    sortie = fft_sortie.calculer_ifft()

    if nom != "":
        sortie._Signal1Base__nom = nom
    else:
        sortie._Signal1Base__nom = entree.lire_nom() + "_filtre_par_" + filtre.lire_nom() 
    return sortie

if __name__ == "__main__":
    F = 1e5
    Te = 1/(100*F)
    # filtre = Filtre("zorro", False, lambda f: 1 / (1+1j*f/1e2))
    # entree = Signal("carre", F = F, liste_tmin_tmax = [0, 10/F], Te = Te) + 1
    # sortie = calculer_sortie_filtre(filtre, entree)
    # tracer(entree, sortie)