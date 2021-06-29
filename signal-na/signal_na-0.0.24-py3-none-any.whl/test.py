from filtres.filtre_base import FiltreBase
from bode.bode_base import BodeGain, BodePhase
from base.plot_base import tracer
from signaux.signalll import Signal

sig = Signal()
filtre = FiltreBase(nom = "zorro", omega = True, fonction_H= lambda x: 1 / (1 + 1j*1e-3*x)**4)

filtre.calculer_bode(liste_x_min_x_max = [1e2,1e4], N = 100, omega = None, arrondi = False, logX = True)
bode_gain = BodeGain(filtre, omega = True)
bode_phase = BodePhase(filtre, deg = False, phi0 = None)

tracer(sig, filtre.bode_gain(), filtre.bode_phase(), superposition = False, color = "red", titre = "ZORRO")