import numpy as np
from scipy.integrate import quad
from scipy.interpolate import interp1d

from Alexandria.constructs.array import dx_v


class one_d:

    @classmethod
    def trapezoidal(cls, f, x):
        f_prime = np.zeros(len(f))
        dt_f = dx_v(x)
        for i in range(f.size - 1):
            f_prime[i] = dt_f[i] * (f[i] + (f[i + 1] - f[i]) / 2)
        np.append(f_prime, dt_f[-2] * (f[-1] + (f[-2] - f[-1]) / 2))
        return f_prime.sum(), f_prime


class two_d:

    @classmethod
    def Q_interp1d(cls, x1, x2, target, log=False):
        """
        :param x1:
        :param x2:
        :param target:
        :param log:
        :return:
        """

        # Integral about x_p axis
        int_z = np.empty(target.shape[1])

        for i in range(x1.size):
            spl_x2 = interp1d(x2, target[:, i])
            int_z[i] = quad(spl_x2, x2.min(), x2.max())[0]*1000

        # Integral about z_p axis
        spl_x1 = interp1d(x1, int_z)
        int_x1 = quad(spl_x1, x1[1], x1[-2])[0]

        if log:
            print(f"Maximum value of target distribution:    {target.max():.5f}")
            print(f"Average value over x2 axis:              {np.mean(target):.5f}")
            print(f"Integral over x1, x2 axes:               {int_z:.5f}")

        return int_x1, spl_x1
