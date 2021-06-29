import matplotlib.pyplot as plt
import numpy as np

import os, sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))

import base.utiles_base as utb
import base.angle_base as anb

class AxePlotConfig():
    def __init__(self, plot_base, config_plot):
        axe_x_base = plot_base._PlotBase__lire_axe_x_base()
        ux, nomx = axe_x_base.unite, axe_x_base.nom

        axe_y_base = plot_base._PlotBase__lire_axe_y_base()
        uy, nomy = axe_y_base.unite, axe_y_base.nom

        if ux == "s":
            self.nomx = "$t$"
            self.ux = "s"
            self.nomy = "$u$"
            self.uy = "V"
            self.fonction_plot = plt.plot
            self.vecteur_x = plot_base.lire_vecteur_x()
            self.vecteur_y = plot_base.lire_vecteur_y()
            
        elif ux == "Hz":
            if uy == "V.Hz":
                omega = config_plot.omega if config_plot.omega != None else False

                self.nomx = "$\\omega$" if omega else "$f$"
                self.ux = "rad/s" if omega else "Hz"
                dB = config_plot.dB if config_plot.dB != None else False
                self.nomy = "$U$"
                self.uy = "dB" if dB else "SI"

                logX = config_plot.logX if config_plot.logX != None else False
                self.fonction_plot = plt.semilogx if logX else plt.plot
                
                N = plot_base._PlotBase__lire_axe_x_base().lire_N()
                self.vecteur_x = 2*np.pi*plot_base.lire_vecteur_x()[:N//2] if omega else plot_base.lire_vecteur_x()[:N//2]
                self.vecteur_y = utb.calculer_vecteur_dB(plot_base.lire_vecteur_y()[:N//2], config_plot.dBmin) if dB else np.abs(plot_base.lire_vecteur_y()[:N//2])

            elif uy == "":
                omega = config_plot.omega if config_plot.omega != None else plot_base._FiltreBase__omega
                self.nomx = "$\\omega$" if omega else "$f$"
                self.ux = "rad/s" if omega else "Hz"
                dB = config_plot.dB if config_plot.dB != None else True

                logX = config_plot.logX if config_plot.logX != None else True
                self.fonction_plot = plt.semilogx if logX else plt.plot
                
                self.vecteur_x = 2*np.pi*plot_base.lire_vecteur_x() if omega else plot_base.lire_vecteur_x()
                if config_plot.G:
                    self.vecteur_y = utb.calculer_vecteur_dB(plot_base.lire_vecteur_y(), config_plot.dBmin) if dB else np.abs(plot_base.lire_vecteur_y())
                    self.nomy = "$G$"
                    self.uy = "dB" if dB else "_"
                else:
                    self.vecteur_y = anb.calculer_vecteur_angles(plot_base.lire_vecteur_y(), config_plot.deg, config_plot.phi0)
                    self.nomy = "$\\varphi$"
                    self.uy = "°" if config_plot.deg else "rad"

            pass
        
