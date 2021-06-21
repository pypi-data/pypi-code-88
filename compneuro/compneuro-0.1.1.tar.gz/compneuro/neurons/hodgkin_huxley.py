# pylint:disable=C0103

from collections import OrderedDict
import numpy as np
from ..base_model import BaseModel


class HodgkinHuxley(BaseModel):
    """Hodgkin Huxley Neuron Model"""

    Time_Scale = 1e3  # s to ms
    """Hodgkin-Huxley Operates on Milisecond Scale"""
    Default_States = OrderedDict(
        V=-60, n=(0.0, 0.0, 1.0), m=(0.0, 0.0, 1.0), h=(1.0, 0.0, 1.0)
    )
    """Default State Variables of the Hodgkin-Huxley Model"""
    Default_Params = OrderedDict(
        g_Na=120.0, g_K=36.0, g_L=0.3, E_Na=50.0, E_K=-77.0, E_L=-54.387
    )
    """Default Parameters of the Hodgkin-Huxley Model"""

    def ode(self, t, states, I_ext):
        """Hodgkin-Huxley gradient function"""
        V, n, m, h = states

        alpha = np.exp(-(V + 55.0) / 10.0) - 1.0
        beta = 0.125 * np.exp(-(V + 65.0) / 80.0)
        d_n = np.zeros_like(alpha)
        _mask = np.abs(alpha) <= 1e-7
        d_n[_mask] = 0.1 * (1.0 - n[_mask]) - beta[_mask] * n[_mask]
        _mask = np.logical_not(_mask)
        d_n[_mask] = (-0.01 * (V[_mask] + 55.0) / alpha[_mask]) * (
            1.0 - n[_mask]
        ) - beta[_mask] * n[_mask]

        alpha = np.exp(-(V + 40.0) / 10.0) - 1.0
        beta = 4.0 * np.exp(-(V + 65.0) / 18.0)
        _mask = np.abs(alpha) <= 1e-7
        d_m = np.zeros_like(alpha)
        d_m[_mask] = (1.0 - m[_mask]) - beta[_mask] * m[_mask]
        _mask = np.logical_not(_mask)
        d_m[_mask] = (-0.1 * (V[_mask] + 40.0) / alpha[_mask]) * (
            1.0 - m[_mask]
        ) - beta[_mask] * m[_mask]

        alpha = 0.07 * np.exp(-(V + 65.0) / 20.0)
        beta = 1.0 / (np.exp(-(V + 35.0) / 10.0) + 1.0)
        d_h = alpha * (1 - h) - beta * h

        i_na = self.params["g_Na"] * np.power(m, 3) * h * (V - self.params["E_Na"])
        i_k = self.params["g_K"] * np.power(n, 4) * (V - self.params["E_K"])
        i_l = self.params["g_L"] * (V - self.params["E_L"])

        d_V = I_ext - i_na - i_k - i_l
        return np.vstack([d_V, d_n, d_m, d_h])
