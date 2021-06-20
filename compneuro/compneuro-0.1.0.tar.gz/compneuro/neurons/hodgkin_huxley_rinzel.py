# pylint:disable=C0103

from collections import OrderedDict
import numpy as np
from ..base_model import BaseModel


class HodgkinHuxleyRinzel(BaseModel):
    """Rinzel neuron model"""

    Time_Scale = 1e3  # s to ms
    Default_States = OrderedDict(V=-65, W=(0.0, 0.0, 1.0))
    Default_Params = OrderedDict(
        C=1.0,
        g_Na=120.0,
        g_K=36.0,
        g_L=0.3,
        E_Na=50.0,
        E_K=-77.0,
        E_L=-54.387,
        S=1.27135220916422,
    )

    def ode(self, t, states, I_ext):
        V, W = states

        alpha_n = 0.01 * (10 - (V + 65)) / (np.exp((10 - (V + 65)) / 10) - 1)
        alpha_m = 0.1 * (25 - (V + 65)) / (np.exp((25 - (V + 65)) / 10) - 1)
        alpha_h = 0.07 * np.exp(-(V + 65) / 20)

        beta_n = 0.125 * np.exp(-(V + 65) / 80)
        beta_m = 4 * np.exp(-(V + 65) / 18)
        beta_h = 1 / (np.exp((30 - (V + 65)) / 10) + 1)

        n_infty = alpha_n / (alpha_n + beta_n)
        m_infty = alpha_m / (alpha_m + beta_m)
        h_infty = alpha_h / (alpha_h + beta_h)
        W_infty = (
            self.params["S"]
            / (1 + self.params["S"] ** 2)
            * (n_infty + self.params["S"] * (1 - h_infty))
        )

        tau_W = 1 + 5 * np.exp(-(((V + 65) - 10) ** 2) / 55 ** 2)

        d_W = 3.0 * W_infty / tau_W - 3.0 * W / tau_W

        # Update the ionic currents and membrane voltage:
        I_K = (
            self.params["g_K"] * (W / self.params["S"]) ** 4 * (V - self.params["E_K"])
        )
        I_Na = self.params["g_Na"] * m_infty ** 3 * (1 - W) * (V - self.params["E_Na"])
        I_L = self.params["g_L"] * (V - self.params["E_L"])
        d_V = (I_ext - I_K - I_Na - I_L) / self.params["C"]

        return np.vstack([d_V, d_W])
