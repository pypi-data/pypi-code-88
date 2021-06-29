import numpy as np
import matplotlib.pyplot as plt

import os, sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))
from filtres.filtre_transfert import FiltreTransfert
from filtres.filtre_sysam import FiltreSysam
from filtres.filtre_base import FiltreBase
import base.utiles_base as utb
from plot.plot_base import tracer
from signaux.signalll import Signal

liste_types_filtres = ["sysam", "transfert"]

class Filtre(FiltreSysam):
    def __init__(self, *args, **kwargs):
        args = list(args)
        type_filtre = utb.analyser_args_kwargs(args, kwargs, "type_filtre", lambda x: isinstance(x, str), "transfert")
        liste_coef_num = utb.analyser_args_kwargs(args, kwargs, "liste_coef_num", lambda x: isinstance(x, list), [0])
        liste_coef_den = utb.analyser_args_kwargs(args, kwargs, "liste_coef_den", lambda x: isinstance(x, list), [1])

        liste_xmin_xmax = utb.analyser_args_kwargs(args, kwargs, "liste_xmin_xmax", lambda x: isinstance(x, list) and len(x) == 2, [1e1, 1e4])
        nombre_de_points = utb.analyser_args_kwargs(args, kwargs, "nombre_de_points", lambda x: isinstance(x, int), 5)
        logX = utb.analyser_args_kwargs(args, kwargs, "logX", lambda x: isinstance(x, bool), True)
        omega = utb.analyser_args_kwargs(args, kwargs, "omega", lambda x: isinstance(x, bool), False)
        nom = utb.analyser_args_kwargs(args, kwargs, "nom", lambda x: isinstance(x, str), "")

        voie_sortie_sysam = utb.analyser_args_kwargs(args, kwargs, "voie_sortie_sysam", lambda x: isinstance(x, str), "SA1")
        voie_entree_filtre = utb.analyser_args_kwargs(args, kwargs, "voie_entree_filtre", lambda x: isinstance(x, str), "EA0")
        calibre_entree_filtre = utb.analyser_args_kwargs(args, kwargs, "calibre_entree_filtre", lambda x: x == None or isinstance(x, (int, float)), None)
        Vpp_sortie_sysam = utb.analyser_args_kwargs(args, kwargs, "Vpp_sortie_sysam", lambda x: isinstance(x, (int, float)), 10.)
        voie_sortie_filtre = utb.analyser_args_kwargs(args, kwargs, "voie_sortie_filtre", lambda x: isinstance(x, str), "EA1")
        calibre_sortie_filtre = utb.analyser_args_kwargs(args, kwargs, "calibre_sortie_filtre", lambda x: x == None or isinstance(x, (int, float)), None)
        temps_de_reponse = utb.analyser_args_kwargs(args, kwargs, "temps_de_reponse", lambda x: isinstance(x, float), 1e-2)
        
        nombre_de_points_par_periode_min = utb.analyser_args_kwargs(args, kwargs, "nombre_de_points_par_periode_min", lambda x: isinstance(x, int), 20)
        nombre_de_periodes_de_mesure = utb.analyser_args_kwargs(args, kwargs, "nombre_de_periodes_de_mesure", lambda x: isinstance(x, int), 5)
        nombre_cs_frequence = utb.analyser_args_kwargs(args, kwargs, "nombre_cs_frequence", lambda x: isinstance(x, int), 2)


        assert type_filtre in liste_types_filtres, "Ce type de filtres n'existe pas"

        if type_filtre == "transfert":
            FiltreTransfert.__init__(self, liste_coef_num = liste_coef_num, liste_coef_den = liste_coef_den, 
            omega = omega, nombre_cs_frequence = nombre_cs_frequence, nom = nom)
            if nombre_de_points > 0:
                self.calculer_bode(liste_xmin_xmax = liste_xmin_xmax, nombre_de_points = nombre_de_points, omega = omega, logX = logX)

        elif type_filtre == "sysam":
            FiltreSysam.__init__(self, voie_sortie_sysam = voie_sortie_sysam, voie_entree_filtre = voie_entree_filtre, voie_sortie_filtre = voie_sortie_filtre, 
            Vpp_sortie_sysam = Vpp_sortie_sysam, calibre_entree_filtre = calibre_entree_filtre, calibre_sortie_filtre = calibre_sortie_filtre, 
            temps_de_reponse = temps_de_reponse, nombre_de_points_par_periode_min = nombre_de_points_par_periode_min, 
            nombre_de_periodes_de_mesure = nombre_de_periodes_de_mesure, nombre_cs_frequence = nombre_cs_frequence)
            if nombre_de_points > 0:
                self.acquerir_bode(liste_xmin_xmax = liste_xmin_xmax, nombre_de_points = nombre_de_points, omega = omega, logX = logX)


        # elif type_signal == "carre":
        #     SignalCarre.__init__(self, F, Vpp, offset, alpha, tr, liste_tmin_tmax, Te, nom)
        # elif type_signal == "triangle":
        #     SignalTriangle.__init__(self, F, Vpp, offset, alpha, tr, liste_tmin_tmax, Te, nom)
        # elif type_signal == "fourier":
        #     SignalFourier.__init__(self, F, liste_an, liste_bn, liste_tmin_tmax, Te, nom)
        # elif type_signal == "wav":
        #     SignalWav.__init__(self, nom_fichier_wav, Pbits, liste_umin_umax, nom)
        # else:
            # SignalComplet.__init__(self, axe_x_base, [], nom)



if __name__ == "__main__":
    fil = Filtre("transfert", liste_coef_num = [1], liste_coef_den = [1, 1/5e2], nombre_de_points = 100)#, nombre_de_points = 0)
    
    e = Signal("carre")
    s = fil.calculer_sortie(e)
    tracer(e, s)
    # fil.tracer()
    
    # fil = Filtre("sysam")
    # fil.tracer()
    # e, s = fil.acquerir_reponse_indicielle()
    # tracer(e, s)

