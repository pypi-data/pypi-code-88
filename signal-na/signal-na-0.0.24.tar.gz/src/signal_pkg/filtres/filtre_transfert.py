import numpy as np
import matplotlib.pyplot as plt

import os, sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))

from filtres.filtre_base import FiltreBase
from base.mesure_bode_base import MesureBodeBase

class FiltreTransfert(FiltreBase):

    def __init__(self, liste_coef_num = [1], liste_coef_den = [1], omega = False, nombre_cs_frequence = None, nom = ""):
        def fonction_H(x):
            X = 1j*x
            num = 0
            Xn = 1
            for a in liste_coef_num:
                num += a*Xn
                Xn *= X

            den = 0
            Xn = 1
            for a in liste_coef_den:
                den += a*Xn
                Xn *= X
            return num/den
        FiltreBase.__init__(self, fonction_H = fonction_H, omega = omega, nombre_cs_frequence = nombre_cs_frequence, nom = nom)

    def calculer_H(self, x):
        return complex(self._FiltreBase__fonction_H(x))

    def calculer_bode(self, liste_xmin_xmax = [1e2, 1e5], nombre_de_points = 100, omega = None, logX = True):
        omega = self.__omega if omega == None else omega
        vecteur_f = self._FiltreBase__calculer_vecteur_f(liste_xmin_xmax, nombre_de_points, omega, logX)
        if self._FiltreBase__tester_nouvelles_frequences(vecteur_f):
            for f in vecteur_f:
                x = self._FiltreBase__calculer_x(f, omega)
                if f not in [mesure.f for mesure in self._FiltreBase__liste_mesures]:
                    H = self.calculer_H(x)
                    if H != None:
                        self._FiltreBase__liste_mesures.append( MesureBodeBase(f, H) )
            self._FiltreBase__liste_mesures.sort(key = lambda m: m.f)

if __name__ == "__main__":
    fil = FiltreTransfert([0, 1], [1, 1e-3], omega = True)
    fil.calculer_bode([10,1e5],100)
    fil.tracer(deg=True, omega=False)
    plt.show()
    