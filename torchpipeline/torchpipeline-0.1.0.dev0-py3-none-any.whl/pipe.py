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
import torch
import torch.nn as nn

import torchpipeline.routing.default_router as default_router
import torchpipeline.routing.router as router

from typing import Generic
from typing import Optional
from typing import TypeVar

from torchpipeline.typing import Args
from torchpipeline.typing import ArgsKwargs
from torchpipeline.typing import Kwargs


__author__ = "Patrick Hohenecker"
__copyright__ = "Copyright (c) 2021, Patrick Hohenecker"
__license__ = "BSD-3-Clause"
__version__ = "0.1.0"
__maintainer__ = "Patrick Hohenecker"
__email__ = "patrick.hohenecker@gmx.at"
__status__ = "Development"


_Data = TypeVar("_Data")
_Target = TypeVar("_Target", bound=nn.Module)


class Pipe(Generic[_Target], nn.Module):
    """A piece of a :class:`~torchpipe.pipeline.Pipeline` that invokes a single module that is part of the same.

    A :class:`~.Pipe` is basically a wrapper for a single PyTorch module that moves any :class:`~torch.Tensor`s that are
    provided as args/kwargs to the right device (the one that the module is on) before invoking the module with them.

    TODO:
        * Special case: target has no parameters.
        * Dynamic routing is supported, i.e., the device is determined on every invocation.

    Attributes:
        routing_fn: The :class:`~.router.Router` that is used for moving :class:`~torch.Tensor` args/kwargs to the
            required device before the are provided to the :attr:`~.Pipe.target`.
        target: The PyTorch module that is invoked after moving args/kwargs to the required device.
    """

    #  CONSTRUCTOR  ####################################################################################################

    def __init__(
            self,
            target: _Target,
            routing_fn: Optional[router.Router] = None
    ) -> None:
        """Creates a new :class:`~.Pipe`."""

        super().__init__()

        insanity.sanitize_type("target", target, nn.Module)
        insanity.sanitize_type("routing_fn", routing_fn, router.Router, none_allowed=True)

        self._routing_fn = default_router.DefaultRouter() if routing_fn is None else routing_fn
        self._target = target

    #  PROPERTIES  #####################################################################################################

    @property
    def routing_fn(self) -> router.Router:

        return self._routing_fn

    @property
    def target(self) -> _Target:

        return self._target

    #  METHODS  ########################################################################################################

    def _find_device(self) -> Optional[torch.device]:
        """Determines the device used by the :attr:`~.Pipe.target` module.

        This is achieved by fetching the first (in terms of iteration order) parameters of the :attr:`~.Pipe.target`,
        and retrieving the device that this parameter is currently on.

        Returns:
            The device that the :attr:`~.Pipe.target` module is on or ``None``, if the latter does not have any
            parameters.
        """

        try:

            return next(self._target.parameters()).device

        except StopIteration:

            # If we arrive at this point, then the target module does not have any registered parameters.
            return None

    def _route_args(self, args: Args, kwargs: Kwargs) -> ArgsKwargs:
        """Uses the :attr:`~.Pipe.routing_fn` to map the provided args/kwargs to the target device.

        Notice that this method assumes that the router is configured to the required device already.

        Args:
            args: A `tuple` of positional args to map.
            kwargs: A `dict` if keywords args to map.

        Returns:
            args: The mapped `args`.
            kwargs: The mapped `kwargs`.
        """

        new_args = tuple(self._routing_fn(x) for x in args)
        new_kwargs = {k: self._routing_fn(v) for k, v in kwargs.items()}

        return new_args, new_kwargs

    def forward(self, *args, **kwargs):

        # Move the args to the identified target device.
        target_device = self._find_device()  # -> The device that the target module is on at the moment.
        if target_device is not None:

            # Update the router to the target device, and use it to move the args/kwargs.
            self._routing_fn.target_device = target_device
            args, kwargs = self._route_args(args, kwargs)

        # Run the target module.
        return self._target(*args, **kwargs)
