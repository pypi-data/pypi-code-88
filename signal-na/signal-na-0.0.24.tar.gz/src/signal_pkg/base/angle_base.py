import numpy as np
import copy

import os, sys

from numpy.lib import angle
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))

class AngleBase():
    def __init__(self, nombre, deg = False):
        if isinstance(nombre, (int, float)):
            AngleBase.__init_int_float(self, nombre, deg)
        elif isinstance(nombre, complex):
            AngleBase.__init_complex(self, nombre, deg)
        else:
            print("AngleBase: nombre non pris en charge")
            sys.exit()

    def __init_int_float(self, angle, deg):
        if deg == True:
            angle *= (np.pi/180)
        angle %=  2*np.pi
        # if angle >= np.pi:
        #     angle -= np.pi
        self.angle = angle
        self.deg = deg

    def __init_complex(self, nombre, deg):
        self.angle = np.angle(nombre)
        if self.angle < 0:
            self.angle += 2*np.pi
        self.deg = deg

    def lire_angle(self, deg = None):
        if deg == None:
            deg = self.deg
        angle = self.angle
        if angle >= np.pi:
            angle -= (2*np.pi)
        if deg == True:
            return angle * 180 / np.pi
        else:
            return angle

    def __lire_angle_le_plus_proche_rad(self, angle_rad):
        if angle_rad == None:
            return self.__lire_angle_le_plus_proche_rad(0)
        n = angle_rad // (2*np.pi)
        angle_decale = self.angle + 2*n*np.pi
        if np.abs(angle_decale+2*np.pi - angle_rad) < np.abs(angle_decale - angle_rad):
            angle_decale += (2*np.pi)
        if np.abs(angle_decale-2*np.pi - angle_rad) < np.abs(angle_decale - angle_rad):
            angle_decale -= (2*np.pi)
        return angle_decale

    def lire_angle_le_plus_proche(self, angle, deg = False):
        if deg:
            angle *= (np.pi/180)
        angle_decale = self.__lire_angle_le_plus_proche_rad(angle)
        if deg:
            angle_decale *= (180/np.pi)
        return angle_decale


    def __str__(self):
        return str(self.lire_angle())


def calculer_vecteur_angles(vecteur_angles, deg = True, phi0 = None):
    N = len(vecteur_angles)
    vecteur_angles_sortie = np.zeros(N, dtype = np.float64)
    vecteur_angles_sortie[0] = AngleBase(vecteur_angles[0], deg).lire_angle_le_plus_proche(phi0, deg)
    for i in range(1, N):
        vecteur_angles_sortie[i] = AngleBase(vecteur_angles[i], deg).lire_angle_le_plus_proche(vecteur_angles_sortie[i-1], deg)
    return vecteur_angles_sortie

if __name__ == "__main__":
    nombre = 1.
    angle = AngleBase(nombre, False)
    
    print(angle.lire_angle())
