import numpy as np
import matplotlib.pyplot as plt

import os, sys, time
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))

try:
    import pycanum.main as pycan
except:
    # print("Attention: la bibliothèque pycanum n'est pas installée")
    # print(" -> Fonctionnement en mode émulation")
    import acquisition.emulateur_sysam_sp5 as pycan

from signaux.signal_1_base import Signal1Base
from signaux.signalll import Signal

import base.axe_x_base
import base.voie_base
import base.utiles_base as utb

from sysam.sysam_sp5 import demarrer_sysam
from signaux.signalll import Signal
from plot.plot_base import tracer

__all__ = ["AcquisitionES"]

class AcquisitionES():
    def __init__(self, *args, **kwargs):
        args = list(args)
        signal_sortie_sysam = utb.analyser_args_kwargs(args, kwargs, "signal_sortie_sysam", lambda x: x == None or isinstance(x, Signal), None)
        voie_entree_filtre = utb.analyser_args_kwargs(args, kwargs, "voie_entree_filtre", lambda x: isinstance(x, str), "EA0")
        calibre_entree_filtre = utb.analyser_args_kwargs(args, kwargs, "calibre_entree_filtre", lambda x: x == None or isinstance(x, (int, float)), None)
        voie_sortie_filtre = utb.analyser_args_kwargs(args, kwargs, "voie_sortie_filtre", lambda x: isinstance(x, str), "EA1")
        calibre_sortie_filtre = utb.analyser_args_kwargs(args, kwargs, "calibre_sortie_filtre", lambda x: x == None or isinstance(x, (int, float)), None)
        duree_acquisition = utb.analyser_args_kwargs(args, kwargs, "duree_acquisition", lambda x: x == None or isinstance(x, (int, float)), 1)
        duree_attente_avant_acquisition = utb.analyser_args_kwargs(args, kwargs, "duree_attente_avant_acquisition", lambda x: x == None or isinstance(x, (int, float)), 1)
        voie_trigger = utb.analyser_args_kwargs(args, kwargs, "voie_trigger", lambda x: isinstance(x, str), "voie_entree_filtre")
        seuil = utb.analyser_args_kwargs(args, kwargs, "seuil", lambda x: isinstance(x, (int, float)), 0)
        pretrigger = utb.analyser_args_kwargs(args, kwargs, "pretrigger", lambda x: isinstance(x, int), 0)
        montant = utb.analyser_args_kwargs(args, kwargs, "montant", lambda x: isinstance(x, bool), True)
        affichage = utb.analyser_args_kwargs(args, kwargs, "affichage", lambda x: isinstance(x, bool), False)
        Te = utb.analyser_args_kwargs(args, kwargs, "Te", lambda x: x == None or isinstance(x, (int, float)), None)
        
        liste_tmin_tmax = [duree_attente_avant_acquisition, duree_attente_avant_acquisition + duree_acquisition]
        Te = Te if Te != None else signal_sortie_sysam._PlotBase__lire_axe_x_base().lire_Xe()
    
        calibre_entree_filtre_mesure = calibre_entree_filtre if calibre_entree_filtre != None else 10
        calibre_sortie_filtre_mesure = calibre_sortie_filtre if calibre_sortie_filtre != None else 10

        signal_entree_filtre = Signal(type_signal = "sysam", Te = Te, calibre = calibre_entree_filtre_mesure, liste_tmin_tmax = liste_tmin_tmax, nom_voie = voie_entree_filtre, nom = "$e$")
        signal_sortie_filtre = Signal(type_signal = "sysam", Te = Te, calibre = calibre_sortie_filtre_mesure, liste_tmin_tmax = liste_tmin_tmax, nom_voie = voie_sortie_filtre, nom = "$s$")
        
        trigger_base = signal_sortie_filtre._Signal6Sysam__lire_trigger_base() if voie_trigger == "voie_sortie_filtre" else signal_entree_filtre._Signal6Sysam__lire_trigger_base()
        trigger_base.seuil = seuil
        trigger_base.montant = montant
        trigger_base.pretrigger = pretrigger

        demarrer_sysam(signal_sortie_sysam, signal_entree_filtre, signal_sortie_filtre, affichage)
        
        calibre_entree_filtre_optimal = signal_entree_filtre._Signal6Sysam__calculer_calibre_optimal()
        calibre_sortie_filtre_optimal = signal_sortie_filtre._Signal6Sysam__calculer_calibre_optimal()

        test_recommencer = False

        if calibre_entree_filtre == None and calibre_entree_filtre_mesure != calibre_entree_filtre_optimal:
            test_recommencer = True
            signal_entree_filtre.configurer_voie(nom = voie_entree_filtre, calibre = calibre_entree_filtre_optimal)
        
        if calibre_sortie_filtre == None and calibre_sortie_filtre_mesure != calibre_sortie_filtre_optimal:
            test_recommencer = True
            signal_sortie_filtre.configurer_voie(nom = voie_sortie_filtre, calibre = calibre_sortie_filtre_optimal)
        
        if test_recommencer == True:
            demarrer_sysam(signal_sortie_sysam, signal_entree_filtre, signal_sortie_filtre, affichage)
    
        self.signal_entree_filtre = signal_entree_filtre
        self.signal_sortie_filtre = signal_sortie_filtre
                
if __name__ == "__main__":
    F = 5e4
    s = Signal(nom_voie = "SA1", F = F, liste_tmin_tmax = [0, 1/F], Te = 1e-6)
    a = AcquisitionES(signal_sortie_sysam = s, duree_acquisition = 7/F, duree_attente_avant_aquisition = 1, seuil = 0., montant = True, pretrigger = 0)
    tracer(s, a.signal_entree_filtre, a.signal_sortie_filtre, superposition = False)