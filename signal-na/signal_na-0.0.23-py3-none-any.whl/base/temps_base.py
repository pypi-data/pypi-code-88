import numpy as np
import copy

import os, sys

from numpy.core.numeric import convolve
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))

import base.constantes_base as cst

def calculer_base_de_temps(vecteur_t):
        """
        Renvoie une base de temps correspondant au vecteur_t
        """
        assert len(vecteur_t) > 0, "calculer_base_de_temps: vecteur_t ne doit pas être vide"
        tmin, tmax = vecteur_t[0], vecteur_t[-1]
        vecteur_Te = vecteur_t[1:] - vecteur_t[:-1]
        Te = vecteur_Te.mean()
        return TempsBase([tmin, tmax+Te], Te)

class TempsBase():
    __Pa = cst.Pa

    liste_bases_de_temps_sysam = [0]

    def __init__(self, liste_tmin_tmax = cst.liste_tmin_tmax, Te = cst.Te, Nbase = 0):
        """
        Initialisation d'une base de temps:
        """
        tmin, tmax = liste_tmin_tmax
        self.__NTa = int(np.round(Te * 10**self.__Pa))
        self.__iemin =self.__convertir_ia_vers_ie(self.__convertir_t_vers_ia(tmin))
        self.__iemax = self.__convertir_ia_vers_ie(self.__convertir_t_vers_ia(tmax))
        self.__Nbase = Nbase

    def lire_NTa(self):
        return self.__NTa

    def lire_iemin(self):
        return self.__iemin

    def lire_iemax(self):
        return self.__iemax

    def lire_Nbase(self):
        return self.__Nbase
        
    def lire_Ta(self):
        return self.__Ta
    
    def lire_Pa(self):
        return self.__Pa
        
    def calculer_N(self):
        return self.__iemax - self.__iemin

    def calculer_Te(self):
        return self.__NTa / 10**self.__Pa

    def calculer_liste_tmin_tmax(self):
        """
        Calcule la liste liste_tmin_tamx de la base de temps
        """
        return list(self.__convertir_ia_vers_t(self.__convertir_ie_vers_ia([self.__iemin, self.__iemax])))
        
    def calculer_vecteur_t(self, liste_imin_imax = None):
        """
            Renvoie le vecteur des instants présents dans la base de temps entre les indices imin et imax
        """
        if liste_imin_imax == None:
            imin, imax = 0, self.__iemax - self.__iemin
        else:
            imin, imax = liste_imin_imax
        imin, imax = max(0, imin), min(self.__iemax - self.__iemin, imax)
        return self.__convertir_ia_vers_t(self.__convertir_i_vers_ia(np.arange(imin, imax)))   

    def copier(self):
        return copy.deepcopy(self)

    def __str__(self):
        return str([self.__iemin, self.__iemax, self.__NTa, self.__Nbase])

    def __eq__(self, other):
        return self.__iemin == other.__iemin and self.__iemax == other.__iemax and  self.__NTa == other.__NTa and  self.__Nbase == other.__Nbase 

    def __convertir_t_vers_ia(self, t):
        if type(t) == list:
            t = np.array(t)
        return np.round(t * 10**self.__Pa).astype(dtype = np.int64)

    def __convertir_ia_vers_t(self, ia):
        if type(ia) == list:
            ia = np.array(ia)
        return ia / 10**self.__Pa

    def __convertir_ia_vers_ie(self, ia):
        if type(ia) == list:
            ia = np.array(ia)
        return np.round(ia / self.__NTa).astype(dtype = np.int64)

    def __convertir_ie_vers_ia(self, ie):
        if type(ie) == list:
            ie = np.array(ie)
        return ie * self.__NTa
    
    def __convertir_ia_vers_i(self, ia):
        if type(ia) == list:
            ia = np.array(ia)
        return np.round(ia / self.__NTa - self.__iemin).astype(dtype = np.int64)

    def __convertir_i_vers_ia(self, i):
        if type(i) == list:
            ia = np.array(i)
        return (i + self.__iemin) * self.__NTa

if __name__ == "__main__":
    Te = 1e-2
    liste_tmin_tmax = 0.111, 0.989
    bdt = TempsBase(liste_tmin_tmax, Te)
    print(bdt)
    vecteur_t = bdt.calculer_vecteur_t()
    print(vecteur_t)
    bdt2 = calculer_base_de_temps(vecteur_t)

    # print(bdt)    
    print(bdt2)

