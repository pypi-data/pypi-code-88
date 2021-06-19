# AUTOGENERATED! DO NOT EDIT! File to edit: nbs/03_trainer.ipynb (unless otherwise specified).

__all__ = ['MODEL_DICT', 'OPT_DICT', 'create_classifier', 'create_cnn', 'Trainer', 'InterpretModel', 'Learner']

# Cell
from typing import Callable, Union

import tensorflow as tf
import tensorflow_addons as tfa
from tensorflow.keras.models import Model
from typeguard import check_argument_types, check_return_type, typechecked

from .datagenerator import Dataset

# Cell
from functools import partial

import matplotlib.cm as cm
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from tf_keras_vis.gradcam import Gradcam, GradcamPlusPlus
from tf_keras_vis.utils import normalize

# Cell
import inspect
import sys

MODEL_DICT = {}
for name, func in inspect.getmembers(tf.keras.applications):
    if inspect.isfunction(func):
        MODEL_DICT[name.lower()] = func

OPT_DICT = {}
for name, func in inspect.getmembers(tf.keras.optimizers):
    if inspect.isclass(func):
        OPT_DICT[name.lower()] = func

# Cell
@typechecked
def _get_base_cnn(
    base_model: Union[str, Model],
    pooling: str = "avg",
    weights: Union[str, None] = "imagenet",
    include_top: bool = False,
) -> Model:
    if isinstance(base_model, str):
        assert (
            base_model in MODEL_DICT.keys()
        ), f"base_model name must be in {tuple(MODEL_DICT.keys())}"
        base_model = MODEL_DICT[base_model]
        base_model = base_model(
            include_top=include_top, pooling=pooling, weights=weights
        )
    return base_model

# Cell
@typechecked
def _add_output_layers(
    base_model: Model, outputs: int, drop_out: Union[float, None] = None, name=None
) -> Model:

    x = base_model.output
    # x = tf.keras.layers.GlobalMaxPool2D()(x)
    if drop_out:
        x = tf.keras.layers.Dropout(drop_out)(x)
    x = tf.keras.layers.Dense(outputs, name="output")(x)

    model = tf.keras.Model(base_model.input, x, name=name)
    return model

# Cell
def create_classifier(
    base_model_fn: callable,
    num_classes: int,
    weights="imagenet",
    dropout=0,
    include_top=False,
    name=None,
):

    outputs = 1 if num_classes == 2 else num_classes

    base_model = base_model_fn(
        include_top=include_top,
        weights=weights,
    )
    if include_top:
        return base_model
    drop_out = 0.5
    outputs = 1

    x = base_model.output
    x = tf.keras.layers.GlobalMaxPool2D()(x)
    if drop_out:
        x = tf.keras.layers.Dropout(drop_out)(x)
    x = tf.keras.layers.Dense(outputs, name="output")(x)

    model = tf.keras.Model(base_model.input, x)
    return model

# Cell
@typechecked
def create_cnn(
    base_model: Union[str, Model],
    num_classes: int,
    drop_out=0.5,
    keras_applications: bool = True,
    pooling: str = "avg",
    weights: Union[str, None] = "imagenet",
    name=None,
) -> Model:

    assert pooling in ("avg", "max")

    if keras_applications:
        if num_classes == 2:
            outputs = 1
        else:
            outputs = num_classes
    else:
        print(f"num_classes is ignored. returning the passed model as it is.")

    if isinstance(base_model, (str, Model)) and keras_applications:
        base_model = _get_base_cnn(base_model, pooling=pooling, weights=weights)
        assert (
            "pool" in base_model.layers[-1].name
        ), f"base_model last layer must be a pooling layer"
        model = _add_output_layers(base_model, outputs, drop_out=drop_out, name=name)

    elif isinstance(base_model, Model) and keras_applications is False:
        model = base_model

    elif isinstance(base_model, str) and keras_applications is False:
        model = _get_base_cnn(base_model, weights="imagenet", include_top=True)

    else:
        print(f"Invalid arguments!")
    return model

# Cell
class Trainer(Model):
    """
    The Trainer class inherits tf.keras.Model and contains everything a model needs for training.
    It exposes trainer.cyclic_fit method which trains the model using Cyclic Learning rate discovered by Leslie Smith.

    Arguments:
    ds: Dataset object
    model: object of type tf.keras.Model
    num_classes (int, None): number of classes in the dataset. If None then will auto infer from Dataset

    """

    _AUTOTUNE = tf.data.experimental.AUTOTUNE

    @typechecked
    def __init__(
        self, ds: Dataset, model: Model, num_classes: Union[int, None] = None, **kwargs
    ):
        assert check_argument_types()

        super(Trainer, self).__init__()
        self.ds = ds
        self.total = len(ds)
        if num_classes:
            self.NUM_CLASSES = num_classes
        else:
            self.NUM_CLASSES = ds.NUM_CLASSES
        self.gradcam = None
        self.model = model
        self.cyclic_opt_set = False

    def build(self):
        pass

    def summary(self):
        return self.model.summary()

    # def get_layer(name=None, index=None): return self.model(name, index)

    def compile(self, *args, **kwargs):
        return self.model.compile(*args, **kwargs)

    def call(self, *args, **kwargs):
        return self.model.call(*args, **kwargs)

    def fit(self, *args, **kwargs):
        return self.model.fit(*args, **kwargs)

    def warmup(self):
        pass

    def prewhiten(self, image):
        image = tf.cast(image, tf.float32)
        image = image / 127.5 - 1.0
        return image

    def rescale(self, image, label):
        image = self.prewhiten(image)
        return image, label

    def _get_optimizer(self, optimizer, momentum=0.9, **kwargs):
        if optimizer.__name__ == "SGD":
            optimizer = partial(
                optimizer, momentum=momentum, nesterov=kwargs.get("nesterov", True)
            )
        else:
            optimizer = partial(
                optimizer,
                momentum=momentum,
            )
        return optimizer

    def _prepare_dl(self, bs=8, shuffle=True):
        ds = self.ds
        dl = ds.get_tf_dataset(shuffle=shuffle)
        dl = dl.map(self.rescale, Trainer._AUTOTUNE)
        return dl.batch(bs).prefetch(Trainer._AUTOTUNE)

    def cyclic_fit(
        self,
        epochs: int,
        batch_size: int,
        lr_range: Union[tuple, list] = (1e-4, 1e-2),
        optimizer=tf.keras.optimizers.SGD,
        momentum=0.9,
        validation_data=None,
        callbacks=None,
        *args,
        **kwargs,
    ):
        """Trains model on ds as train data with cyclic learning rate.
        Dataset will be automatically converted into `tf.data` format and images will be prewhitened in range of [-1, 1].
        Cyclical Learning Rates for Training Neural Networks: https://arxiv.org/abs/1506.01186

        Args:
            epochs (int): number of epochs for training
            batch_size (int): batch size
            lr_range (tuple): learning rate will cycle from lr_min to lr_max
            optimizer (callable): Keras callable optimizer
            momentum(int): momentum for the optimizer
        kwargs:
            step_size (int): step size for the Cyclic learning rate. By default it is `2 * len(self.ds)//batch_size`
            scale_mode (str): cycle or exp
            shuffle(bool): Dataset will be shuffle on each epoch if True
        """
        if not self.cyclic_opt_set:
            self.max_lr, self.min_lr = lr_range
            ds = self.ds
            step_size = 2 * len(self.ds) // batch_size
            lr_schedule = tfa.optimizers.Triangular2CyclicalLearningRate(
                initial_learning_rate=lr_range[0],
                maximal_learning_rate=lr_range[1],
                step_size=kwargs.get("step_size", step_size),
                scale_mode=kwargs.get("scale_mode", "cycle"),
            )

            optimizer = self._get_optimizer(optimizer, momentum=momentum)
            optimizer = optimizer(learning_rate=lr_schedule)
            self.model.optimizer = optimizer
            self.cyclic_opt_set = True
        else:
            print("cyclic learning rate already set!")

        return self.model.fit(
            self._prepare_dl(batch_size, kwargs.get("shuffle", True)),
            validation_data=validation_data,
            epochs=epochs,
            callbacks=callbacks,
        )

    @typechecked
    def compile2(
        self,
        batch_size: int,
        optimizer: Union[str, tf.keras.optimizers.Optimizer] = "adam",
        lr_range: Union[tuple, list] = (1e-4, 1e-2),
        loss=None,
        metrics=None,
        loss_weights=None,
        weighted_metrics=None,
        run_eagerly=None,
        **kwargs,
    ):
        """Compile2 compiles the model of Trainer for cyclic learning rate.
        Cyclical Learning Rates for Training Neural Networks: https://arxiv.org/abs/1506.01186

        Args:
            batch_size (int): batch size
            lr_range (tuple): learning rate will cycle from lr_min to lr_max
            optimizer (str, keras.optimizer.Optimizer): Keras optimizer

        kwargs:
            step_size (int): step size for the Cyclic learning rate. By default it is `2 * len(self.ds)//batch_size`
            scale_mode (str): cycle or exp
            momentum(int): momentum for the optimizer when optimizer is of type str
        """
        self.max_lr, self.min_lr = lr_range
        self.batch_size = batch_size

        self.step_size = step_size = 2 * len(self.ds) // batch_size

        lr_schedule = tfa.optimizers.Triangular2CyclicalLearningRate(
            initial_learning_rate=lr_range[0],
            maximal_learning_rate=lr_range[1],
            step_size=kwargs.get("step_size", step_size),
            scale_mode=kwargs.get("scale_mode", "cycle"),
        )

        if isinstance(optimizer, str):
            optimizer = OPT_DICT[optimizer]
            optimizer = optimizer(learning_rate=lr_schedule)
            if kwargs.get("momentum"):
                optimizer.momentum = kwargs.get("momentum")

        else:
            optimizer.learning_rate = lr_schedule

        self.compile(optimizer=optimizer, loss=loss, metrics=metrics)
        self.cyclic_opt_set = True
        print(f"Model compiled!")

# Cell
class InterpretModel:
    def __init__(self, gradcam_pp: bool, learner: Trainer, clone: bool = False):
        """Args:
        gradcam_pp: if True GradCam class will be used else GradCamPlusplus
        clone: whether GradCam will clone learner.model
        """
        if gradcam_pp:
            self.gradcam_fn = GradcamPlusPlus
        else:
            self.gradcam_fn = Gradcam
        self.learner = learner

        self.gradcam = self.gradcam_fn(learner.model, self.model_modifier, clone=clone)

        # if self.learner.include_top is not True:
        #     self.gradcam._find_penultimate_output = self.patch

    def __call__(self, image: Image.Image, auto_resize: bool = True, image_size=None):
        # assert check_argument_types()
        gradcam = self.gradcam
        get_loss = self.get_loss
        if auto_resize and image_size is None:
            image_size = self.learner.ds.img_sz_list.get_size()
        if image_size:
            image = image.resize(image_size)

        X = np.asarray(image, np.float32)
        X = self.learner.prewhiten(X)
        X = np.expand_dims(X, 0)

        cam = gradcam(
            get_loss,
            X,
            penultimate_layer=-1,  # model.layers number
            seek_penultimate_conv_layer=True,
        )
        cam = normalize(cam)
        heatmap = np.uint8(cm.jet(cam[0])[..., :3] * 255)
        plt.imshow(image)
        plt.imshow(heatmap, cmap="jet", alpha=0.5)
        plt.show()

    def __patch(self, *args, **kwargs):
        """Path _find_penultimate_output method of tf_keras_vis"""
        if self.learner.include_top:
            return self.learner.model.layers[-1].output
        return self.learner.model.layers[0].get_output_at(-1)

    def model_modifier(self, m):
        """Sets last activation to linear"""
        m.layers[-1].activation = tf.keras.activations.linear
        return m

    def get_loss(self, preds):
        if self.learner.NUM_CLASSES == 2:
            ret = preds[0]
        else:
            index = tf.argmax(tf.math.softmax(preds), axis=1)[0]
            # print(index, preds.shape)
            ret = preds[0, index]
            print(f"index: {index}")
        return ret

# Cell
from typing import List, Union

from tensorflow import keras
import pytorch_lightning as pl
from .utility.import_utils import INSTALLED_MODULES
from .converter.core import tf2_to_onnx, tf2_to_pytorch, onnx_to_pytorch, pytorch_to_onnx

# Cell
class Learner:
    TF = ("TF", "TENSORFLOW")
    PT = ("PYTORCH", "PT", "TORCH")

    def __init__(self,
                 model: Union[pl.LightningModule, keras.models.Model],
                 mode: str = "TF"):
        self.MODE = mode.upper()
        self.model = model
        self.epochs_trained = 0

        if self.MODE in Learner.PT:
            self.trainer = None

    def fit(self,
            train_data,
            epochs,
            val_data=None,
            test_data=None,
            callbacks=None,
            **kwargs):
        """train models
        For TF:
            Just pass train data and start training
        For PyTorch:
            You can enter configs to Lightning Trainer
        """
        MODE = self.MODE
        initial_epoch = self.epochs_trained
        self.epochs_trained += epochs

        if MODE in Learner.TF:
            return self.model.fit(
                train_data,
                epochs=epochs,
                initial_epoch=initial_epoch,
                validation_data=val_data,
                callbacks=callbacks,
            )
        elif MODE in Learner.PT:
            lit_confs = kwargs.get('LIT_TRAINER_CONFIG', {})
            if not self.trainer:
                self.trainer = pl.Trainer(max_epochs=epochs, **lit_confs)
            return self.trainer.fit(self.model, train_data, val_data)

    def to_onnx(self, tensor=None, export_path=None):
        MODE = self.MODE
        if MODE in Learner.TF:
            return tf2_to_onnx(self.model, output_path=export_path)

        if MODE in Learner.PT:
            return pytorch_to_onnx(self.model, tensor, export_path)