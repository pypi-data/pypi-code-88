"""
Define a generic MLP for training
Uses to learn model from embedding

Example:
    from deepchain.models import MLP
    from deepchainps.data import TorchDataloader

    mlp = MLP()
    dl = TorchDataloader(X,y)
    mlp.fit(dl)
"""


import typing
from collections import Counter, OrderedDict
from typing import Optional

import numpy as np
import pytorch_lightning as pl
import torch
import torch.nn.functional as F  # noqa
from deepchain import log
from sklearn.model_selection import train_test_split
from sklearn.utils.class_weight import compute_class_weight
from torch import Tensor, nn

from .utils import classification_dataloader_from_numpy


class MLP(pl.LightningModule):
    """A `pytorch` based deep learning model"""

    def __init__(self, input_shape: int, n_class: int, n_neurons: int = 128, lr: float = 1e-3):
        """Instantiante a pytorch-lightning model

        This model is a template MLP to learn directly from embeddings.
        It's composed of 2 Dense layers with Relu activation. This template works only
        for classification model.
        The trainings logs are saved in the logs folder.

        Args:
            input_shape (int): shape input layer.
            n_class (int): number of class to predict
                           - n_class=2 for (0/1) binary classification
                           - n_class>=2 for multiclass problem
            n_neurons (int, optional): Number or neurons in each layer. Defaults to 128.
            lr (float, optional): learning rate. Defaults to 1e-3.
        """
        super().__init__()
        self.n_neurons = n_neurons
        self.lr = lr
        self.input_shape = input_shape
        self.output_shape = 1 if n_class <= 2 else n_class
        self.activation = nn.Sigmoid() if n_class <= 2 else nn.Softmax(dim=-1)
        self.model = nn.Sequential(
            nn.Linear(self.input_shape, self.n_neurons),
            nn.ReLU(),
            nn.Linear(self.n_neurons, self.output_shape),
            self.activation,
        )

    def forward(self, x):
        """Defines forward pass"""
        if not isinstance(x, torch.Tensor):
            x = torch.tensor(x).float()
        return self.model(x)

    def training_step(self, batch, batch_idx):
        """training_step defined the train loop. It is independent of forward"""
        x, y = batch
        y_hat = self.model(x).squeeze()
        y = y.squeeze()

        if self.output_shape > 1:
            y_hat = torch.log(y_hat)

        loss = self.loss(y_hat, y)
        self.log("train_loss", loss, on_epoch=True, on_step=False)
        return {"loss": loss}

    def validation_step(self, batch, batch_idx):
        """training_step defined the train loop. It is independent of forward"""
        x, y = batch
        y_hat = self.model(x).squeeze()
        y = y.squeeze()

        if self.output_shape > 1:
            y_hat = torch.log(y_hat)

        loss = self.loss(y_hat, y)
        self.log("val_loss", loss, on_epoch=True, on_step=False)
        return {"val_loss": loss}

    def configure_optimizers(self):
        """(Optional) Configure training optimizers."""
        return torch.optim.Adam(self.parameters(), lr=self.lr)

    def compute_class_weight(self, y: np.array, n_class: int):
        """Compute class weight for binary/multiple classification

        If n_class=2, only compute weights for the positve class.
        If n>2, compute for all classes.
        Args:
            y ([np.array]):vector of int represented the class
            n_class (int) : number fo class to use
        """
        if n_class == 2:
            class_count: typing.Counter = Counter(y)
            cond_binary = (0 in class_count) and (1 in class_count)
            assert cond_binary, "Must have O and 1 class for binary classification"
            weight = class_count[0] / class_count[1]
        else:
            weight = compute_class_weight(class_weight="balanced", classes=np.unique(y), y=y)

        return torch.tensor(weight).float()

    def fit(
        self,
        x: np.ndarray,
        y: np.array,
        epochs: int = 10,
        batch_size: int = 32,
        class_weight: Optional[str] = None,
        validation_data: bool = True,
        **kwargs
    ):
        """Fit a MLP on X,y which are numpy array.
        Torch Dataloader are automatically computed
        class_weights are computed with sklearn for multiclass or y_negative/y_positive for binary
        Fit is done with pytorch lightning, so any arguments suitable with pytorch lightning fit function
        could be passed in kwargs.

        Args:
            x (np.ndarray): [description]
            y (np.array): [description]
            epochs (int, optional): [description]. Defaults to 10.
            batch_size (int, optional): [description]. Defaults to 32.
            class_weight (str, optional):
                        None or 'balanced'. Compute weights if 'balanced specified'.
                        Can specified your own torch.tensor weight
            validation_data (bool, optional): [description]. Defaults to True.
            **kwargs: any options that can be use in pytorch lightning method
        """
        assert isinstance(x, np.ndarray), "X should be a numpy array"
        assert isinstance(y, np.ndarray), "y should be a numpy array"
        assert class_weight in (
            None,
            "balanced",
        ), "the only choice available for class_weight is 'balanced'"
        n_class = len(np.unique(y))
        weight = None
        self.input_shape = x.shape[1]
        self.output_shape = 1 if n_class <= 2 else n_class
        self.activation = nn.Sigmoid() if n_class <= 2 else nn.Softmax(dim=-1)

        if class_weight == "balanced":
            weight = self.compute_class_weight(y, n_class)

        self.loss = nn.NLLLoss(weight) if self.output_shape > 1 else nn.BCELoss(weight)

        if validation_data:
            x_train, x_val, y_train, y_val = train_test_split(x, y, test_size=0.2)
            train_loader = classification_dataloader_from_numpy(
                x_train, y_train, batch_size=batch_size
            )
            val_loader = classification_dataloader_from_numpy(x_val, y_val, batch_size=batch_size)
        else:
            train_loader = classification_dataloader_from_numpy(x, y, batch_size=batch_size)
            val_loader = None

        self.trainer = pl.Trainer(max_epochs=epochs, **kwargs)
        self.trainer.fit(self, train_loader, val_loader)

    def predict(self, x):
        """Run inference on data."""
        if self.output_shape is None:
            log.warning("Model is not fitted. Can't do predict")
            return
        return self.forward(x).detach().numpy()

    def save(self, path: str):
        """Save the state dict model with torch"""
        torch.save(self.model.state_dict(), path)
        log.info("Save state_dict parameters in model.pt")

    def load_state_dict(self, state_dict: "OrderedDict[str, Tensor]", strict: bool = False):
        """Load state_dict saved parameters

        Args:
            state_dict (OrderedDict[str, Tensor]): state_dict tensor
            strict (bool, optional): [description]. Defaults to False.
        """
        self.model.load_state_dict(state_dict, strict=strict)
        self.model.eval()
