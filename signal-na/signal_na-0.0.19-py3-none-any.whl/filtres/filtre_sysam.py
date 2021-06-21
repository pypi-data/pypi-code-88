import numpy as np
import matplotlib.pyplot as plt

import os, sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))

from filtres.filtre_base import FiltreBase
from filtres.affichage_mesure import FigureDynamique
from signaux.signal_gbf import SignalGBF
from signaux.signal_sysam import SignalSysam
from sysam.sysam_sp5 import demarrer_sysam

class FiltreSysam(FiltreBase):
    def __init__(self, temps_de_reponse = 1e-1):
        FiltreBase.__init__(self, temps_de_reponse)
        self.temps_de_reponse = temps_de_reponse
        self.voie_sortie_sysam = "SA1"
        self.Vpp_sortie_sysam = 10.
        self.voie_entree_filtre = "EA0"
        self.calibre_entree_filtre = 10.
        self.calibre_auto_entree_filtre = True
        self.voie_sortie_filtre = "EA1"
        self.calibre_sortie_filtre = 10.
        self.calibre_auto_sortie_filtre = True
        self.n_periodes = 10
        
    def faire_une_mesure_frequentielle(self, f):
        T = 1/f
        Te = max(T/100, 2e-7)
        
        calibre_entree_filtre_init  = self.calibre_entree_filtre
        calibre_sortie_filtre_init  = self.calibre_sortie_filtre

        sortie_sysam = SignalGBF(type_signal = "cosinus", F = f, Vpp = self.Vpp_sortie_sysam, liste_tmin_tmax = [0, T], Te = Te)
        sortie_sysam.configurer_voie(self.voie_sortie_sysam, calibre = 10., repetition = True)
        liste_tmin_tmax = [self.temps_de_reponse, self.temps_de_reponse + self.n_periodes*T]
        entree_filtre = SignalSysam(nom_voie = self.voie_entree_filtre, calibre = self.calibre_entree_filtre, liste_tmin_tmax = liste_tmin_tmax, Te = Te, nom = "$e$")
        sortie_filtre = SignalSysam(nom_voie = self.voie_sortie_filtre, calibre = self.calibre_sortie_filtre, liste_tmin_tmax = liste_tmin_tmax, Te = Te, nom = "$s$")
        entree_filtre.configurer_trigger(0)
        demarrer_sysam(sortie_sysam, entree_filtre, sortie_filtre, False)

        calibre_entree = entree_filtre.calculer_calibre_optimal()
        calibre_sortie = sortie_filtre.calculer_calibre_optimal()

        test_recommencer = False

        if self.calibre_auto_entree_filtre and entree_filtre.voie.calibre != calibre_entree:
            test_recommencer = True
            entree_filtre.configurer_voie(self.voie_entree_filtre, calibre_entree)
        if self.calibre_auto_sortie_filtre and sortie_filtre.voie.calibre != calibre_sortie:
            test_recommencer = True
            sortie_filtre.configurer_voie(self.voie_sortie_filtre, calibre_sortie)
        if test_recommencer == True:
            demarrer_sysam(sortie_sysam, entree_filtre, sortie_filtre, False)
            self.calibre_entree_filtre = calibre_entree_filtre_init
            self.calibre_auto_sortie_filtre = calibre_sortie_filtre_init

        self.entree_filtre = entree_filtre
        self.sortie_filtre = sortie_filtre
        self.vecteur_t = self.entree_filtre.calculer_vecteur_t()
        self.f_mes = 1/entree_filtre.mesurer_T()
        
        
        G = sortie_filtre.mesurer_Vpp() / entree_filtre.mesurer_Vpp()
        phi = sortie_filtre.mesurer_dephasage_par_rapport_a(entree_filtre)
        return self.f_mes, G, phi

    def calculer_vecteur_H_cplx(self, liste_fmin_fmax, n_points, affichage = True):
        self.acquerir_bode(liste_fmin_fmax, n_points, affichage)
        
    def acquerir_bode(self, liste_fmin_fmax, n_points, affichage = True):
        self.configurer_liste_fmin_fmax(liste_fmin_fmax)
        self.configurer_n_points(n_points)
        try:
            N = len(self.vecteur_H_cplx)
        except:
            if not os.path.isdir("graphs-bode"):
                os.mkdir("graphs-bode")
            self.calculer_vecteur_f(liste_fmin_fmax, n_points)
            
            self.vecteur_G = np.zeros(self.n_points, dtype = 'float')
            self.vecteur_G_dB = np.zeros(self.n_points, dtype = 'float')
            self.vecteur_phi = np.zeros(self.n_points, dtype = 'float')
            self.vecteur_H_cplx = np.zeros(self.n_points, dtype = 'complex128')
            if affichage:
                fd = FigureDynamique(self)

            for i in range(self.n_points):
                f, G, phi = self.faire_une_mesure_frequentielle(self.vecteur_f[i])
                self.vecteur_f[i] = f
                self.vecteur_G[i] = G
                self.vecteur_G_dB[i] = 20*np.log10(G)
                self.vecteur_phi[i] = phi
                self.vecteur_H_cplx[i] = G*np.exp(1j*phi)
                if affichage:
                    fd.mettre_a_jour(i+1)
            plt.ioff()                

    def acquerir_reponse_indicielle(self):
        try:
            N = len(self.reponse_indicielle)
        except:
            calibre_entree_filtre_init  = self.calibre_entree_filtre
            calibre_sortie_filtre_init  = self.calibre_sortie_filtre
            Te = max(2e-7, self.temps_de_reponse/1e5)
            T = 1
            Vpp = min(self.Vpp_sortie_sysam, 10)
            sortie_sysam = SignalGBF(type_signal = "carre", F = 1/T, Vpp = Vpp, offset = 0.5*Vpp, tr = 0.4*T, liste_tmin_tmax = [0, 0.7*T], Te = T/10)
            sortie_sysam.configurer_voie(self.voie_sortie_sysam, calibre = 10., repetition = False)
            
            liste_tmin_tmax = [0, self.temps_de_reponse]
            
            entree_filtre = SignalSysam(nom_voie = self.voie_entree_filtre, calibre = self.calibre_entree_filtre, liste_tmin_tmax = liste_tmin_tmax, Te = Te, nom = "$e$")
            sortie_filtre = SignalSysam(nom_voie = self.voie_sortie_filtre, calibre = self.calibre_sortie_filtre, liste_tmin_tmax = liste_tmin_tmax, Te = Te, nom = "$s$")
            
            seuil = 0.5*Vpp
            entree_filtre.configurer_trigger(seuil, pretrigger = 10, pretrigger_souple=True)
            demarrer_sysam(sortie_sysam, entree_filtre, sortie_filtre, False)

            calibre_entree = entree_filtre.calculer_calibre_optimal()
            calibre_sortie = sortie_filtre.calculer_calibre_optimal()

            test_recommencer = False

            if self.calibre_auto_entree_filtre and entree_filtre.voie.calibre != calibre_entree:
                test_recommencer = True
                entree_filtre.configurer_voie(self.voie_entree_filtre, calibre_entree)
            if self.calibre_auto_sortie_filtre and sortie_filtre.voie.calibre != calibre_sortie:
                test_recommencer = True
                sortie_filtre.configurer_voie(self.voie_sortie_filtre, calibre_sortie)
            if test_recommencer == True:
                demarrer_sysam(sortie_sysam, entree_filtre, sortie_filtre, False)
                self.calibre_entree_filtre = calibre_entree_filtre_init
                self.calibre_auto_sortie_filtre = calibre_sortie_filtre_init

            self.entree_filtre = entree_filtre
            self.sortie_filtre = sortie_filtre
            
            return entree_filtre, sortie_filtre

    def configurer_sortie_sysam(self, nom_voie = "SA1", Vpp = 2.):
        self.voie_sortie_sysam  = nom_voie
        self.Vpp_sortie_sysam = Vpp

    
    def configurer_entree_filtre(self, nom_voie = "EA0", calibre = 10., calibre_auto = True):
        self.voie_entree_filtre = nom_voie
        self.calibre_entree_filtre = calibre
        self.calibre_auto_entree_filtre = calibre_auto

    def configurer_sortie_filtre(self, nom_voie = "EA1", calibre = 10., calibre_auto = True):
        self.voie_sortie_filtre = nom_voie
        self.calibre_sortie_filtre = calibre
        self.calibre_auto_sortie_filtre = calibre_auto
    
    def configurer_n_periodes(self, n_periodes):
        self.n_periodes = n_periodes

if __name__ == "__main__":
    filtre = FiltreSysam(temps_de_reponse = 1e-3)
    liste_fmin_fmax = [100, 100000]
    n_points = 3

    filtre.configurer_sortie_sysam("SA2", 19)
    filtre.configurer_sortie_filtre("EA3")
    filtre.configurer_entree_filtre("EA2")

    filtre.acquerir_bode(liste_fmin_fmax, n_points)
    
    plt.figure()
    filtre.tracer_G_dB(liste_fmin_fmax, n_points)
    # entree, sortie = filtre.acquerir_reponse_indicielle()
    
    # entree.tracer_signaux(sortie)
    
    
    print("fin")
    