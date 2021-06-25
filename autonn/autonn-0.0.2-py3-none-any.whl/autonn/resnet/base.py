from __future__ import annotations

import functools
import typing

import numpy as np
import torch

from ..fields import OrdinalHyperParameter
from ..nn import NNClassifier
from ._backend import make_resnet_from_cfg

__authors__ = ["Hao Wang", "Yuanhao Guo"]


# TODO: verify the documentation
# TODO: implement a model selector to choose among ResNet18, 50, ... using MOO BO algorithm
class _ResNet(NNClassifier):
    """ResNet network class

    Hyper-parameters
    ----------------
    input_kernel : int, optional
        kernel size of input convolution layer, by default 7
    width_per_group : int, optional
        base channels for intermediate convolution layer in residual block,
        for example, in_channels -> width_per_group * expansion -> out_channels,
        only required for bottle_neck block, by default 64.
    expansion : int, optional
        channel expansion rate for intermediate convolution layer in residual block,
        by default 1
    block : str, optional
        residual block type, by default
        "basic_block" --> in --> conv1 --> conv2 --> (out + in);
        "bottle_neck" --> in --> conv1 --> conv2 --> conv3 --> (out + in)
    batch_size : int, optional
        training batch size, by default 256
    """

    block = OrdinalHyperParameter(["basic_block", "bottle_neck"], "basic_block")
    input_kernel = OrdinalHyperParameter([3, 5, 7], 7)
    # TODO: @yuanhao: `width_per_group` is only effective for 'bottle_neck'?
    width_per_group = OrdinalHyperParameter([16, 32, 64], 64)
    expansion = OrdinalHyperParameter([1, 2], 1)

    def __init__(self, *args, **kwargs):
        # TODO: @Yuanhao do you recall why we set _parallel = False?
        # is this caused by the data loader?
        self._parallel = False
        super().__init__(*args, **kwargs)

    def set_data(
        self, data_train: typing.Iterable, data_val: typing.Optional[typing.Iterable] = None
    ) -> _ResNet:
        super().set_data(data_train, data_val)
        self._create_model = functools.partial(
            make_resnet_from_cfg,
            model_type=self.__class__.__name__.lower(),
            num_classes=self.num_classes,
        )
        return self

    def predict_prob(self, X: torch.Tensor) -> np.ndarray:
        """predict classification probability

        Parameters
        ----------
        X : `torch.Tensor`
            data to predict, of the shape (batch_size, n_channel, height, width)

        Returns
        -------
        np.ndarray
            probablities of each input tensor belonging to each labels. It is of the shape
            (batch_size, `self.num_classes`) and each row of it should sums to one,
            up to some numerical error...
        """
        assert self._task == "classification"
        with torch.no_grad():
            self._model.eval()
            if self._use_gpu:
                X = X.cuda()
            output = self._model(X)
            return torch.softmax(output, dim=1).detach().cpu().numpy()


class ResNet18(_ResNet):
    pass


class ResNet34(_ResNet):
    pass


class ResNet50(_ResNet):
    pass


class ResNet101(_ResNet):
    pass


class ResNet152(_ResNet):
    pass
