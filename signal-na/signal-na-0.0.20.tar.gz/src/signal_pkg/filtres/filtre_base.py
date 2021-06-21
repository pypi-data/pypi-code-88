import numpy as np
import matplotlib.pyplot as plt

def __calculer_argument(complexe):
    re, im = np.real(complexe), np.imag(complexe)
    if re > 0:
        return np.arctan(im/re)
    elif re == 0:
        if im > 0:
            return np.pi/2
        elif im < 0:
            return -np.pi/2
        else:
            return 0
    else:
        if im > 0:
            return  np.arctan(im/re) + np.pi 
        elif im < 0:
            return  np.arctan(im/re) - np.pi 
        else:
            return -np.pi

calculer_argument = np.vectorize(__calculer_argument)

class FiltreBase():
    liste_n_signaux = [0]
    
    def __init__(self, nom=""):
        self.__chercher_nom_valide(nom)

    def raz(self):
        print("raz")
        try:
            del(self.vecteur_f)
        except:
            pass
        try:
            del(self.vecteur_p)
        except:
            pass
        try:
            del(self.vecteur_H_cplx)
        except:
            pass
        try:
            del(self.vecteur_G)
        except:
            pass
        try:
            del(self.vecteur_G_dB)
        except:
            pass
        try:
            del(self.vecteur_phi)
        except:
            pass
        
    def configurer_liste_fmin_fmax(self, liste_fmin_fmax):
        try:
            liste_fmin_fmax_ancien = self.liste_fmin_fmax
        except:
            liste_fmin_fmax_ancien = liste_fmin_fmax

        if liste_fmin_fmax_ancien != liste_fmin_fmax:
            self.liste_fmin_fmax = liste_fmin_fmax
            self.raz()
        else:
            self.liste_fmin_fmax = liste_fmin_fmax
            

    def configurer_n_points(self, n_points):
        try:
            n_points_ancien = self.n_points
        except:
            n_points_ancien = n_points

        if n_points_ancien != n_points:
            self.n_points = n_points
            self.raz()
        else:
            self.n_points = n_points
               
    def __chercher_nom_valide(self, nom):
        if nom != "":
            self.nom = nom
        else:
            numero = np.max(self.liste_n_signaux)+1
            self.nom = "filtre_" + str(numero)
            self.liste_n_signaux.append(numero)

    def calculer_vecteur_f(self, liste_fmin_fmax, n_points):
        self.configurer_liste_fmin_fmax(liste_fmin_fmax)
        self.configurer_n_points(n_points)
        try:
            N = len(self.vecteur_f)
        except:
            fmin, fmax = self.liste_fmin_fmax
            self.vecteur_f = np.logspace(np.log10(fmin), np.log10(fmax), self.n_points)
            print("On calcule vecteur f")
        return self.vecteur_f

    def calculer_vecteur_p(self, liste_fmin_fmax, n_points):
        self.configurer_liste_fmin_fmax(liste_fmin_fmax)
        self.configurer_n_points(n_points)
        try:
            N = len(self.vecteur_p)
        except:
            self.calculer_vecteur_f(liste_fmin_fmax, n_points)
            self.vecteur_p = 1j*2*np.pi*self.vecteur_f
            print("On calcule vecteur p")
        return self.vecteur_p

    def calculer_vecteur_H_cplx(self, liste_fmin_fmax, n_points):
        self.configurer_liste_fmin_fmax(liste_fmin_fmax)
        self.configurer_n_points(n_points)
        try:
            N = len(self.vecteur_H_cplx)
        except:
            self.calculer_vecteur_p(liste_fmin_fmax, n_points)
            N = len(self.vecteur_p)
            self.vecteur_H_cplx = np.ones(N)
            print("On calcule vecteur H cplx")

            return self.vecteur_H_cplx
    
    def calculer_vecteur_G(self, liste_fmin_fmax, n_points):
        self.configurer_liste_fmin_fmax(liste_fmin_fmax)
        self.configurer_n_points(n_points)
        try:
            N = len(self.vecteur_G)
        except:
            self.calculer_vecteur_H_cplx(liste_fmin_fmax, n_points)
            self.vecteur_G = np.abs(self.vecteur_H_cplx)
            print("On calcule vecteur G")
        return self.vecteur_G

    def calculer_vecteur_G_dB(self, liste_fmin_fmax, n_points):
        self.configurer_liste_fmin_fmax(liste_fmin_fmax)
        self.configurer_n_points(n_points)
        try:
            N = len(self.vecteur_G_dB)
        except:
            self.calculer_vecteur_G(liste_fmin_fmax, n_points)
            self.vecteur_G_dB = 20*np.log10(self.vecteur_G)
            print("On calcule vecteur G dB")
        return self.vecteur_G_dB

    def calculer_vecteur_phi(self, liste_fmin_fmax, n_points):
        self.configurer_liste_fmin_fmax(liste_fmin_fmax)
        self.configurer_n_points(n_points)
        try:
            N = len(self.vecteur_phi)
        except:
            self.calculer_vecteur_H_cplx(liste_fmin_fmax, n_points)
            self.vecteur_phi = calculer_argument(self.vecteur_H_cplx)
            print("On calcule vecteur phi")

        return self.vecteur_phi

    def tracer_G_dB(self, liste_fmin_fmax, n_points, affichage = True):
        self.calculer_vecteur_G_dB(liste_fmin_fmax, n_points)
        plt.semilogx(self.vecteur_f, self.vecteur_G_dB)
        plt.xlabel("$f$ (Hz)")
        plt.ylabel("$G_{dB}$ (dB)")
        if affichage == True:
            plt.show()

    def tracer_phi(self, liste_fmin_fmax, n_points, affichage = True):
        self.calculer_vecteur_phi(liste_fmin_fmax, n_points)
        plt.semilogx(self.vecteur_f, self.vecteur_phi)
        plt.xlabel("$f$ (Hz)")
        plt.ylabel("$\\varphi$ (rad)")
        if affichage == True:
            plt.show()

    def tracer_bode(self, liste_fmin_fmax, n_points, affichage = True):
        self.calculer_vecteur_G_dB(liste_fmin_fmax, n_points)
        fig, liste_axes = plt.subplots(2, 1, constrained_layout=True)
        plt.sca(liste_axes[0])
        self.tracer_G_dB(liste_fmin_fmax, n_points, False)
        plt.sca(liste_axes[1])
        self.tracer_phi(liste_fmin_fmax, n_points, False)
        if affichage == True:
            plt.show()

if __name__ == "__main__":
    f = FiltreBase("zorro")
    f.tracer_bode([10, 100], 100)