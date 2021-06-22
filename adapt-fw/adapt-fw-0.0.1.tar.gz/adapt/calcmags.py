#!/usr/bin/env python

import sys
import obspy
import numpy as np


EPIDIST = 7.3  # km
DEPTH = 2.0  # km
A0CORRPOINTS = ((0.0, -1.3), (60.0, -2.8), (400.0, -4.5), (1000.0, -5.85))
RESPONSEFILT = {
    'pre_filt': None,
    'water_level': 100,
    # Defaults from obspy
    'zero_mean': False,
    'taper': False,
    'taper_fraction': False
    }


# =================================================================

def __calculate_correction_factor(epidist, magpoints=None):
    """  Calculate the amplitude corrections for Richter magnitude.

    The corrections are made only fot the log10(A0) value.
    No site effect accounted for

    - Default SC3
    module.trunk.global.MLv.logA0 = "0 -1.3;60 -2.8;400 -4.5;1000 -5.85"

    The logA0 configuration string consists of an arbitrary number of
    distance-value pairs separated by semicolons.
    The distance is in km and the value corresponds to the log10(A0)
    term above.

    Within each interval the values are computed by linear interpolation.
    E.g. for the above default specification, at a distance of 100 km the
        logA0 value would be ((-4.5)-(-2.8))*(100-60)/(400-60)-2.8 = -3.0 --
        in other words, at 100 km distance the magnitude would be -3)

        `mag = \log10(A) - (-3) = \log10(A) + 3`

        which is according to the original Richter (1935) formula if the
        amplitude is measured in millimeters. Note that the baseline
        for logA0 is millimeters for historical reasons, while internally
        in SeisComP 3 the Wood-Anderson amplitudes are measured and stored
        micrometers.

    Link(https://www.seiscomp.de/seiscomp3/doc/seattle/2013.149/apps/global_mlv.html)

    """
    if not magpoints:
        magpoints = A0CORRPOINTS
    #
    magdists = [xx[0] for xx in magpoints]
    magvalues = [xx[1] for xx in magpoints]

    if epidist in magdists:
        # if epidist is equal to a point, return the related value
        return magvalues[magdists.index(epidist)]
    else:
        # ... else interpolate, find upper tuple and lower tuple
        upidx = [ii for ii, xx in enumerate(magdists) if epidist < xx][0]
        lpidx = upidx - 1
        #
        up, lp = magpoints[upidx], magpoints[lpidx]

        # (-4.5  -  (-2.8)  ) * (X-60)/(400-60) -2.8
        corrfact = (up[1] - lp[1]) * (epidist - lp[0]) / (up[0] - lp[0]) + lp[1]
    return corrfact


def __simulate_wood_anderson(optr, water_level=10):
    """ Simple as it it. We want to simulate a WoodAnderson """
    # Sensitivity is 2080 according to:
    # P. Bormann: New Manual of Seismological Observatory Practice
    # IASPEI Chapter 3, page 24
    #
    # (PITSA has 2800)
    #

    # Seiscomp3 (puoi pure invertire la parte immaginaria)
    PAZ_WA_SC3 = {
         'poles': [(-6.283185-4.712389j),
                   (-6.283185+4.712389j)],
         'zeros': [0+0j],
         'gain': 1.0,
         'sensitivity': 2800}

    # # ----- ObsPy
    # # Sensitivity is 2080 according to:
    # # P. Bormann: New Manual of Seismological Observatory Practice
    # # IASPEI Chapter 3, page 24
    # # (PITSA has 2800)
    # PAZ_WA_OBSPY = {
    #      'poles': [-6.283 + 4.7124j, -6.283 - 4.7124j],
    #      'zeros': [0+0j],
    #      'gain': 1.0,
    #      'sensitivity': 2080}

    # --- (Bormann and Dewey, 2014) revised
    # PAZ_WA_BD = {
    #       'poles': [-5.49779 - 5.60886j,
    #                 -5.49779 + 5.60886j],
    #       'zeros': [0.0 + 0.0j, 0.0 + 0.0j],
    #       'gain': 1.0028,
    #       'sensitivity': 2080}

    optr.simulate(paz_simulate=PAZ_WA_SC3,
                  paz_remove=None,
                  water_level=10)
    return optr


def __calc_minmax_amp(wt):
    Amax = np.max(wt.data)
    Amin = np.min(wt.data)
    # Define Amp
    return (np.abs(Amax) + np.abs(Amin)) / 2.0


# ===================  IMPORTANT

def calc_station_mag_MLv(st, epidist=EPIDIST):
    """ MLv Calc """
    if not epidist:
        raise ValueError("I need an epicentral distance")
    else:
        print("EpicentralDistance:  %4.3f" % epidist)
    #
    tr = st.select(channel="*Z")[0]
    tr = __simulate_wood_anderson(tr)  # simulateWA
    A0 = __calculate_correction_factor(epidist)
    #
    A = np.max(np.abs(tr.data))
    return np.log10(A) - A0


def calc_station_mag_MLh(st, epidist=EPIDIST):
    """ MLv Calc """
    if not epidist:
        raise ValueError("I need an epicentral distance")
    #
    A0 = __calculate_correction_factor(epidist)
    #
    trN = st.select(channel="*N")[0]
    trN = __simulate_wood_anderson(trN)  # simulateWA
    ampN = __calc_minmax_amp(trN)
    trE = st.select(channel="*E")[0]
    trE = __simulate_wood_anderson(trE)  # simulateWA
    ampE = __calc_minmax_amp(trE)
    #
    A = (np.abs(ampN) + np.abs(ampE)) / 2.0

    return np.log10(A) - A0


def process_stream(st):
    st.detrend('demean')
    st.detrend('simple')
    st.taper(max_percentage=0.05, type='cosine')  # 'hann'
    # ====== BP
    st.filter("bandpass",
              freqmin=1,
              freqmax=50,    # originally 30
              corners=4,     # originally 2
              zerophase=True)
    return st


def remove_response(st, inv, response_filt_parameters):
    for tr in st:
        tr.attach_response(inv)
        tr.remove_response(
            output="VEL",
            **response_filt_parameters)
        tr.data = tr.data * 1000.0
    return st


# ================================

def main(strpath=None, invpath=None):
    if strpath and invpath:
        strpath = sys.argv[1]
        invpath = sys.argv[2]
        print("... read stream")
        st = obspy.read(strpath)
        print("... read inventory")
        inv = obspy.read_inventory(invpath)
    else:
        print("... read stream")
        st = obspy.read()
        print("... read inventory")
        inv = obspy.read_inventory()
    #
    st = process_stream(st)
    st = remove_response(st, inv, RESPONSEFILT)

    # --- MLv
    # simulate WA
    # get amp
    # Cal mag
    MLV = calc_station_mag_MLv(st)

    # --- MLh
    # simulate WA
    # get amp
    # Cal mag
    MLH = calc_station_mag_MLh(st)

    print("MLv:  %5.2f" % MLV)
    print("MLh:  %5.2f" % MLH)

    return MLV, MLH


if __name__ == "__main__":
    if len(sys.argv) == 3:
        _, _ = main(sys.argv[1], sys.argv[2])
    else:
        _, _ = main()
