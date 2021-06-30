"""
This file is part of Apricopt.

Apricopt is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

Apricopt is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with Apricopt.  If not, see <http://www.gnu.org/licenses/>.

Copyright (C) 2020-2021 Marco Esposito, Leonardo Picchiami.
"""

from abc import abstractmethod, ABC
from typing import Dict, List


class BlackBox(ABC):
    @abstractmethod
    def evaluate(self, parameters: Dict[str, float]) -> Dict[str, float]:
        """
        Evaluate the black box over the given assignment of the parameters.
        :param parameters:
        :return:
        """

    @abstractmethod
    def get_optimization_parameters_number(self) -> int:
        """
        Returns the number of parameters to be optimized.
        :return: an integer representing the number of optimization parameters.
        """
        pass

    @abstractmethod
    def get_optimization_parameters_ids(self) -> List[str]:
        """
        Returns the identifiers of the optimization parameters as a list of strings.
        The order in which the identifiers appear in the list should be consistent among multiple calls.
        :return: a list of strings representing the identifiers of the optimization parameters, in some fixed order.
        """
        pass

    @abstractmethod
    def get_optimization_parameter_lower_bound(self, param_id) -> float:
        """
        Returns the lower bound of the optimization parameter with the given identifier.
        :param param_id: the identifier of the parameter.
        :return: a float representing the lower bound of the optimization parameter with the given identifier.
        """
        pass

    @abstractmethod
    def get_optimization_parameter_upper_bound(self, param_id) -> float:
        """
        Returns the upper bound of the optimization parameter with the given identifier.
        :param param_id: the identifier of the parameter.
        :return: a float representing the upper bound of the optimization parameter with the given identifier.
        """
        pass

    @abstractmethod
    def get_optimization_parameter_initial_value(self, param_id) -> float:
        """
        Returns the initial_value of the optimization parameter with the given identifier.
        :param param_id: the identifier of the parameter.
        :return: a float representing the initial_value of the optimization parameter with the given identifier.
        """
        pass

    @abstractmethod
    def set_optimization_parameters_initial_values(self, param_values: Dict[str, float]) -> None:
        """
        Sets the initial_values of the optimization parameters in the dictionary with the given values.
        :param param_values: a dictionary that maps valid parameter identifiers to values.
        :return: None.
        """
        pass

    @abstractmethod
    def get_optimization_parameter_granularity(self, param_id) -> float:
        """
        Returns the granularity of the optimization parameter with the given identifier.
        If the parameter has no granularity, i.e. it should be optimized over a continuous domain, this
        method should return 0 (zero).
        :param param_id: the identifier of the parameter.
        :return: a float representing the granularity of the optimization parameter with the given identifier. If
        the parameter has no granularity, returns 0.
        """
        pass

    @abstractmethod
    def get_extreme_barrier_constraints_number(self) -> int:
        """
        Returns the number of extreme barrier constraints, i.e. the number of constraints that define the optimization
        space. If any of the extreme barrier constraints is violated, the point is considered as invalid by the solver
        in the optimization.
        :return: a non-negative int representing the number of extreme barrier constraints.
        """
        pass

    @abstractmethod
    def get_progressive_barrier_constraints_number(self) -> int:
        """
        Returns the number of progressive barrier constraints, i.e. the number of constraints that define the space
        of feasible solutions. If a progressive barrier constraints is violated, the point is still considered as valid
        by the solver and used in the optimization process.
        :return: a non-negative int representing the number of progressive barrier constraints.
        """
        pass

    @abstractmethod
    def get_extreme_barrier_constraints_ids(self) -> List[str]:
        """
        Returns the identifiers of extreme barrier constraints, i.e. the constraints that define the optimization
        space. If any of the extreme barrier constraints is violated, the point is considered as invalid by the solver
        in the optimization.
        The order in which the identifiers are returned in the list must be consistent among all method calls.
        :return: a list of strings representing the identifiers of extreme barrier constraints.
        """
        pass

    @abstractmethod
    def get_progressive_barrier_constraints_ids(self) -> List[str]:
        """
        Returns the identifiers of progressive barrier constraints, i.e. the constraints that define the space
        of feasible solutions. If a progressive barrier constraints is violated, the point is still considered as valid
        by the solver and used in the optimization process.
        The order in which the identifiers are returned in the list must be consistent among all method calls.
        :return: a list of strings representing the identifiers of progressive barrier constraints.
        """
        pass

    @abstractmethod
    def get_objective_id(self) -> str:
        """
        Returns an identifier for the objective value. It must be different from any of the identifiers
        of the parameters.
        :return: A string representing an identifier for the objective value.
        """
        pass

    @abstractmethod
    def get_objective_upper_bound(self) -> float:
        pass

    @staticmethod
    @abstractmethod
    def get_raisable_exception_type():
        return Exception

    @abstractmethod
    def finalize(self) -> None:
        """
        Performs all needed operations to finalize the black box.
        This method is invoked by BlackBoxSolver at the end of the optimization.
        :return:
        """
        pass

