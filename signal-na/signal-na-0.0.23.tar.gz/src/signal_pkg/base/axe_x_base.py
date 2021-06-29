import numpy as np
import copy

import os, sys

from numpy.core.numeric import convolve
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))

import base.constantes_base as cst
from base.axe_base import AxeBase

def calculer_axe_x_base(vecteur_x, nom = "t", unite = "s"):
        """
        Renvoie une base de temps correspondant au vecteur_x
        """
        assert len(vecteur_x) > 0, "calculer_axe_x_base: vecteur_x ne doit pas être vide"
        xmin, xmax = vecteur_x[0], vecteur_x[-1]
        vecteur_Xe = vecteur_x[1:] - vecteur_x[:-1]
        Xe = vecteur_Xe.mean()
        return AxeXBase([xmin, xmax+Xe], Xe, nom, unite)

class AxeXBase(AxeBase):
    Pa = cst.Pa

    liste_NBase = [0]

    def __init__(self, liste_xmin_xmax = cst.liste_xmin_xmax, Xe = cst.Xe, nom = "t", unite = "s", NBase = 0):
        """
        Initialisation d'une base de temps:
        """
        AxeBase.__init__(self, nom, unite)
        xmin, xmax = liste_xmin_xmax
        self.NXa = int(np.round(Xe * 10**self.Pa))
        self.iemin = self.convertir_ia_vers_ie(self.convertir_x_vers_ia(xmin))
        self.iemax = self.convertir_ia_vers_ie(self.convertir_x_vers_ia(xmax))
        self.NBase = NBase

    def choisir_nouvel_NBase(self):
        self.NBase = max(self.liste_NBase)+1
        self.liste_NBase.append(self.NBase)

    def cloner(self, other):
        AxeBase.cloner(self, other)
        self.NXa = other.NXa
        self.iemin = other.iemin
        self.iemax = other.iemax
        self.NBase = other.NBase

    def lire_Ta(self):
        return self.__Ta
    
    def lire_Pa(self):
        return self.Pa
        
    def lire_N(self):
        return self.iemax - self.iemin

    def lire_Xe(self):
        return self.NXa / 10**self.Pa

    def calculer_liste_xmin_xmax(self):
        """
        Calcule la liste liste_xmin_tmax de la base
        """
        return list(self.convertir_ia_vers_x(self.convertir_ie_vers_ia([self.iemin, self.iemax])))
        
    def lire_vecteur_x(self):
        return self.convertir_ia_vers_x(self.convertir_i_vers_ia(np.arange(0, self.iemax - self.iemin)))   

    def copier(self):
        return copy.deepcopy(self)

    def __str__(self):
        return str([self.iemin, self.iemax, self.NXa, self.NBase])

    def __eq__(self, other):
        return self.iemin == other.iemin and self.iemax == other.iemax and  self.NXa == other.NXa and  self.NBase == other.NBase and self.unite == other.unite

    def convertir_x_vers_ia(self, t):
        if type(t) == list:
            t = np.array(t)
        return np.round(t * 10**self.Pa).astype(dtype = np.int64)

    def convertir_ia_vers_x(self, ia):
        if type(ia) == list:
            ia = np.array(ia)
        return ia / 10**self.Pa

    def convertir_ia_vers_ie(self, ia):
        if type(ia) == list:
            ia = np.array(ia)
        return np.round(ia / self.NXa).astype(dtype = np.int64)

    def convertir_ie_vers_ia(self, ie):
        if type(ie) == list:
            ie = np.array(ie)
        return ie * self.NXa
    
    def convertir_ia_vers_i(self, ia):
        if type(ia) == list:
            ia = np.array(ia)
        return np.round(ia / self.NXa - self.iemin).astype(dtype = np.int64)

    def convertir_i_vers_ia(self, i):
        if type(i) == list:
            ia = np.array(i)
        return (i + self.iemin) * self.NXa

if __name__ == "__main__":
    Xe = 1e-2
    liste_xmin_xmax = 0.111, 0.989
    bdt = AxeXBase(liste_xmin_xmax, Xe)
    print(bdt)
    vecteur_x = bdt.lire_vecteur_x()
    print(vecteur_x)
    # bdt2 = calculer_axe_x_base(vecteur_x)

    # # print(bdt)    
    # print(bdt2)

