import numpy as np
import matplotlib.pyplot as plt

import os, sys, time
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))

from signaux.signalll import Signal
from sysam.sysam_sp5 import demarrer_sysam


def acquerir_reponse_indicielle(amplitude = 1, duree = 1e-2):
    N = 1e5
    T = 1
    Te = max(duree / N, 1e-7)
    indice_sortie = Signal("carre", F=1/T, Vpp=amplitude, offset=0.5*amplitude, tr = T/4, liste_tmin_tmax = [0, T/2], Te = T/10)
    indice_entree = Signal(nom_voie = "EA0", liste_tmin_tmax = [0, duree], Te = Te)
    reponse_indice = Signal(nom_voie = "EA1", liste_tmin_tmax = [0, duree], Te = Te)

    indice_sortie.configurer_voie("SA1", repetition = False)
    indice_entree.configurer_trigger(amplitude/2, pretrigger = 10)
    demarrer_sysam([indice_sortie, indice_entree, reponse_indice])

    calibre_entree = indice_entree.calculer_calibre_optimal()
    calibre_reponse = reponse_indice.calculer_calibre_optimal()

    if indice_entree.lire_voie_base().calibre != calibre_entree or reponse_indice.lire_voie_base().calibre != calibre_reponse:
        indice_entree.configurer_voie("EA0", calibre_entree)
        reponse_indice.configurer_voie("EA1", calibre_reponse)
        demarrer_sysam([indice_sortie, indice_entree, reponse_indice])

    return indice_entree, reponse_indice
    


if __name__ == "__main__":
    e2, s2 = acquerir_reponse_indicielle(9, 1e-3)
    # Signal.tracer_signaux([e2, s2], superposition=False)
