import operator

import numpy as np

from pymtsp.engine.city import City
from pymtsp.engine.depot import Depot
from pymtsp.engine.salesman import calc_dist, Salesman
from pymtsp.engine.status import CityStatus, SalesmanStatus


def filter_dict(info: dict, status, return_idx=True):
    ret = dict(filter(lambda elem: elem[1].status == status, info.items()))
    if return_idx:
        ret = list(ret.keys())
    return ret


class mTSPManager:

    def __init__(self,
                 m: int,
                 coords: np.array):
        super(mTSPManager, self).__init__()

        self.n = coords.shape
        self.n_cities = coords.shape[0] - 1
        self.m = m
        self.coords = coords

        self.depot = Depot(idx=0, loc=coords[0])
        self.cities = {_n + 1: City(idx=_n + 1, loc=coords[_n + 1]) for _n in range(self.n_cities)}
        self.salesmen = {_m: Salesman(idx=_m, first_city=self.depot) for _m in range(self.m)}
        self.time = 0.0
        self.target_agent = None

    def get_idle_agents(self, return_idx=True):
        return filter_dict(self.salesmen, SalesmanStatus.IDLE, return_idx)

    def get_assigned_agents(self, return_idx=True):
        return filter_dict(self.salesmen, SalesmanStatus.ASSIGNED, return_idx)

    def get_inactive_agents(self, return_idx=True):
        return filter_dict(self.salesmen, SalesmanStatus.INACTIVE, return_idx)

    def get_active_cities(self, return_idx=True):
        return filter_dict(self.cities, CityStatus.IDLE, return_idx)

    def get_inactive_cities(self, return_idx=True):
        return filter_dict(self.cities, CityStatus.INACTIVE, return_idx)

    def get_non_depot_returning_agents(self):
        return dict(filter(lambda elem: elem[1].is_returning == False, self.salesmen.items()))

    def get_depot_returning_agents(self):
        return dict(filter(lambda elem: elem[1].is_returning == True, self.salesmen.items()))

    def set_target_agent(self):
        idle_agents = self.get_idle_agents()
        assert len(idle_agents) >= 1

        if self.target_agent is not None:
            self.salesmen[self.target_agent].is_target = False

        target_idx = np.random.choice(idle_agents)
        self.salesmen[target_idx].is_target = True
        self.target_agent = target_idx

    def set_next_city(self, agent_idx, next_city_idx):
        if next_city_idx == 0:  # when salesmen choose to early depot return
            self.salesmen[agent_idx].set_next_city(self.depot)
        else:
            self.salesmen[agent_idx].set_next_city(self.cities[next_city_idx])

    def transit(self):
        # check all agents are not idle
        assert len(self.get_idle_agents()) == 0

        # find event-triggering time and simulate
        # while loop is introduced since the event-triggering time
        # can be for the depot-retuning
        dt = 0.0
        while len(self.get_idle_agents()) == 0:
            assigned_agents = self.get_assigned_agents(False)
            _dt = min([v.remaining_distance for v in assigned_agents.values()])
            for agent in assigned_agents.values():
                agent.simulate(_dt)
            dt += _dt

        self.time += dt

    def transit_last(self):
        # remaining only one unvisited city and may have multiple salesmen
        # therefore, this state-action selection is not subject of learning
        # "apply heuristics that minimally increase makespan"

        assert len(self.get_active_cities(return_idx=True)) == 1
        remaining_city = self.cities[self.get_active_cities(return_idx=True)[0]]
        non_depot_returning_agents = self.get_non_depot_returning_agents()

        def calc_remaining_cost(agent):
            finish_sub_tour = agent.remaining_distance  # to finish current subtour
            next_loc = agent.loc if finish_sub_tour == 0.0 else agent.next_city.loc
            additional_tour = calc_dist(next_loc, remaining_city.loc)  # to tour next city -> remaining city
            depot_returning = calc_dist(remaining_city.loc, self.depot.loc)  # returning to the depot
            return finish_sub_tour + additional_tour + depot_returning

        remain_cost = {k: calc_remaining_cost(v) for k, v in non_depot_returning_agents.items()}
        agent_idx = min(remain_cost.items(), key=operator.itemgetter(1))[0]

        # finish current tour and return to the depot
        for agent in non_depot_returning_agents.keys():
            # finish current tour if required
            if self.salesmen[agent].status == SalesmanStatus.ASSIGNED:
                self.salesmen[agent].simulate(self.salesmen[agent].remaining_distance)

            if agent == agent_idx:
                self.salesmen[agent].set_next_city(remaining_city)
                self.salesmen[agent].simulate(self.salesmen[agent].remaining_distance)

            # append depot
            self.salesmen[agent].set_next_city(self.depot)
            self.salesmen[agent].simulate(self.salesmen[agent].remaining_distance)

        self.time += min(remain_cost.values())
