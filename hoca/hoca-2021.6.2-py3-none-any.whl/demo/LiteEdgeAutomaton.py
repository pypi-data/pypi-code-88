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

import random
from enum import Enum, auto

import numpy

from hoca.core.automata_framework import Automaton, AutomatonStatus
from hoca.core.ImageField import ImageField
from hoca.core.utilities import AutomataUtilities


class LiteEdgeAutomaton(Automaton):
    """
    The LiteEdgeAutomaton is a rework of EdgeAutomaton.
    As before, it works on one color component selected with one of the ComponentSelect.
    But it also adds various controls:
        direction_select: int or DirectionSelect
        roughness: the lesser, the more the automaton is sensitive to small image edges
        edge_factor:
    """
    class ComponentSelect(Enum):
        R = auto()
        G = auto()
        B = auto()
        A = auto()
        GREATEST = auto()
        RANDOM = auto()

    class DirectionSelect(Enum):
        FOLLOW_EDGES = auto()
        RANDOM_CONSTANT = auto()

    component_select = ComponentSelect.GREATEST
    direction_select = DirectionSelect.RANDOM_CONSTANT
    roughness = 0.05  # about 12 / 255
    edge_factor = 2
    smoothness = 0.05

    @classmethod
    def describe(cls, short=True):
        if short:
            return f"{super().describe(short=short)}-" \
                   f"{cls.component_select}-{cls.direction_select}-" \
                   f"r{cls.roughness}-ef{cls.edge_factor}-s{cls.smoothness}"
        else:
            return f"""{super().describe(short=short)}
    component_select: {cls.component_select}
    direction_select: {cls.direction_select}
    roughness: {cls.roughness}
    edge_factor: {cls.edge_factor}
    smoothness: {cls.smoothness}"""

    @classmethod
    def build_field_dict(cls, image_path, *args, **kwargs):
        source_field = ImageField.from_image(image_path, io_mode=ImageField.IOMode.IN, image_mode="RGB")
        return {'source': source_field,
                'result': ImageField.blank(source_field.size, io_mode=ImageField.IOMode.OUT, image_mode="RGB")}

    def __init__(self, automata_population):
        assert 0 <= self.__class__.edge_factor <= 2,\
            f"edge_factor must be in [0, 2] (was {self.__class__.edge_factor})"
        assert isinstance(self.__class__.direction_select, int) or \
            isinstance(self.__class__.direction_select, self.__class__.DirectionSelect), \
            f"direction_select must be either an int or a {self.__class__.DirectionSelect} enum " \
            f"(was {self.__class__.direction_select})"

        super().__init__()

        self.automata_population = automata_population

        # keep a shortcut to the fields, it improves readability
        # and may be efficient as it is called quite often
        # set a shortcut to the fields from the fields dictionary
        self.source_field = self.automata_population.field_dict['source']
        self.destination_field = self.automata_population.field_dict['result']

        # set an initial random position for the automaton
        self.x = random.randint(0, self.source_field.width - 1)
        self.y = random.randint(0, self.source_field.height - 1)

        # select on which color component the automaton will work
        if self.__class__.component_select == self.__class__.ComponentSelect.R:
            # select the red component which index is 0
            self.used_color_component = 0
        elif self.__class__.component_select == self.__class__.ComponentSelect.G:
            # select the green component which index is 1
            self.used_color_component = 1
        elif self.__class__.component_select == self.__class__.ComponentSelect.B:
            # select the blue component which index is 2
            self.used_color_component = 2
        elif self.__class__.component_select == self.__class__.ComponentSelect.A:
            # select the alpha component which index is 3
            self.used_color_component = 3
        elif self.__class__.component_select == self.__class__.ComponentSelect.RANDOM:
            # select a random color component
            self.used_color_component = random.randint(0, self.source_field.depth - 1)
        else:
            # component_select should be ComponentSelect.GREATEST
            # select the greatest color component at the current automaton position
            self.used_color_component = numpy.argmax(self.source_field[self.x, self.y])

        # select how the direction of the next move of the automaton will be computed
        if isinstance(self.__class__.direction_select, int):
            self.__class__.direction_select %= 8
            self.direction_function = lambda v: self.__class__.direction_select
        elif self.__class__.direction_select == self.__class__.DirectionSelect.FOLLOW_EDGES:
            self.direction_function = self.compute_direction
        else:
            # direction_select should be DirectionSelect.RANDOM_CONSTANT
            a_random_direction = random.randint(0, 7)
            self.direction_function = lambda v: a_random_direction

        # This value will keep track of the previous value of the used_color_component
        self.previous_used_color_component_value = self.source_field[self.x, self.y, self.used_color_component]

        # set the automaton life expectancy from the value of the used_color_component
        self.run_before_death = int(self.source_field[self.x, self.y, self.used_color_component] * 64)

        self.status = AutomatonStatus.ALIVE

    def get_field_value(self, x, y):
        """
        If field.is_in(x, y) the method gets and returns the field value at (x, y)
        otherwise it returns 0
        It necessary to overload the field.get_field_value() as even if the automaton
        is in the field, on the borders, the automaton will access adjacent points outside the field.
        :param x: int
        :param y: int
        :return: a dictionary containing the field (multi-)value
        """
        if self.source_field.is_in((x, y)):
            return self.source_field[x, y, self.used_color_component]
        else:
            return 0

    @classmethod
    def is_edge(cls, central_value, adjacent_value):
        return central_value > adjacent_value + cls.smoothness

    def compute_direction(self, central_value):
        """
        Follow edges by their right side (keep them on the left of the automaton displacement).
        See also the compute_direction() method documentation in the EdgeAutomaton class definition.
        :param central_value:
        :return: an int in [0, 7] denoting a direction
        """
        start_position = random.randint(0, 7)
        for d in range(0, 8):
            direction = d + start_position
            dx, dy = AutomataUtilities.get_dx_dy(direction)
            if not self.__class__.is_edge(central_value, self.get_field_value(self.x + dx, self.y + dy)):
                return direction

        return start_position

    def run(self):
        # get the field value at the current automaton position
        used_color_component_value = self.get_field_value(self.x, self.y)

        # compute the edge size
        # edge is the delta between used_color_component_value and its previous value
        edge = used_color_component_value - self.previous_used_color_component_value
        # then if edge is greater than a fixed value, it means that the automaton is on a "higher"
        # position than the previous it occupied
        if edge > self.__class__.roughness:
            # update the second/dual field with a value depending on the edge size and a factor
            # the greater the factor the more contrasted the dual image will be
            dual_component_value = self.destination_field[self.x, self.y, self.used_color_component]
            dual_component_value = max(dual_component_value, min(edge * self.__class__.edge_factor, 1))
            self.destination_field[self.x, self.y, self.used_color_component] = dual_component_value
            if dual_component_value == 1:
                # self.status = AutomatonStatus.DEAD
                self.status = AutomatonStatus.RESPAWN
        else:
            # the automaton hasn't climbed an edge, penalize it
            self.run_before_death //= 2

        # update the automaton memory
        self.previous_used_color_component_value = used_color_component_value

        dx, dy = AutomataUtilities.get_dx_dy(self.direction_function(used_color_component_value))
        self.x += dx
        self.y += dy

        # decrease the automaton life expectancy
        self.run_before_death -= 1

        # as the automaton is often trapped in a path, let it die or respawn elsewhere
        # if it's life expectancy has exhausted or it is on a field cell value that has already reached 1
        if self.run_before_death < 0:
            # self.status = AutomatonStatus.DEAD
            self.status = AutomatonStatus.RESPAWN

    def get_status(self):
        if not self.source_field.is_in((self.x, self.y)):
            self.status = AutomatonStatus.RESPAWN

        return AutomatonStatus(self.status, self.x, self.y)


if __name__ == "__main__":
    from hoca.monitor.CallbackPopulation import CallbackPopulation, SaveFieldsVideoCallback, SaveFieldsImageCallback, \
        SaveTracesImageCallback, SaveTracesVideoCallback, LogProgressCallback, Callback

    # Init the pseudo random generator to be able to replay the same population behaviour
    # This is optional
    random.seed('This is the seed')

    automata_class = LiteEdgeAutomaton

    image_path = '../../images/Edward Hopper_Nighthawks_1942.jpg'

    # Build field
    field_dict = automata_class.build_field_dict(image_path)
    first_field = field_dict[list(field_dict)[0]]

    # Create the automata population and play it
    # The number of run is such that an automaton will process about 52 pixels
    automata_count = 1000
    stop_after = 52 * first_field.width * first_field.height // automata_count
    stop_after = 1500
    automata_population = CallbackPopulation(field_dict, automata_count, automata_class,
                                             stop_after=stop_after,
                                             auto_respawn=False)

    # register callbacks
    automata_population.register_callback(LogProgressCallback(automata_population))

    automata_population.register_callback(
        SaveFieldsVideoCallback(automata_population,
                                activation_condition_function=Callback.condition_each_n_generation(2)))
    automata_population.register_callback(
        SaveTracesImageCallback(automata_population,
                                activation_condition_function=Callback.condition_at_generation(stop_after)))

    # automata_population.register_callback(SaveFieldsImageCallback(automata_population))
    # automata_population.register_callback(SaveTracesImageCallback(automata_population))

    automata_population.play()
