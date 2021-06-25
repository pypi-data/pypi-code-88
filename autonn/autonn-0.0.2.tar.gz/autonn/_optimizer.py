from torch import optim

from .fields import BoolHyperParameter, Parameter, RealHyperParameter
from .operator import AbstractOperator


class PytorchOptimizer(AbstractOperator):
    """Wrapper for Pytorch's stochastic gradient descent optimizers"""

    parameters = Parameter(None)
    _init = None  # TODO: add types here

    @staticmethod
    def _convert_hyper_params(kwargs):
        return kwargs

    def fit(self):
        """'fit' the optimizer to given parameters"""
        assert self.parameters is not None
        kwargs = self._convert_hyper_params(self.get_hyper_params())
        self._optimizer = self._init(self.parameters, **kwargs)

    def zero_grad(self):
        self._optimizer.zero_grad()

    def step(self):
        self._optimizer.step()


class SGD(PytorchOptimizer):
    """Wrapper for Pytorch's SGD optimizer

    Hyper-parameters
    ----------------
    lr : float, optional
        learning rate, by default 0.1
    momentum : float, optional
        momentum factor, by default 0
    dampening : float, optional
        dampening for momentum, by default 0
    weight_decay : float, optional
        weight decay (L2 penalty), by default 0
    nesterov : bool, optional
        enables Nesterov momentum, by default False
    """

    lr = RealHyperParameter([1e-5, 1], 1e-3, scale="log10")
    momentum = RealHyperParameter(
        [1e-5, 1e-1],
        1e-5,
        scale="log10",
        conditions="`nesterov` == True",
        action=lambda x: max(1e-5, x),
    )
    dampening = RealHyperParameter(
        [1e-5, 1e-1], 1e-5, scale="log10", conditions="`nesterov` == True", action=0
    )
    weight_decay = RealHyperParameter([1e-5, 1e-1], 1e-5, scale="log10")
    nesterov = BoolHyperParameter(default_value=False)
    _init = optim.SGD


class Adam(PytorchOptimizer):
    """Wrapper for Pytorch's Adam optimizer

    Hyper-parameters
     ---------------
    lr : float, optional:
    beta1 : float, optional
        coefficients used for computing running averages of gradient (default: 0.9)
    beta2 : float, optional
        coefficients used for computing running averages of squares of the gradient
        (default: 0.999)
    eps : float, optional
        term added to the denominator to improve numerical stability (default: 1e-8)
    weight_decay : float, optional
        weight decay (L2 penalty) (default: 0)
    amsgrad : bool, optional
        whether to use the AMSGrad variant of this algorithm from the paper
        `On the Convergence of Adam and Beyond`_ (default: False)
    """

    lr = RealHyperParameter([1e-10, 1e-1], 0.001, scale="log10")
    beta1 = RealHyperParameter([1e-10, 1e-1], 0.9, scale="log10")
    beta2 = RealHyperParameter([1e-10, 1e-1], 0.999, scale="log10")
    eps = RealHyperParameter([1e-10, 1e-1], 1e-8, scale="log10")
    weight_decay = RealHyperParameter([1e-10, 1e-1], 1e-10, scale="log10")
    amsgrad = BoolHyperParameter(False)
    _init = optim.Adam

    @staticmethod
    def _convert_hyper_params(kwargs):
        kwargs["betas"] = (kwargs["beta1"], kwargs["beta2"])
        del kwargs["beta1"]
        del kwargs["beta2"]
        return kwargs


class RMSprop(PytorchOptimizer):
    """Wrapper for Pytorch's RMSprop optimizer

    Hyper-parameters
    ----------------
    lr : float, optional
        learning rate, by default 0.01
    alpha : float, optional
        smoothing constant, by default 0.99
    eps : float, optional
        term added to the denominator to improve numerical stability, by default 1e-08
    weight_decay : float, optional
        weight decay (L2 penalty), by default 0
    momentum : float, optional
        momentum factor, by default 0
    centered : bool, optional
        if ``True``, compute the centered RMSProp, the gradient is normalized by
        an estimation of its variance, by default False
    """

    lr = RealHyperParameter([1e-10, 1e-1], 0.001, scale="log10")
    alpha = RealHyperParameter([1e-10, 1], 0.99, scale="log10")
    eps = RealHyperParameter([1e-10, 1e-1], 1e-8, scale="log10")
    weight_decay = RealHyperParameter([1e-10, 1e-1], 1e-10, scale="log10")
    momentum = RealHyperParameter([1e-10, 1e-1], 1e-10, scale="log10")
    centered = BoolHyperParameter(False)
    _init = optim.RMSprop


class PytorchScheduler(AbstractOperator):
    """Wrapper for Pytorch's learning rate scheduler"""

    step_size = Parameter(10)
    optimizer = Parameter(None)
    _init = None

    def fit(self):
        assert self.optimizer is not None
        self._scheduler = self._init(
            self.optimizer, step_size=self.step_size, **self.get_hyper_params()
        )

    def set_optimizer(self, optimizer: PytorchOptimizer):
        self._optimizer = getattr(optimizer, "_optimizer", None)

    def step(self):
        self._scheduler.step()


class StepLR(PytorchScheduler):
    """TODO: add docstring here"""

    gamma = RealHyperParameter([1e-3, 1], 0.1, scale="log10")
    _init = optim.lr_scheduler.StepLR


class ExponentialLR(PytorchScheduler):
    """TODO: add docstring here"""

    gamma = RealHyperParameter([1e-10, 1], 0.1, scale="log10")
    _init = optim.lr_scheduler.ExponentialLR


class CosineAnnealingLR(PytorchScheduler):
    """TODO: add docstring here"""

    eta_min = RealHyperParameter([1e-10, 1], 1e-10, scale="log10")
    T_max = Parameter()
    _init = optim.lr_scheduler.CosineAnnealingLR


class MultiStepLR(PytorchScheduler):
    """TODO: add docstring here"""

    gamma = RealHyperParameter([1e-10, 1], 0.1, scale="log10")
    milestones = Parameter()
    _init = optim.lr_scheduler.MultiStepLR


class LambdaLR(PytorchScheduler):
    """TODO: add docstring here"""

    lr_lambda = Parameter()
    _init = optim.lr_scheduler.LambdaLR


class MultiplicativeLR(PytorchScheduler):
    """TODO: add docstring here"""

    lr_lambda = Parameter()
    _init = optim.lr_scheduler.MultiplicativeLR
