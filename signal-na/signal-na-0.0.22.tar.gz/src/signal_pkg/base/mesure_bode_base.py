
import numpy as np

import os, sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))
from base.angle_base import AngleBase


class MesureBodeBase():
    def __init__(self, f, H):
        self.f = f
        self.H = H

    def lire_x(self, omega = False):
        return 2*np.pi*self.f if omega else self.f
        
    def lire_G(self, dB = True):
        G = np.abs(self.H)
        return 20*np.log10(G) if dB else G
    
    def lire_phi(self, deg = False, phi0 = 0):
        phi = AngleBase(self.H)
        return phi.lire_angle_le_plus_proche(phi0, deg)

if __name__ == "__main__":
    bb = MesureBodeBase(10, 1+1j)
    print(bb.lire_G(False))
    print(bb.lire_phi(True, 360))
        