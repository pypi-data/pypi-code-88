# pylint:disable=C0103
from collections import OrderedDict
import numpy as np
from ..base_model import BaseModel


class HodgkinHuxleyWilson(BaseModel):
    Time_Scale = 1e3
    Default_States = OrderedDict(V=-70, R=0.088)
    Default_Params = OrderedDict(C=1.2, E_K=-92.0, g_K=26.0, E_Na=55.0)

    def ode(self, t, states, I_ext):
        V, R = states

        R_infty = 0.0135 * V + 1.03

        d_R = (R_infty - R) / 1.9

        I_Na = (17.81 + 0.4771 * V + 0.003263 * V ** 2) * (V - self.params["E_Na"])
        I_K = self.params["g_K"] * R * (V - self.params["E_K"])
        d_V = 1.0 / self.params["C"] * (I_ext - I_Na - I_K)

        return np.vstack([d_V, d_R])
