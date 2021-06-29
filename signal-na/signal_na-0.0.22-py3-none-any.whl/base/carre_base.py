import numpy as np
import copy

import os, sys
import matplotlib.pyplot as plt

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))

import base.constantes_base as cst
from base.temps_base import TempsBase
from signaux.signal_1_base import Signal1Base

def generer_portion_carre(base_de_temps, F, alpha, tr):
    tmin, tmax = base_de_temps.calculer_liste_tmin_tmax()
    n = int(np.floor((tmin-tr)*F))

    t0 = n/F+tr
    t1 = t0 + alpha/F
    t2 = t0 + 1/F
    t3 = t0 + (1+alpha)/F

    if tmin < t1:
        # On commence par un état haut
        ned = base_de_temps._TempsBase__convertir_ia_vers_ie(base_de_temps._TempsBase__convertir_t_vers_ia(tmin))
        if tmax < t1:
            # Et c'est tout
            nef = base_de_temps._TempsBase__convertir_ia_vers_ie(base_de_temps._TempsBase__convertir_t_vers_ia(tmax))
            vecteur_signal = np.ones(nef-ned)
        else:
            # On poursuit par un état bas
            nef = base_de_temps._TempsBase__convertir_ia_vers_ie(base_de_temps._TempsBase__convertir_t_vers_ia(t1))
            vecteur_signal = np.ones(nef-ned)
            ned = nef
            if tmax < t2:
                # Et c'est tout
                nef = base_de_temps._TempsBase__convertir_ia_vers_ie(base_de_temps._TempsBase__convertir_t_vers_ia(tmax))
                vecteur_signal = np.concatenate([vecteur_signal, np.zeros(nef-ned)])
            else:
                # On poursuit par un état haut
                nef = base_de_temps._TempsBase__convertir_ia_vers_ie(base_de_temps._TempsBase__convertir_t_vers_ia(t2))
                vecteur_signal = np.concatenate([vecteur_signal, np.zeros(nef-ned)])
                ned = nef
                nef = base_de_temps._TempsBase__convertir_ia_vers_ie(base_de_temps._TempsBase__convertir_t_vers_ia(tmax))
                vecteur_signal = np.concatenate([vecteur_signal, np.ones(nef-ned)])
    else:
        # On commence par un état bas
        ned = base_de_temps._TempsBase__convertir_ia_vers_ie(base_de_temps._TempsBase__convertir_t_vers_ia(tmin))
        if tmax < t2:
            # Et c'est tout
            nef = base_de_temps._TempsBase__convertir_ia_vers_ie(base_de_temps._TempsBase__convertir_t_vers_ia(tmax))
            vecteur_signal = np.zeros(nef-ned)
        else:
            # On poursuit par un état haut
            nef = base_de_temps._TempsBase__convertir_ia_vers_ie(base_de_temps._TempsBase__convertir_t_vers_ia(t2))
            vecteur_signal = np.zeros(nef-ned)
            ned = nef
            if tmax < t3:
                # Et c'est tout
                nef = base_de_temps._TempsBase__convertir_ia_vers_ie(base_de_temps._TempsBase__convertir_t_vers_ia(tmax))
                vecteur_signal = np.concatenate([vecteur_signal, np.ones(nef-ned)])
            else:
                # On poursuit par un état bas
                nef = base_de_temps._TempsBase__convertir_ia_vers_ie(base_de_temps._TempsBase__convertir_t_vers_ia(t3))
                vecteur_signal = np.concatenate([vecteur_signal, np.ones(nef-ned)])
                ned = nef
                nef = base_de_temps._TempsBase__convertir_ia_vers_ie(base_de_temps._TempsBase__convertir_t_vers_ia(tmax))
                vecteur_signal = np.concatenate([vecteur_signal, np.zeros(nef-ned)])
    return vecteur_signal

if __name__ == "__main__":
    bdt = TempsBase([0, 1], 1e-1)
    vecteur_signal = generer_portion_carre(bdt, 1, 0.5, 0.1)
    s = Signal1Base(bdt, vecteur_signal)
    s.plot()
    plt.show()