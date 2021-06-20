import pytest
import numpy as np
from collections import OrderedDict
from scipy.integrate import solve_ivp, cumtrapz
from compneuro.base_model import BaseModel
from compneuro.errors import CompNeuroModelError


class DummyNeuron(BaseModel):
    Default_Params = OrderedDict(a=1.0, b=0.1)
    Default_States = OrderedDict(x1=0.0, x2=(1.0, 0.0, 10.0))

    def ode(self, t, states, I_ext=None):
        x1, x2 = states
        d_x1 = -x1 * self.params["a"]
        d_x2 = I_ext
        return np.vstack([d_x1, d_x2])


def res_ref(neuron: DummyNeuron, t: np.ndarray, I_ext: np.ndarray):
    return (
        neuron.states["x1"][:, None] * np.exp(-np.outer(neuron.params["a"], t)),
        np.atleast_2d(np.cumsum(I_ext, axis=0).T * (t[1] - t[0]))
        + neuron.states["x2"][:, None],
    )


def test_neuron_init():
    neuron = DummyNeuron(a=10.0)
    assert neuron.params["a"] == 10.0
    assert neuron.states["x1"] == np.array([0.0])
    assert neuron.states["x2"] == np.array([1.0])
    assert neuron.bounds["x2"][0] == 0.0
    assert neuron.bounds["x2"][1] == 10.0
    assert neuron.bounds["x1"] is None
    np.testing.assert_equal(neuron._state_vec, np.array([[0.0], [1.0]]))

    neuron = DummyNeuron(a=10.0, num=10)
    assert neuron.params["a"] == 10.0
    np.testing.assert_equal(neuron.states["x1"], np.full((10,), 0.0))
    np.testing.assert_equal(neuron.states["x2"], np.full((10,), 1.0))
    assert neuron.bounds["x2"][0] == 0.0
    assert neuron.bounds["x2"][1] == 10.0
    assert neuron.bounds["x1"] is None
    np.testing.assert_equal(
        neuron._state_vec, np.vstack([np.full((10,), 0.0), np.full((10,), 1.0)])
    )


def test_neuron_ode():
    neuron = DummyNeuron(a=10.0, x1=10.0)
    grad = neuron.ode(t=0.0, states=neuron._state_vec, I_ext=0.0)
    np.testing.assert_equal(grad, np.vstack([-neuron.states["x1"] * 10.0, 0.0]))


def test_neuron_solve():
    dt = 1e-4
    t = np.arange(0, 0.1, dt)
    np.random.seed(0)
    I_ext = np.clip(np.random.randn(*t.shape), 0, None)
    neuron = DummyNeuron(num=1, a=1.0, x1=10.0)
    x1_ref, x2_ref = res_ref(neuron, t, I_ext)

    res = neuron.solve(t, I_ext=I_ext, solver="Euler")
    assert res["x1"].shape == (1, len(t))
    assert res["x2"].shape == (1, len(t))
    np.testing.assert_allclose(x1_ref, res["x1"], atol=1e-2, rtol=1e-2)
    np.testing.assert_allclose(x2_ref, res["x2"], atol=1e-2, rtol=1e-2)

    res2 = neuron.solve(t, I_ext=I_ext, solver="lsoda")
    assert res2["x1"].shape == (1, len(t))
    assert res2["x2"].shape == (1, len(t))
    np.testing.assert_allclose(res["x1"], res2["x1"], atol=1e-2, rtol=1e-2)
    np.testing.assert_allclose(res["x2"], res2["x2"], atol=1e-2, rtol=1e-2)

    neuron = DummyNeuron(num=10, a=10.0, x1=10.0)
    res = neuron.solve(t, I_ext=I_ext, solver="RK45", rtol=1e-5)
    x1_ref, x2_ref = res_ref(neuron, t, I_ext)
    assert res["x1"].shape == (10, len(t))
    assert res["x2"].shape == (10, len(t))
    # check to make sure all components respond similarly
    np.testing.assert_array_almost_equal(res["x1"].std(0), 0)
    np.testing.assert_array_almost_equal(res["x2"].std(0), 0)
    np.testing.assert_allclose(x1_ref, res["x1"], atol=1e-2, rtol=1e-2)
    np.testing.assert_allclose(x2_ref, res["x2"], atol=1e-2, rtol=1e-2)

    I_ext = np.clip(np.random.randn(len(t), 10), 0, None)
    res = neuron.solve(t, I_ext=I_ext, solver="lsoda")
    assert res["x1"].shape == (10, len(t))
    assert res["x2"].shape == (10, len(t))
    x1_ref, x2_ref = res_ref(neuron, t, I_ext)
    np.testing.assert_allclose(x1_ref, res["x1"], atol=1e-2, rtol=1e-2)
    np.testing.assert_allclose(x2_ref, res["x2"], atol=1e-2, rtol=1e-2)

    # check I_ext dimensionality
    num = 10
    neuron = DummyNeuron(num=num)
    # 1. If I_ext is 1D, it should work with anything
    I_ext = np.random.randn(
        len(t),
    )
    neuron.solve(t, I_ext=I_ext, solver="Euler")
    neuron.solve(t, I_ext=I_ext, solver="odeint")
    neuron.solve(t, I_ext=I_ext, solver="RK45")
    # 2. If I_ext is 2D, it must have the right shape
    I_ext = np.random.randn(len(t), num)
    neuron.solve(t, I_ext=I_ext, solver="Euler")
    neuron.solve(t, I_ext=I_ext, solver="odeint")
    neuron.solve(t, I_ext=I_ext, solver="RK45")
    # 3. If I_ext is 2D, it must have the right shape
    I_ext = np.random.randn(len(t), num + 1)
    with pytest.raises(CompNeuroModelError, match=r".* expecting shape .*"):
        neuron.solve(t, I_ext=I_ext, solver="Euler")
    with pytest.raises(CompNeuroModelError, match=r".* expecting shape .*"):
        neuron.solve(t, I_ext=I_ext, solver="odeint")
    with pytest.raises(CompNeuroModelError, match=r".* expecting shape .*"):
        neuron.solve(t, I_ext=I_ext, solver="RK45")
    # 4. If I_ext is not 1 or 2D, it will error
    I_ext = np.random.randn(len(t), 2, num + 1)
    with pytest.raises(CompNeuroModelError, match=r".* must be 1D or 2D"):
        neuron.solve(t, I_ext=I_ext, solver="Euler")
