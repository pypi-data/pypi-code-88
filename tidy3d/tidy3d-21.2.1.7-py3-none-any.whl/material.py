import numpy as np
import logging

from .utils import listify, log_and_raise
from .constants import int_, float_, EPSILON_0, C_0
from .dispersion import DispersionModel, Sellmeier

class Medium(object):
    """
    Base class for a custom defined material.
    """

    def __init__(self, name=None, **kwargs):
        """ Define a material. Various input artuments are possible which
        define either frequency-independent material parameters, or a
        dispersive, frequency-dependent model.
        
        Parameters
        ----------
        epsilon : float or DispersionModel, optional
            If numeric, real part of the dimensionless relative permittivity. 
            If a :class:`.DispersionModel` is provided, then the model 
            data is copied. Default is ``1.`` (vacuum).
        sigma : float, optional
            (S/micron) Electric conductivity, s.t. 
            ``Im(eps(omega)) = sigma/omega``, where ``eps(omega)`` is the 
            complex permittivity at frequency omega. This conductivity is 
            added on top of any coming from the dispersion model, if used.
        n : float, optional
            Real part of refractive index.
        k : float, optional
            Imaginary part of refractive index, where eps = (n + 1i*k)**2.
        wl : float, optional
            (micron) Wavelength corresponding to n and k values.
        freq : float, optional
            (Hz) Frequency corresponding to n and k values.
        dn : float, optional
            (1/micron) Refractive index dispersion; derivative of
            refractive index with respect to wavelength.

        Note
        ----
        Only the following combinations of arguments are supported:
        
         * ``Medium(epsilon)``
         * ``Medium(epsilon, sigma)``
         * ``Medium(n)``
         * ``Medium(n, k, wl)``
         * ``Medium(n, k, freq)``
         * ``Medium(n, wl, dn)``
         * ``Medium(n, freq, dn)``
        
        """
        if "epsilon" in kwargs:
            epsilon = kwargs.pop("epsilon")
            sigma = kwargs.pop("sigma", 0)
            if isinstance(epsilon, DispersionModel):
                self.eps = epsilon._eps_inf
                self.sigma = 0
                self.poles = epsilon._poles
                self.dispmod = epsilon
            else:
                self.dispmod = None
                self.eps = epsilon
                self.sigma = sigma
                self.poles = []
            self._check_stability()
            if kwargs:
                log_and_raise(
                    "Invalid keyword arguments specified with epsilon "
                    "and sigma: %r." % tuple(kwargs.keys()),
                    TypeError
                    )
        elif "n" in kwargs:
            n = kwargs.pop("n")
            lam = None
            freq = None
            k = 0
            dn = 0
            if "k" in kwargs:
                k = kwargs.pop("k")
                if "wl" in kwargs:
                    lam = kwargs.pop("wl")
                if "freq" in kwargs:
                    freq = kwargs.pop("freq")
                if lam is None and freq is None:
                    log_and_raise(
                        "wl or freq required when specifying k.",
                        TypeError
                        )
                if lam is not None and freq is not None:
                    log_and_raise(
                        "Only wl or freq may be specified",
                        TypeError
                        )
            if "dn" in kwargs:
                dn = kwargs.pop("dn")
                if dn > 0:
                    log_and_raise(
                        "dn must be smaller than zero.",
                        NotImplementedError
                        )
                if "wl" in kwargs:
                    lam = kwargs.pop("wl")
                if "freq" in kwargs:
                    freq = kwargs.pop("freq")
                if lam is None and freq is None:
                    log_and_raise(
                        "wl or freq required when specifying k.",
                        TypeError
                        )
                if lam is not None and freq is not None:
                    log_and_raise(
                        "Only wl or freq may be specified.",
                        TypeError
                        )
            if kwargs:
                log_and_raise(
                    "Invalid keyword arguments specified with n: %r." %
                    tuple(kwargs.keys()),
                    TypeError
                    )

        
            if freq is not None:
                lam = C_0 / freq
            if lam is not None:
                freq = C_0 / lam

            eps_real = n*n - k*k
            eps_imag = 2*n*k
            sigma = 0
            if k != 0:
                sigma = 2*np.pi*freq*eps_imag*EPSILON_0

            self.eps = eps_real
            self.sigma = sigma
            self._check_stability()

            if dn == 0:
                self.dispmod = None
                self.poles = []
            else:
                if k == 0:
                    self.dispmod = Sellmeier.from_dispersion(lam, n, dn)
                    self.poles = self.dispmod._poles
                else:
                    log_and_raise(
                        "Currently k cannot be specified with dn.",
                        NotImplementedError
                        )

        # If set, this is a tuple (f_lower, f_upper) in Hz of the frequency
        # range of validity of this material model.
        self.frequency_range = None
        
        self.name = None if name is None else str(name)

    def _check_stability(self):
        if 0 < self.eps < 1:
            logging.warning(
                "Permittivity smaller than one could result "
                "in numerical instability. Use Courant stability factor "
                "value lower than the smallest refractive index value."
            )


        elif self.eps <= 0:
            err_msg = (
                "Permittivity smaller than zero can result in "
                "numerical instability and should be included as a "
                "dispersive model."
            )

            if self.eps < -100:
                err_msg += \
                    "For large negative values consider using PEC instead."
                    
            log_and_raise(err_msg, ValueError)

    def epsilon(self, freqs=None):
        """Evaluate the (complex) relative permittivity of the medium.
        
        Parameters
        ----------
        freqs : array_like or None, optional
            (Hz) Array of frequencies at which to query the permittivity. If 
            ``None``, the instantaneous :math:`\\epsilon_\\infty` is returned.
        
        Returns
        -------
        array_like
            The permittivity values, same shape as ``freqs``.
        """

        if self.dispmod is None:
            if freqs is None:
                return self.eps
            else:
                return self.eps + 1j*self.sigma/2/np.pi/freqs/EPSILON_0
        else:
            return self.dispmod.epsilon(freqs)

    @staticmethod
    def variants():
        return None

class PEC(object):
    """ Perfect electric conductor. All tangential electric fields vanish.
    """
    def __init__(self, name='PEC'):
        """ Construct.

        Parameters
        ----------
        name : str, optional
            Custom name of the material.
        """
        self.name=name

class PMC(object):
    """ Perfect magnetic conductor. All tangential magnetic fields vanish.
    """
    def __init__(self, name='PMC'):
        """ Construct.

        Parameters
        ----------
        name : str, optional
            Custom name of the material.
        """
        self.name=name

