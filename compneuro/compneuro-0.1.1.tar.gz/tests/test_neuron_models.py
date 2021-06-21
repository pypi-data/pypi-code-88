import pytest
from scipy.signal import find_peaks
import numpy as np
from collections import OrderedDict
from compneuro.base_model import BaseModel
from compneuro.neurons.hodgkin_huxley import HodgkinHuxley
from compneuro.neurons.hodgkin_huxley_rinzel import HodgkinHuxleyRinzel
from compneuro.neurons.hodgkin_huxley_wilson import HodgkinHuxleyWilson
from compneuro.utils.signal import generate_stimulus
from .test_compneuro import assert_snr
from .reference_neuron_implementations import hh, hhr, hhw


@pytest.fixture
def inputs():
    dt = 1e-5
    t = np.arange(0.0, 0.1, dt)
    I_ext = generate_stimulus("step", dt, 0.1, (0.02, 0.1), 50.0)
    return dt, t, I_ext


def test_hhn(inputs):
    dt, t, I_ext = inputs
    hhn_ref_V, _ = hh(t, I_ext)
    hhn_ref_V -= 65.0
    neu = HodgkinHuxley(num=1, V=-75.0)
    res_euler = neu.solve(t, I_ext, solver="Euler", verbose=False)
    res_odeint = neu.solve(t, I_ext, solver="odeint", rtol=1e-10, verbose=False)
    res_rk45 = neu.solve(t, I_ext, solver="RK45", rtol=1e-10, verbose=False)

    assert_snr(hhn_ref_V, res_euler["V"][0], threshold=6.0)
    assert_snr(res_euler["V"], res_odeint["V"], threshold=10.0)
    assert_snr(res_euler["V"], res_rk45["V"], threshold=10.0)


def test_rinzel(inputs):
    dt, t, I_ext = inputs
    hhr_ref_V, _ = hhr(t, I_ext)
    hhr_ref_V -= 65.0
    neu = HodgkinHuxleyRinzel(num=1)
    res_euler = neu.solve(t, I_ext, solver="Euler", verbose=False)
    res_odeint = neu.solve(t, I_ext, solver="odeint", rtol=1e-10, verbose=False)
    res_rk45 = neu.solve(t, I_ext, solver="RK45", rtol=1e-10, verbose=False)

    assert_snr(hhr_ref_V, res_euler["V"][0], threshold=6.0)
    assert_snr(res_euler["V"], res_odeint["V"], threshold=10.0)
    assert_snr(res_euler["V"], res_rk45["V"], threshold=10.0)


def test_wilson(inputs):
    dt, t, I_ext = inputs
    hhw_ref_V, _ = hhw(t, I_ext)
    neu = HodgkinHuxleyWilson(num=1)
    res_euler = neu.solve(t, I_ext, solver="Euler", verbose=False)
    res_odeint = neu.solve(t, I_ext, solver="odeint", rtol=1e-10, verbose=False)
    res_rk45 = neu.solve(t, I_ext, solver="RK45", rtol=1e-10, verbose=False)

    assert_snr(hhw_ref_V, res_euler["V"][0], threshold=6.0)
    assert_snr(res_euler["V"], res_odeint["V"], threshold=10.0)
    assert_snr(res_euler["V"], res_rk45["V"], threshold=10.0)
