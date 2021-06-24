# Copyright 2020 Q-CTRL Pty Ltd & Q-CTRL Inc. All rights reserved.
#
# Licensed under the Q-CTRL Terms of service (the "License"). Unauthorized
# copying or use of this file, via any medium, is strictly prohibited.
# Proprietary and confidential. You may not use this file except in compliance
# with the License. You may obtain a copy of the License at
#
#     https://q-ctrl.com/terms
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS. See the
# License for the specific language.
"""Module for all the nodes related to stochastic simulation and optimization."""
from typing import (
    List,
    Optional,
    Tuple,
    Union,
)

import forge
import numpy as np

from qctrlcommons.node import types
from qctrlcommons.node.base import Node
from qctrlcommons.node.node_data import StfNodeData
from qctrlcommons.preconditions import (
    check_argument,
    check_argument_integer,
    check_argument_positive_scalar,
    check_argument_real_vector,
)


class RandomColoredNoiseStfSignal(Node):
    r"""
    Samples the one-sided power spectral density (PSD) of a random noise process in the
    time domain and returns the resultant noise trajectories as an `Stf`.

    Parameters
    ----------
    power_spectral_density : np.ndarray or Tensor (1D, real)
        The one-sided power spectral density of the noise sampled at frequencies
        :math:`\{0, \Delta f, 2\Delta f, \ldots , M\Delta f\}`.
    frequency_step : float
        The step size :math:`\Delta f` of power spectrum densities samples
       `power_spectral_density`. Must be a strictly positive number.
    batch_shape : Union[List[int], Tuple[int]], optional
        The batch shape of the returned Stf. By default, the batch shape is (), that is,
        the returned Stf represents only one noise trajectory. If the batch shape is
        `(m,n,...)`, the returned Stf represents `m*n*...` trajectories arranged in
        this batch shape.
    seed : int, optional
        A seed for the random number generator used for sampling. When set, same
        trajectories are produced on every run of this function, provided all the other
        arguments also remain unchanged. Defaults to ``None``, in which case the
        generated noise trajectories can be different from one run to another.

    Returns
    -------
    Stf
        An `Stf` signal representing the noise trajectories in the time domain. The
        batch shape of this `Stf` is same as the argument `batch_shape`.

    Notes
    -----
    Given a frequency step size of :math:`\Delta f` and discrete samples
    :math:`P[k] = P(k\Delta f)` of a one-sided power spectral density function
    :math:`P(f)`, the output is a possibly batched Stf which represents one random
    realization of the random noise process. Each such trajectory is periodic with a
    time period of :math:`1/\Delta f`.
    """
    name = "random_colored_noise_stf_signal"

    args = [
        forge.arg("power_spectral_density", type=Union[np.ndarray, types.Tensor]),
        forge.arg("frequency_step", type=float),
        forge.arg("batch_shape", type=Union[List[int], Tuple[int]], default=()),
        forge.arg("seed", type=Optional[int], default=None),
    ]
    kwargs = {}  # Stfs don't accept name as an argument.
    rtype = types.Stf

    @classmethod
    def create_node_data(cls, _operation, **kwargs):
        power_spectral_density = kwargs.get("power_spectral_density")
        frequency_step = kwargs.get("frequency_step")
        batch_shape = kwargs.get("batch_shape")
        seed = kwargs.get("seed")

        check_argument_real_vector(power_spectral_density, "power_spectral_density")
        check_argument_positive_scalar(frequency_step, "frequency_step")
        check_argument(
            isinstance(batch_shape, (list, tuple))
            and all(isinstance(x, int) and x > 0 for x in batch_shape),
            "batch_shape should be a list or a tuple of positive integers.",
            {"batch_shape": batch_shape},
        )
        if seed is not None:
            check_argument_integer(seed, "seed")

        return StfNodeData(
            _operation,
            value_shape=(),
            batch_shape=batch_shape,
        )
