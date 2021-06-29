from IPython.core.display import clear_output
import numpy as np
import matplotlib.pyplot as plt

from IPython import display

import os, sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))

from filtres.filtre_base import FiltreBase
from signaux.signalll import Signal

class FigureDynamique():
    def display(self):
        try:
            __IPYTHON__
            display.display(self.figure)
        except:
            pass

    def __init__(self, filtre):
        plt.ion()
        self.filtre = filtre
        self.figure, self.liste_axes = plt.subplots(2, 2, constrained_layout = True)
        
        self.axe_G_dB = self.liste_axes[0][0]
        vecteur_f = [m.f for m in self.filtre._FiltreBase__liste_mesures]
        vecteur_GdB = [m.lire_G() for m in self.filtre._FiltreBase__liste_mesures]
        # vecteur_phi = [m.lire_phi() for m in self.filtre._FiltreBase__liste_mesures]
        N = len(self.filtre._FiltreBase__liste_mesures)
        if N > 0:
            vecteur_phi = [self.filtre._FiltreBase__liste_mesures[0].lire_phi(phi0 = 0., deg = True)]
        else:
            vecteur_phi = []
        for i in range(1, N):
            vecteur_phi.append( self.filtre._FiltreBase__liste_mesures[i].lire_phi(phi0 = vecteur_phi[i-1], deg = True) )

        self.lignes_G_dB, = self.axe_G_dB.semilogx(vecteur_f, vecteur_GdB, "*")
        self.axe_G_dB.set_autoscale_on(True)
        self.axe_G_dB.set_xlim(*self.filtre.liste_fmin_fmax)
        self.axe_G_dB.set_xlabel("$f$ (Hz)")
        self.axe_G_dB.set_ylabel("$G_{dB}$")
        
        self.axe_phi = self.liste_axes[1][0]
        self.lignes_phi, = self.axe_phi.semilogx(vecteur_f, vecteur_phi, "*")
        self.axe_phi.set_autoscale_on(True)
        self.axe_phi.set_xlim(*self.filtre.liste_fmin_fmax)
        self.axe_phi.set_xlabel("$f$ (Hz)")
        self.axe_phi.set_ylabel("$\\varphi$ (°)")
        
        
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
        # display.display(self.figure)
        # self.figure.show()
        self.display()

    def mettre_a_jour(self):
        vecteur_f = [m.f for m in self.filtre._FiltreBase__liste_mesures]
        vecteur_GdB = [m.lire_G() for m in self.filtre._FiltreBase__liste_mesures]
        # vecteur_phi = [m.lire_phi() for m in self.filtre._FiltreBase__liste_mesures]
        N = len(self.filtre._FiltreBase__liste_mesures)
        if N > 0:
            vecteur_phi = [self.filtre._FiltreBase__liste_mesures[0].lire_phi(phi0 = 0., deg = True)]
        else:
            vecteur_phi = []
        for i in range(1, N):
            vecteur_phi.append( self.filtre._FiltreBase__liste_mesures[i].lire_phi(phi0 = vecteur_phi[i-1], deg = True) )
        
        self.lignes_G_dB.set_xdata(vecteur_f)
        self.lignes_G_dB.set_ydata(vecteur_GdB)
        self.axe_G_dB.relim()
        self.axe_G_dB.autoscale_view()
        
        self.lignes_phi.set_xdata(vecteur_f)
        self.lignes_phi.set_ydata(vecteur_phi)
        self.axe_phi.relim()
        self.axe_phi.autoscale_view()
        
        self.lignes_entree.set_xdata(self.filtre.es.signal_entree_filtre.lire_vecteur_x())
        self.lignes_entree.set_ydata(self.filtre.es.signal_entree_filtre.lire_vecteur_y())
        self.axe_entree.relim()
        self.axe_entree.autoscale_view()
        
        self.lignes_sortie.set_xdata(self.filtre.es.signal_sortie_filtre.lire_vecteur_x())
        self.lignes_sortie.set_ydata(self.filtre.es.signal_sortie_filtre.lire_vecteur_y())
        self.axe_sortie.relim()
        self.axe_sortie.autoscale_view()
        
        self.figure.canvas.draw()
        self.figure.canvas.flush_events()
    
        # nom_fichier = "graphs-bode/{0}_f_{1}_Hz.pdf".format(self.filtre.lire_nom(), str(int(self.filtre.es.f)).zfill(6))
        # self.figure.savefig(nom_fichier)
        # display.display(self.figure, silence=True)
        self.display()


    def finir(self):
        plt.ioff()
        plt.show()
        del(self.filtre.es)
        del(self.filtre.liste_fmin_fmax)

if __name__ == "__main__":
    filtre = FiltreBase("zorro")
    filtre.vecteur_f = np.logspace(1,4,10)
    filtre.vecteur_G_dB = 2*filtre.vecteur_f
    filtre.vecteur_phi = -2*filtre.vecteur_f
    fd = FigureDynamique(filtre)
    input()
    filtre.vecteur_G_dB = -2*filtre.vecteur_f
    filtre.vecteur_phi = 2*filtre.vecteur_f
    fd.mettre_a_jour()
    input()