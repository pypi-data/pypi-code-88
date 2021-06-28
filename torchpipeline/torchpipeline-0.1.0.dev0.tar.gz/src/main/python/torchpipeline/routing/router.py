# -*- coding: utf-8 -*-

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                                                     #
#   BSD 3-Clause License                                                              #
#                                                                                     #
#   Copyright (c) 2021, Patrick Hohenecker                                            #
#   All rights reserved.                                                              #
#                                                                                     #
#   Redistribution and use in source and binary forms, with or without                #
#   modification, are permitted provided that the following conditions are met:       #
#                                                                                     #
#   1. Redistributions of source code must retain the above copyright notice, this    #
#      list of conditions and the following disclaimer.                               #
#                                                                                     #
#   2. Redistributions in binary form must reproduce the above copyright notice,      #
#      this list of conditions and the following disclaimer in the documentation      #
#      and/or other materials provided with the distribution.                         #
#                                                                                     #
#   3. Neither the name of the copyright holder nor the names of its                  #
#      contributors may be used to endorse or promote products derived from           #
#      this software without specific prior written permission.                       #
#                                                                                     #
#   THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"       #
#   AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE         #
#   IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE    #
#   DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE      #
#   FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL        #
#   DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR        #
#   SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER        #
#   CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,     #
#   OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE     #
#   OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.              #
#                                                                                     #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


import abc

import insanity
import torch

from typing import TypeVar


__author__ = "Patrick Hohenecker"
__copyright__ = "Copyright (c) 2021, Patrick Hohenecker"
__license__ = "BSD-3-Clause"
__version__ = "0.1.0"
__maintainer__ = "Patrick Hohenecker"
__email__ = "patrick.hohenecker@gmx.at"
__status__ = "Development"


_Data = TypeVar("_Data")


class Router(metaclass=abc.ABCMeta):
    """An abstract base class for routers that move data to the :attr:`~.DefaultRouter.target_device`.

    Attributes:
        target_device: The PyTorch device that tensors are routed to.
    """

    #  CONSTRUCTOR  ####################################################################################################

    def __init__(self, target_device: torch.device = torch.device("cpu")) -> None:
        """Creates a new :class:`~.Router` that maps tensors to the specified ``target_device``."""

        self._target_device = None
        self.target_device = target_device  # -> This sanitizes the arg.

    #  MAGIC FUNCTIONS  ################################################################################################

    def __call__(self, data: _Data) -> _Data:

        return self.route(data)

    #  PROPERTIES  #####################################################################################################

    @property
    def target_device(self) -> torch.device:

        return self._target_device

    @target_device.setter
    def target_device(self, target_device: torch.device) -> None:

        insanity.sanitize_type("target_device", target_device, torch.device)
        self._target_device = target_device

    #  METHODS  ########################################################################################################

    @abc.abstractmethod
    def route(self, data: _Data) -> _Data:
        """Routes the provided ``data`` to the :attr:`~.DefaultRouter.target_device`.

        If the ``data`` is not moved to a different device for some reason (e.g., because it is on the right device
        already), then this can be a no-op, which means that the ``data`` is returned as-is.

        Args:
            data: The instance that has to be routed to the right device.

        Returns:
            The new ``data``, which is on the desired :attr:`~.DefaultRouter.target_device` now.
        """
