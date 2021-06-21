# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------

"""Classes that contain all the optimizer parameters associated with training
models. """
from azureml.contrib.automl.dnn.vision.common.constants import TrainingLiterals


class SgdOptimizerParameters:
    """Class that contains all parameters associated with SGD optimizer."""

    def __init__(self, settings):
        """
        :param settings: dictionary containing settings for training. Currently supported include:
          -optimizer: optimizer type
          -learning_rate: learning rate
          -weight_decay: weight decay
          -momentum: momentum
          -nesterov: nesterov
        :type settings: dict
        """
        self._optimizer_type = settings[TrainingLiterals.OPTIMIZER]
        self._learning_rate = settings[TrainingLiterals.LEARNING_RATE]
        self._weight_decay = settings[TrainingLiterals.WEIGHT_DECAY]
        # specific to SGD
        self._momentum = settings[TrainingLiterals.MOMENTUM]
        self._nesterov = settings[TrainingLiterals.NESTEROV]

    @property
    def optimizer_type(self):
        """Get optimizer type

        :returns: optimizer type
        :rtype: str
        """
        return self._optimizer_type

    @property
    def learning_rate(self):
        """Get learning rate value

        :returns: learning rate
        :rtype: float
        """
        return self._learning_rate

    @property
    def weight_decay(self):
        """Get weight decay value

        :returns: weight decay
        :rtype: float
        """
        return self._weight_decay

    @property
    def momentum(self):
        """Get momentum value

        :returns: momentum
        :rtype: float
        """
        return self._momentum

    @property
    def nesterov(self):
        """Get nesterov enabled-ness

        :returns: nesterov
        :rtype: bool
        """
        return self._nesterov


class AdamOptimizerParameters:
    """Class that contains all parameters associated with Adam and AdamW optimizer."""

    def __init__(self, settings):
        """
        :param settings: dictionary containing settings for training. Currently supported include:
          -optimizer_type: optimizer type
          -learning_rate: learning rate
          -weight_decay: weight decay
          -beta1: beta1
          -beta2: beta2
          -amsgrad: amsgrad
        :type settings: dict
        """
        self._optimizer_type = settings[TrainingLiterals.OPTIMIZER]
        self._learning_rate = settings[TrainingLiterals.LEARNING_RATE]
        self._weight_decay = settings[TrainingLiterals.WEIGHT_DECAY]
        # specific to Adam and AdamW
        self._beta1 = settings[TrainingLiterals.BETA1]
        self._beta2 = settings[TrainingLiterals.BETA2]
        self._amsgrad = settings[TrainingLiterals.AMSGRAD]

    @property
    def optimizer_type(self):
        """Get optimizer type

        :returns: optimizer type
        :rtype: str
        """
        return self._optimizer_type

    @property
    def learning_rate(self):
        """Get learning rate value

        :returns: learning rate
        :rtype: float
        """
        return self._learning_rate

    @property
    def weight_decay(self):
        """Get weight decay value

        :returns: weight decay
        :rtype: float
        """
        return self._weight_decay

    @property
    def beta1(self):
        """Get beta1 value

        :returns: beta1
        :rtype: float
        """
        return self._beta1

    @property
    def beta2(self):
        """Get beta2 value

        :returns: beta2
        :rtype: float
        """
        return self._beta2

    @property
    def amsgrad(self):
        """Get amsgrad enabled-ness

        :returns: amsgrad
        :rtype: bool
        """
        return self._amsgrad
