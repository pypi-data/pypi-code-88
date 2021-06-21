"""Test Utility Module of CompNeuro

Tests:
    1. Plot Submodule
    2. Signal Submodule
"""
import pytest
import numpy as np
import matplotlib.pyplot as plt
from compneuro import plot, signal
import compneuro.errors as err

DT = 1e-4
DUR = 1.0
T = np.arange(0, DUR, DT)


@pytest.fixture
def signal_data():
    dt = 1e-4
    dur = 1.0
    t = np.arange(0, 1.0, dt)
    bw = 100  # 30 Hz
    num = 2
    seed = 0
    return dt, dur, t, bw, num, seed


@pytest.fixture
def signal_spikes(signal_data):
    dt, dur, t, bw, num, seed = signal_data

    rate = 100
    randvar = np.random.rand(len(t), num)
    spikes = randvar < rate * dt
    return rate, spikes


@pytest.fixture
def matrix_data():
    return np.random.rand(100, len(T))


@pytest.fixture
def spike_data():
    spikes = np.random.rand(100, len(T)) < 0.5
    return spikes.astype(float)


def test_plot_mat(matrix_data):
    ax, cbar = plot.plot_mat(matrix_data, dt=DT, cax=True)
    assert isinstance(ax, plt.Axes)
    (ax,) = plot.plot_mat(matrix_data, dt=DT, cax=False)
    assert isinstance(ax, plt.Axes)
    (ax,) = plot.plot_mat(matrix_data, t=T, cax=False)
    assert isinstance(ax, plt.Axes)

    fig, ax = plt.subplots(1, 1)
    (ax2,) = plot.plot_mat(matrix_data, t=T, cax=False, ax=ax)
    assert ax == ax2

    fig, axes = plt.subplots(1, 2)
    ax, cbar = plot.plot_mat(matrix_data, t=T, ax=axes[0], cax=axes[1])
    assert ax == axes[0]

    fig, axes = plt.subplots(1, 2)
    ax, cbar = plot.plot_mat(
        matrix_data,
        t=T,
        y=np.arange(matrix_data.shape[0]),
        ax=axes[0],
        cax=axes[1],
        cbar_kw={"orientation": "horizontal"},
    )
    assert ax == axes[0]

    with pytest.raises(
        err.CompNeuroPlotError, match=r"Time vector .* does not have the same shape"
    ):
        ax, cbar = plot.plot_mat(matrix_data, t=[0], cax=True)

    with pytest.raises(
        err.CompNeuroPlotError, match=r"Time vector .* does not have the same shape"
    ):
        ax, cbar = plot.plot_mat(matrix_data.T, t=T, cax=True)


def test_plot_spikes(spike_data):
    ax = plot.plot_spikes(spike_data)
    assert isinstance(ax, plt.Axes)

    ax = plot.plot_spikes(spike_data, t=T)
    assert isinstance(ax, plt.Axes)

    ax = plot.plot_spikes(spike_data, dt=DT)
    assert isinstance(ax, plt.Axes)

    with pytest.raises(
        err.CompNeuroPlotError, match=r"Time vector .* does not have the same shape"
    ):
        ax = plot.plot_spikes(spike_data.T, t=[0])

    with pytest.raises(err.CompNeuroPlotError, match=r"dt must be a scalar value"):
        ax = plot.plot_spikes(spike_data.T, dt=[DT])

    with pytest.raises(err.CompNeuroPlotError, match=r"dt must be a scalar value"):
        ax = plot.plot_spikes(spike_data.T, dt=T)


def test_generate_stimulus(signal_data):
    dt, dur, t, bw, num, seed = signal_data
    step = signal.generate_stimulus("step", dt, dur, (0.2 * dur, 0.8 * dur), 100)
    para = signal.generate_stimulus("parabola", dt, dur, (0.2 * dur, 0.8 * dur), 100)
    ramp = signal.generate_stimulus("ramp", dt, dur, (0.2 * dur, 0.8 * dur), 100)

    assert len(step) == len(t)
    assert len(para) == len(t)
    assert len(ramp) == len(t)
    assert step.max() == 100
    assert para.max() == 100
    assert ramp.max() == 100

    amps = np.linspace(1, 100, num)
    step = signal.generate_stimulus("step", dt, dur, (0.2 * dur, 0.8 * dur), amps)
    para = signal.generate_stimulus("parabola", dt, dur, (0.2 * dur, 0.8 * dur), amps)
    ramp = signal.generate_stimulus("ramp", dt, dur, (0.2 * dur, 0.8 * dur), amps)

    assert step.shape == (len(amps), len(t))
    assert para.shape == (len(amps), len(t))
    assert ramp.shape == (len(amps), len(t))

    np.testing.assert_equal(step.max(axis=1), amps)
    np.testing.assert_equal(para.max(axis=1), amps)
    np.testing.assert_equal(ramp.max(axis=1), amps)


def test_generate_spike_from_psth(signal_data):
    dt, dur, t, bw, num, seed = signal_data
    rate = 100
    step = signal.generate_stimulus("step", dt, dur, (0.2 * dur, 0.8 * dur), rate)
    ss = signal.generate_spike_from_psth(dt, step, num=num, seed=seed)
    assert ss.shape == (num, len(t))
    assert np.sum(ss[:, np.logical_and(t < 0.2 * dur, t > 0.8 * dur)]) == 0
    assert np.max(np.abs(np.sum(ss, axis=1) / (0.6 * dur) - rate) / rate) < 0.2

    ss = signal.generate_spike_from_psth(dt, step, num=1, seed=seed)
    assert ss.shape == (len(t),)


def test_compute_psth(signal_data, signal_spikes):
    dt, dur, t, bw, num, seed = signal_data
    rate, ss = signal_spikes
    psth, psth_t = signal.compute_psth(ss, dt, window=2e-2, interval=1e-2)
    assert np.abs(np.mean(psth) - rate) / rate < 0.2


def test_snr(signal_data):
    dt, dur, t, bw, num, seed = signal_data

    amps = np.arange(0, 100, num)
    step = signal.generate_stimulus("step", dt, dur, (0.2 * dur, 0.8 * dur), amps)
    snr_inf = signal.snr(step, step)
    assert snr_inf.shape == step.shape
    assert np.all(snr_inf == np.inf)


def test_random_signal(signal_data):
    dt, dur, t, bw, num, seed = signal_data
    sig = signal.random_signal(t, bw, num, seed=seed)
    assert sig.shape == (num, len(t))

    # test Power
    for v in np.mean(sig ** 2, axis=-1):
        assert np.abs(v - 1) < 1e-10

    # test Bandwidth

    # test seed
    sig2 = signal.random_signal(t, bw, num, seed=seed)
    np.testing.assert_equal(sig, sig2)

    # test RNG
    rng = np.random.RandomState(seed)
    sig1_1 = signal.random_signal(t, bw, num, seed=rng)
    sig1_2 = signal.random_signal(t, bw, num, seed=rng)
    sig1_3 = signal.random_signal(t, bw, num, seed=rng)
    rng = np.random.RandomState(seed)
    sig2_1 = signal.random_signal(t, bw, num, seed=rng)
    sig2_2 = signal.random_signal(t, bw, num, seed=rng)
    sig2_3 = signal.random_signal(t, bw, num, seed=rng)
    np.testing.assert_equal(sig1_1, sig2_1)
    np.testing.assert_equal(sig1_2, sig2_2)
    np.testing.assert_equal(sig1_3, sig2_3)


def test_spikes_detect():
    volt = np.array([0.0, 1.0, 0.0, 0.0, 5.0, 2.0, 0.0])
    mask_ref = np.array([False, True, False, False, True, False, False])
    mask = signal.spike_detect(volt)
    np.testing.assert_equal(mask_ref, mask)

    volt = np.array([0.0, 1.0, 0.0, 0.0, 5.0, 2.0, 0.0])
    mask_ref = np.array([False, False, False, False, True, False, False])
    mask = signal.spike_detect(volt, threshold=2.0)
    np.testing.assert_equal(mask_ref, mask)

    volt = np.array(
        [[0.0, 1.0, 0.0, 0.0, 5.0, 2.0, 0.0], [0.0, 0.0, 5.0, 0.0, 0.0, 2.0, 0.0]]
    )
    mask_ref = np.array(
        [
            [False, True, False, False, True, False, False],
            [False, False, True, False, False, True, False],
        ]
    )
    mask = signal.spike_detect(volt)
    np.testing.assert_equal(mask_ref, mask)
