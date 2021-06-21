import numpy as np
import matplotlib.pyplot as plt

from IPython import display

import os, sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))

from filtres.filtre_base import FiltreBase
from signaux.signal_gbf import SignalGBF
from signaux.signal_sysam import SignalSysam
from sysam.sysam_sp5 import demarrer_sysam

class FigureDynamique():
    def __init__(self, filtre):
        plt.ion()
        self.filtre = filtre
        self.figure, self.liste_axes = plt.subplots(2, 2, constrained_layout = True)
        self.axe_G_dB = self.liste_axes[0][0]
        self.lignes_G_dB, = self.axe_G_dB.semilogx([], [], "*")
        self.axe_G_dB.set_autoscale_on(True)
        self.axe_G_dB.set_xlim(*self.filtre.liste_fmin_fmax)
        self.axe_G_dB.set_xlabel("$f$ (Hz)")
        self.axe_G_dB.set_ylabel("$G_{dB}$")
        
        self.axe_phi = self.liste_axes[1][0]
        self.lignes_phi, = self.axe_phi.semilogx([], [], "*")
        self.axe_phi.set_autoscale_on(True)
        self.axe_phi.set_xlim(*self.filtre.liste_fmin_fmax)
        self.axe_phi.set_xlabel("$f$ (Hz)")
        self.axe_phi.set_ylabel("$\\varphi$ (rad)")
        
        
        self.axe_entree = self.liste_axes[0][1]
        self.lignes_entree, = self.axe_entree.plot([], [])
        self.axe_entree.set_autoscale_on(True)
        self.axe_entree.set_xlabel("$t$ (s)")
        self.axe_entree.set_ylabel("$e$ (V)")
        
        self.axe_sortie = self.liste_axes[1][1]
        self.lignes_sortie, = self.axe_sortie.plot([], [])
        self.axe_sortie.set_autoscale_on(True)
        self.axe_sortie.set_xlabel("$t$ (s)")
        self.axe_sortie.set_ylabel("$s$ (V)")
        display.display(self.figure)

    def mettre_a_jour(self, i):
        self.lignes_G_dB.set_xdata(self.filtre.vecteur_f[:i])
        self.lignes_G_dB.set_ydata(self.filtre.vecteur_G_dB[:i])
        self.axe_G_dB.relim()
        self.axe_G_dB.autoscale_view()
        
        self.lignes_phi.set_xdata(self.filtre.vecteur_f[:i])
        self.lignes_phi.set_ydata(self.filtre.vecteur_phi[:i])
        self.axe_phi.relim()
        self.axe_phi.autoscale_view()
        
        self.lignes_entree.set_xdata(self.filtre.vecteur_t)
        self.lignes_entree.set_ydata(self.filtre.entree_filtre.vecteur_signal)
        self.axe_entree.relim()
        self.axe_entree.autoscale_view()
        
        self.lignes_sortie.set_xdata(self.filtre.vecteur_t)
        self.lignes_sortie.set_ydata(self.filtre.sortie_filtre.vecteur_signal)
        self.axe_sortie.relim()
        self.axe_sortie.autoscale_view()
        
        self.figure.canvas.draw()
        self.figure.canvas.flush_events()
    
        nom_fichier = "graphs-bode/{0}_f_{1}_Hz.pdf".format(self.filtre.nom, str(int(self.filtre.f_mes)).zfill(6))
        self.figure.savefig(nom_fichier)
        display.display(self.figure)

    def __del__(self):
        try:
            del(self.filtre.entree_filtre)
        except:
            pass
        try:
            del(self.filtre.sortie_filtre)
        except:
            pass
        try:
            del(self.filtre.vecteur_t)
        except:
            pass
        plt.ioff()

if __name__ == "__main__":
    filtre = FiltreBase("zorro")
    filtre.vecteur_f = np.logspace(1,3,10)
    filtre.vecteur_G_dB = 2*filtre.vecteur_f
    filtre.vecteur_phi = -2*filtre.vecteur_f
    fd = FigureDynamique(filtre)
    input()
    filtre.vecteur_G_dB = -2*filtre.vecteur_f
    filtre.vecteur_phi = 2*filtre.vecteur_f
    fd.mettre_a_jour()
    input()