import matplotlib.pyplot as plt
import numpy as np

import os, sys

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))

import base.utiles_base as utb
import base.angle_base as anb

from plot.plot_config import PlotConfig
from plot.axe_plot_config import AxePlotConfig

from base.axe_base import AxeBase
from base.axe_x_base import AxeXBase

import signal_pkg

__all__ = ["PlotBase", "tracer"]

class PlotBase():
    def __tester_plot_base(self):
        return True

    def __lire_axe_x_base(self):
        try:
            axe_x_base = self.__axe_x_base
        except:
            self.__axe_x_base = axe_x_base = AxeXBase()
        return axe_x_base

    def __lire_axe_y_base(self):
        try:
            axe_y_base = self.__axe_y_base
        except:
            self.__axe_y_base = axe_y_base = AxeBase()
        return axe_y_base
        
    def __str__(self):
        return "nom"
    
    def tracer(self, *args, **kwargs):
        tracer(self, *args, **kwargs)


def tester_liste_unites(axe, axe_plot_config):
    ux, uy = [axe_plot_config.ux, axe_plot_config.uy]
    try:
        liste_unites_axe = axe.liste_unites
    except:
        axe.liste_unites = liste_unites_axe = [ux, uy]
    return ux == liste_unites_axe[0] and uy == liste_unites_axe[1]

def __plot(signal, config_plot, *args, **kwargs):
    args = list(args)
    
    axe  = config_plot.lire_axe()
    axe_plot_config = AxePlotConfig(signal, config_plot)

    assert tester_liste_unites(axe, axe_plot_config), "Les unités de l'axe sont incompatibles"

    if "label" not in kwargs:
        kwargs["label"] = str(signal)

    plt.sca(axe)

    axe_plot_config = AxePlotConfig(signal, config_plot)

    axe_plot_config.fonction_plot(axe_plot_config.vecteur_x, axe_plot_config.vecteur_y, **kwargs)

    if config_plot.liste_xmin_xmax != None:
        plt.xlim(*config_plot.liste_xmin_xmax)
    if config_plot.liste_ymin_ymax != None:
        plt.ylim(*config_plot.liste_ymin_ymax)

    plt.xlabel("{0} (en {1})".format(axe_plot_config.nomx, axe_plot_config.ux))
    plt.ylabel("{0} (en {1})".format(axe_plot_config.nomy, axe_plot_config.uy))

    if config_plot.legende:
        plt.legend()

    if config_plot.titre:
        plt.suptitle(config_plot.titre)

    if config_plot.affichage:
        plt.show()    

def tracer(*args, **kwargs):
    args = list(args)
    
    liste_a_tracer = []
    
    try:
        test_signal = args[0]._PlotBase__tester_plot_base()
    except:
        test_signal = False

    
    while test_signal:
        liste_a_tracer.append(utb.analyser_args(args, " ", lambda x: True, "?")[0])
        try:
            test_signal = args[0]._PlotBase__tester_plot_base()
        except:
            test_signal = False

    liste_xmin_xmax = utb.analyser_args_kwargs(args, kwargs, "liste_xmin_xmax", lambda x: x== None or (isinstance(x, list) and len(x) ==2), None)
    superposition = utb.analyser_args_kwargs(args, kwargs, "superposition", lambda x: isinstance(x, bool), True)
    titre = utb.analyser_args_kwargs(args, kwargs, "titre", lambda x: x == None or isinstance(x, str), None)
    liste_ymin_ymax = utb.analyser_args_kwargs(args, kwargs, "liste_ymin_ymax", lambda x: x== None or (isinstance(x, list) and len(x) ==2), None)
    affichage = utb.analyser_args_kwargs(args, kwargs, "affichage", lambda x: isinstance(x, bool), True)
    nouvelle_figure = utb.analyser_args_kwargs(args, kwargs, "nouvelle_figure", lambda x: isinstance(x, bool), True)
    legende = utb.analyser_args_kwargs(args, kwargs, "legende", lambda x: isinstance(x, bool), True)
    indice_axe = utb.analyser_args_kwargs(args, kwargs, "indice_axe", lambda x: isinstance(x, int), 0)
    liste_nombre_axes = utb.analyser_args_kwargs(args, kwargs, "liste_nombre_axes", lambda x: x== None or (isinstance(x, list) and len(x) ==2), None)


    omega = utb.analyser_args_kwargs(args, kwargs, "omega", lambda x: x == None or isinstance(x, bool), None)
    deg = utb.analyser_args_kwargs(args, kwargs, "deg", lambda x: isinstance(x, bool), True)
    dB = utb.analyser_args_kwargs(args, kwargs, "dB", lambda x: x == None or isinstance(x, bool), None)
    logX = utb.analyser_args_kwargs(args, kwargs, "logX", lambda x: x == None or isinstance(x, bool), None)
    G = utb.analyser_args_kwargs(args, kwargs, "G", lambda x: isinstance(x, bool), True)

    phi0 = utb.analyser_args_kwargs(args, kwargs, "deg", lambda x: isinstance(x, (int, float)), 0)
    dBmin = utb.analyser_args_kwargs(args, kwargs, "dBmin", lambda x: isinstance(x, (int, float)), -500)
    
    N = len(liste_a_tracer)

    if N == 1:
        cfg = PlotConfig(liste_xmin_xmax=liste_xmin_xmax, liste_ymin_ymax=liste_ymin_ymax, nouvelle_figure=nouvelle_figure, affichage=affichage, legende=legende, titre=titre, liste_nombre_axes = liste_nombre_axes, indice_axe=indice_axe, deg = deg, dB = dB, logX = logX, phi0 = phi0, dBmin = dBmin, omega = omega, G = G)
        __plot(liste_a_tracer[0], cfg)
    elif N > 1: 
        if superposition:
            cfg = PlotConfig(liste_xmin_xmax=liste_xmin_xmax, liste_ymin_ymax=liste_ymin_ymax, nouvelle_figure=nouvelle_figure, affichage=False, legende=legende, titre=titre, liste_nombre_axes = liste_nombre_axes, indice_axe=indice_axe, deg = deg, dB = dB, logX = logX, phi0 = phi0, dBmin = dBmin, omega = omega, G = G)
            __plot(liste_a_tracer[0], cfg)
            cfg.nouvelle_figure = False
            for i in range(1, N-1):
                __plot(liste_a_tracer[i], cfg)
            cfg.affichage = affichage
            __plot(liste_a_tracer[-1], cfg)
        else:
            liste_nombre_axes = liste_nombre_axes if liste_nombre_axes != None else [N, 1]
            cfg = PlotConfig(liste_xmin_xmax=liste_xmin_xmax, liste_ymin_ymax=liste_ymin_ymax, nouvelle_figure=nouvelle_figure, affichage=False, legende=legende, titre=titre, liste_nombre_axes = liste_nombre_axes, indice_axe=0, deg = deg, dB = dB, logX = logX, phi0 = phi0, dBmin = dBmin, omega = omega, G = G)
            __plot(liste_a_tracer[0], cfg)
            cfg.nouvelle_figure = False
            for i in range(1, N-1):
                cfg.indice_axe = i
                __plot(liste_a_tracer[i], cfg)
            cfg.affichage = affichage
            cfg.indice_axe = N-1
            __plot(liste_a_tracer[-1], cfg)
