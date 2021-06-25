from __future__ import annotations

import logging
import os
from abc import abstractmethod
from typing import Callable, Dict, Iterable, List, Optional, Union

import numpy as np
import torch
from torch import nn

from ._optimizer import SGD, PytorchOptimizer, PytorchScheduler, StepLR
from .base import BaseModel
from .fields import Parameter
from .loss_metric import (
    CLASS_LOSS,
    CLASS_METRIC,
    REGR_LOSS,
    REGR_METRIC,
    balanced_accuracy,
    f1,
    tpr,
)
from .operator import AbstractOperator

__authors__ = ["Hao Wang", "Yuanhao Guo"]


class BaseObserver(AbstractOperator):
    """basic observer for logging each step and epoch, saving the model on various
    event, and terminating the training upon staganation
    """

    save_every_x_epochs = Parameter(1)
    verbose_for_every_x_steps = Parameter(1)
    checkpoints_path = Parameter(None)
    patience = Parameter(5)  # How many epochs to wait before stopping since the last improvement

    def __init__(self, *args, **kwargs):
        self.target_metric: str = None
        self.logger: Optional[logging.Logger] = None
        # only support single target performance for now
        self.best_perf: float = -np.inf
        self.epoch_counter: int = 1
        self.step_counter: int = 1
        self.early_stop: bool = False
        self._patience_counter: int = 0
        self.hist_perf: List[Dict] = []  # performance history (for each epoch)
        super().__init__(*args, **kwargs)

    def set_checkpoints_path(self, path):
        if path is not None and isinstance(path, str):
            os.makedirs(path, exist_ok=True)
        self._checkpoints_path = path

    def set_verbose_for_every_x_steps(self, steps):
        steps = int(steps)
        self._verbose_for_every_x_steps = None if steps <= 0 else steps

    def set_save_every_x_epochs(self, epochs):
        epochs = int(epochs)
        self._save_every_x_epochs = None if epochs <= 0 else epochs

    def epoch(self, model, score: Dict[str, float] = None):
        if score and self.target_metric:
            # get the target metric value
            model.performance = _perf = score[self.target_metric]
            self.hist_perf.append(score)
            if _perf > self.best_perf:
                # TODO: support multicriteria decision making
                self.best_perf = _perf
                self._patience_counter = 0
                self.logger.info(f"target metric {self.target_metric} improved...")
                if self.checkpoints_path:
                    self.logger.info("saving the model...")
                    model.save(os.path.join(self.checkpoints_path, "best_epoch"))
            else:
                self._patience_counter += 1
                self.logger.warn(
                    f"target metric {self.target_metric} stagnates for "
                    f"{self._patience_counter}/{self.patience} epochs"
                )
                if self._patience_counter >= self.patience:
                    self.logger.warn("early stopping...")
                    self.early_stop = True

        if (
            self.checkpoints_path
            and self.save_every_x_epochs
            and self.epoch_counter % self.save_every_x_epochs == 0
        ):
            model.save(
                os.path.join(self.checkpoints_path, f"checkpoints_epoch_{self.epoch_counter}")
            )
        self.epoch_counter += 1
        self.step_counter = 1

    def step(self, loss):
        if (
            self.verbose_for_every_x_steps
            and self.step_counter % self.verbose_for_every_x_steps == 0
        ):
            self.logger.info(f"Step {self.step_counter} with Loss: {loss:.5f}.")
        self.step_counter += 1


class _PyTorchMetricCollector(object):
    """Compute and collect the model metrics"""

    def __init__(
        self,
        metrics: List[Callable],
        stage: str = "training",
        logger: Optional[logging.Logger] = None,
    ):
        assert stage in ["training", "validation"]
        self._metrics: Dict[str, Callable] = {m.__name__: m for m in metrics}
        self._predictions: List[torch.Tensor] = []
        self._targets: List[torch.Tensor] = []
        self._stage: str = stage
        self._logger: Optional[logging.Logger] = logger

    def _log_metric(self, score):
        """logging the performance metric values"""
        if self._logger is not None:
            for k, v in score.items():
                msg = ", ".join([f"{_:.4f}" for _ in v]) if hasattr(v, "__iter__") else f"{v:.4f}"
                self._logger.info(f"{self._stage}-{k}={msg}")

    def log(self, predictions: torch.Tensor, targets: torch.Tensor):
        assert isinstance(predictions, torch.Tensor)
        assert isinstance(targets, torch.Tensor)
        self._predictions.append(predictions.squeeze())
        self._targets.append(targets.squeeze())

    def __call__(self):
        # TODO: @yuanhao: what is the difference from `.numpy()`
        y_pred = torch.cat(self._predictions, dim=0).data.cpu().numpy()
        y_true = torch.cat(self._targets, dim=0).data.cpu().numpy()
        score = {k: fun(y_true, y_pred) for k, fun in self._metrics.items()}
        self._log_metric(score)
        return score


# TODO: `BaseNN` -> `BasePytorchNN`?
class BaseNN(BaseModel):
    """Base class for all Pytorch-NN models"""

    # parameters without default values
    optimizer = Parameter()
    scheduler = Parameter()
    loss = Parameter()
    metrics = Parameter()  # all metrics to be computed
    target_metric = Parameter()  # the metrics for hyper-parameter optimization
    observer = Parameter()  # observer
    # ... with default values
    pre_train = Parameter(False)
    val_batch_size = Parameter(16)
    epochs = Parameter(10)
    gpu_list = Parameter([])

    __losses__: List[Callable] = {}
    __metrics__: Dict[str, Callable] = {}
    _create_model: Callable = lambda x: x

    def __init__(self, *args, **kwargs):
        self.performance = None
        super().__init__(*args, **kwargs)

    def validate_data(self, data):
        # TODO: check if we need this!
        pass

    def set_optimizer(self, optimizer: PytorchOptimizer):
        assert isinstance(optimizer, PytorchOptimizer)
        self._optimizer = optimizer

    def set_scheduler(self, scheduler: PytorchScheduler):
        assert isinstance(scheduler, PytorchScheduler)
        self._scheduler = scheduler

    def set_loss(self, loss: Callable):
        assert any([isinstance(loss, l) for l in self.__losses__])
        self._loss: Callable = loss

    def set_metrics(self, metrics: Union[callable, List[callable]]):
        if hasattr(metrics, "__call__"):
            metrics = [metrics]
        metrics = list(set(metrics))
        assert all(_ in self.__metrics__ for _ in metrics)
        self._metrics: List[callable] = metrics

    def set_target_metric(self, target_metric: Union[str, callable]):
        assert hasattr(self, "_metrics")
        if isinstance(target_metric, str):
            assert target_metric in [m.__name__ for m in self._metrics]
        elif hasattr(target_metric, "__call__"):
            assert target_metric in self._metrics
            target_metric = target_metric.__name__
        self._target_metric: str = target_metric

    def set_gpu_list(self, gpu_list: Union[str, List[str]]):
        self._gpu_list = gpu_list
        # TODO: add check of the availability of specifie GPUs
        self._use_gpu = len(self._gpu_list) >= 1 and torch.cuda.is_available()
        self._parallel = len(self._gpu_list) > 1

    def fit(self) -> BaseNN:
        # TODO: find a more elegant way of doing this
        if self._use_gpu:
            torch.cuda.manual_seed(self.random_seed)
        else:
            torch.manual_seed(self.random_seed)
        # create the torch model from hyperparameters
        self._model = self._create_model(**self.get_hyper_params())
        self._set_model()
        # create the BP optimizer and learning rate scheduler
        self._init_optimizer(self._model.parameters())
        self._init_observer()

        self.logger.info("Start training...")
        for e in range(self.epochs):
            self.logger.info(f"Epoch: {e + 1}/{self.epochs}:")
            # training
            self._train()
            # validate the model
            score = self._validate() if self._perform_validation else None
            # observe the epoch and set the best-so-far performance
            self.observer.epoch(self, score)
            self.logger.info(f"End of epoch {e + 1}/{self.epochs}")
            if self.observer.early_stop:
                break
        return self

    def _init_observer(self):
        self.observer.logger = self.logger
        self.observer.target_metric = self.target_metric

    def _train(self) -> Dict[str, float]:
        assert self._model is not None
        # set to the training model
        self._model.train()
        # initialize the metric collector
        compute_metric = _PyTorchMetricCollector(self._metrics, logger=self.logger)
        for data, target in self.data_train:
            if self._use_gpu:
                data, target = data.cuda(), target.cuda()
            # TODO: @yuanhao: should this be part of the `BCEWithLogitsLoss` function?
            if isinstance(self.loss, nn.BCEWithLogitsLoss):
                target = target.float()

            # clear the gradients of all optimized variables
            self.optimizer.zero_grad()
            # forward pass: compute predicted outputs by passing inputs to the model
            output = self._model(data)
            # calculate the loss
            loss = self.loss(output, target)
            # log the prediction and target to the metric collector
            compute_metric.log(output, target)
            # backward pass: compute gradient of the loss with respect to model parameters
            loss.backward()
            # perform a single optimization step (parameter update)
            self.optimizer.step()
            # log the step-size loss
            self.observer.step(loss)
        # perform a single scheduler step (adjusting the learning rate)
        self.scheduler.step()
        # compute the training metrics
        return compute_metric()

    def _validate(self, data_val=None) -> Dict[str, float]:
        assert self._model is not None
        with torch.no_grad():
            # set to the testing model
            self._model.eval()
            # initialize the metric collector
            compute_metric = _PyTorchMetricCollector(self._metrics, "validation", self.logger)
            data_val = self.data_val if data_val is None else data_val
            for data, target in data_val:
                if self._use_gpu:
                    data = data.cuda()
                # forward pass: compute predicted outputs by passing inputs to the model
                output = self._model(data)
                # special output computation
                if isinstance(self.loss, nn.BCEWithLogitsLoss):
                    output = torch.sigmoid(output)
                else:
                    output = torch.softmax(output, dim=1)
                # log the prediction and target to the metric collector
                compute_metric.log(output, target)
        # compute the validation metrics
        return compute_metric()

    def _set_model(self):
        """Set all auxilary variables used by `self._model` and its status"""
        if self._use_gpu and torch.cuda.is_available():
            if len(self.gpu_list) == 1:  # single GPU mode
                torch.cuda.set_device(self.gpu_list[0])
                self._model.cuda()
            elif len(self.gpu_list) > 1:  # multi-gpu parallel mode
                self._model.cuda()
                self._model = nn.DataParallel(self._model, device_ids=self.gpu_list)

    def _init_optimizer(self, parameters):
        """initialize the pytorch optimizers"""
        self.optimizer.parameters = parameters
        self.optimizer.fit()
        self.scheduler.optimizer = self.optimizer
        self.scheduler.fit()

    def predict(self, X: torch.Tensor) -> np.ndarray:
        """Prediction

        Parameters
        ----------
        X : `torch.Tensor`
            data to predict, of the shape (batch_size, n_channel, height, width)

        Returns
        -------
        np.ndarray
            of shape (batch_size, n_output), where
                * n_output = 1 for simple classification task
                * n_output = `self.num_classes` for multi-label classification
                * for regression tasks, it depends on the number of target values
            if `self._idx_to_class` exists, then the output is an array of string showing
            the label names; Otherwise an int-valued array indexing the classes
        """
        assert self._model is not None
        # NOTE: do not compute the gradient
        with torch.no_grad():
            # NOTE: BatchNormalization and Dropout remain unchanged by `eval`
            self._model.eval()
            if self._use_gpu:
                X = X.cuda()

            # TODO: perhaps it is not very reasonable to consider those two cases here
            if self._task == "classification":
                y_ = self.predict_prob(X)
                y_ = y_.argmax(axis=1)
                # if class names are provided
                if hasattr(self, "_idx_to_class"):
                    y_ = np.array([self._idx_to_class[i] for i in y_])
            elif self._task == "regression":
                y_ = self._model(X).detach().cpu().numpy()

            return y_

    def save(self, filename: str, exclude: List[str] = None):
        """Dump a BaseNN instance to a file

        Parameters
        ----------
        filename : str
            base name of the files to save a BaseNN object. The model attributes will be
            saved to 'filename.dump' and the network architecture will be saved to
            'filename.pth'

        exclude : Tuple[str]
            non-serializable attributes should be excluded from ``super().save`` function call,
            by default ['_model', 'optimizer', '_optimizer', '_parameters']
        """
        if self._model is not None:
            model = self._model.module if self._parallel else self._model
            torch.save(model.state_dict(), filename + ".pth")
        # all those are not serializable... reconstruct those when loading
        # `optimizer` is a generator and hence can not be pickled
        exclude = [] if exclude is None else exclude
        exclude += [
            "optimizer",
            "_optimizer",
            "scheduler",
            "_scheduler",
            "_model",
            "_parameters",
            "scheduler.optimizer",
        ]
        super().save(filename, exclude)

    @classmethod
    def load(cls, filename: str) -> BaseNN:
        """Load a neural network model from a dump file

        Parameters
        ----------
        filename : str
            Base name of the dump file

        Returns
        -------
        obj: a BaseNN instance
        """
        obj = super().load(filename)
        model_file = filename + ".pth"
        # set the model is the dump file exists
        if not os.path.exists(model_file):
            return obj

        kwargs = dict(obj.get_hyper_params())
        # don't load the pre-trained model
        kwargs.update({"pre_train": False})
        setattr(obj, "_model", getattr(obj, "_create_model")(**kwargs))
        setattr(obj, "_use_gpu", len(getattr(obj, "_gpu_list")) >= 1 and torch.cuda.is_available())
        device = torch.device("cuda" if getattr(obj, "_use_gpu") else "cpu")
        getattr(obj, "_model").load_state_dict(torch.load(model_file, map_location=device))
        getattr(obj, "_set_model")()  # set aux. var. used by _model
        # TODO: probably this is not needed?
        # obj._init_optimizer(obj._model.parameters())  # set optimizers
        return obj


class NNRegressor(BaseNN):
    """NN for regression"""

    _task = "regression"
    __losses__ = REGR_LOSS
    __metrics__ = REGR_METRIC

    def __init__(self, *args, **kwargs):
        # default parameters
        kwargs_ = {"loss": nn.MSELoss(), "observer": BaseObserver()}
        kwargs_.update(kwargs)
        super().__init__(*args, **kwargs_)


class NNClassifier(BaseNN):
    """NN for classification"""

    num_classes = Parameter(None)

    _task = "classification"
    __losses__ = CLASS_LOSS
    __metrics__ = CLASS_METRIC

    def __init__(self, *args, **kwargs):
        # default parameters
        kwargs_ = {
            "optimizer": SGD(),
            "scheduler": StepLR(),
            "loss": nn.CrossEntropyLoss(**{"reduction": "mean"}),
            "metrics": [balanced_accuracy, f1, tpr],
            "target_metric": f1,
            "observer": BaseObserver(),
        }
        kwargs_.update(kwargs)
        super().__init__(*args, **kwargs_)

    def set_data(self, data_train: Iterable, data_val: Optional[Iterable] = None) -> NNClassifier:
        """Set the training and validation data set (optional) and validate
        both data sources

        Parameters
        ----------
        data_train : Iterable
            The training data set
        data_val : Optional[Iterable], optional
            The validation data set, by default None

        Returns
        -------
        self : a ``BaseNN`` instance
        """
        super().set_data(data_train, data_val)
        if hasattr(self.data_train.dataset, "num_classes"):
            self.num_classes = self.data_train.dataset.num_classes
        elif hasattr(self.data_train.dataset, "dataset"):
            self.num_classes = self.data_train.dataset.dataset.num_classes

        # setup the conversion dict. for `self.predict`
        if hasattr(self.data_train.dataset, "class_to_idx"):
            class_to_idx = self.data_train.dataset.class_to_idx
        # for torch's Subset. TODO: see how we get rid of it..
        elif hasattr(self.data_train.dataset, "dataset"):
            class_to_idx = self.data_train.dataset.dataset.class_to_idx
        self._idx_to_class = {v: k for k, v in class_to_idx.items()}
        return self

    @abstractmethod
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
