import numpy as np
import matplotlib.pyplot as plt

import os, sys


sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))

import base.utiles_base as utb
from base.mesure_bode_base import MesureBodeBase
from plot.plot_base import PlotBase
from base.axe_base import AxeBase
from base.axe_x_base import AxeXBase
from base.filtrage_base import calculer_sortie_filtre

fonction_H_0 = lambda f: 1

class FiltreBase(PlotBase):
    __liste_n_filtres = [0]
    
    def __init__(self, fonction_H = None, omega = False, nombre_cs_frequence = None, nom = ""):
        PlotBase.__init__(self)
        axe_x_base = self._PlotBase__lire_axe_x_base()
        axe_y_base = self._PlotBase__lire_axe_y_base()        
        axe_x_base.cloner(AxeXBase(nom = "f", unite = "Hz"))
        axe_y_base.cloner(AxeBase("H", ""))
        # axe_x_base.omega = omega

        self.__liste_mesures = []    
        self.__fonction_H = fonction_H
        self.__omega = omega
        self.__nombre_cs_frequence = nombre_cs_frequence

        self.__ecrire_nom(nom)

    def __ecrire_nom(self, nom):
        if nom != "":
            self.__nom = nom
        else:
            numero = np.max(self.__liste_n_filtres)+1
            self.__nom = "f_" + str(numero)
            self.__liste_n_filtres.append(numero)

    def lire_nom(self):
        return self.__nom
        
    def lire_vecteur_x(self):
        return np.array([m.f for m in self.__liste_mesures])
        
    def lire_vecteur_y(self):
        return np.array([m.H for m in self.__liste_mesures])
        
    def __str__(self):
        return self.__nom

    
    def __calculer_f(self, x, omega = False):
        def calculer_1f(self, x, omega):
            f = x/(2*np.pi) if omega else x
            return self.__arrondir_f(f)
                    
        if isinstance(x, (int, float, np.int64, np.float64)):
            return calculer_1f(self, x, omega)
        elif isinstance(x, (list, np.ndarray)):
            liste_f = [calculer_1f(self, xi, omega) for xi in x]
            if isinstance(x, list):
                return liste_f
            else:
                return np.array(liste_f, dtype=np.float64)

        assert 1 == 2, "__calculer_f non pris en charge pour ces données"
    
    def __calculer_vecteur_f(self, liste_xmin_xmax, N, omega = False, logX = True):
        fmin, fmax = self.__calculer_f(liste_xmin_xmax, omega)
        fonction_space = np.logspace if logX else np.linspace
        Xmin, Xmax = (np.log10(fmin), np.log10(fmax)) if logX else (fmin, fmax)
        
        return self.__calculer_f(fonction_space(Xmin, Xmax, N), omega = False)

    def __arrondir_f(self, f):
        if self.__nombre_cs_frequence == None:
            return f
        else:
            nombre_cs_frequence = max(1, self.__nombre_cs_frequence)
            mult = 1
            while f >= 10**nombre_cs_frequence:
                f /= 10
                mult *= 10
            return np.round(f)*mult
    
    def __calculer_x(self, f, omega = False):
        def calculer_1x(self, f, omega):
            return f*2*np.pi if omega else f
                    
        if isinstance(f, (int, float, np.int64, np.float64)):
            return calculer_1x(self, f, omega)
        elif isinstance(f, (list, np.ndarray)):
            liste_x = [calculer_1x(self, fi, omega) for fi in f]
            if isinstance(f, list):
                return liste_x
            else:
                return np.array(liste_x, dtype = np.float64)
        assert 1 == 2, "__calculer_x non pris en charge pour ces données"
        
    def calculer_H(self, x):
        return complex(self.__fonction_H(x))

    def __tester_nouvelles_frequences(self, vecteur_f):
        liste_f = [m.f for m in self.__liste_mesures]
        for f in vecteur_f:
            if f not in liste_f:
                return True
        return False

    def calculer_bode(self, liste_xmin_xmax = [1e2, 1e5], nombre_de_points = 100, omega = None, logX = True):
        omega = self.__omega if omega == None else omega
        vecteur_f = self.__calculer_vecteur_f(liste_xmin_xmax, nombre_de_points, omega, logX)
        if self.__tester_nouvelles_frequences(vecteur_f):
            for f in vecteur_f:
                x = self.__calculer_x(f, omega)
                if f not in [mesure.f for mesure in self.__liste_mesures]:
                    H = self.calculer_H(x)
                    if H != None:
                        self.__liste_mesures.append( MesureBodeBase(f, H) )
            self.__liste_mesures.sort(key = lambda m: m.f)

    def calculer_sortie(self, entree):
        return calculer_sortie_filtre(self, entree)

    # def plot_asymptote(self, *args, **kwargs):
    #     args = list(args)
    #     a = utb.analyser_args_kwargs(args, kwargs, "a", lambda x: isinstance(x, (int, float)), 0.)
    #     b = utb.analyser_args_kwargs(args, kwargs, "b", lambda x: isinstance(x, (int, float)), 0.)
    #     xmin = utb.analyser_args_kwargs(args, kwargs, "xmin", lambda x: x == None or isinstance(x, (int, float)), None)
    #     xmax = utb.analyser_args_kwargs(args, kwargs, "xmax", lambda x: x == None or isinstance(x, (int, float)), None)
    #     omega = utb.analyser_args_kwargs(args, kwargs, "omega", lambda x: x == None or isinstance(x, bool), None)

    #     omega = self.__omega if omega == None else omega

    #     ux = "rads" if omega else "Hz"
    #     assert utb.tester_ux(ux), "Impossible de réaffecter l'axe des abscisses"

    #     f1 = np.min([mes.f for mes in self.__liste_mesures]) if xmin == None else self.__calculer_f(xmin, omega, False)
    #     f2 = np.max([mes.f for mes in self.__liste_mesures]) if xmax == None else self.__calculer_f(xmax, omega, False)

    #     vecteur_x = self.__calculer_x(np.array([f1, f2]), omega)
    #     vecteur_y = a * np.log10(vecteur_x) + b
        

    #     args = [vecteur_x, vecteur_y] + list(args)
    #     plt.plot(*args, **kwargs)

    #     plt.xlabel("$\\omega$ (rad/s)" if omega  else "$f$ (Hz)")

    def tracer(self, *args, **kwargs):
        affichage = kwargs.get("affichage", True)
        indice_axe = kwargs.get("indice_axe", 0)

        kwargs["G"] = False
        kwargs["affichage"] = False
        kwargs["indice_axe"] = indice_axe + 1

        PlotBase.tracer(self, *args, **kwargs)

        kwargs["G"] = True
        kwargs["nouvelle_figure"] = False
        kwargs["affichage"] = affichage
        kwargs["indice_axe"] = indice_axe
        PlotBase.tracer(self, *args, **kwargs)

        

if __name__ == "__main__":
    fil = FiltreBase(fonction_H = lambda f: 1 / (1 + 1j * f / 1000)**8)
    filou = FiltreBase(fonction_H = lambda f: 1 / (1 + 1j * f / 1000)**3)
    fil.calculer_bode(liste_xmin_xmax=[1, 1e6], nombre_de_points=100, logX = True)
    filou.calculer_bode(liste_xmin_xmax=[1, 1e6], nombre_de_points=100, logX = True)

    # print([m.f for m in filou.__liste_mesures])
    fil.tracer(liste_nombre_axes = [2, 2], indice_axe = 2)

    # filou.tracer(nouvelle_figure = False, dB = True, logX = True)

