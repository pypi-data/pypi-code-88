import matplotlib.pyplot as plt
import numpy as np

import os, sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))

import base.utiles_base as utb

class PlotConfig():
    def __init__(self, liste_xmin_xmax = None, liste_ymin_ymax = None, nouvelle_figure = False, affichage = False, legende = False, titre = None, liste_nombre_axes = None, indice_axe = None, logX = False, omega = None, deg = True, phi0 = 0, dB = False, dBmin = -100, G = True):
        self.liste_xmin_xmax = liste_xmin_xmax
        self.liste_ymin_ymax = liste_ymin_ymax
        self.nouvelle_figure = nouvelle_figure
        self.titre = titre
        self.affichage = affichage
        self.legende = legende
        self.liste_nombre_axes = liste_nombre_axes
        self.indice_axe = indice_axe
        self.dB = dB
        self.deg = deg
        self.logX = logX
        self.phi0 = phi0
        self.dBmin = dBmin
        self.omega = omega
        self.G = G
        
    def lire_axe(self):
        indice_axe = 1 if self.indice_axe == None else self.indice_axe + 1
        liste_nombre_axes = [indice_axe, 1] if self.liste_nombre_axes == None else self.liste_nombre_axes

        if self.nouvelle_figure or (len(plt.get_fignums()) == 0):
            plt.subplots(liste_nombre_axes[0], liste_nombre_axes[1], constrained_layout = True)
            fig = plt.gcf()
            fig.liste_nombre_axes = liste_nombre_axes
            plt.sca(fig.axes[0])
        
        fig = plt.gcf()
        if self.liste_nombre_axes != None:
            assert self.__tester_ou_initialiser_liste_nombre_axes(fig), "La configuration des sous axes n'est pas valide"
            if self.indice_axe != None:
                fig = plt.gcf()
                assert self.indice_axe < len(fig.axes), "La configuration des sous axes n'est pas valide"
                return fig.axes[self.indice_axe]
        elif self.indice_axe != None:
            fig = plt.gcf()
            assert self.indice_axe < len(fig.axes), "La configuration des sous axes n'est pas valide"
            return fig.axes[self.indice_axe]

        return plt.gca()

    def __tester_ou_initialiser_liste_nombre_axes(self, fig):
        try:
            liste_nombre_axes_fig = fig.liste_nombre_axes
        except:
            if len(fig.axes) == self.liste_nombre_axes[0]*self.liste_nombre_axes[1]:
                fig.liste_nombre_axes = liste_nombre_axes_fig = self.liste_nombre_axes
            else:
                return False
        return liste_nombre_axes_fig[0] == self.liste_nombre_axes[0] and liste_nombre_axes_fig[1] == self.liste_nombre_axes[1]
