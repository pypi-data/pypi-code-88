import os, sys
import numpy as np

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))
import base.voie_base

class Sysam():
    def __init__(self, nom):
        print("Sysam: ", end = "SignalSysam(")
        print("nom: ", nom, end = ")\n")        


    def fermer(self):
        print("Sysam: fermer()")

    def config_entrees(self, voies, calibres, diff=[]):
        print("Sysam: ", end = "config_entrees(")
        print("voies=", voies, end = ", ")        
        print("calibre=", calibres, end = ", ")        
        print("diff=", diff, end = ")\n")
        self.voies = voies
        self.calibre = calibres
        self.diff = diff

    def config_echantillon(self, techant, nbpoints):
        print("Sysam: ", end = "config_echantillon(")
        print("techant=", techant, end = ", ")        
        print("nbpoints=", nbpoints, end = ")\n")        
        self.techant = techant
        self.nbpoints = nbpoints

    def config_trigger(self, voie, seuil, montant = 1, pretrigger = 0, pretriggerSouple = 0, hysteresys = 0):
        print("Sysam: ", end = "config_trigger(")
        print("voie=", voie, end = ", ")        
        print("seuil=", seuil, end = ", ")        
        print("montant=", montant, end = ", ")        
        print("pretrigger=", pretrigger, end = ", ")        
        print("pretriggerSouple=", pretriggerSouple, end = ", ")        
        print("hysteresys=", hysteresys, end = ")\n")        

    def config_trigger_externe(self, pretrigger = 0, pretriggerSouple = 0):
        print("Sysam: ", end = "config_trigger_externe(")
        print("pretrigger=", pretrigger, end = ", ")        
        print("pretriggerSouple=", pretriggerSouple, end = ")\n")        

    def desactiver_trigger(self):
        print("Sysam: desactiver_trigger()")

    def acquerir(self):
        print("Sysam: acquerir()")

    def temps(self, reduction=1):
        print("Sysam: ", end = "temps(")
        print("reduction=", reduction, end = ")\n")        

        try:
            techant = self.techant
            nbpoints = self.nbpoints
            voies = self.voies
            self.temps = np.zeros([len(voies), nbpoints])
            for i in range(len(voies)):
                self.temps[i, :] = np.arange(nbpoints)*techant*base.voie_base.T_sysam
            return np.array(self.temps[:, ::reduction])
        except:
            print("Problème: lecture des temps avant fin config")

    def entrees(self, reduction=1):
        print("Sysam: ", end = "entrees(")
        print("reduction=", reduction, end = ")\n")        
        try:
            techant = self.techant
            nbpoints = self.nbpoints
            voies = self.voies
            self.signaux = np.zeros([len(voies), nbpoints])
            for i in range(len(voies)):
                valeur = voies[i]
                if valeur in self.diff:
                    valeur = - valeur 
                self.signaux[i, :] = np.ones(nbpoints)*valeur
            return np.array(self.signaux[:, ::reduction])
        except:
            print("Problème: lecture des signaux avant fin config")
        
    def config_sortie(self, nsortie, techant, tensions, repetion=0):
        print("Sysam: ", end = "config_sortie(")
        print("nsortie=", nsortie, end = ", ")        
        print("techant=", techant, end = ", ")        
        print("tensions=", tensions, end = ", ")        
        print("repetion=", repetion, end = ")\n")        
        
    def declencher_sorties(self, s1, s2):
        print("Sysam: ", end = "declencher_sorties(")
        print("s1=", s1, end = ", ")        
        print("s2=", s2, end = ")\n")        
        
    def stopper_sorties(self, s1, s2):
        print("Sysam: ", end = "stopper_sorties(")
        print("s1=", s1, end = ", ")        
        print("s2=", s2, end = ")\n")        
        
    def acquerir_avec_sorties(self, tension1, tension2):
        print("Sysam: ", end = "acquerir_avec_sorties(")
        print("tension1=", tension1, end = ", ")        
        print("tension2=", tension2, end = ")\n")        
    
if __name__ == "__main__":
    s = SignalSysam("SP5")
    s.config_entrees([0, 2, 3], [10., 10., 10.], diff=[2])
    s.config_echantillon(1, 10)
    s.config_trigger(0, 3., montant = 1, pretrigger = 0, pretriggerSouple = 0, hysteresys = 0)
    s.config_trigger_externe(pretrigger = 0, pretriggerSouple = 0)
    s.desactiver_trigger()
    s.acquerir()
    print(s.temps(reduction=1))
    print(s.entrees(reduction=1))
    # s.config_sortie(1, 3, np.zeros(10), repetion=0)
    # s.declencher_sorties(1, 1)
    # s.stopper_sorties(1, 1)
    # s.acquerir_avec_sorties(np.zeros(10), np.zeros(10))
