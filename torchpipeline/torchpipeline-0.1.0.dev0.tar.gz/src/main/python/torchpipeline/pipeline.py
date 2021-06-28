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


import insanity
import torch.nn as nn

import torchpipeline.coupling.coupling as coupling
import torchpipeline.coupling.default_coupling as default_coupling
import torchpipeline.pipe as pipe
import torchpipeline.routing.router as router

from typing import Any
from typing import Optional


__author__ = "Patrick Hohenecker"
__copyright__ = "Copyright (c) 2021, Patrick Hohenecker"
__license__ = "BSD-3-Clause"
__version__ = "0.1.0"
__maintainer__ = "Patrick Hohenecker"
__email__ = "patrick.hohenecker@gmx.at"
__status__ = "Development"


class Pipeline(nn.Module):
    """A pipeline of PyTorch modules that are invoked one after the other.

    TODO:
        * Explain connectors.
        * First module cannot have connector.
    """

    #  CONSTRUCTOR  ####################################################################################################

    def __init__(self) -> None:
        """Creates a new, empty :class:`~.Pipeline`."""

        super().__init__()

        self._couplings = []  # -> For each registered module, the preceding coupling (which is None for the first one).
        self._pipes = []  # -> A list of registered modules (wrapped in Pipes) in the order that they are invoked in.

    #  MAGIC FUNCTIONS  ################################################################################################

    def __len__(self) -> int:

        return len(self._pipes)

    #  METHODS  ########################################################################################################

    def forward(self, *args, **kwargs) -> Any:

        # Ensure that the pipeline is not empty.
        if not self._pipes:

            raise ValueError("Cannot run an empty pipeline.")

        output = None
        for some_coupling, some_pipe in zip(self._couplings, self._pipes):

            if some_coupling is None:  # -> The current pipe is the first in the pipeline

                output = some_pipe(*args, **kwargs)

            else:

                next_args, next_kwargs = some_coupling(output)
                output = some_pipe(*next_args, **next_kwargs)

        return output

    def register(
            self,
            module: nn.Module,
            routing_fn: Optional[router.Router] = None,
            connect_fn: Optional[coupling.Coupling] = None
    ) -> None:
        """TODO"""

        insanity.sanitize_type("module", module, nn.Module)
        insanity.sanitize_type("routing_fn", routing_fn, router.Router, none_allowed=True)
        insanity.sanitize_type("connect_fn", connect_fn, coupling.Coupling, none_allowed=True)

        if connect_fn is None:

            # If the registered module is not the first one in the pipeline, then we use a DefaultCoupling with the
            # previous module.
            if self._pipes:

                connect_fn = default_coupling.DefaultCoupling()

        elif not self._pipes:  # -> There are no modules yet, i.e., the first one is being registered.

            # The first module in the pipeline does not need a coupling, i.e., cannot have a connect_fn.
            raise ValueError("The first module in the pipeline cannot have a preceding <connect_fn>.")

        self._pipes.append(pipe.Pipe(module, routing_fn=routing_fn))
        self._couplings.append(connect_fn)
