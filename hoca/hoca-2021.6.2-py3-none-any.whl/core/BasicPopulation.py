# Copyright (C) 2021 Jean-Louis Paquelin <jean-louis.paquelin@villa-arson.fr>
#
# This file is part of the hoca (Higher-Order Cellular Automata) library.
#
# hoca is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# hoca is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with hoca.  If not, see <http://www.gnu.org/licenses/>.

from .automata_framework import Population, AutomatonStatus

import random
from enum import Enum


class BasicPopulation(Population):
    """This class provides an execution environment for the automata population.

    Each time the run() method is invoked, each automaton is run once. At the end of the run
    the population may have increased or decreased.

    Status: as each automaton has its own status, population as a whole has a status.
    These are the available status values:
    EMPTY: the population has decreased to 0 before reaching the final condition.
    COMPLETED: the population has reached one of the expected final condition.
    RUNNABLE: the run() method should be called in order to reach the final condition.
    """

    class Status(Enum):
        RUNNABLE = 0
        COMPLETED = 1
        EMPTY = 2

    def __init__(self, field_dict, population_size, automata_class,
                 auto_respawn=False, stop_after=None, shuffle=False):
        """

        The stop_after parameter controls the number of execution/run/generation a population must
        achieve before it is completed (self.status == Status.COMPLETED).

        The auto_respawn parameter controls if an automaton which status is RESPAWN after it
        has been should be respawn i.e. released then reinstanciated in a new (random) place.

        The shuffle parameter controls if the population is shuffled after each run. This prevents
        to get a deterministic order of execution of the automata.

        :param field_dict:
        :param population_size: int
        :param automata_class:
        :param auto_respawn: bool
        :param stop_after: int or None
        :param shuffle: bool
        """
        assert stop_after is None or stop_after >= 0,\
            f"stop_after should be None or greater than or equal to 0 ({stop_after})"

        super().__init__()

        self.field_dict = field_dict
        self.population_size = population_size
        self.automata_class = automata_class

        self.auto_respawn = auto_respawn
        self.stop_after = stop_after
        self.shuffle = shuffle

        self.status = BasicPopulation.Status.RUNNABLE

        # TODO: define (or make it clear) the difference between self.population_size and self.alive_count
        # self.alive_count seems to be some kind of instantaneous self.population_size

        # create the initial automata population
        self.automata_population = list(map(lambda _: automata_class(self), range(population_size)))
        self.alive_count = self.population_size
        if self.alive_count == 0:
            self.status = BasicPopulation.Status.EMPTY

    def run(self):
        if self.status != BasicPopulation.Status.RUNNABLE:
            return self.status

        if self.stop_after is not None and self.stop_after < self.generation:
            self.status = BasicPopulation.Status.COMPLETED
            return self.status

        super().run()

        next_automata_population = []
        self.alive_count = 0

        for automaton in self.automata_population:
            status = automaton.get_status()
            if status.s == AutomatonStatus.ALIVE:
                # automaton is alive, run it
                automaton.run()
                next_automata_population.append(automaton)
                self.alive_count += 1
            elif status.s == AutomatonStatus.RESPAWN:
                next_automata_population.append(self.automata_class(self))
            elif status.s == AutomatonStatus.DEAD:
                if self.auto_respawn:
                    # replace the dead automaton by a new one
                    next_automata_population.append(self.automata_class(self))

        # shuffle the population execution order before the next run
        if self.shuffle:
            random.shuffle(next_automata_population)

        # TODO: it may be interesting to be able to access the population both thru
        # an organized data structure (e.g. organized by x, y) and access it in
        # random way (as now)

        self.automata_population = next_automata_population
        self.population_size = len(self.automata_population)

        # All the automata have died
        if self.population_size == 0:
            self.status = BasicPopulation.Status.EMPTY
            return self.status

        return self.status

    def play(self, stop_after=None, **kwargs):
        stop_after = stop_after if stop_after is not None else self.stop_after

        for _ in range(stop_after):
            if self.run() != self.Status.RUNNABLE:
                break

    def describe(self, short=True):
        if short:
            return f"{self.automata_class.describe()}_" \
                   f"g{self.generation}_" \
                   f"s{self.population_size}"
        else:
            return f"""Population: {self.__class__.__name__}
    generation: {self.generation}
    size: {self.population_size}
    status: {self.status}
    auto_respawn: {self.auto_respawn}
    stop_after: {self.stop_after}
    shuffle: {self.shuffle}
    automata: {self.automata_class.describe(short=False)}"""

