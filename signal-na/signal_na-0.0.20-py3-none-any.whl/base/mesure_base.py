
class MesureBase():
    def __init__(self, T_th = None):
        self.T_th = T_th
        self.Vmin = None
        self.Vmax = None
        self.liste_i_trigger = None
        self.T = None
        self.phi = None
        self.Vpp = None
        self.Vdc = None
        self.Veff = None
        self.trigger_bas = None
        self.trigger_haut = None
