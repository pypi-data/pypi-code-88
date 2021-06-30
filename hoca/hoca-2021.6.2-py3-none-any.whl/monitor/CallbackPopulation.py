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

from hoca.core.automata_framework import Field
from hoca.core.BasicPopulation import AutomatonStatus, BasicPopulation
from hoca.monitor.PILMonitor import PILMonitor
from hoca.monitor.ColorGradient import ColorGradient

from abc import ABC, abstractmethod
from enum import IntFlag
from collections import namedtuple

import time
import datetime
import os
import logging

import numpy
import av


class CallbackPopulation(BasicPopulation):
    def __init__(self, field_dict, population_size, automata_class, **kwargs):
        super(CallbackPopulation, self).__init__(field_dict, population_size, automata_class, **kwargs)

        self.callbacks = []

    def register_callback(self, callback_instance):
        """register_callback() method registers a new callback

        :param callback_instance: Callback
        :return: None
        """
        self.callbacks.append(callback_instance)

    def play(self, stop_after=None, **kwargs):
        stop_after = stop_after if stop_after is not None else self.stop_after

        start_time = time.time()
        for _ in range(stop_after):
            if self.run() != self.Status.RUNNABLE:
                break

            elapsed_time = time.time() - start_time

            for callback_instance in self.callbacks:
                callback_instance.callback(elapsed_time)


class Callback(ABC):
    def __init__(self, population, base_directory=None, activation_condition_function=(lambda p: True)):
        self.population = population
        self.activation_condition_function = activation_condition_function

        if base_directory is None:
            base_directory = self.population.automata_class.__name__ # describe()
        # Make the base directory name unique by adding the date and PID
        self.base_directory = f"{base_directory}_{datetime.datetime.now().strftime('%Y%m%d')}_{os.getpid()}"

    @staticmethod
    def condition_each_n_generation(report_progress_each):
        return lambda population: (population.generation % report_progress_each) == 0

    @staticmethod
    def condition_at_generation(generation):
        return lambda population: population.generation == generation

    @staticmethod
    def condition_or(activation_condition_function_list):
        return lambda population: any([activation_condition_function(population)
                                       for activation_condition_function in activation_condition_function_list])

    @abstractmethod
    def callback(self, elapsed_time):
        """The callback() method is supposed to be called by the play() method of a CallbackPopulation
        instance."""
        pass


class LogProgressCallback(Callback):
    def __init__(self, *args, logfile=None, loglevel=logging.INFO, **kwargs):
        super(LogProgressCallback, self).__init__(*args, **kwargs)

        if logfile:
            logging.basicConfig(level=loglevel, filename=logfile)
        else:
            logging.basicConfig(level=loglevel)

        logging.info(self.population.describe(short=False))

    def callback(self, elapsed_time):
        if self.activation_condition_function(self.population):
            # Some progress has been done, log it
            logging.info(f"generation = {self.population.generation} "
                         f"(elapsed time {elapsed_time:.3f}s, average {self.population.generation / elapsed_time:.3f}gps)")


class ImageCallback(Callback):
    # We will have to pad numerical filenames in order to maintain directory
    # content in lexicographic order
    zero_padding_length = 6

    def __init__(self, *args, **kwargs):
        super(ImageCallback, self).__init__(*args, **kwargs)

    @abstractmethod
    def callback(self, elapsed_time):
        """The callback() method is supposed to be called by the play() method of a CallbackPopulation
        instance."""
        pass

    def _zero_padded_generation(self):
        """The private _zero_padded_generation() method returns a string containing the
        current generation of self.population padded with zeros. The padding length is
        the zero_padding_length class variable.

        :return: str
        """
        return f"{str(self.population.generation).zfill(self.zero_padding_length)}"


class SaveTracesImageCallback(ImageCallback):
    class Trace(IntFlag):
        TRAJECTORIES = 0b01
        POSITIONS = 0b10

    def __init__(self, *args, trace=Trace.TRAJECTORIES+Trace.POSITIONS, **kwargs):
        super(SaveTracesImageCallback, self).__init__(*args, **kwargs)

        field_size = self._get_field_size()

        if trace & self.Trace.TRAJECTORIES:
            # Create a directory to save the automata trajectories
            self.trajectories_save_path = os.path.join(self.base_directory, f"trajectories")
            if not os.path.exists(self.trajectories_save_path):
                os.makedirs(self.trajectories_save_path)
            # Prepare a monitor to keep track of the automata trajectories
            self.trajectories_monitor = PILMonitor(field_size, ColorGradient.create())
        else:
            self.trajectories_monitor = None

        if trace & self.Trace.POSITIONS:
            # Create a directory to save the automata position
            self.positions_save_path = os.path.join(self.base_directory, f"positions")
            if not os.path.exists(self.positions_save_path):
                os.makedirs(self.positions_save_path)
            # Prepare a monitor to keep track of the automata positions
            self.positions_monitor = PILMonitor(field_size, ColorGradient.create(gradient_name='cgy'))
        else:
            self.positions_monitor = None

    def callback(self, elapsed_time):
        # TODO: This should be optimized as the complexity is twice the population size in the worst case
        if self.trajectories_monitor is not None:
            # even if the trajectories aren't reported this time,
            # update the trajectories monitor for each automaton
            self._update_monitor(self.trajectories_monitor)

            # should it report the automata trajectories?
            if self.activation_condition_function(self.population):
                output_image_path = os.path.join(self.trajectories_save_path, f"{self._zero_padded_generation()}.png")
                self.trajectories_monitor.image.save(output_image_path)

        if self.positions_monitor is not None:
            # should it report the automata position?
            if self.activation_condition_function(self.population):
                # clear the previous monitored positions
                self.positions_monitor.reset()
                # update position monitor for each automaton
                self._update_monitor(self.positions_monitor)
                # and eventually save the image
                output_image_path = os.path.join(self.positions_save_path, f"{self._zero_padded_generation()}.png")
                self.positions_monitor.image.save(output_image_path)

    def _get_field_size(self):
        # Get the first output field size, we expect it to be at the same size/scale as the
        # field where the automata lay
        # TODO: This may be wrong (e.g. if the automata coordinates are on the image
        #       and output their results on a smaller field
        field_size = None
        for subfield in self.population.field_dict.values():
            if subfield.io_mode != Field.IOMode.IN:
                field_size = subfield.size
                break

        if field_size is not None:
            for subfield in self.population.field_dict.values():
                if subfield.io_mode == Field.IOMode.IN:
                    field_size = subfield.size
                    break

        return field_size

    def _update_monitor(self, monitor):
        # for each automaton update the monitor
        for automaton in self.population.automata_population:
            status = automaton.get_status()
            if status.s == AutomatonStatus.ALIVE:
                monitor.update(status.x, status.y)


class SaveFieldsImageCallback(ImageCallback):
    def __init__(self, *args, **kwargs):
        super(SaveFieldsImageCallback, self).__init__(*args, **kwargs)

        self.subfield_directories = {}

        # For each subfield in the field
        for subfield_name, subfield in self.population.field_dict.items():
            # Save the input subfields content (they won't be save later)
            if subfield.io_mode == Field.IOMode.IN:
                image_path = os.path.join(self.base_directory, f"{subfield_name}_field.png")
                subfield.image.save(image_path)
            else:
                # Create the subdirectories corresponding to the subfields
                subfield_save_path = os.path.join(self.base_directory, f"{subfield_name}_field")
                if not os.path.exists(subfield_save_path):
                    os.makedirs(subfield_save_path)

                # Store the directory path for later use
                self.subfield_directories[subfield_name] = subfield_save_path

    def callback(self, elapsed_time):
        if self.activation_condition_function(self.population):
            # Some progress has been done, save the output fields now
            for subfield_name, subfield in self.population.field_dict.items():
                if subfield.io_mode != Field.IOMode.IN:
                    # Compute the image path
                    output_image_path = os.path.join(self.subfield_directories[subfield_name],
                                                     f"{self._zero_padded_generation()}.png")
                    subfield.image.save(output_image_path)


class VideoCallback(Callback):
    # These class variables control the video encoding format.
    # Any combination of values compatible with pyav/FFMPEG should work but mp4 codec
    # has shown luminance artifacts
    # crf stands for Constant Rate Factor, when set to 0 it provides a lossless encoding
    # see: https://trac.ffmpeg.org/wiki/Encode/H.265
    codec_name = "libx265"
    video_extension = "mp4"
    pixel_format = "yuv444p"
    crf = "0"

    def __init__(self, population, fps=25, **kwargs):
        super(VideoCallback, self).__init__(population, **kwargs)

        self.fps = fps

        # Create the destination directory of the video(s)
        if not os.path.exists(self.base_directory):
            os.makedirs(self.base_directory)

        # Use a named tuple for a convenient way to retrieve data
        # TODO: this should be a class stuff
        self.AVData = namedtuple("AVData", "container stream")

    @abstractmethod
    def callback(self, elapsed_time):
        # The Class VideoCallback is still abstract
        pass

    def _prepare_avdata(self, width, height, path):
        # Inspiration came from https://pyav.org/docs/stable/cookbook/numpy.html#generating-video
        container = av.open(path, mode='w')

        stream = container.add_stream(self.codec_name, rate=self.fps)
        # Set the video image size from the subfield size
        stream.width = width
        stream.height = height
        stream.pix_fmt = self.pixel_format
        # Set lossless encoding
        stream.options["crf"] = self.crf

        return self.AVData(container, stream)

    @staticmethod
    def _add_frame(array, avdata):
        # Encode the numpy as a video frame
        frame = av.VideoFrame.from_ndarray(array, format='rgb24')
        # Then mux the frame in the video container
        for packet in avdata.stream.encode(frame):
            avdata.container.mux(packet)

    @staticmethod
    def _close_avdata(avdata):
        # Flush streams
        for packet in avdata.stream.encode():
            avdata.container.mux(packet)

        # Close the files
        avdata.container.close()


class SaveTracesVideoCallback(VideoCallback):
    class Trace(IntFlag):
        TRAJECTORIES = 0b01
        POSITIONS = 0b10

    def __init__(self, *args, trace=Trace.TRAJECTORIES+Trace.POSITIONS, **kwargs):
        super(SaveTracesVideoCallback, self).__init__(*args, **kwargs)

        # Get the first output field size, we expect it to be at the same size/scale as the
        # field where the automata lay
        # TODO: This may be wrong (e.g. if the automata coordinates are on the image
        #       and output their results on a smaller field
        field_size = None
        for subfield in self.population.field_dict.values():
            if subfield.io_mode != Field.IOMode.IN:
                field_size = subfield.size
                break

        if trace & self.Trace.TRAJECTORIES:
            # Prepare a monitor to keep track of the automata trajectories
            self.trajectories_monitor = PILMonitor(field_size, ColorGradient.create())

            # Prepare and store the av data (container and stream) for later use
            video_path = os.path.join(self.base_directory, f"trajectories.{self.video_extension}")
            self.trajectories_avdata = self._prepare_avdata(field_size[0], field_size[1], video_path)
        else:
            self.trajectories_monitor = None
            self.trajectories_avdata = None

        if trace & self.Trace.POSITIONS:
            # Prepare a monitor to keep track of the automata positions
            self.positions_monitor = PILMonitor(field_size, ColorGradient.create(gradient_name='cgy'))

            # Prepare and store the av data (container and stream) for later use
            video_path = os.path.join(self.base_directory, f"positions.{self.video_extension}")
            self.positions_avdata = self._prepare_avdata(field_size[0], field_size[1], video_path)
        else:
            self.positions_monitor = None
            self.positions_avdata = None

    def callback(self, elapsed_time):
        # TODO: This should be optimized as the complexity is twice the population size in the worst case
        if self.trajectories_monitor is not None:
            # even if the trajectories aren't reported this time,
            # update the trajectories monitor for each automaton
            for automaton in self.population.automata_population:
                status = automaton.get_status()
                if status.s == AutomatonStatus.ALIVE:
                    self.trajectories_monitor.update(status.x, status.y)

            # should it report the automata trajectories?
            if self.activation_condition_function(self.population):
                # Get the trajectories as a numpy array and add it to the video
                trajectories_data = numpy.asarray(self.trajectories_monitor.image)
                self.__class__._add_frame(trajectories_data, self.trajectories_avdata)

        if self.positions_monitor is not None:
            # should it report the automata position?
            if self.activation_condition_function(self.population):
                # clear the previous monitored positions
                self.positions_monitor.reset()
                # update position monitor for each automaton
                for automaton in self.population.automata_population:
                    status = automaton.get_status()
                    if status.s == AutomatonStatus.ALIVE:
                        self.positions_monitor.update(status.x, status.y)
                # Get the positions as a numpy array and add it to the video
                positions_data = numpy.asarray(self.positions_monitor.image)
                self.__class__._add_frame(positions_data, self.positions_avdata)

    def __del__(self):
        if self.trajectories_avdata:
            self.__class__._close_avdata(self.trajectories_avdata)

        if self.positions_avdata:
            self.__class__._close_avdata(self.positions_avdata)


class SaveFieldsVideoCallback(VideoCallback):
    def __init__(self, *args, **kwargs):
        super(SaveFieldsVideoCallback, self).__init__(*args, **kwargs)

        # subfield_avdata will store the references to av objects
        self.subfield_avdata = {}

        # For each subfield in the field
        for subfield_name, subfield in self.population.field_dict.items():
            # Save the input subfields content (they won't be save later)
            if subfield.io_mode == Field.IOMode.IN:
                image_path = os.path.join(self.base_directory, f"{subfield_name}_field.png")
                subfield.image.save(image_path)
            else:
                # Prepare and store the av data (container and stream) for later use
                video_path = os.path.join(self.base_directory, f"{subfield_name}.{self.video_extension}")
                self.subfield_avdata[subfield_name] = self._prepare_avdata(subfield.width, subfield.height, video_path)

    def callback(self, elapsed_time):
        if self.activation_condition_function(self.population):
            # Enough progress has been done, save the output fields now
            for subfield_name, subfield in self.population.field_dict.items():
                if subfield.io_mode != Field.IOMode.IN:
                    # Get the field (numpy) data, convert it as bytes and encode it as a video frame
                    field_data = (subfield[:, :, :].transpose(1, 0, 2) * 255).astype(numpy.uint8)
                    self.__class__._add_frame(field_data, self.subfield_avdata[subfield_name])

    def __del__(self):
        for avdata in self.subfield_avdata.values():
            self.__class__._close_avdata(avdata)


