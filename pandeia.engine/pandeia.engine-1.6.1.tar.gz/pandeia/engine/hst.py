# Licensed under a 3-clause BSD style license - see LICENSE.rst
from __future__ import division, absolute_import

from .telescope import Telescope
from .instrument import Instrument
import astropy.units as u
import stsynphot as st
import numpy as np


class HST(Telescope):

    def get_ote_eff(self, wave):
        """
        Temporary function; allow stsynphot to handle all of the graph table functionality in one go.
        """
        return np.ones_like(wave)



class HSTInstrument(Instrument):

    """
    Generic HST Instrument class
    """
    def __init__(self, mode=None, config={}, **kwargs):
        telescope = HST()
        self.instrument_pars = {}
        self.instrument_pars['detector'] = ["nexp", "ngroup", "nint", "readout_pattern", "subarray"]
        self.instrument_pars['instrument'] = ["aperture", "disperser", "detector", "filter", "instrument", "mode"]
        self.api_parameters = list(self.instrument_pars.keys())

        # these are required for calculation, but ok to live with config file defaults
        self.api_ignore = ['dynamic_scene', 'max_scene_size', 'scene_size']
        Instrument.__init__(self, telescope=telescope, mode=mode, config=config, **kwargs)

    def _get_disperser(self):
        if self.instrument['disperser'] is None:
            return None
        elif "cenwave" in self.instrument:
            return "{},{},{},{}".format(self.instrument['instrument'], self.instrument['detector'], self.instrument['disperser'], self.instrument['cenwave'])
        else:
            return "{},{},{}".format(self.instrument['instrument'], self.instrument['detector'], self.instrument['disperser'])

    def _get_filter_key(self):
        if self.instrument['filter'] is None:
            return None
        else:
            return "{},{},{}".format(self.instrument['instrument'], self.instrument['detector'], self.instrument['filter'])


    def _get_cdbs(self, wave, key):
        """
        HST data is available in the $PYSYN_CBDS trees, so it should be loaded differently.

        Parameters
        ----------
        wave: numpy.ndarray
            Wavelength array onto which the throughput curve is to be interpolated
        key: str
            Key to get filename from the $PYSYN_CDBS tree

        Returns
        -------
        eff: numpy.ndarray or float
            If ref file exists, return efficiency(wave), else return 1.0
        """
        if 'None' not in key:
            bp = st.spectrum.band(key)
            eff = bp(wave*u.micron).value #don't want to pass the Quantity
        else:
            # If it's explicitly None, there is no element; pass through 1.0
            eff = np.ones_like(wave)*1.0
        return eff

    def get_filter_eff(self, wave):
        """
        Temporary function; allow stsynphot to handle all of the graph table functionality in one go.
        """
        return np.ones_like(wave)

    def get_disperser_eff(self, wave):
        """
        Temporary function; allow stsynphot to handle all of the graph table functionality in one go.
        """
        return np.ones_like(wave)

    def get_detector_qe(self, wave):
        """
        Temporary function; allow stsynphot to handle all of the graph table functionality in one go.
        """
        return np.ones_like(wave)

    def get_internal_eff(self,wave):
        """
        This is the only temporary function that will actually do anything. It relies on
        stsynphot for graph table functionality
        
        Parameters
        ----------
        wave: numpy.ndarray
            Wavelength vector to interpolate throughput onto

        Returns
        -------
        eff: numpy.ndarray or float
            Disperser efficiency as a function of wave
        """
        obsmode = self._get_disperser() if self._get_filter_key() is None else self._get_filter_key()
        bp = st.spectrum.band(obsmode)
        eff = bp(wave*u.micron).value #don't want to pass the Quantity

        return eff


class COSFUV(HSTInstrument):

    """
    Special methods unique to HST COS/FUV
    """
    def _get_filter_key(self):
        if self.instrument['filter'] is None:
            return None
        else:
            return "cos,{},{}".format(self.instrument['detector'], self.instrument['filter'])

    def _get_disperser(self):
        if self.instrument['disperser'] is None:
            return None
        elif "cenwave" in self.instrument:
            return "cos,{},{},{}".format(self.instrument['detector'], self.instrument['disperser'], self.instrument['cenwave'])
        else:
            return "cos,{},{}".format(self.instrument['detector'], self.instrument['disperser'])


    def _loadpsfs(self):
        """
        The COS PSFs differ greatly by focus position, and we thus need to 
        know lifetime position (currently only LP4), disperser, and cenwave.
        """
        if self.instrument['mode'] == "spectroscopy":
            psf_key = "{}{}{}{}".format(self.instrument['aperture'], "lp4", self.instrument['disperser'], self.instrument['cenwave'])
        else:
            psf_key = self.instrument['aperture']
        self.psf_library = self._load_psf_library(psf_key)


class WFC3IR(HSTInstrument):

    """
    Special methods unique to HST WFC3IR
    """
    def _get_filter_key(self):
        if self.instrument['filter'] is None:
            return None
        else:
            return "wfc3,{},{}".format(self.instrument['detector'], self.instrument['filter'])


class WFC3UVIS(HSTInstrument):

    """
    Special methods unique to HST WFC3UVIS
    """
    def _get_filter_key(self):
        if self.instrument['filter'] is None:
            return None
        else:
            return "wfc3,{},{}".format(self.instrument['detector'], self.instrument['filter'])

class ACS(HSTInstrument):

    """
    Special methods unique to HST ACS
    """
    pass

class STIS(HSTInstrument):

    """
    Special methods unique to HST STIS
    """
        
    def get_wave_blaze(self):
        """
        Get wavelength vector used in the grating efficiency (blaze) file

        Returns
        -------
        wave_blaze: numpy.ndarray
            Wavelength vector from the grating efficiency file
        """
        key = self._get_disperser()
        if key is not None:
            bp = st.spectrum.band(key)
        return bp.waveset.to_value(u.micron)
