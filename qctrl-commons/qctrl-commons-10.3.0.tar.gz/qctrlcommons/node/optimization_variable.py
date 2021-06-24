# Copyright 2021 Q-CTRL. All rights reserved.
#
# Licensed under the Q-CTRL Terms of service (the "License"). Unauthorized
# copying or use of this file, via any medium, is strictly prohibited.
# Proprietary and confidential. You may not use this file except in compliance
# with the License. You may obtain a copy of the License at
#
#      https://q-ctrl.com/terms
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS. See the
# License for the specific language.
"""
Module for OptimizationVariableNode.
"""
import forge

from qctrlcommons.exceptions import QctrlException
from qctrlcommons.node import types
from qctrlcommons.node.base import Node
from qctrlcommons.node.deprecation import deprecated_node
from qctrlcommons.node.node_data import TensorNodeData


class OptimizationVariable(Node):
    r"""
    Creates optimization variables, which can be bounded, semi-bounded, or unbounded.

    Use this function to create a sequence of variables that can be tuned by
    the optimizer (within specified bounds) in order to minimize the cost
    function.

    Parameters
    ----------
    count : int
        The number :math:`N` of individual real-valued variables to create.
    lower_bound : float
        The lower bound :math:`v_\mathrm{min}` for generating an initial value for the variables.
        This will also be used as lower bound if the variables are lower bounded.
        The same lower bound applies to all `count` individual variables.
    upper_bound : float
        The upper bound :math:`v_\mathrm{max}` for generating an initial value for the variables.
        This will also be used as upper bound if the variables are upper bounded.
        The same upper bound applies to all `count` individual variables.
    is_lower_unbounded : bool, optional
        Defaults to False. Set this flag to `True` to define a semi-bounded variable with
        lower bound :math:`-\infty`; in this case, the `lower_bound` parameter is used only for
        generating an initial value.
    is_upper_unbounded : bool, optional
        Defaults to False. Set this flag to True to define a semi-bounded variable with
        upper bound :math:`+\infty`; in this case, the `upper_bound` parameter is used only for
        generating an initial value.
    name : str, optional
        The name of the node.

    Returns
    -------
    Tensor
        The sequence :math:`\{v_n\}` of :math:`N` optimization variables. If both
        `is_lower_unbounded` and `is_upper_unbounded` are `False`, these variables are
        bounded such that :math:`v_\mathrm{min}\leq v_n\leq v_\mathrm{max}`. If one of the
        flags is `True` (for example `is_lower_unbounded=True`), these variables are
        semi-bounded (for example :math:`-\infty \leq v_n \leq v_\mathrm{max}`).
        If both of them are `True`, then these variables are unbounded and satisfy that
        :math:`-\infty \leq v_n \leq +\infty`.

    See Also
    --------
    anchored_difference_bounded_variables : Create anchored optimization variables
        with a difference bound.
    :func:`~qctrl.dynamic.namespaces.FunctionNamespace.calculate_optimization` : Find the minimum
        of a generic function.
    """

    name = "optimization_variable"
    optimizable_variable = True
    args = [
        forge.arg("count", type=int),
        forge.arg("lower_bound", type=float),
        forge.arg("upper_bound", type=float),
        forge.arg("is_lower_unbounded", type=bool, default=False),
        forge.arg("is_upper_unbounded", type=bool, default=False),
    ]
    rtype = types.Tensor

    @classmethod
    def create_node_data(cls, _operation, **kwargs):
        count = kwargs["count"]
        lower_bound = kwargs["lower_bound"]
        upper_bound = kwargs["upper_bound"]
        if count <= 0:
            raise QctrlException(f"count={count} must be positive.")
        if upper_bound <= lower_bound:
            raise QctrlException(
                f"lower_bound={lower_bound} must be less than upper_bound={upper_bound}."
            )
        return TensorNodeData(_operation, shape=(count,))


@deprecated_node("optimization_variable")
class BoundedOptimizationVariableDeprecated(Node):
    """Deprecated node."""

    name = "bounded_optimization_variable"
    optimizable_variable = True
    args = [
        forge.arg("count", type=int),
        forge.arg("lower_bound", type=float),
        forge.arg("upper_bound", type=float),
    ]
    rtype = types.Tensor

    @classmethod
    def create_node_data(cls, _operation, **kwargs):
        count = kwargs["count"]
        lower_bound = kwargs["lower_bound"]
        upper_bound = kwargs["upper_bound"]
        if count <= 0:
            raise QctrlException(f"count={count} must be positive.")
        if upper_bound <= lower_bound:
            raise QctrlException(
                f"lower_bound={lower_bound} must be less than upper_bound={upper_bound}."
            )
        return TensorNodeData(_operation, shape=(count,))


@deprecated_node("optimization_variable")
class UnboundedOptimizationVariableDeprecated(Node):
    """Deprecated node."""

    name = "unbounded_optimization_variable"
    optimizable_variable = True
    args = [
        forge.arg("count", type=int),
        forge.arg("initial_lower_bound", type=float),
        forge.arg("initial_upper_bound", type=float),
    ]
    rtype = types.Tensor

    @classmethod
    def create_node_data(cls, _operation, **kwargs):
        count = kwargs["count"]
        initial_lower_bound = kwargs["initial_lower_bound"]
        initial_upper_bound = kwargs["initial_upper_bound"]
        if count <= 0:
            raise QctrlException(f"count={count} must be positive.")
        if initial_upper_bound <= initial_lower_bound:
            raise QctrlException(
                f"initial_lower_bound={initial_lower_bound} must be less than "
                f"initial_upper_bound={initial_upper_bound}."
            )
        return TensorNodeData(_operation, shape=(count,))
