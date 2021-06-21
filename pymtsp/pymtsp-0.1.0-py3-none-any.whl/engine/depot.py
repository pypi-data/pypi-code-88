import numpy as np

from pymtsp.engine.status import DepotStatus


class Depot:
    def __init__(self,
                 idx,
                 loc):
        self.status = DepotStatus.IDLE
        self.idx = idx
        self.loc = np.array(loc)
