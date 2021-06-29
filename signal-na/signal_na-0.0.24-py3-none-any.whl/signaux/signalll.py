#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 15:43:58 2019

@author: nicolas
"""

import os, sys
import matplotlib.pyplot as plt

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))

import base.constantes_base as cst

import base.utiles_base as utb
from base.axe_x_base import AxeXBase
from signaux.signal_complet import SignalComplet
from signaux.signal_sinus import SignalSinus
from signaux.signal_carre import SignalCarre
from signaux.signal_triangle import SignalTriangle
from signaux.signal_wav import SignalWav
from signaux.signal_fourier import SignalFourier

import numpy as np

__all__ = ["Signal"]

liste_types_signaux = ["cosinus", "carre", "triangle", "wav", "fourier", "sysam"]

class Signal(SignalComplet):
    def __init__(self, *args, **kwargs):
        args = list(args)
        type_signal = utb.analyser_args_kwargs(args, kwargs, "type_signal", lambda x: isinstance(x, str), cst.type_signal)
        F = utb.analyser_args_kwargs(args, kwargs, "F", lambda x: isinstance(x, (int, float)), cst.F)
        Vpp = utb.analyser_args_kwargs(args, kwargs, "Vpp", lambda x: isinstance(x, (int, float)), cst.Vpp)
        offset = utb.analyser_args_kwargs(args, kwargs, "offset", lambda x: isinstance(x, (int, float)), 0.)
        Te = utb.analyser_args_kwargs(args, kwargs, "Te", lambda x: isinstance(x, (int, float)), cst.Xe)
        liste_tmin_tmax = utb.analyser_args_kwargs(args, kwargs, "liste_tmin_tmax", lambda x: isinstance(x, list) and len(x) ==2, cst.liste_xmin_xmax)
        nom = utb.analyser_args_kwargs(args, kwargs, "nom", lambda x: isinstance(x, str), "")
        tr = utb.analyser_args_kwargs(args, kwargs, "tr", lambda x: isinstance(x, (int, float)), 0.)
        phi = utb.analyser_args_kwargs(args, kwargs, "phi", lambda x: isinstance(x, (int, float)), 0.)
        alpha = utb.analyser_args_kwargs(args, kwargs, "alpha", lambda x: isinstance(x, (int, float)), 0.5)

        liste_an = utb.analyser_args_kwargs(args, kwargs, "liste_an", lambda x: isinstance(x, list), cst.liste_an)
        liste_bn = utb.analyser_args_kwargs(args, kwargs, "liste_bn", lambda x: isinstance(x, list), cst.liste_bn)

        nom_fichier_wav = utb.analyser_args_kwargs(args, kwargs, "nom_fichier_wav", lambda x: isinstance(x, str), "Choisir un nom.wav")
        Pbits = utb.analyser_args_kwargs(args, kwargs, "alpha", lambda x: isinstance(x, int), 16)
        liste_umin_umax = utb.analyser_args_kwargs(args, kwargs, "liste_umin_umax", lambda x: isinstance(x, list) and len(x) ==2, cst.liste_umin_umax)

        nom_voie = utb.analyser_args_kwargs(args, kwargs, "nom_voie", lambda x: (x == None) or isinstance(x, str), None)
        calibre = utb.analyser_args_kwargs(args, kwargs, "calibre", lambda x: isinstance(x, (int, float)), cst.calibre)
        repetition = utb.analyser_args_kwargs(args, kwargs, "repetition", lambda x: isinstance(x, bool), cst.repetition)

        seuil = utb.analyser_args_kwargs(args, kwargs, "seuil", lambda x: (x == None) or isinstance(x, (int, float)), None)
        montant = utb.analyser_args_kwargs(args, kwargs, "montant", lambda x: isinstance(x, bool), True)
        pretrigger = utb.analyser_args_kwargs(args, kwargs, "pretrigger", lambda x: isinstance(x, int), 0)
        pretrigger_souple = utb.analyser_args_kwargs(args, kwargs, "pretrigger_souple", lambda x: isinstance(x, bool), False)
        hysteresys = utb.analyser_args_kwargs(args, kwargs, "hysteresys", lambda x: isinstance(x, bool), False)
        

        axe_x_base = AxeXBase(liste_tmin_tmax, Te)

        assert type_signal in liste_types_signaux, "Ce type de signaux n'existe pas"

        if type_signal == "cosinus":
            SignalSinus.__init__(self, F, Vpp, offset, phi, tr, liste_tmin_tmax, Te, nom)
        elif type_signal == "carre":
            SignalCarre.__init__(self, F, Vpp, offset, alpha, tr, liste_tmin_tmax, Te, nom)
        elif type_signal == "triangle":
            SignalTriangle.__init__(self, F, Vpp, offset, alpha, tr, liste_tmin_tmax, Te, nom)
        elif type_signal == "fourier":
            SignalFourier.__init__(self, F, liste_an, liste_bn, liste_tmin_tmax, Te, nom)
        elif type_signal == "wav":
            SignalWav.__init__(self, nom_fichier_wav, Pbits, liste_umin_umax, nom)
        else:
            SignalComplet.__init__(self, axe_x_base, [], nom)

        voie_base = self._Signal6Sysam__lire_voie_base()
        voie_base.nom = nom_voie
        voie_base.calibre = calibre
        voie_base.repetition = repetition

        trigger_base = self._Signal6Sysam__lire_trigger_base()        
        trigger_base.seuil = seuil
        trigger_base.montant = montant
        trigger_base.pretrigger = pretrigger
        trigger_base.pretrigger_souple = pretrigger_souple
        trigger_base.hysteresys = hysteresys

if __name__ == "__main__":

    # s1 = Signal("cosinus", 2e2, nom_voie = "EA0", seuil = 0, phi=-np.pi/2)
    # s1.tracer()
    s1 = Signal(voie = "SA1", F = 440, Vpp = 19, liste_tmin_tmax = [0, 5], Te = 1/40e3).quantifier(8)
    s1.tracer()