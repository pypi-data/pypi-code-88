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
from signaux.signal_base import SignalBase
from base.temps_base import BaseTemps
import base.utiles_base as utb

__all__ = ["tracer_signaux"]

def tracer_signaux(*args, **kwargs):
    args = list(args)
    if isinstance(args, list) and len(args) > 0 and isinstance(args[0], SignalBase):
        s = args.pop(0)
    else:
        print("Quels sont les signaux à tracer?")
        return
    s.tracer_signaux(*args, **kwargs)
    
class SignalPlot(SignalBase):
    def tracer_signal(self, liste_tmin_tmax, **kwargs):
        axe = plt.gca()    
        if self.nom != "":
            kwargs["label"] = self.nom
        imin, imax = self.__choisir_liste_imin_imax(liste_tmin_tmax)
        vecteur_t = self.calculer_vecteur_t([imin, imax])
        axe.plot(vecteur_t, self.vecteur_signal[imin:imax], **kwargs)
        plt.xlabel("$t$ (en s)")
        plt.ylabel("$u$ (en V)")
        plt.legend()
        tmin, tmax = liste_tmin_tmax 
        axe.set_xlim(tmin, tmax)
        try:
            axe.liste_signaux.append(self)
        except:
            axe.liste_signaux = [self]
        liste_signaux_base_de_temps_ko = utb.lister_test(axe.liste_signaux[:], lambda s: s.base_de_temps.Nsysam != self.base_de_temps.Nsysam, lambda s: s.nom)
        if len(liste_signaux_base_de_temps_ko) > 0:
            print("La base de temps du signal {0} n'est pas compatible avec celle des signaux suivants:".format(self), end = "\n ->")
            utb.print_liste(liste_signaux_base_de_temps_ko)

    def tracer(self, *args, **kwargs):
        args = list(args)
        liste_tmin_tmax = utb.analyser_args_kwargs(args, kwargs, "liste_tmin_tmax", lambda x: isinstance(x, list) and len(x) ==2, [None, None])
        titre = utb.analyser_args_kwargs(args, kwargs, "titre", lambda x: isinstance(x, str), "")
        affichage = utb.analyser_args_kwargs(args, kwargs, "affichage", lambda x: isinstance(x, bool), True)
        nom_fichier = utb.analyser_args_kwargs(args, kwargs, "nom_fichier", lambda x: isinstance(x, str), "")
        
        tmin, tmax = self.__choisir_liste_tlim([self], liste_tmin_tmax)
        self.tracer_signal([tmin, tmax], **kwargs)
        axe = plt.gca()
        if titre != "":
            plt.suptitle(titre)
        if nom_fichier != "":
            plt.savefig(nom_fichier)
            if not affichage:
                plt.close(fig)
        if affichage:
            plt.show()
        
    def tracer_signaux(self, *args, **kwargs):
        args = list(args)
        liste_signaux = [self]
        test_signal = len(args) > 0 and isinstance(args[0], SignalBase)
        while test_signal:
            liste_signaux.append(utb.analyser_args(args, " ", lambda x: isinstance(x, SignalBase), self)[0])
            test_signal = len(args) > 0 and isinstance(args[0], SignalBase)
        liste_tmin_tmax = utb.analyser_args_kwargs(args, kwargs, "liste_tmin_tmax", lambda x: isinstance(x, list) and len(x) ==2, [None, None])
        superposition = utb.analyser_args_kwargs(args, kwargs, "superposition", lambda x: isinstance(x, bool), True)
        titre = utb.analyser_args_kwargs(args, kwargs, "titre", lambda x: isinstance(x, str), "")
        affichage = utb.analyser_args_kwargs(args, kwargs, "affichage", lambda x: isinstance(x, bool), True)
        nom_fichier = utb.analyser_args_kwargs(args, kwargs, "nom_fichier", lambda x: isinstance(x, str), "")
              
        if superposition == True:
            SignalPlot.__tracer_signaux_superposes(liste_signaux, liste_tmin_tmax)
        else:
            SignalPlot.__tracer_signaux_non_superposes(liste_signaux, liste_tmin_tmax)
        if titre != "":
            plt.suptitle(titre)
        if nom_fichier != "":
            plt.savefig(nom_fichier)
            if not affichage:
                    fig = plt.gcf()
                    plt.close(fig)
        if affichage:
            plt.show()

    def __choisir_liste_tlim(self, liste_signaux, liste_tmim_tmax):
        tmin, tmax = liste_tmim_tmax
        _tmin = np.min([s.base_de_temps.calculer_t(s.base_de_temps.Nmin) for s in liste_signaux])
        _tmax = np.max([s.base_de_temps.calculer_t(s.base_de_temps.Nmax) for s in liste_signaux])
        if tmin == None:
            tmin = _tmin
        if tmax == None:
            tmax = _tmax
        return tmin, tmax

    def __choisir_liste_imin_imax(self, liste_tmin_tmax):
        tmin, tmax = liste_tmin_tmax
        _tmin , _tmax = self.base_de_temps.calculer_t(self.base_de_temps.Nmin), self.base_de_temps.calculer_t(self.base_de_temps.Nmax)
        if tmin < _tmin:
            tmin = _tmin
        if tmax > _tmax:
            tmax = _tmax
        Nmin, Nmax = self.base_de_temps.calculer_n(tmin), self.base_de_temps.calculer_n(tmax)
        return self.base_de_temps.convertir_n_vers_i(Nmin), self.base_de_temps.convertir_n_vers_i(Nmax)

    def __tracer_signaux_superposes(liste_signaux, liste_tmin_tmax = [None, None]):
        Nsignaux = len(liste_signaux)
        fig = plt.gcf()
        liste_axes = fig.axes
        if len(liste_axes) > 1:
            fig = plt.Figure()
        _tmin, _tmax = liste_signaux[0].__choisir_liste_tlim(liste_signaux, liste_tmin_tmax)
        for i in range(Nsignaux):
            liste_signaux[i].tracer([_tmin, _tmax], affichage = False)
        axe = plt.gca()

    def __tracer_signaux_non_superposes(liste_signaux, liste_tmin_tmax = [None, None]):
        Nsignaux = len(liste_signaux)
        if Nsignaux == 1:
            liste_signaux[0].tracer(liste_tmin_tmax, affichage = False)
            return
        fig, liste_axes = plt.subplots(Nsignaux, 1, constrained_layout=True)
        _tmin, _tmax = liste_signaux[0].__choisir_liste_tlim(liste_signaux, liste_tmin_tmax)
        for i in range(Nsignaux):
            axe = liste_axes[i]
            plt.sca(axe)
            liste_signaux[i].tracer([_tmin, _tmax], affichage = False)

if __name__ == "__main__":
    Te1 = 1e-4
    liste_tmin_tmax1 = -1.05, 0.35

    Te2 = 1e-3
    liste_tmin_tmax2 = 0.05, 1.05

    bdt1 = BaseTemps(liste_tmin_tmax1, Te1)
    bdt2 = BaseTemps(liste_tmin_tmax2, Te2)

    vecteur_t1 = bdt1.calculer_vecteur_t()
    vecteur_t2 = bdt2.calculer_vecteur_t()
    vecteur_signal1 = np.cos(2*np.pi*vecteur_t1)
    vecteur_signal2 = np.sin(2*np.pi*vecteur_t2)

  

    s1 = SignalPlot(bdt1, vecteur_signal1)
    s2 = SignalPlot(bdt2, vecteur_signal2)
    #s1.tracer([-2, 0.1], nom_fichier = "essai.pdf", color = "red")
    tracer_signaux(s2, s1, [0,1], affichage = False, nom_fichier = "abc.pdf", titre = "zorro", superposition = False)
    tracer_signaux(s1, s2, [0,1], affichage = False, titre = "zara", superposition = True)
    plt.show()
    