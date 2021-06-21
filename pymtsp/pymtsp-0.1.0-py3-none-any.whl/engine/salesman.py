import numpy as np

from pymtsp.engine.city import City, CityStatus
from pymtsp.engine.status import SalesmanStatus


def calc_dist(src, dst):
    return np.sqrt(np.sum((src - dst) ** 2))


class Salesman:
    def __init__(self,
                 idx: int,
                 first_city):
        super(Salesman, self).__init__()

        self.idx = idx
        self.status = SalesmanStatus.IDLE
        self.is_target = False
        self.is_returning = False

        # Tour from "cur city" to "next city"
        self.cur_city_idx = first_city.idx
        self.cur_city = first_city
        self.next_city = None
        self.remaining_distance = 0.0

        self.loc = np.array(first_city.loc)  # current position

        # tour information
        self.tour_idx = [self.cur_city_idx]
        self.tour = [self.loc]
        self.tour_length = 0.0

    def set_next_city(self, next_city):
        assert self.status == SalesmanStatus.IDLE

        if isinstance(next_city, City):
            assert next_city.status == CityStatus.IDLE
            next_city.status = CityStatus.ASSIGNED
            next_city.assigned_by = self.idx
        else:
            self.is_returning = True

        self.next_city = next_city
        self.status = SalesmanStatus.ASSIGNED
        self.remaining_distance = calc_dist(self.loc, self.next_city.loc)

    def simulate(self, time: float):
        """
        simulate the salesman's tour; assuming the unit traveling speed
        """

        # check current settings are valid
        assert self.status == SalesmanStatus.ASSIGNED
        assert self.remaining_distance > 0.0

        # traveling
        cur_x, cur_y = self.loc
        next_x, next_y = self.next_city.loc
        dy, dx = (next_y - cur_y), (next_x - cur_x)
        theta = np.arctan(np.abs(dy / dx))
        self.loc += np.array([np.sign(dx) * time * np.cos(theta),
                              np.sign(dy) * time * np.sin(theta)])
        self.remaining_distance -= time
        self.tour_length += time

        # if reach to the destination city
        if np.allclose(self.loc, self.next_city.loc):
            if isinstance(self.next_city, City):
                # visit the next city
                self.status = SalesmanStatus.IDLE
                self.next_city.status = CityStatus.INACTIVE
            else:  # next city is the depot
                self.status = SalesmanStatus.INACTIVE

            self.loc = np.array(self.next_city.loc)
            self.cur_city_idx = self.next_city.idx
            self.tour_idx.append(self.next_city.idx)
            self.tour.append(self.next_city.loc)
            self.cur_city = self.next_city
            self.next_city = None
            self.remaining_distance = 0.0

    def __repr__(self):
        msg = "Salesman {} | Pos {} | Status: {} | Remain dist. {} | Return to depot {}".format(self.idx,
                                                                                                self.loc,
                                                                                                self.status,
                                                                                                self.remaining_distance,
                                                                                                self.is_returning)
        return msg
