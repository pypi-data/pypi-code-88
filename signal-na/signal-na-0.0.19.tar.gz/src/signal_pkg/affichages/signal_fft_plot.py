#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 15:43:58 2019

@author: nicolas
"""
import numpy as np
import matplotlib.pyplot as plt

import os, sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))
from traitements.signal_fft import SignalFFT
from signaux.signal_base import SignalBase
from base.temps_base import BaseTemps
from base.frequence_base import BaseFrequence
import base.utiles_base as utb

__all__ = ["tracer_spectres"]

def tracer_spectres(liste_signaux, liste_fmin_fmax = [None, None], superposition = True, nom_fichier = ""):
    SignalFFTPlot.tracer_spectres(liste_signaux, liste_fmin_fmax, superposition)

def tracer_spectres(*args, **kwargs):
    args = list(args)
    if isinstance(args, list) and len(args) > 0 and isinstance(args[0], SignalBase):
        s = args.pop(0)
    else:
        print("Quels sont les signaux à tracer?")
        return
    s.tracer_spectres(*args, **kwargs)

class SignalFFTPlot(SignalFFT, SignalBase):
    def __tracer_spectre(self, liste_fmin_fmax, **kwargs):
        axe = plt.gca()    
        if self.nom != "":
            kwargs["label"] = self.nom

        fmin, fmax = liste_fmin_fmax

        liste_imin_imax = self.__choisir_liste_ilim(liste_fmin_fmax)
        vecteur_spectre = self.calculer_vecteur_spectre(liste_imin_imax)
        vecteur_f = self.base_de_frequence.calculer_vecteur_f(liste_imin_imax)

        plt.plot(vecteur_f, vecteur_spectre, **kwargs)
        plt.xlabel("$f$ (en Hz)")
        plt.ylabel("$U$ (en SI)")
        axe.set_xlim(fmin, fmax)
        plt.legend()

    def tracer_spectre(self, *args, **kwargs):
        args = list(args)
        liste_fmin_fmax = utb.analyser_args_kwargs(args, kwargs, "liste_fmin_fmax", lambda x: isinstance(x, list) and len(x) ==2, [None, None])
        titre = utb.analyser_args_kwargs(args, kwargs, "titre", lambda x: isinstance(x, str), "")
        affichage = utb.analyser_args_kwargs(args, kwargs, "affichage", lambda x: isinstance(x, bool), True)
        nom_fichier = utb.analyser_args_kwargs(args, kwargs, "nom_fichier", lambda x: isinstance(x, str), "")
        
        fmin, fmax = self.__choisir_liste_flim([self], liste_fmin_fmax)
        
        self.__tracer_spectre([fmin, fmax], **kwargs)
        if titre != "":
            plt.suptitle(titre)
        if nom_fichier != "":
            plt.savefig(nom_fichier)
            if not affichage:
                plt.close(fig)
        if affichage:
            plt.show()

    def tracer_spectres(self, *args, **kwargs):
        args = list(args)
        liste_signaux = [self]
        test_signal = len(args) > 0 and isinstance(args[0], SignalBase)
        while test_signal:
            liste_signaux.append(utb.analyser_args(args, " ", lambda x: isinstance(x, SignalBase), self)[0])
            test_signal = len(args) > 0 and isinstance(args[0], SignalBase)
        liste_fmin_fmax = utb.analyser_args_kwargs(args, kwargs, "liste_fmin_fmax", lambda x: isinstance(x, list) and len(x) ==2, [None, None])
        superposition = utb.analyser_args_kwargs(args, kwargs, "superposition", lambda x: isinstance(x, bool), True)
        titre = utb.analyser_args_kwargs(args, kwargs, "titre", lambda x: isinstance(x, str), "")
        affichage = utb.analyser_args_kwargs(args, kwargs, "affichage", lambda x: isinstance(x, bool), True)
        nom_fichier = utb.analyser_args_kwargs(args, kwargs, "nom_fichier", lambda x: isinstance(x, str), "")
              
        if superposition == True:
            SignalFFTPlot.__tracer_spectres_superposes(liste_signaux, liste_fmin_fmax)
        else:
            SignalFFTPlot.__tracer_spectres_non_superposes(liste_signaux, liste_fmin_fmax)
        if titre != "":
            plt.suptitle(titre)
        if nom_fichier != "":
            plt.savefig(nom_fichier)
            if not affichage:
                    fig = plt.gcf()
                    plt.close(fig)
        if affichage:
            plt.show()

    def __choisir_liste_flim(self, liste_signaux, liste_fmim_fmax):
        fmin, fmax = liste_fmim_fmax
        _fmin = 0
        _fmax = np.max([1/(2*s.base_de_temps.Te) for s in liste_signaux])
        if fmin == None:
            fmin = _fmin
        if fmax == None:
            fmax = _fmax
        return fmin, fmax

    def __choisir_liste_ilim(self, liste_fmim_fmax):
        fmin, fmax = liste_fmim_fmax
        _fmin , _fmax = 0, 1/(2*self.base_de_temps.Te)
        if fmin < 0:
            fmin = _fmin
        if fmax > _fmax:
            fmax = _fmax
        return self.base_de_frequence.calculer_i(fmin), self.base_de_frequence.calculer_i(fmax)

    def __tracer_spectres_superposes(liste_signaux, liste_fmin_fmax = [None, None]):
        Nsignaux = len(liste_signaux)
        fig = plt.gcf()
        liste_axes = fig.axes
        if len(liste_axes) > 1:
            fig = plt.Figure()
        _fmin, _fmax = liste_signaux[0].__choisir_liste_flim(liste_signaux, liste_fmin_fmax)
        for i in range(Nsignaux):
            liste_signaux[i].tracer_spectre([_fmin, _fmax], affichage = False)
        axe = plt.gca()

    def __tracer_spectres_non_superposes(liste_signaux, liste_fmin_fmax = [None, None]):
        Nsignaux = len(liste_signaux)
        if Nsignaux == 1:
            liste_signaux[0].tracer_spectre(liste_fmin_fmax, affichage = False)
            return
        fig, liste_axes = plt.subplots(Nsignaux, 1, constrained_layout=True)
        _fmin, _fmax = liste_signaux[0].__choisir_liste_flim(liste_signaux, liste_fmin_fmax)
        for i in range(Nsignaux):
            axe = liste_axes[i]
            plt.sca(axe)
            liste_signaux[i].tracer_spectre([_fmin, _fmax], affichage = False)
        
if __name__ == "__main__":
    Te1 = 1e-4
    liste_tmin_tmax1 = 0, 10

    Te2 = 1e-3
    liste_tmin_tmax2 = 0.05, 1.05

    bdt1 = BaseTemps(liste_tmin_tmax1, Te1)
    bdt2 = BaseTemps(liste_tmin_tmax2, Te2)

    vecteur_t1 = bdt1.calculer_vecteur_t()
    vecteur_t2 = bdt2.calculer_vecteur_t()
    vecteur_signal1 = 3*np.cos(2*np.pi*30*vecteur_t1)
    vecteur_signal2 = np.sin(2*np.pi*10*vecteur_t2)

    s1 = SignalFFTPlot(bdt1, vecteur_signal1, nom="s1")
    s2 = SignalFFTPlot(bdt2, vecteur_signal2, nom="s2")

    tracer_spectres(s1, s2, [0, 100], superposition = False)
