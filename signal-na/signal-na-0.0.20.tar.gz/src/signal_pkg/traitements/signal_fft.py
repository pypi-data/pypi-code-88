
import numpy as np
import matplotlib.pyplot as plt

import os, sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))
from signaux.signal_base import SignalBase
from base.temps_base import BaseTemps
from base.frequence_base import BaseFrequence


__all__ = ["SignalFFT"]
class SignalFFT(SignalBase):
    def calculer_vecteur_spectre(self, liste_imin_imax = [None, None]):
        imin, imax = liste_imin_imax
        _imin, _imax = 0, self.base_de_frequence.imax
        if imin < 0:
            imin = _imin
        if imax > _imax:
            imax = _imax

        vecteur_spectre = 2*(np.abs(np.fft.fft(self.vecteur_signal))/self.base_de_temps.N)[imin: imax]
        if imin == 0:
            vecteur_spectre[0] = vecteur_spectre[0]/2
        return vecteur_spectre
    

    
if __name__ == "__main__":
    
    Te1 = 1e-5
    liste_tmin_tmax1 =0, 1


    bdt1 = BaseTemps(liste_tmin_tmax1, Te1)

    vecteur_t1 = bdt1.calculer_vecteur_t()
    vecteur_signal1 = np.cos(2*np.pi*30*vecteur_t1)

    s1 = SignalFFT(bdt1, vecteur_signal1)
    s1.vecteur_signal = s1.vecteur_signal+2



    fmin, fmax = 0, 100
    imin, imax = s1.base_de_frequence.calculer_i(fmin), s1.base_de_frequence.calculer_i(fmax)
    
    vecteur_f = s1.calculer_vecteur_f([imin, imax])
    vecteur_spectre = s1.calculer_vecteur_spectre([imin, imax])
    plt.plot(vecteur_f, vecteur_spectre)
    plt.show()
    
