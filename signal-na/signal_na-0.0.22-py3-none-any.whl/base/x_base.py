import numpy as np
import copy

import os, sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))

import base.constantes_base as cst

def calculer_base_de_temps(vecteur_t):
    return TempsBase.calculer_base_de_temps(vecteur_t)

class TempsBase():
    __Pa = cst.Pa

    liste_bases_de_temps_sysam = [0]

    def __init__(self, liste_tmin_tmax = cst.liste_tmin_tmax, Te = cst.Te, Nbase = 0):
        """
        Initialisation d'une base de temps:
        """
        tmin, tmax = liste_tmin_tmax
        NTa = int(np.round(Te * 10**self.__Pa))
        Te = NTa / 10**self.__Pa
        Nmin, Nmax = int( np.ceil( tmin/Te ) ), int( np.ceil( tmax / Te ))

        self.__NTa = NTa
        self.__Nmin, self.__Nmax = Nmin, Nmax
        self.__Nbase = Nbase

    def lire_NTa(self):
        return self.__NTa

    def lire_Nmin(self):
        return self.__Nmin

    def lire_Nmax(self):
        return self.__Nmax

    def lire_Nbase(self):
        return self.__Nbase
        
    def lire_Ta(self):
        return self.__Ta
    
    def lire_Pa(self):
        return self.__Pa
        
    def calculer_N(self):
        return self.__Nmax - self.__Nmin

    def calculer_Te(self):
        return self.__NTa / 10**self.__Pa

    def __calculer_n(self, t):
        """
            Détermine l'indice, n, correspondant à t
        """
        return int( np.round( t * 10**self.__Pa / self.__NTa ) )

    def __convertir_n_vers_i(self, n):
        return n - self.__Nmin

    def __convertir_i_vers_n(self, i):
        return self.__Nmin + i

    def calculer_i(self, t):
        """
            Détermine l'indice, i, correspondant à t
        """
        return self.__convertir_n_vers_i( self.__calculer_n (t) ) 

    def __calculer_t(self, n):
        """
            Détermine l'instant, t, correspondant à n
        """
        return self.__NTa * self.__Ta * n 

    def calculer_t(self, i):
        """
            Détermine l'instant, t, correspondant à i
        """
        return self.__calculer_t( self.__convertir_i_vers_n(i) )

    def calculer_liste_tmin_tmax(self):
        """
        Calcule la liste liste_tmin_tamx de la base de temps
        """
        return self.__Nmin*self.__NTa / 10**self.__Pa, self.__Nmax*self.__NTa / 10**self.__Pa
        
    def __calculer_vecteur_n(self, liste_imin_imax = [None, None]):
        imin, imax = liste_imin_imax
        
        if imin == None:
            imin = 0
        if imax == None:
            imax = self.__convertir_n_vers_i(self.__Nmax)
        Nmin, Nmax = self.__convertir_i_vers_n(imin), self.__convertir_i_vers_n(imax)

        return np.arange(Nmin, Nmax)*self.__NTa

    def calculer_vecteur_t(self, liste_imin_imax = [None, None]):
        """
            Renvoie le vecteur des instants présents dans la base de temps entre les indices imin et imax
        """
        return self.__calculer_vecteur_n(liste_imin_imax) / 10**self.__Pa

    def copier(self):
        return copy.deepcopy(self)

    def __str__(self):
        return str([self.__Nmin, self.__Nmax, self.__NTa, self.__Nbase])

    def __eq__(self, other):
        return self.__Nmin == other.__Nmin and self.__Nmax == other.__Nmax and  self.__NTa == other.__NTa and  self.__Nbase == other.__Nbase 

    def calculer_base_de_temps(vecteur_t):
        """
        Renvoie une base de temps correspondant au vecteur_t
        """
        vecteur_Te = vecteur_t[1:] - vecteur_t[:-1]
        Te = vecteur_Te.mean()
        bdt = TempsBase(Te = Te)
        Nmin = bdt.__calculer_n(vecteur_t[0])
        Nmax = bdt.__calculer_n(vecteur_t[-1])+1
        liste_tmin_tmax = Nmin*bdt.calculer_Te(), Nmax*bdt.calculer_Te()
        return TempsBase(liste_tmin_tmax, Te)


if __name__ == "__main__":
    Te = 1e-1
    liste_tmin_tmax = 0.09, 3.01
    bdt = TempsBase(liste_tmin_tmax, Te)
    vecteur_t = bdt.calculer_vecteur_t()
    bdt2 = calculer_base_de_temps(vecteur_t)

    print(bdt)    
    print(bdt2)
    print(bdt2.calculer_liste_tmin_tmax())