import numpy as np
# import copy
# from math import ceil, floor

import os, sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))
from base.temps_base import TempsBase

class BaseFrequence():
    def __init__(self, base_de_temps):
        N = base_de_temps.convertir_n_vers_i(base_de_temps.Nmax)
        self.Fe = 1 / (N*base_de_temps.Te)
        self.imin = 0
        self.imax = int(np.round(N/2))

    def calculer_vecteur_f(self, liste_imin_imax = [None, None]):
        """
            Renvoie le vecteur des frequences présentes dans le spectre
        """
        imin, imax = liste_imin_imax
        
        if imin == None:
            imin = self.imin
        if imax == None:
            imax = self.imax

        return np.arange(imin, imax)*self.Fe

    def calculer_i(self, f):
        return int(np.round(f/self.Fe))

    def calculer_f(self, i):
        return i*self.Fe

if __name__ == "__main__":
    Te = 1e-6
    liste_tmin_tmax = 0.00, 1.95
    bdt = BaseTemps(liste_tmin_tmax, Te)

    bdf = BaseFrequence(bdt)
    fmin, fmax = 10, 30
    imin, imax = bdf.calculer_i(fmin), bdf.calculer_i(fmax)
    print(bdf.calculer_vecteur_f([imin, imax]))