import numpy as np

from pymtsp.engine.status import CityStatus


class City:
    def __init__(self,
                 idx,
                 loc):
        self.status = CityStatus.IDLE
        self.idx = idx
        self.loc = np.array(loc)
        self.assigned_by = None

    def __repr__(self):
        msg = "City {} | Pos {} | Status: {}".format(self.idx, self.loc, self.status)
        return msg
