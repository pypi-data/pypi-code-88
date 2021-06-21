import numpy as np

from pymtsp.engine.manager import mTSPManager
from pymtsp.utils.generate_coords import get_uniform_coords
from pymtsp.utils.observations import default_obs_func
from pymtsp.utils.process_tour_dict import process_tour_info
from pymtsp.utils.rewards import default_reward_func


class mTSPenv:
    """
    Single depot-returning mTSP environment.
    TODO: Adjust event index properly.
    """

    def __init__(self,
                 m: int,
                 n: int = None,
                 coords: np.array = None,
                 allow_early_return: bool = True,
                 observation_func=default_obs_func,
                 reward_func=default_reward_func,
                 verbose: bool = False):

        """
        :param m: (int) Number of salesmen. >= 1
        :param n: (int) Number of cities including the depot
        :param coords: (np.array) 2D coordinates of cities; [n x 2]
        :param allow_early_return: (bool) whether to allow salesmen return to the depot before visiting all cities.
        :param observation_func: (a callable function) observation function; f(self) -> observation
        :param verbose: (bool) For
        """

        assert n is not None or coords is not None, "Required to specify 'n' or 'coords'"

        self.m = m
        self.n = coords.shape[0] if n is None else n
        self.coords = get_uniform_coords(n) if coords is None else coords

        self.allow_early_return = allow_early_return
        self.verbose = verbose
        self.observation_func = observation_func
        self.reward_func = reward_func

        self.manager = None
        self.event_counter = 0
        self.done = False
        _ = self.reset()

    def step(self, action):
        if self.verbose:
            print(
                "[Event {}] | Assigning City {} to Salesman {}".format(self.event_counter,
                                                                       action,
                                                                       self.target_agent))
        self.manager.set_next_city(self.target_agent, action)
        self.event_counter += 1

        # check "all assigned" and
        # if "all assigned" transit the simulator state until the next event
        if len(self.manager.get_idle_agents()) == 0:
            if self.verbose:
                print("[Event {}] | Simulate Tour(s)".format(self.event_counter))
            self.manager.transit()

        if self.check_last_state():
            self.manager.transit_last()
            self.done = True
        else:
            self.manager.set_target_agent()
            self.done = False

        reward = self.reward_func(self)
        return self.observation_func(self), reward, self.done

    def check_last_state(self):
        is_last_state = True if len(self.manager.get_active_cities()) == 1 else False
        return is_last_state

    def get_action_space(self):
        action_space = self.manager.get_active_cities()
        if self.allow_early_return:
            # check whether "early returning is actually possible"
            # if not all agents except the target agent are already depot-returning
            early_returning_cond = len(self.manager.get_depot_returning_agents()) != self.m - 1
            zero_tour_cond = self.manager.salesmen[self.manager.target_agent].tour_length <= 0.0

            if early_returning_cond and not zero_tour_cond:
                action_space += [0]

        return action_space

    @property
    def target_agent(self):
        return self.manager.target_agent

    def reset(self):
        self.manager = mTSPManager(self.m, self.coords)
        self.event_counter = 0
        self.manager.set_target_agent()
        self.done = False

        # TODO: state -> observation function
        state = self.observation_func(self)
        return state

    @staticmethod
    def from_coords(self, coords, m):
        pass

    @staticmethod
    def from_state(self, state):
        pass

    def get_summary(self):
        info = dict()
        info['n'] = int(self.n)
        info['m'] = int(self.m)
        info['coords'] = self.coords

        if self.done:
            info['solve'] = True
        else:
            info['solve'] = False

        tour_dict = {idx: sm.tour_idx for idx, sm in self.manager.salesmen.items()}
        tl_dict, amp, ttl, n_inact = process_tour_info(tour_dict, self.coords)
        info['tours'] = tour_dict
        info['amplitude'] = amp
        info['total_length'] = ttl
        info['tour_length'] = tl_dict
        info['n_inactive'] = n_inact
        info['utilization'] = (self.m - n_inact) / self.m
        info['obj_val'] = max(tl_dict.values())

        return info
