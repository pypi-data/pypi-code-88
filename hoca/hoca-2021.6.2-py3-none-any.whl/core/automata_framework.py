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

from abc import ABC, abstractmethod
from enum import Enum


class Field(ABC):
    class IOMode(Enum):
        IN = 0
        OUT = 1
        INOUT = 2

    def __init__(self, io_mode=IOMode.IN):
        self.io_mode = io_mode

    @abstractmethod
    def __getitem__(self, idx):
        """
        TODO: a better documentation
        :param idx: slice
        :return: a value
        """
        pass

    @abstractmethod
    def __setitem__(self, idx, value):
        """
        TODO: a better documentation
        :param idx: slice
        :param value:
        :return: None
        """
        pass

    @abstractmethod
    def is_in(self, coordinates):
        """
        Returns True if the coordinates points in the field
        :param coordinates: list or tuple of ints
        :return: bool
        """
        pass

    # TODO: add a describe method


class Automaton(ABC):
    @classmethod
    @abstractmethod
    def build_field_dict(cls, *args, **kwargs):
        return {}

    # TODO: add a class method providing the optimal number of automata for the current Field and set of parameters
    # TODO: add a class method providing the optimal number of generation for the current Field, set of parameters and number of automata

    def __init__(self):
        # Even if the class is abstract,
        # it provides basic initialization
        self.status = AutomatonStatus.ALIVE

    @abstractmethod
    def run(self):
        pass

    @classmethod
    def describe(cls, short=True):
        return cls.__name__


class AutomatonStatus:
    DEAD = 0
    ALIVE = 1
    RESPAWN = 2

    def __init__(self, s, x, y):
        assert s in (AutomatonStatus.DEAD, AutomatonStatus.ALIVE, AutomatonStatus.RESPAWN)

        self.s = s
        self.x = x
        self.y = y


class Population(ABC):
    def __init__(self):
        super().__init__()

        self.generation = 0

    @abstractmethod
    def run(self):
        self.generation += 1

    @abstractmethod
    def play(self):
        pass

    @abstractmethod
    def describe(self, short=True):
        return self.__class__.__name__
