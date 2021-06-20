# pylint:disable=C0103
"""Base Class for ODE-based Models
"""
import numpy as np
from numpy.core.numeric import full
from tqdm.auto import tqdm  # pylint:disable=F0002
from warnings import warn
from collections import OrderedDict
from numpy.core.fromnumeric import var
from scipy.integrate import solve_ivp, odeint
from scipy.integrate._ivp.base import OdeSolver
from scipy.interpolate import interp1d
from . import errors as err
from . import types as tpe


class BaseModel:
    """Base Model Class

    This base class is an opinionated implementation of ODE-based models
    for Comp Neuro.

    Attributes:
        Time_Scale: scaling for the time-step :code:`dt`. For models that
            must be simulated on a milisecond scale, set to :code:`1000.`
        Default_Params: a dictionary of (name, value) pair for parameters
        Default_States: a dictionary of state variables where each entry is either
            - scalar: initial value of state variable
            - 3 tuple: (initial value, min, max) of the state variable

    .. warning::
        Due to a lack of variable bounding API in scipy, bounding variables
        are currently only available for :code:`Euler` method when solving
        ODEs.

    Methods:
        ode: compute gradient of model given current states and input
        solve: solve model output for given input signal

    Arguments:
        num: number of state variables to simulate simultaneously
        kwargs: keyword arguments that overwrite initial conditions of state
            variables and values of parameters
    """

    Time_Scale: float = 1.0
    Default_Params = OrderedDict()
    Default_States = OrderedDict()

    def __init__(self, num: int = 1, **kwargs):
        if not isinstance(self.Default_States, OrderedDict):
            warn(
                "States need to be OrderedDict to maintain variable ordering, "
                "converting..."
            )
            self.Default_States = OrderedDict(self.Default_States)

        duplicate_vars = set(self.Default_Params.keys()).intersection(
            set(self.Default_States.keys())
        )
        if len(duplicate_vars) > 0:
            raise err.CompNeuroModelError(
                f"Params and States cannot duplicate names: {duplicate_vars}"
            )
        self.num = num
        self.params = OrderedDict(self.Default_Params.copy())
        self.states = OrderedDict()
        self.initial_states = OrderedDict()
        self.bounds = OrderedDict()

        for var_name, var_val in self.Default_States.items():
            var_val = np.atleast_1d(var_val)
            if len(var_val) == 1:
                self.initial_states[var_name] = var_val[[0]].copy()
                self.states[var_name] = var_val[[0]].copy()
                self.bounds[var_name] = None
            elif len(var_val) == 3:
                self.initial_states[var_name] = var_val[[0]].copy()
                self.states[var_name] = var_val[[0]].copy()
                self.bounds[var_name] = var_val[1:].copy()
            else:
                raise err.CompNeuroModelError(
                    f"Expect state variable {var_name} to have length 1 or 3, "
                    f"got {len(var_val)}"
                )

        for key, val in kwargs.items():
            if key in self.params:
                self.params[key] = val
            elif key in self.states:
                self.states[key] = val
                self.initial_states[key] = val
            else:
                raise err.CompNeuroModelError(f"Unrecognized argument {key}")
        self.__check_dimensions()

    def reset(self) -> None:
        """Reset Initial Values of the System"""
        for var_name, var_val in self.initial_states.items():
            var_val = np.atleast_1d(var_val)
            self.states[var_name] = var_val.copy()

    @property
    def _state_vec(self) -> np.ndarray:
        return np.vstack(list(self.states.values()))

    @_state_vec.setter
    def _state_vec(self, new_value) -> None:
        for var_name, new_val in zip(self.states.keys(), new_value):
            self.states[var_name] = new_val

    def __check_dimensions(self):
        for key, val in self.params.items():
            if np.isscalar(val):
                continue
            else:
                if len(val) == 1:
                    self.params[key] = np.repeat(val, self.num)
                else:
                    if len(val) != self.num:
                        raise err.CompNeuroModelError(
                            f"Parameter '{key}'' should have scalar value or array of "
                            f"length num={self.num}, got {len(val)} instead."
                        )
        for key, val in self.states.items():
            if np.isscalar(val):
                self.states[key] = np.full((self.num,), val)
            else:
                if len(val) == 1:
                    self.states[key] = np.repeat(val, self.num)
                else:
                    if len(val) != self.num:
                        raise err.CompNeuroModelError(
                            f"State '{key}' should have scalar value or array of "
                            f"length num={self.num}, got {len(val)} instead."
                        )

        for key, val in self.initial_states.items():
            if np.isscalar(val):
                self.initial_states[key] = np.full((self.num,), val)
            else:
                if len(val) == 1:
                    self.initial_states[key] = np.repeat(val, self.num)
                else:
                    if len(val) != self.num:
                        raise err.CompNeuroModelError(
                            f"Initial State '{key}' should have scalar value or array of "
                            f"length num={self.num}, got {len(val)} instead."
                        )

    def ode(self, t: float, states: np.ndarray, I_ext: float = None) -> np.ndarray:
        """Definition of Differential Equation

        .. note::

            For dynamical models described by ODEs, the function
            definition of the model should be of the form :math:`dx/dt=f(t,x)`,
            where :math:`x` is usually a vector variable that describes
            the current state values at which the gradient is evaluted, and
            :math:`t` is the current time. Also note that :code:`t` is required
            to be compatible with scipy ode solver's API, although it is not
            needed for `autonomous` ODEs.

        .. seealso:: :py:mod:`scipy.integrate.solve_ivp`
            and :py:mod:`scipy.integrate.odeint`

        Arguments:
            t: current time value
            states: vector of state variable
            I_ext: external input current, optional

        Returns:
            A vector of gradient value evaluated based on the
            model dynamics. Should have the same shape as the
            states input vector.
        """

    def _ode_update(self, t: float, y: np.ndarray, *args, **kwargs) -> np.ndarray:
        """The actual update function that is passed to ode solvers"""

    def solve(
        self,
        t: np.ndarray,
        I_ext: np.ndarray = None,
        solver: tpe.solvers = "Euler",
        reset_initial_state: bool = True,
        verbose: bool = True,
        full_output: bool = False,
        **solver_kws,
    ) -> np.ndarray:
        """Solve model equation for entire input

        Arguments:
            t: 1d numpy array of time vector of the simulation
            I_ext: 1d/2d numpy array of external input current of shape
                - 1D: :code:`(len(t),)`, where the same input is shared for all
                    model instances.
                - 2D: :code:`(len(t), num)` where :code:`num` is the number
                    of components to simulate. The value `num` must be equal
                    to the `self.num` value.
            solver: Which ODE solver to use, defaults to Euler which uses
                custom forward euler solver.

                - 'Euler': Custom forward euler solver, default.
                - 'odeint': Use :py:mod:`scipy.integrate.odeint` which uses
                    LSODA
                - 'LSODA': Use :py:mod:`scipy.integrate.odeint` which uses
                    LSODA
                - 'RK45/RK23/DOP853/Radu/BDF': Use
                    :py:mod:`scipy.integrate.solve_ivp` with the specified
                    method
                - scipy.integrate.OdeSolver instace: Use
                    :py:mod:`scipy.integrate.solve_ivp` with the provided
                    custom solver

            reset_initial_state: whether to reset the initial state value of the
                model to the values in :code:`Default_State`. Default to True.
            verbose: whether to show progress
            full_output: whether to return the entire output from scipy's
                    ode solvers.

        .. note::

            String names for :code:`solve_ivp` are case-sensitive
            but not for any other methods.


        Keyword Arguments:
            solver_kws: arguments to be passed into the ode solvers if scipy
                solvers are used.

                .. seealso: :py:mod:`scipy.integrate.solve_ivp` and
                    :py:mod:`scipy.integrate.odeint`

        Returns:
            Return dictionary of a 2-tuple depending on argument
            :code:`full_output`:

            - :code:`False`: An dictionary of simulation results keyed by
                state variables and each entry is of shape :code:`(num, len(t))`
            - :code:`True`: A 2-tuple where the first entry is as above, and
                the second entry is the ode result from either
                :py:mod:`scipy.integrate.odeint` or
                :py:mod:`scipy.integrate.solve_ivp`.
                The second entry will be :code:`None` if solver is :code:`Euler`
        """
        if reset_initial_state:
            self.reset()

        t_long = t * self.Time_Scale
        d_t = t_long[1] - t_long[0]

        if verbose:
            pbar = tqdm(total=len(t_long))

        if I_ext is not None:
            if I_ext.ndim == 1:
                I_ext = np.repeat(I_ext[:, None], self.num, axis=-1)
            elif I_ext.ndim != 2:
                raise err.CompNeuroModelError("I_ext must be 1D or 2D")
            if len(I_ext) != len(t):
                raise err.CompNeuroModelError(
                    "I_ext's first dimesion must be the same length as t"
                )
            if I_ext.shape[1] > 1:
                if I_ext.shape != (len(t_long), self.num):
                    raise err.CompNeuroModelError(
                        f"I_ext expecting shape ({len(t_long)},{self.num}), "
                        f"got {I_ext.shape}"
                    )

        ode_res_info = None
        if solver.lower() == "euler":
            res = np.zeros((len(t_long), len(self._state_vec), self.num))
            res[0] = self._state_vec
            if I_ext is not None:
                for tt, (_I, _t) in enumerate(zip(I_ext[:-1], t_long[:-1])):
                    d_x = self.ode(states=self._state_vec, I_ext=_I, t=_t)
                    self._state_vec += d_t * d_x
                    self.clip()
                    res[tt + 1] = self._state_vec
                    if verbose:
                        pbar.update()
            else:
                for tt, _t in enumerate(t_long[:-1]):
                    d_x = self.ode(states=self._state_vec, t=_t)
                    self._state_vec += d_t * d_x
                    self.clip()
                    res[tt + 1] = self._state_vec
                    if verbose:
                        pbar.update()
            res = np.moveaxis(res, 0, 2)
        else:
            state_var_shape = self._state_vec.shape
            x0 = np.ravel(self._state_vec)

            # if system receives external input
            if I_ext is not None:
                interp_f = interp1d(
                    t_long, I_ext, axis=0, kind="zero", fill_value="extrapolate"
                )

                def update(t_eval, states):
                    if verbose:
                        pbar.n = int(t_eval // d_t)
                        pbar.update()
                    I_ext_t = interp_f(t_eval)
                    return self.ode(
                        states=np.reshape(states, state_var_shape),
                        I_ext=I_ext_t,
                        t=t_eval,
                    ).ravel()

            else:

                def update(t_eval, states):
                    if verbose:
                        pbar.n = int(t_eval // d_t)
                        pbar.update()
                    return self.ode(
                        states=np.reshape(states, state_var_shape), t=t_eval
                    ).ravel()

            self._ode_update = update
            if isinstance(solver, OdeSolver):
                rtol = solver_kws.pop("rtol", 1e-8)
                ode_res = solve_ivp(
                    self._ode_update,
                    t_span=(t_long.min(), t_long.max()),
                    y0=x0,
                    t_eval=t_long,
                    method=solver,
                    rtol=rtol,
                )
                ode_res_info = ode_res
                res = ode_res.y.reshape((len(self._state_vec), -1, len(t)))
            elif solver.lower() in ["lsoda", "odeint"]:
                ode_res = odeint(
                    self._ode_update,
                    y0=x0,
                    t=t_long,
                    tfirst=True,
                    full_output=full_output,
                    **solver_kws,
                )
                if full_output:
                    ode_res_y = ode_res[0]
                    ode_res_info = ode_res[1]
                    res = ode_res_y.T.reshape((len(self._state_vec), -1, len(t)))
                else:
                    res = ode_res.T.reshape((len(self._state_vec), -1, len(t)))
            else:
                rtol = solver_kws.pop("rtol", 1e-8)
                ode_res = solve_ivp(
                    self._ode_update,
                    t_span=(t_long.min(), t_long.max()),
                    y0=x0,
                    t_eval=t_long,
                    method=solver,
                    rtol=rtol,
                )
                ode_res_info = ode_res
                res = ode_res.y.reshape((len(self._state_vec), -1, len(t_long)))

        if verbose:
            pbar.close()

        res = OrderedDict({key: res[n] for n, key in enumerate(self.states.keys())})
        if full_output:
            return res, ode_res_info
        return res

    def clip(self) -> None:
        """Clip state variables based on bounds"""
        for var_name, var_val in self.states.items():
            if self.bounds[var_name] is None:
                continue
            self.states[var_name] = np.clip(
                var_val, self.bounds[var_name][0], self.bounds[var_name][1]
            )
