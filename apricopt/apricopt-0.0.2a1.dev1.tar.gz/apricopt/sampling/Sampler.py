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

from apricopt.model.Model import Model
from apricopt.model.Parameter import Parameter
from apricopt.simulation.SimulationEngine import SimulationEngine
from typing import Dict, List
import numpy as np


class Sampler:
    def __init__(self, model: Model, sim_engine: SimulationEngine, horizon: float):
        self.model = model
        self.sim_engine = sim_engine
        self.horizon = horizon

    def random_sampling_admissible_parameter_with_respect_constraints(self) -> Dict[str, float]:
        sampled_parameters = self.parameters_random_sampling()
        self.model.set_fixed_params(sampled_parameters)
        evaluated_constraints = self.sim_engine.simulate(self.model, self.horizon)
        admissible = all(evaluated_constraints[constraint.id] <= 0 for constraint in self.model.constraints)
        while not admissible:
            sampled_parameters = self.parameters_random_sampling()
            self.model.set_fixed_params(sampled_parameters)
            evaluated_constraints = self.sim_engine.simulate(self.model, self.horizon)
            admissible = all(evaluated_constraints[constraint.id] <= 0 for constraint in self.model.constraints)
        return sampled_parameters

    def random_sampling_admissible_parameter_with_respect_fast_constraints(self) -> Dict[str, float]:
        pass

    def random_sampling_admissible_parameter_with_respect_all_constraints(self) -> Dict[str, float]:
        pass

    def parameters_random_sampling(self) -> Dict[str, float]:
        parameters: List[Parameter] = list(self.model.parameters.values())
        parameters.sort(key=lambda x: x.id)
        sample = np.random.rand(len(parameters))
        sampled_parameters: Dict[str, float] = dict()
        for i in range(len(parameters)):
            param = parameters[i]
            if param.distribution == 'uniform':
                sampled_parameters[param.id] = \
                    round(param.lower_bound + (
                            param.upper_bound - param.lower_bound) * sample[i])
        return sampled_parameters

