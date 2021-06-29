import numpy as np
import matplotlib.pyplot as plt

import os, sys


sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))

import base.utiles_base as utb
from base.axe_x_base import AxeXBase
from base.angle_base import AngleBase
from filtres.filtre_base import FiltreBase
from filtres.filtre_transfert import FiltreTransfert
from filtres.affichage_mesure import FigureDynamique
from signaux.signalll import Signal
from sysam.sysam_sp5 import demarrer_sysam
from base.mesure_bode_base import MesureBodeBase
from sysam.acquerir_es import AcquisitionES
from plot.plot_base import tracer

nombre_de_points_par_sortie_sysam_max = 131000
nombre_de_points_sysam_max = 262000
Te_min = 2e-7
Delta_Te = 2e-7


class FiltreSysam(FiltreTransfert):
    def __init__(self, voie_sortie_sysam = "SA1", voie_entree_filtre = "EA0", voie_sortie_filtre = "EA1", 
    Vpp_sortie_sysam = 10., calibre_entree_filtre = None, calibre_sortie_filtre = None, 
    temps_de_reponse = 1., nombre_de_points_par_periode_min = 20, nombre_de_periodes_de_mesure = 10, nombre_cs_frequence = 2, nom = ""):

        FiltreBase.__init__(self, fonction_H = None, omega = False, nombre_cs_frequence = nombre_cs_frequence, nom = nom)
        
        self.__voie_sortie_sysam = voie_sortie_sysam
        self.__voie_entree_filtre = voie_entree_filtre
        self.__voie_sortie_filtre = voie_sortie_filtre

        self.__Vpp_sortie_sysam = Vpp_sortie_sysam
        self.__calibre_entree_filtre = calibre_entree_filtre
        self.__calibre_sortie_filtre = calibre_sortie_filtre
        
        self.__temps_de_reponse = temps_de_reponse
        self.__nombre_de_points_par_periode_min = nombre_de_points_par_periode_min
        self.__nombre_de_periodes_de_mesure = nombre_de_periodes_de_mesure

    def acquerir_H(self, f, affichage = False):
        def choisir_sortie_sysam(self, f):
            def choisir_nombre_de_periodes_sysam(self, f, Te, nombre_de_points_par_periode):
                nombre_de_periodes_sysam_max = int(nombre_de_points_par_sortie_sysam_max / nombre_de_points_par_periode)

                bdtTe = AxeXBase([0, 1], Te)
                NTaxe = bdtTe.NXa
                
                for nombre_de_periodes_sysam in range(1, nombre_de_periodes_sysam_max):
                    nT = nombre_de_periodes_sysam/f
                    bdtnT = AxeXBase([0, 1], nT)
                    NTanT = bdtnT.NXa
                    r = np.mod(NTanT, NTaxe)
                    nT_calc = bdtnT.lire_Xe()
                    T_calc = nT_calc / nombre_de_periodes_sysam
                    f_calc = 1/T_calc
                    if r == 0:
                        if np.abs(f_calc - f) < 1e-2:
                            return nombre_de_periodes_sysam, f_calc
                return None, None

            def tester_nombre_d_echantillons_memoire(self, f, Te, nombre_de_periodes_sysam):
                nb_d_echantillons_sortie_sysam = AxeXBase([0, nombre_de_periodes_sysam/f], Te).lire_N()
                nb_d_echantillons_entrees_sysam = AxeXBase([0, self.__nombre_de_periodes_de_mesure/f], Te).lire_N()

                if nb_d_echantillons_sortie_sysam > nombre_de_points_par_sortie_sysam_max:
                    return False
                
                if 2*nb_d_echantillons_entrees_sysam + nb_d_echantillons_sortie_sysam > nombre_de_points_sysam_max:
                    return False
                return True
            T = 1/f

            Te = 2e-7
            
            Te_OK = None
            nombre_de_periodes_sysam_OK = None
            Te_max = T / self.__nombre_de_points_par_periode_min
            k_max = int( (Te_max - Te_min) / Delta_Te )
            for k in range(k_max):
                Te = Te_min + k * Delta_Te
                nombre_de_points_par_periode = AxeXBase([0, T], Te).lire_N()
                if nombre_de_points_par_periode < self.__nombre_de_points_par_periode_min:
                    break
            
                nombre_de_periodes_sysam, f_calc = choisir_nombre_de_periodes_sysam(self, f, Te, nombre_de_points_par_periode)
                
                if nombre_de_periodes_sysam != None and tester_nombre_d_echantillons_memoire(self, f, Te, nombre_de_periodes_sysam):
                    Te_OK = Te
                    nombre_de_periodes_sysam_OK = nombre_de_periodes_sysam
                    signal_sortie_sysam =  Signal(nom_voie = self.__voie_sortie_sysam, Vpp = self.__Vpp_sortie_sysam, repetition = True, F = f_calc, liste_tmin_tmax= [0, nombre_de_periodes_sysam_OK/f_calc], Te = Te_OK, nom = "sortie_sysam")
                    # print("f = ", f, "Te = ", Te, "nb_periodes = ", nombre_de_periodes_sysam)
                    return signal_sortie_sysam
        
            print("Impossible de générer la fréquence {0} correctement".format(f))
            return None

        signal_sortie_sysam = choisir_sortie_sysam(self, f)
        if signal_sortie_sysam != None:
            self.es = AcquisitionES(signal_sortie_sysam = signal_sortie_sysam, voie_entree_filtre = self.__voie_entree_filtre, calibre_entree_filtre = self.__calibre_entree_filtre, voie_sortie_filtre = self.__voie_sortie_filtre, calibre_sortie_filtre = self.__calibre_sortie_filtre, duree_acquisition = self.__nombre_de_periodes_de_mesure/f, duree_attente_avant_acquisition = self.__temps_de_reponse, affichage = affichage) 
            G = self.es.signal_sortie_filtre.lire_Vpp() / self.es.signal_entree_filtre.lire_Vpp()
            phi = self.es.signal_sortie_filtre.lire_dephasage_par_rapport_a(self.es.signal_entree_filtre)
            self.es.f = f
            return G*np.exp(1j*phi)

    def acquerir_bode(self, liste_xmin_xmax = [1e2, 1e4], nombre_de_points = 5, omega = None, logX = True, affichage = False):
        omega = self._FiltreBase__omega if omega == None else omega
        vecteur_f = self._FiltreBase__calculer_vecteur_f(liste_xmin_xmax, nombre_de_points, omega, logX)
        liste_f = list(vecteur_f)
        liste_f.extend([m.f for m in self._FiltreBase__liste_mesures])
        self.liste_fmin_fmax = min(liste_f), max(liste_f)

        fd = FigureDynamique(self)

        if self._FiltreBase__tester_nouvelles_frequences(vecteur_f):
            for f in vecteur_f:
                x = self._FiltreBase__calculer_x(f, omega)
                if f not in [mesure.f for mesure in self._FiltreBase__liste_mesures]:
                    H = self.acquerir_H(x, affichage)
                    if H != None:
                        self._FiltreBase__liste_mesures.append( MesureBodeBase(f, H) )
                        fd.mettre_a_jour()
        self._FiltreBase__liste_mesures.sort(key = lambda m: m.f)
        fd.finir()


    # def acquerir_bode(self, liste_x, omega = None):
    #     omega = self._FiltreBase__omega if omega == None else omega
    #     liste_f = list(np.array(liste_x) / (2*np.pi)) if omega else list(liste_x)
        
    #     liste_f.extend([m.f for m in self._FiltreBase__liste_mesures])
    #     liste_f.sort()
    #     self.liste_fmin_fmax = [liste_f[0], liste_f[-1]]
        
    #     fd = FigureDynamique(self)

    #     for x in liste_x:
    #         f = int( x / (2*np.pi) ) if omega else int(x)
    #         f = self.__arrondir_f(f)
    #         x = 2*np.pi*f if omega else f
    #         if f not in [mesure.f for mesure in self._FiltreBase__liste_mesures]:
    #             H = self.__calculer_H(x)
    #             if H != None:
    #                 self._FiltreBase__liste_mesures.append( MesureBodeBase(f, H) )
    #                 fd.mettre_a_jour()
    #     plt.ioff()                
    #     self._FiltreBase__liste_mesures.sort(key = lambda m: m.f)

    def acquerir_reponse_indicielle(self):
        Te = max(2e-7, self.__temps_de_reponse/1e5)
        T = 1
        Vpp = min(self.__Vpp_sortie_sysam, 10)
        signal_sortie_sysam = Signal(type_signal = "carre", F = 1/T, Vpp = Vpp, offset = 0.5*Vpp, tr = 0.4*T, liste_tmin_tmax= [0, 0.7*T], Te = T/10, nom_voie = self.__voie_sortie_sysam, repetition = False)
        es = AcquisitionES(signal_sortie_sysam = signal_sortie_sysam, duree_attente_avant_acquisition = 0, duree_acquisition = self.__temps_de_reponse, seuil = 0.5*Vpp, pretrigger = 5, voie_entree_filtre = self.__voie_entree_filtre, calibre_entree_filtre = self.__calibre_entree_filtre, voie_sortie_filtre = self.__voie_sortie_filtre, calibre_sortie_filtre = self.__calibre_sortie_filtre, affichage = True, Te = Te)
        return es.signal_entree_filtre, es.signal_sortie_filtre

    def configurer_sortie_sysam(self, nom_voie = "SA1", Vpp = 10.):
        self.__voie_sortie_sysam  = nom_voie
        self.__Vpp_sortie_sysam = Vpp
    
    def configurer_entree_filtre(self, nom_voie = "EA0", calibre = None):
        self.__voie_entree_filtre = nom_voie
        self.__calibre_entree_filtre = calibre

    def configurer_sortie_filtre(self, nom_voie = "EA1", calibre = None):
        self.__voie_sortie_filtre = nom_voie
        self.__calibre_sortie_filtre = calibre
    
    def configurer_nombre_de_periodes_de_mesure(self, nombre_de_periodes_de_mesure):
        self.__nombre_de_periodes_de_mesure = nombre_de_periodes_de_mesure

if __name__ == "__main__":
    filtre = FiltreSysam(temps_de_reponse = 1e-3, nom = "citron", voie_sortie_sysam = "SA1", Vpp_sortie_sysam = 19, voie_entree_filtre = "EA0", calibre_sortie_filtre = 10)
    print(filtre._FiltreBase__fonction_H)
    filtre.calculer_bode(liste_xmin_xmax = [1e1, 1e5], nombre_de_points=10)
    filtre.tracer()
    