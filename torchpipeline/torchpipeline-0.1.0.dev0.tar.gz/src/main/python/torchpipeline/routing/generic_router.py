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


import torch

import torchpipeline.routing.router as router

from typing import Callable
from typing import TypeVar


__author__ = "Patrick Hohenecker"
__copyright__ = "Copyright (c) 2021, Patrick Hohenecker"
__license__ = "BSD-3-Clause"
__version__ = "0.1.0"
__maintainer__ = "Patrick Hohenecker"
__email__ = "patrick.hohenecker@gmx.at"
__status__ = "Development"


_Data = TypeVar("_Data")


class GenericRouter(router.Router):
    """TODO

    Attributes:
        routing_fn: TODO
    """

    #  CONSTRUCTOR  ####################################################################################################

    def __init__(
            self,
            routing_fn: Callable[[_Data, torch.device], _Data],
            target_device: torch.device = torch.device("cpu")
    ) -> None:
        """Creates a new :class:`~.DefaultRouter` that maps tensors to the specified ``target_device``."""

        super().__init__(target_device)

        if not callable(routing_fn):

            raise TypeError("The <routing_fn> has to be callable")

        self._routing_fn = routing_fn

    #  PROPERTIES  #####################################################################################################

    @property
    def routing_fn(self) -> Callable[[_Data, torch.device], _Data]:

        return self._routing_fn

    #  METHODS  ########################################################################################################

    def route(self, data: _Data) -> _Data:

        return self._routing_fn(data, self._target_device)
