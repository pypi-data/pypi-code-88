import math
import numpy as np
from .constants import C_0, HBAR

class DispersionModel(object):
    """
    Base class for a model of material dispersion.
    All dispersion models are required to fit into the pole-residue model,
    in which
    ``epsilon(omega) = epsilon_infinity +
                       sum_i [      c[i] /(j omega -      a[i])  +
                               conj(c[i])/(j omega - conj(a[i])) ]``
    poles are stored internally in units of rad/s.
    """

    def __init__(self, eps_inf = 1.0, poles = None):
        """ Initialize a raw DispersionModel.
        eps_inf: The relative permittivity at infinite frequency, usually 1.
        poles: A list of the (a, c) coefficients, specified here in rad/s.
        """
        self._eps_inf = eps_inf
        # A list of (a, c) coefficients for the underlying pole-residue model.
        # The units of (a, c) are in angular frequency (rad/s).
        if poles is None:
            self._poles = []
        else:
            self._poles = [(pole[0], pole[1]) for pole in poles]

    def epsilon(self, freqs=None):
        """Evaluate the (complex) relative permittivity defined by the model.
        
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
        if freqs is None:
            return self._eps_inf

        w = 2*np.pi*freqs
        eps = self._eps_inf
        for (a,c) in self._poles:
            eps += c/(1j*w-a) + c.conjugate()/(1j*w-a.conjugate())
        return eps

class Sellmeier(DispersionModel):
    """
    Sellmeier dispersion refractive index model.
    """
    def __init__(self, coeffs, name=None):
        """ Define a material with Sellmeier dispersion.
        
        Parameters
        ----------
        coeffs : list, of the form [(:math:`B_0, C_0`), ...]
            The dispersion formula is:

            .. math::
            
                n^2 - 1 = \\sum_p \\frac{B_p \\lambda^2}{\\lambda^2 - C_p}

            where :math:`\\lambda` is in microns.
        """
        self._eps_inf = 1
        self._poles = []
        self.name = name
        for BC in coeffs:
            # C enters with units of microns**2, B is unitless
            # If we let c = alpha*1j, a = beta*1j, then
            # B = 2*alpha/beta, C = (2*pi*c0/beta)**2
            beta = 2*np.pi*C_0 / np.sqrt(BC[1]) # This has units of rad/s
            alpha = -0.5*beta*BC[0]
            a = 1j*beta
            c = 1j*alpha
            self._poles.append((a, c))

    @classmethod
    def from_dispersion(cls, lam, n, dn_dlam, name=None):
        """ Create a 1-pole Sellmeier model from dispersion data.

        Parameters
        ----------
        lam: float
            The center wavelength in microns.
        n: float
            The refractive index at the center wavelength.
        dn_dlam: float
            The refractive index dispersion at the center wavelength,
            in inverse microns.
        """
        nm1 = n - 1
        ld = lam*dn_dlam
        B = nm1*nm1 / (nm1 - 0.5*ld)
        C = -lam*lam*ld / (2*nm1 - ld)
        coeffs = [(B, C)]
        return cls(coeffs, name);

class Lorentz(DispersionModel):
    """
    Lorentz dispersion permittivity model.
    """
    def __init__(self, eps_inf, coeffs, name=None):
        """ Define a material with Lorentz dispersion.
        
        Parameters
        ----------
        eps_inf: float
            The relative permittivity at infinite frequency, usually 1.
        coeffs : list, of the form [(:math:`\\Delta\\epsilon_0, f_0, \\delta_0`), ...]
            The dispersion formula is:
            
            .. math::

                \\epsilon(f) = \\epsilon_\\infty + \\sum_p 
                \\frac{\\Delta\\epsilon_p f_p^2}{f_p^2 + 2jf\\delta_p - f^2}

            where :math:`f, f_p, \\delta_p` are in Hz.
        """
        self._eps_inf = eps_inf
        self._poles = []
        self.name = name
        for c in coeffs:
            w = 2*math.pi*c[1]
            d = 2*math.pi*c[2]
            if d > w:
                r = 1j*np.sqrt(d*d-w*w)
            else:
                r = np.sqrt(w*w - d*d)
            a = -d - 1j*r
            c = 0.5j*c[0]*w*w / r
            self._poles.append((a, c))

class Debye(DispersionModel):
    """
    Debye dispersion permittivity model.
    """
    
    def __init__(self, eps_inf, coeffs, name=None):
        """ Define a material with Debye dispersion.
        
        Parameters
        ----------
        eps_inf: float
            The relative permittivity at infinite frequency, usually 1.  
        coeffs : list, of the form [(:math:`\\Delta\\epsilon_0, \\tau_0`), ...]
            The dispersion formula is:
            
            .. math::

                \\epsilon(f) = \\epsilon_\\infty + \\sum_p 
                \\frac{\\Delta\\epsilon_p}{1 + jf\\tau_p}
            
            where :math:`f` is in Hz, and :math:`\\tau_p` is in s.
        """
        self._eps_inf = eps_inf
        self._poles = []
        self.name = name
        for c in coeffs:
            a = -2*math.pi / c[1]
            c = -0.5*c[0]*a
            self._poles.append((a, c))

def fit(x, y, x_units='um', y_units='nk', npoles=3):
    """ Fits numerical material dispersion data to a model.
    x : sequence of floats
        Values for x-axis (wavelength, energy, frequency, etc.)
    y : sequence of floats
        Values for y-axis (permittivity, refractive index, etc.)
    x_units : string
        The units of the values in x. Valid units are:
        'um': microns
        'eV': electron-volts
        '1/cm': inverse centimeters
        '1/um': inverse microns
        'Hz': Hertz
    y_units : string
        The units of the values in y. Valid units are:
        'nk': refractive index, real part is n, complex part is k.
              Lossy materials have a positive complex part.
        'eps': permittivity. Lossy materials have a positive complex part.
    npoles : int
        The number of poles in the fitted model. Higher numbers produce
        more accurate models, but require more simulation time. Typically,
        6 poles per decade of x values are used.
    """
    raise NotImplementedError("Fitting is not yet implemented.")

    
