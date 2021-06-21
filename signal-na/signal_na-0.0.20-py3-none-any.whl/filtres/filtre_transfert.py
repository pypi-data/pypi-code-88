import numpy as np
import matplotlib.pyplot as plt

import os, sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))

from filtres.filtre_base import FiltreBase

class FiltreTransfert(FiltreBase):
    def __init__(self, liste_coef_num = [], liste_coef_den = [], nom = ""):
        FiltreBase.__init__(self, nom)
        self.liste_coef_num = liste_coef_num
        self.liste_coef_den = liste_coef_den

    def calculer_vecteur_H_cplx(self, liste_fmin_fmax, n_points):
        self.configurer_liste_fmin_fmax(liste_fmin_fmax)
        self.configurer_n_points(n_points)
        try:
            N = len(self.vecteur_H_cplx)
        except:
            self.calculer_vecteur_p(liste_fmin_fmax, n_points)
            
            N = len(self.vecteur_p)
            
            vecteur_pn = np.ones(N, dtype = 'complex128')
            vecteur_num = np.zeros(N, dtype='complex128')
            for coef_num in self.liste_coef_num:
                vecteur_num += coef_num*vecteur_pn
                vecteur_pn *= self.vecteur_p

            vecteur_pn = np.ones(N, dtype = 'complex128')
            vecteur_den = np.zeros(N, dtype = 'complex128')
            for coef_den in self.liste_coef_den:
                vecteur_den += coef_den*vecteur_pn
                vecteur_pn *= self.vecteur_p
            
            self.vecteur_H_cplx = vecteur_num / vecteur_den
        return self.vecteur_H_cplx

if __name__ == "__main__":
    fil = FiltreTransfert([1], [1, 1e-3])
    fil.tracer_bode([1, 1e4], 100)
    fil.tracer_bode([1, 1e2], 100)